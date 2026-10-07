"""Exportação do ranking para CSV."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Union

from .models import Contributor

CSV_FIELDS = [
    "Posição",
    "Nome de Usuário",
    "URL Perfil",
    "Commits Totais",
    "Linhas Inseridas",
    "Linhas Deletadas",
    "Impacto Líquido (Ins - Del)",
    "Último Commit",
]


def default_csv_filename(repo_name: str) -> str:
    return f"ranking_contribuicao_{repo_name}.csv"


def export_to_csv(
    contributors: list[Contributor],
    path: Union[str, Path],
    delimiter: str = ";",
) -> Path:
    """
    Grava o ranking em CSV e retorna o caminho do arquivo.

    Usa ``utf-8-sig`` (UTF-8 com BOM) para que o Excel exiba os acentos
    corretamente, e ``;`` como separador (padrão do Excel em pt-BR).
    """
    path = Path(path)
    if not contributors:
        raise ValueError("Não há dados de ranking para exportar.")

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(c.to_row() for c in contributors)
    return path
