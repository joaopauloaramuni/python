"""Transformação dos dados brutos da API em um ranking de colaboradores."""

from __future__ import annotations

from datetime import date, datetime, timezone
from enum import Enum
from typing import Iterable, Optional

from .models import Contributor


class SortCriterion(str, Enum):
    """Critérios de ordenação do ranking (critério principal + desempate)."""

    COMMITS = "commits"
    NET_IMPACT = "impacto"
    ADDITIONS = "insercoes"

    @property
    def label(self) -> str:
        return {
            SortCriterion.COMMITS: "Commits (desempate: impacto líquido)",
            SortCriterion.NET_IMPACT: "Impacto líquido (desempate: commits)",
            SortCriterion.ADDITIONS: "Linhas inseridas (desempate: commits)",
        }[self]

    def key(self, c: Contributor) -> tuple:
        if self is SortCriterion.COMMITS:
            return (c.commits, c.net_impact)
        if self is SortCriterion.NET_IMPACT:
            return (c.net_impact, c.commits)
        return (c.additions, c.commits)


def _last_active_week(weeks: Iterable[dict]) -> Optional[date]:
    """Início da última semana com commits (usado como data aproximada)."""
    active = [w["w"] for w in weeks if w.get("c", 0) > 0 and "w" in w]
    if not active:
        return None
    return datetime.fromtimestamp(max(active), tz=timezone.utc).date()


def build_contributors(contributors_data: list[dict]) -> list[Contributor]:
    """
    Converte o JSON de ``/stats/contributors`` em objetos :class:`Contributor`.

    Não faz nenhuma requisição: a data do último commit é preenchida aqui com
    uma estimativa (semana da última atividade) e pode ser refinada depois.
    """
    contributors: list[Contributor] = []

    for item in contributors_data:
        # 'author' pode vir nulo (ex.: conta excluída / e-mail não vinculado)
        author = item.get("author") or {}
        username = author.get("login") or "(usuário desconhecido)"
        profile_url = author.get("html_url") or ""
        weeks = item.get("weeks") or []

        contributors.append(
            Contributor(
                username=username,
                profile_url=profile_url,
                commits=int(item.get("total", 0)),
                additions=sum(int(w.get("a", 0)) for w in weeks),
                deletions=sum(int(w.get("d", 0)) for w in weeks),
                last_commit=_last_active_week(weeks),
                last_commit_is_estimate=True,
            )
        )

    return contributors


def rank_contributors(
    contributors: list[Contributor],
    criterion: SortCriterion = SortCriterion.COMMITS,
) -> list[Contributor]:
    """Ordena (decrescente) e preenche o campo ``rank`` (1, 2, 3…)."""
    ranked = sorted(contributors, key=criterion.key, reverse=True)
    for position, contributor in enumerate(ranked, start=1):
        contributor.rank = position
    return ranked
