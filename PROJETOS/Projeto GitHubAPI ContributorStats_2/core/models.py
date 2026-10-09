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
    # Commits que não estão na branch padrão (só no modo "todas as branches")
    unmerged_commits: Optional[int] = None
    # Branches (exceto a padrão) em que o colaborador tem commits ainda não mergeados
    branches: list[str] = field(default_factory=list)

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
            "Commits Fora da Branch Padrão": (
                "" if self.unmerged_commits is None else self.unmerged_commits
            ),
            "Branches (não mergeadas)": ", ".join(self.branches),
        }


@dataclass
class AnalysisResult:
    """Resultado completo de uma análise de repositório."""

    owner: str
    repo: str
    contributors: list[Contributor] = field(default_factory=list)
    # True = considerou todas as branches; False = só a branch padrão
    all_branches: bool = False
    default_branch: Optional[str] = None
    branch_names: list[str] = field(default_factory=list)

    @property
    def scope_label(self) -> str:
        if self.all_branches:
            return f"todas as branches ({len(self.branch_names)})"
        return f"branch padrão ({self.default_branch})" if self.default_branch else "branch padrão"

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
class CommitRecord:
    """Um commit lido de uma branch (modo "todas as branches")."""

    oid: str
    author_key: str          # login do GitHub ou, na falta dele, o e-mail
    author_name: str
    profile_url: str
    additions: int
    deletions: int
    authored_date: str       # ISO 8601
    committed_date: str      # ISO 8601
    message_headline: str
    is_merge: bool
    branch: str              # primeira branch em que o commit foi encontrado
    in_default_branch: bool


@dataclass
class ProgressEvent:
    """Mensagem de progresso enviada pela regra de negócio à interface (CLI ou GUI)."""

    message: str
    level: str = "info"  # info | success | warning | error
    current: Optional[int] = None
    total: Optional[int] = None


ProgressCallback = Callable[[ProgressEvent], None]
