"""Exceções da regra de negócio (a camada de apresentação decide como exibi-las)."""

from __future__ import annotations


class ContributorStatsError(Exception):
    """Erro base do projeto."""


class InvalidRepoURLError(ContributorStatsError):
    """A URL / identificador do repositório não pôde ser interpretado."""


class GitHubAPIError(ContributorStatsError):
    """A API do GitHub retornou um erro (ou não pôde ser acessada)."""

    def __init__(self, message: str, status_code: int | None = None):
        super().__init__(message)
        self.status_code = status_code


class StatsNotReadyError(ContributorStatsError):
    """O GitHub não terminou de calcular as estatísticas dentro do tempo limite."""


class OperationCancelledError(ContributorStatsError):
    """A operação foi cancelada pelo usuário."""
