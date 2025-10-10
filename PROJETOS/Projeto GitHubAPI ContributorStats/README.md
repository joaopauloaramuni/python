# 🚀 Projeto GitHubAPI ContributorStats

O **GitHubAPI ContributorStats** é uma ferramenta Python desenvolvida para analisar repositórios do GitHub (públicos e **privados**) e gerar um **ranking detalhado dos colaboradores** com base em métricas reais de código. O projeto utiliza o Token de Acesso Pessoal (PAT) do GitHub para acessar os dados e lida com o processamento assíncrono das estatísticas da API, garantindo uma execução robusta e automática.

### 🎯 Objetivo

O objetivo principal é fornecer uma visão clara de quem mais contribuiu para um repositório, não apenas em termos de frequência de *commits*, mas também pelo **volume de linhas de código** adicionadas e removidas (**Impacto Líquido**). O resultado é exportado para um arquivo CSV de fácil consumo.

---

## 🛠️ Pré-requisitos

- **Python 3.7+** instalado.
- Acesso a um **Personal Access Token (PAT)** do GitHub com o *scope* **`repo`** marcado (necessário para repositórios privados).

---

## 🐍 Ambiente virtual (recomendado)
1. **Crie o ambiente virtual:**
```bash
python -m venv .venv
```

2. **Ative o ambiente virtual:**

- **Windows:**
```bash
.venv\Scripts\activate
```

- **Linux/macOS:**
```bash
source .venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install requests
```

---

## ⚙️ Execução

### 1. Configuração

Substitua o *placeholder* `"SEU_TOKEN_AQUI"` (ou o token de exemplo) pela sua chave real de **PAT** na variável `GITHUB_TOKEN` do arquivo `contributor_stats.py`.

### 2. Comando Principal

Execute o script principal, passando a URL do repositório como argumento (ou usando a URL padrão definida no script):

```bash
python contributor_stats.py <URL_DO_REPOSITORIO_AQUI>
```

**Exemplo (com a URL padrão):**
```bash
python contributor_stats.py
```

### 3. Exemplo de Saída no Terminal

A ferramenta exibe o progresso do *pooling* da API e, após o sucesso, mostra o Top 10 no console:

```
Buscando estatísticas (Tentativa 1/6) de: [https://api.github.com/repos/ICEI-PUC-Minas-PMGES-TI/](https://api.github.com/repos/ICEI-PUC-Minas-PMGES-TI/)...
Dados de contribuição recebidos com sucesso.

✅ Sucesso! Ranking exportado para: ranking_contribuicao_pmg-es-2025-2-ti3-9577100-repoexemplo.csv
As métricas são: Commits Totais, Linhas Inseridas, Linhas Deletadas e Impacto Líquido.

--- TOP 10 Contribuidores (Console) ---
1. aluno1 (https://github.com/aluno1)
   -> Commits: 77 | Inserções: 39 | Deletas: 34 | Impacto Líquido: 5
2. aluno2 (https://github.com/aluno2)
   -> Commits: 29 | Inserções: 1495 | Deletas: 884 | Impacto Líquido: 611
3. aluno3 (https://github.com/aluno3)
   -> Commits: 23 | Inserções: 2186 | Deletas: 305 | Impacto Líquido: 1881
4. aluno4 (https://github.com/aluno4)
   -> Commits: 14 | Inserções: 66 | Deletas: 29 | Impacto Líquido: 37
5. aluno5 (https://github.com/aluno5)
   -> Commits: 10 | Inserções: 196 | Deletas: 7 | Impacto Líquido: 189
6. aluno6 (https://github.com/aluno6)
   -> Commits: 9 | Inserções: 19020 | Deletas: 17984 | Impacto Líquido: 1036
7. professor1 (https://github.com/professor1)
   -> Commits: 5 | Inserções: 10 | Deletas: 5 | Impacto Líquido: 5
8. github-classroom[bot] (https://github.com/apps/github-classroom)
   -> Commits: 2 | Inserções: 476 | Deletas: 0 | Impacto Líquido: 476
...
```

---

## 📊 O que cada função faz

Abaixo seguem as assinaturas das funções presentes no script e uma explicação curta do propósito de cada uma:

| Função | Assinatura | Propósito |
| :--- | :--- | :--- |
| **`parse_repo_url`** | `(repo_url: str) -> tuple[str, str]` | Extrai o **dono** e o **nome** do repositório a partir da URL. |
| **`fetch_contributors_stats`** | `(owner: str, repo_name: str) -> list` | Faz requisições à API, implementando um **loop de retentativa** para lidar com o processamento de dados (`202 Accepted`). |
| **`generate_ranking`** | `(contributors_data: list) -> list` | Processa os dados brutos, calcula o **Impacto Líquido** (`Inseridas - Deletadas`) e ordena os colaboradores. |
| **`export_to_csv`** | `(ranking: list, repo_name: str)` | Cria e salva um arquivo CSV com o ranking final, usando ponto e vírgula (`;`) como delimitador. |
| **`main`** | `(repo_url: str)` | Função principal que coordena a execução do script. |

---

## 📚 Documentação e Links Úteis

- 🔑 **Página de Geração de Tokens (PATs) no GitHub:** [github.com/settings/tokens](https://github.com/settings/tokens)
- 🔑 **Como criar seu Personal Access Token (PAT):** [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- 🧩 **Documentação oficial da API do GitHub (Estatísticas):** [REST API Endpoints for Repository Statistics](https://docs.github.com/en/rest/metrics/statistics?apiVersion=2022-11-28)
- 🐍 **Documentação oficial do módulo `requests`:** [Python Requests](https://docs.python-requests.org/en/latest/)

---

## 🧾 Licença

Este projeto é disponibilizado sob a licença **MIT**.

---
