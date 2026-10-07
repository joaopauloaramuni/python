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
from .models import ProgressCallback, ProgressEvent


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
