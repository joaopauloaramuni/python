"""Interpretação de URLs / identificadores de repositórios do GitHub."""

from __future__ import annotations

import re
from urllib.parse import urlparse

from .exceptions import InvalidRepoURLError

# Nomes válidos de usuário/organização e de repositório no GitHub
_NAME_RE = re.compile(r"^[A-Za-z0-9_.-]+$")


def parse_repo_url(repo_url: str) -> tuple[str, str]:
    """
    Extrai ``(owner, repo)`` de diversos formatos aceitos:

    - ``https://github.com/owner/repo``
    - ``https://github.com/owner/repo.git`` ou ``.../tree/main/pasta``
    - ``github.com/owner/repo``
    - ``git@github.com:owner/repo.git``
    - ``owner/repo``

    Lança :class:`InvalidRepoURLError` se não for possível interpretar.
    """
    text = (repo_url or "").strip()
    if not text:
        raise InvalidRepoURLError("Informe a URL do repositório.")

    # Formato SSH: git@github.com:owner/repo.git
    if text.startswith("git@"):
        _, _, text = text.partition(":")
        path = text
    else:
        if "://" not in text and text.lower().startswith("github.com"):
            text = "https://" + text
        parsed = urlparse(text)
        if parsed.scheme and parsed.netloc:
            host = parsed.netloc.lower()
            if host not in ("github.com", "www.github.com"):
                raise InvalidRepoURLError(
                    f"O host '{parsed.netloc}' não é github.com."
                )
            path = parsed.path
        else:
            path = text  # formato curto owner/repo

    parts = [p for p in path.strip("/").split("/") if p]
    if len(parts) < 2:
        raise InvalidRepoURLError(
            "URL inválida. Use o formato https://github.com/<dono>/<repositório>."
        )

    owner, repo = parts[0], parts[1]
    if repo.endswith(".git"):
        repo = repo[:-4]

    if not (_NAME_RE.match(owner) and _NAME_RE.match(repo)):
        raise InvalidRepoURLError(f"Nome de repositório inválido: {owner}/{repo}")

    return owner, repo
