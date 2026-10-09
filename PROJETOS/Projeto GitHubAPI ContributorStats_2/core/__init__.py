"""
Regra de negócio do GitHubAPI ContributorStats.

Este pacote não depende de nenhuma interface (CLI ou GUI).
"""

from .exceptions import (
    ContributorStatsError,
    GitHubAPIError,
    InvalidRepoURLError,
    OperationCancelledError,
    StatsNotReadyError,
)
from .exporter import default_csv_filename, export_to_csv
from .github_client import GitHubClient
from .models import AnalysisResult, CommitRecord, Contributor, ProgressEvent
from .ranking import (
    SortCriterion,
    build_contributors,
    build_contributors_from_commits,
    rank_contributors,
)
from .repo_url import parse_repo_url
from .service import analyze_repository

__all__ = [
    "AnalysisResult",
    "CommitRecord",
    "Contributor",
    "ContributorStatsError",
    "GitHubAPIError",
    "GitHubClient",
    "InvalidRepoURLError",
    "OperationCancelledError",
    "ProgressEvent",
    "SortCriterion",
    "StatsNotReadyError",
    "analyze_repository",
    "build_contributors",
    "build_contributors_from_commits",
    "default_csv_filename",
    "export_to_csv",
    "parse_repo_url",
    "rank_contributors",
]
