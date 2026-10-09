"""Cliente HTTP para os endpoints da API do GitHub usados pelo projeto."""

from __future__ import annotations

import threading
from datetime import date, datetime, timezone
from typing import Optional

import requests

from . import config
from .exceptions import (
    GitHubAPIError,
    OperationCancelledError,
    StatsNotReadyError,
)
from .models import CommitRecord, ProgressCallback, ProgressEvent

_BRANCHES_QUERY = """
query($owner: String!, $name: String!, $cursor: String) {
  repository(owner: $owner, name: $name) {
    defaultBranchRef { name target { oid } }
    refs(refPrefix: "refs/heads/", first: 100, after: $cursor) {
      totalCount
      pageInfo { hasNextPage endCursor }
      nodes { name target { oid } }
    }
  }
}
"""

_HISTORY_QUERY = """
query($owner: String!, $name: String!, $oid: GitObjectID!, $cursor: String, $n: Int!) {
  repository(owner: $owner, name: $name) {
    object(oid: $oid) {
      ... on Commit {
        history(first: $n, after: $cursor) {
          totalCount
          pageInfo { hasNextPage endCursor }
          nodes {
            oid
            additions
            deletions
            authoredDate
            committedDate
            messageHeadline
            parents { totalCount }
            author { name email user { login url } }
          }
        }
      }
    }
  }
}
"""


def _noop(_: ProgressEvent) -> None:
    pass


