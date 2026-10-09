"""
Caso de uso principal: analisar um repositório e produzir o ranking.

É a única função que a CLI e a GUI precisam chamar. Ela não imprime nada
nem conhece Tkinter: comunica o andamento por meio de ``on_progress``.
"""

from __future__ import annotations

import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Optional

from . import config
from .exceptions import ContributorStatsError, OperationCancelledError
from .github_client import GitHubClient
from .models import AnalysisResult, CommitRecord, ProgressCallback, ProgressEvent
from .ranking import (
    SortCriterion,
    build_contributors,
    build_contributors_from_commits,
    rank_contributors,
)
from .repo_url import parse_repo_url


def _noop(_: ProgressEvent) -> None:
    pass


def analyze_repository(
    repo_url: str,
    token: Optional[str] = None,
    *,
    criterion: SortCriterion = SortCriterion.COMMITS,
    fetch_exact_dates: bool = True,
    all_branches: bool = True,
    include_merges: bool = False,
    on_progress: ProgressCallback = _noop,
    cancel_event: Optional[threading.Event] = None,
    client: Optional[GitHubClient] = None,
) -> AnalysisResult:
    """
    Com ``all_branches=True`` (padrão), percorre o histórico de TODAS as
    branches via GraphQL, sem contar o mesmo commit duas vezes.

    Com ``all_branches=False``, usa ``/stats/contributors`` (só a branch padrão):
    1. Interpreta a URL;
    2. busca as estatísticas (com *polling*);
    3. monta e ordena o ranking;
    4. opcionalmente busca a data exata do último commit (em paralelo).
    """
    cancel_event = cancel_event or threading.Event()
    owner, repo = parse_repo_url(repo_url)
    client = client or GitHubClient(token)

    if all_branches:
        if not token:
            raise ContributorStatsError(
                "A análise de todas as branches usa a API GraphQL do GitHub, que exige "
                "um token. Informe um PAT ou desative a opção \"todas as branches\"."
            )
        return _analyze_all_branches(
            client, owner, repo, criterion, include_merges, on_progress, cancel_event
        )

    if not token:
        on_progress(
            ProgressEvent(
                "Nenhum token informado: apenas repositórios públicos poderão ser "
                "analisados (limite de 60 requisições/hora).",
                "warning",
            )
        )

    raw = client.fetch_contributors_stats(
        owner, repo, on_progress=on_progress, cancel_event=cancel_event
    )
    contributors = build_contributors(raw)

    if fetch_exact_dates and contributors:
        total = len(contributors)
        on_progress(ProgressEvent("Buscando a data do último commit…", current=0, total=total))

        with ThreadPoolExecutor(max_workers=config.MAX_WORKERS) as pool:
            futures = {
                pool.submit(client.fetch_last_commit_date, owner, repo, c.username): c
                for c in contributors
                if c.profile_url  # ignora autores desconhecidos
            }
            done = total - len(futures)
            for future in as_completed(futures):
                if cancel_event.is_set():
                    for f in futures:
                        f.cancel()
                    raise OperationCancelledError("Operação cancelada.")
                contributor = futures[future]
                try:
                    exact = future.result()
                except Exception:  # falha pontual não interrompe a análise
                    exact = None
                if exact is not None:
                    contributor.last_commit = exact
                    contributor.last_commit_is_estimate = False
                done += 1
                on_progress(
                    ProgressEvent(
                        f"Último commit de {contributor.username}: "
                        f"{contributor.last_commit_display}",
                        current=done,
                        total=total,
                    )
                )

    ranked = rank_contributors(contributors, criterion)
    on_progress(
        ProgressEvent(
            f"Ranking gerado com {len(ranked)} colaborador(es).", "success"
        )
    )
    return AnalysisResult(owner=owner, repo=repo, contributors=ranked, all_branches=False)


def _analyze_all_branches(
    client: GitHubClient,
    owner: str,
    repo: str,
    criterion: SortCriterion,
    include_merges: bool,
    on_progress: ProgressCallback,
    cancel_event: threading.Event,
) -> AnalysisResult:
    """
    Lê o histórico de cada branch (a padrão primeiro) e deduplica os commits:

    - pelo SHA: um commit presente em várias branches conta uma vez só;
    - por "impressão digital" (autor + data de autoria + mensagem + linhas):
      commits copiados por *rebase* ou *cherry-pick* têm outro SHA, mas são o
      mesmo trabalho, então também contam uma vez só.

    Commits de *merge* são ignorados por padrão (as alterações já foram contadas
    nos commits originais da branch).
    """
    on_progress(ProgressEvent(f"Listando as branches de {owner}/{repo}…"))
    default_branch, branches = client.fetch_branches(owner, repo)
    if not branches:
        on_progress(ProgressEvent("O repositório não possui branches/commits.", "warning"))
        return AnalysisResult(owner=owner, repo=repo, all_branches=True,
                              default_branch=default_branch)

    on_progress(ProgressEvent(
        f"{len(branches)} branch(es) encontrada(s). Branch padrão: {default_branch}.", "success"))

    seen_oids: set[str] = set()
    seen_fingerprints: set[tuple] = set()
    walked_tips: set[str] = set()
    commits: list[CommitRecord] = []
    skipped_merges = skipped_copies = 0
    total = len(branches)

    for index, (branch, tip) in enumerate(branches, start=1):
        if cancel_event.is_set():
            raise OperationCancelledError("Operação cancelada.")
        in_default = branch == default_branch
        if tip in walked_tips or tip in seen_oids:
            # Branch sem nenhum commit próprio (aponta para um commit já lido)
            on_progress(ProgressEvent(
                f"Branch {branch}: sem commits novos.", current=index, total=total))
            continue
        walked_tips.add(tip)

        new_here = 0
        for node in client.iter_branch_history(owner, repo, tip, cancel_event=cancel_event):
            oid = node["oid"]
            if oid in seen_oids:
                continue
            seen_oids.add(oid)
            record = client.to_commit_record(node, branch, in_default)
            if record.is_merge and not include_merges:
                skipped_merges += 1
                continue
            fingerprint = (
                record.author_key, record.authored_date, record.message_headline,
                record.additions, record.deletions,
            )
            if fingerprint in seen_fingerprints:
                skipped_copies += 1
                continue
            seen_fingerprints.add(fingerprint)
            commits.append(record)
            new_here += 1

        label = "padrão" if in_default else "novos (fora da padrão)"
        on_progress(ProgressEvent(
            f"Branch {branch}: {new_here} commit(s) {label}.", current=index, total=total))

    if skipped_merges:
        on_progress(ProgressEvent(f"{skipped_merges} commit(s) de merge ignorado(s)."))
    if skipped_copies:
        on_progress(ProgressEvent(
            f"{skipped_copies} commit(s) duplicado(s) por rebase/cherry-pick ignorado(s)."))

    contributors = build_contributors_from_commits(commits, default_branch)
    ranked = rank_contributors(contributors, criterion)
    unmerged = sum(1 for c in commits if not c.in_default_branch)
    on_progress(ProgressEvent(
        f"Ranking gerado com {len(ranked)} colaborador(es) · {len(commits)} commit(s) "
        f"únicos em {total} branch(es), {unmerged} fora da {default_branch}.", "success"))
    return AnalysisResult(
        owner=owner, repo=repo, contributors=ranked, all_branches=True,
        default_branch=default_branch, branch_names=[b for b, _ in branches],
    )
