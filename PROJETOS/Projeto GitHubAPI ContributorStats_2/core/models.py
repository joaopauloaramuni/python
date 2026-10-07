"""Estruturas de dados usadas pela regra de negócio."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Callable, Optional


@dataclass
class Contributor:
    """Métricas consolidadas de um colaborador do repositório."""

    username: str
    profile_url: str
    commits: int
    additions: int
    deletions: int
    last_commit: Optional[date] = None
    # True quando a data veio da semana de atividade (aproximada), e não do commit
    last_commit_is_estimate: bool = False
    rank: int = 0

    @property
    def net_impact(self) -> int:
        """Impacto líquido = linhas inseridas - linhas deletadas."""
        return self.additions - self.deletions

    @property
    def last_commit_display(self) -> str:
        if self.last_commit is None:
            return "N/A"
        text = self.last_commit.strftime("%d/%m/%Y")
        return f"~{text}" if self.last_commit_is_estimate else text

    def to_row(self) -> dict:
        """Linha no formato usado pelo CSV e pelo console."""
        return {
            "Posição": self.rank,
            "Nome de Usuário": self.username,
            "URL Perfil": self.profile_url,
            "Commits Totais": self.commits,
            "Linhas Inseridas": self.additions,
            "Linhas Deletadas": self.deletions,
            "Impacto Líquido (Ins - Del)": self.net_impact,
            "Último Commit": self.last_commit_display,
        }


@dataclass
class AnalysisResult:
    """Resultado completo de uma análise de repositório."""

    owner: str
    repo: str
    contributors: list[Contributor] = field(default_factory=list)

    @property
    def full_name(self) -> str:
        return f"{self.owner}/{self.repo}"

    @property
    def total_commits(self) -> int:
        return sum(c.commits for c in self.contributors)

    @property
    def total_additions(self) -> int:
        return sum(c.additions for c in self.contributors)

    @property
    def total_deletions(self) -> int:
        return sum(c.deletions for c in self.contributors)

    @property
    def total_net_impact(self) -> int:
        return self.total_additions - self.total_deletions


@dataclass
class ProgressEvent:
    """Mensagem de progresso enviada pela regra de negócio à interface (CLI ou GUI)."""

    message: str
    level: str = "info"  # info | success | warning | error
    current: Optional[int] = None
    total: Optional[int] = None


ProgressCallback = Callable[[ProgressEvent], None]
