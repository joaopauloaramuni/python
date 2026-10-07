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
from .exceptions import OperationCancelledError
from .github_client import GitHubClient
from .models import AnalysisResult, ProgressCallback, ProgressEvent
from .ranking import SortCriterion, build_contributors, rank_contributors
from .repo_url import parse_repo_url


def _noop(_: ProgressEvent) -> None:
    pass


def analyze_repository(
    repo_url: str,
    token: Optional[str] = None,
    *,
    criterion: SortCriterion = SortCriterion.COMMITS,
    fetch_exact_dates: bool = True,
    on_progress: ProgressCallback = _noop,
    cancel_event: Optional[threading.Event] = None,
    client: Optional[GitHubClient] = None,
) -> AnalysisResult:
    """
    1. Interpreta a URL;
    2. busca as estatísticas (com *polling*);
    3. monta e ordena o ranking;
    4. opcionalmente busca a data exata do último commit (em paralelo).
    """
    cancel_event = cancel_event or threading.Event()
    owner, repo = parse_repo_url(repo_url)
    client = client or GitHubClient(token)

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
    return AnalysisResult(owner=owner, repo=repo, contributors=ranked)
