"""
Configurações centrais do projeto.
"""

from __future__ import annotations

import os

# ======================================================================
# 🔑 COLOQUE AQUI O SEU TOKEN DE ACESSO PESSOAL (PAT) DO GITHUB
#    Gere em: https://github.com/settings/tokens  (escopo "repo")
#    Exemplo: GITHUB_TOKEN = "ghp_AbCdEf123..."
#    ⚠️ Não faça commit/push do seu token real para o GitHub!
# ======================================================================
GITHUB_TOKEN = "SEU_TOKEN_AQUI"  # Substitua pelo seu token real

# URL base da API REST do GitHub
GITHUB_API_BASE = "https://api.github.com"

# Versão da API recomendada pela documentação oficial
GITHUB_API_VERSION = "2022-11-28"

# Repositório usado como exemplo quando nenhuma URL é informada
DEFAULT_REPO_URL = (
    "https://github.com/ICEI-PUC-Minas-PMGES-TI/ti3-es-template-repository"
)

# Polling do endpoint /stats/contributors (a API responde 202 enquanto calcula)
MAX_TRIES = 6
WAIT_TIME = 10  # segundos entre tentativas

# Tempo máximo (s) de cada requisição HTTP
REQUEST_TIMEOUT = 30

# Nº de requisições simultâneas ao buscar a data do último commit de cada usuário
MAX_WORKERS = 8

# Valor de exemplo (indica que o token ainda não foi substituído)
TOKEN_PLACEHOLDER = "SEU_TOKEN_AQUI"

# Variável de ambiente opcional, usada só se o token acima não for preenchido
TOKEN_ENV_VAR = "GITHUB_TOKEN"


def get_configured_token() -> str | None:
    """
    Retorna o token configurado em ``GITHUB_TOKEN`` (acima, no código).
    Se ele ainda for o valor de exemplo, tenta a variável de ambiente
    ``GITHUB_TOKEN``. Retorna ``None`` se nenhum token foi definido.
    """
    for token in (GITHUB_TOKEN, os.getenv(TOKEN_ENV_VAR, "")):
        token = (token or "").strip()
        if token and token != TOKEN_PLACEHOLDER:
            return token
    return None