class GitHubClient:
    """
    Encapsula o acesso à API REST do GitHub.

    - Reaproveita conexões com ``requests.Session``.
    - Aplica *timeout* em todas as requisições.
    - Converte erros HTTP em exceções com mensagens amigáveis.
    """

    def __init__(
        self,
        token: Optional[str] = None,
        *,
        base_url: str = config.GITHUB_API_BASE,
        timeout: float = config.REQUEST_TIMEOUT,
        session: Optional[requests.Session] = None,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = session or requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": config.GITHUB_API_VERSION,
                "User-Agent": "GitHubAPI-ContributorStats",
            }
        )
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"

    # ------------------------------------------------------------------ #
    # Infraestrutura
    # ------------------------------------------------------------------ #
    def _get(self, path: str, params: Optional[dict] = None) -> requests.Response:
        url = f"{self.base_url}{path}"
        try:
            return self.session.get(url, params=params, timeout=self.timeout)
        except requests.Timeout as exc:
            raise GitHubAPIError("Tempo limite excedido ao acessar a API do GitHub.") from exc
        except requests.RequestException as exc:
            raise GitHubAPIError(f"Falha de conexão com a API do GitHub: {exc}") from exc

    def _graphql(self, query: str, variables: dict) -> dict:
        """POST /graphql — devolve ``data`` ou lança :class:`GitHubAPIError`."""
        url = config.GITHUB_GRAPHQL_URL
        try:
            response = self.session.post(
                url, json={"query": query, "variables": variables}, timeout=self.timeout
            )
        except requests.Timeout as exc:
            raise GitHubAPIError(
                "Tempo limite excedido ao acessar a API GraphQL do GitHub.", status_code=504
            ) from exc
        except requests.RequestException as exc:
            raise GitHubAPIError(f"Falha de conexão com a API do GitHub: {exc}") from exc

        if response.status_code != 200:
            raise self._error_from_response(response)

        payload = response.json()
        errors = payload.get("errors") or []
        if errors:
            types = {e.get("type") for e in errors}
            if "RATE_LIMITED" in types:
                raise GitHubAPIError(
                    "Limite de requisições da API GraphQL do GitHub atingido. "
                    "Tente novamente mais tarde.", status_code=403)
            if "NOT_FOUND" in types:
                raise GitHubAPIError(
                    "Repositório não encontrado (404). Verifique a URL ou, se o "
                    "repositório for privado, se o token tem o escopo 'repo'.", status_code=404)
            msg = "; ".join(e.get("message", "erro desconhecido") for e in errors[:3])
            raise GitHubAPIError(f"Erro da API GraphQL do GitHub: {msg}")
        return payload.get("data") or {}

    @staticmethod
    def _error_from_response(response: requests.Response) -> GitHubAPIError:
        """Monta uma mensagem de erro amigável a partir da resposta HTTP."""
        try:
            api_message = response.json().get("message", "")
        except ValueError:
            api_message = response.text[:200]

        status = response.status_code
        remaining = response.headers.get("X-RateLimit-Remaining")

        if status in (403, 429) and remaining == "0":
            reset = response.headers.get("X-RateLimit-Reset")
            when = ""
            if reset and reset.isdigit():
                reset_dt = datetime.fromtimestamp(int(reset))
                when = f" O limite será renovado às {reset_dt:%H:%M:%S}."
            msg = "Limite de requisições da API do GitHub atingido." + when
            msg += " Usar um token aumenta o limite de 60 para 5.000 requisições/hora."
        elif status == 401:
            msg = "Token inválido ou expirado (401). Gere um novo PAT no GitHub."
        elif status == 404:
            msg = (
                "Repositório não encontrado (404). Verifique a URL ou, se o "
                "repositório for privado, se o token tem o escopo 'repo'."
            )
        elif status == 403:
            msg = f"Acesso negado (403). {api_message}".strip()
        else:
            msg = f"Erro {status} da API do GitHub. {api_message}".strip()

        return GitHubAPIError(msg, status_code=status)

    # ------------------------------------------------------------------ #
    # Endpoints
    # ------------------------------------------------------------------ #
    def fetch_contributors_stats(
        self,
        owner: str,
        repo: str,
        *,
        max_tries: int = config.MAX_TRIES,
        wait_time: float = config.WAIT_TIME,
        on_progress: ProgressCallback = _noop,
        cancel_event: Optional[threading.Event] = None,
    ) -> list[dict]:
        """
        GET /repos/{owner}/{repo}/stats/contributors

        A API responde ``202 Accepted`` enquanto calcula as estatísticas;
        nesse caso é feito *polling* até ``max_tries`` vezes.
        """
        path = f"/repos/{owner}/{repo}/stats/contributors"
        cancel_event = cancel_event or threading.Event()

        for attempt in range(1, max_tries + 1):
            if cancel_event.is_set():
                raise OperationCancelledError("Operação cancelada.")

            on_progress(
                ProgressEvent(
                    f"Buscando estatísticas (tentativa {attempt}/{max_tries}) de {owner}/{repo}…"
                )
            )
            response = self._get(path)

            if response.status_code == 200:
                on_progress(ProgressEvent("Estatísticas recebidas com sucesso.", "success"))
                return response.json() or []

            if response.status_code == 204:  # repositório vazio
                on_progress(ProgressEvent("O repositório não possui commits.", "warning"))
                return []

            if response.status_code == 202:
                if attempt == max_tries:
                    break
                on_progress(
                    ProgressEvent(
                        f"O GitHub está calculando as estatísticas. "
                        f"Aguardando {wait_time:g} s…",
                        "warning",
                    )
                )
                # wait() em vez de sleep(): permite cancelar durante a espera
                if cancel_event.wait(wait_time):
                    raise OperationCancelledError("Operação cancelada.")
                continue

            raise self._error_from_response(response)

        raise StatsNotReadyError(
            "O GitHub ainda está processando as estatísticas e o tempo limite foi "
            "atingido. Tente novamente em alguns instantes."
        )

    def fetch_last_commit_date(self, owner: str, repo: str, username: str) -> Optional[date]:
        """
        Data do commit mais recente de ``username`` no branch padrão.
        Retorna ``None`` se não for possível determinar (ex.: contas *bot*).
        """
        response = self._get(
            f"/repos/{owner}/{repo}/commits",
            params={"author": username, "per_page": 1},
        )
        if response.status_code != 200:
            return None

        commits = response.json()
        if not commits:
            return None

        commit = commits[0].get("commit", {})
        date_str = (commit.get("committer") or {}).get("date") or (
            commit.get("author") or {}
        ).get("date")
        if not date_str:
            return None

        # ex.: '2025-09-30T15:23:45Z'
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.astimezone(timezone.utc).date()

    # ------------------------------------------------------------------ #
    # Todas as branches (GraphQL)
    # ------------------------------------------------------------------ #
    def fetch_branches(self, owner: str, repo: str) -> tuple[Optional[str], list[tuple[str, str]]]:
        """
        Lista as branches do repositório.

        Retorna ``(branch_padrão, [(nome, oid_do_último_commit), ...])`` com a
        branch padrão sempre em primeiro lugar.
        """
        branches: list[tuple[str, str]] = []
        default_name: Optional[str] = None
        cursor = None
        while True:
            data = self._graphql(_BRANCHES_QUERY, {"owner": owner, "name": repo, "cursor": cursor})
            repository = data.get("repository")
            if repository is None:
                raise GitHubAPIError("Repositório não encontrado (404).", status_code=404)
            default_ref = repository.get("defaultBranchRef") or {}
            default_name = default_ref.get("name") or default_name
            refs = repository["refs"]
            for node in refs["nodes"]:
                target = node.get("target") or {}
                if target.get("oid"):
                    branches.append((node["name"], target["oid"]))
            if not refs["pageInfo"]["hasNextPage"]:
                break
            cursor = refs["pageInfo"]["endCursor"]

        branches.sort(key=lambda b: (b[0] != default_name, b[0].lower()))
        return default_name, branches

    def iter_branch_history(
        self,
        owner: str,
        repo: str,
        tip_oid: str,
        *,
        cancel_event: Optional[threading.Event] = None,
        page_size: Optional[int] = None,
    ):
        """
        Percorre todo o histórico a partir de ``tip_oid`` (página a página) e
        devolve os nós de commit do GraphQL. Em caso de timeout/502 (commits muito
        grandes), reduz o tamanho da página e tenta de novo.
        """
        cancel_event = cancel_event or threading.Event()
        cursor = None
        # Reaproveita o tamanho reduzido entre branches, se já houve timeout
        n = page_size or getattr(self, "_history_page_size", config.GRAPHQL_PAGE_SIZE)
        while True:
            if cancel_event.is_set():
                raise OperationCancelledError("Operação cancelada.")
            try:
                data = self._graphql(
                    _HISTORY_QUERY,
                    {"owner": owner, "name": repo, "oid": tip_oid, "cursor": cursor, "n": n},
                )
            except GitHubAPIError as exc:
                if exc.status_code in (502, 503, 504) or "timeout" in str(exc).lower():
                    if n > 10:
                        n = self._history_page_size = max(10, n // 2)
                        continue
                raise
            obj = ((data.get("repository") or {}).get("object")) or {}
            history = obj.get("history")
            if not history:
                return
            yield from history["nodes"]
            if not history["pageInfo"]["hasNextPage"]:
                return
            cursor = history["pageInfo"]["endCursor"]

    @staticmethod
    def to_commit_record(node: dict, branch: str, in_default: bool) -> CommitRecord:
        """Converte um nó de commit do GraphQL em :class:`CommitRecord`."""
        author = node.get("author") or {}
        user = author.get("user") or {}
        name = author.get("name") or ""
        email = (author.get("email") or "").lower()
        login = user.get("login")

        if login:
            key, display, url = login.lower(), login, user.get("url") or f"https://github.com/{login}"
        elif name.endswith("[bot]"):
            # Contas bot não são "User" no GraphQL
            key, display = name.lower(), name
            url = f"https://github.com/apps/{name[:-5]}"
        else:
            # E-mail não vinculado a nenhuma conta do GitHub
            key = email or name.lower() or "(usuário desconhecido)"
            display = f"{name or 'desconhecido'} <{email}>" if email else (name or "(usuário desconhecido)")
            url = ""

        return CommitRecord(
            oid=node["oid"],
            author_key=key,
            author_name=display,
            profile_url=url,
            additions=int(node.get("additions") or 0),
            deletions=int(node.get("deletions") or 0),
            authored_date=node.get("authoredDate") or "",
            committed_date=node.get("committedDate") or "",
            message_headline=node.get("messageHeadline") or "",
            is_merge=((node.get("parents") or {}).get("totalCount") or 0) > 1,
            branch=branch,
            in_default_branch=in_default,
        )
