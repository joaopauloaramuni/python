"""
GitHubAPI ContributorStats — interface de linha de comando (CLI).

Toda a regra de negócio está no pacote ``core``; este arquivo só lê os
argumentos, exibe o progresso no terminal e mostra o Top N.

Uso:
    python contributor_stats.py [URL] [--token TOKEN] [--sort commits|impacto|insercoes]
                                [--no-exact-dates] [--output arquivo.csv] [--top 10]

Para a interface gráfica, execute:  python main_gui.py
"""

from __future__ import annotations

import argparse
import sys

from core import (
    ContributorStatsError,
    ProgressEvent,
    SortCriterion,
    analyze_repository,
    default_csv_filename,
    export_to_csv,
)
from core.config import DEFAULT_REPO_URL, get_configured_token

_ICONS = {"info": "•", "success": "✔", "warning": "!", "error": "✖"}


def print_progress(event: ProgressEvent) -> None:
    icon = _ICONS.get(event.level, "•")
    counter = f"[{event.current}/{event.total}] " if event.total else ""
    print(f"{icon} {counter}{event.message}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Gera o ranking de colaboradores de um repositório do GitHub."
    )
    parser.add_argument(
        "repo_url", nargs="?", default=DEFAULT_REPO_URL,
        help="URL do repositório (ou owner/repo). Padrão: repositório de exemplo.",
    )
    parser.add_argument(
        "--token", default=None,
        help="Personal Access Token. Se omitido, usa o GITHUB_TOKEN de core/config.py.",
    )
    parser.add_argument(
        "--sort", choices=[c.value for c in SortCriterion], default=SortCriterion.COMMITS.value,
        help="Critério de ordenação (padrão: commits).",
    )
    parser.add_argument(
        "--no-exact-dates", action="store_true",
        help="Não busca a data exata do último commit (usa a semana aproximada; mais rápido).",
    )
    parser.add_argument("--output", "-o", default=None, help="Caminho do CSV de saída.")
    parser.add_argument("--top", type=int, default=10, help="Quantos exibir no console.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    token = args.token or get_configured_token()

    try:
        result = analyze_repository(
            args.repo_url,
            token,
            criterion=SortCriterion(args.sort),
            fetch_exact_dates=not args.no_exact_dates,
            on_progress=print_progress,
        )
    except ContributorStatsError as exc:
        print(f"\n✖ ERRO: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário.", file=sys.stderr)
        return 130

    if not result.contributors:
        print("\nNenhum colaborador encontrado.")
        return 0

    output = args.output or default_csv_filename(result.repo)
    path = export_to_csv(result.contributors, output)
    print(f"\n✅ Sucesso! Ranking exportado para: {path}")

    print(f"\n--- TOP {args.top} Contribuidores — {result.full_name} ---")
    for c in result.contributors[: args.top]:
        print(f"{c.rank}. {c.username} ({c.profile_url})")
        print(
            f"   -> Commits: {c.commits} | Inseridas: {c.additions} | "
            f"Deletadas: {c.deletions} | Impacto Líquido: {c.net_impact} | "
            f"Último Commit: {c.last_commit_display}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
