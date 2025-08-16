# 🐍 Cliente Python para a API do NVD (CVE / CVE History)

Este projeto é um **cliente Python simples e modular** para consumir a **API do NVD (National Vulnerability Database)** e transformar as respostas JSON em **informações úteis** e um **DataFrame do Pandas** para análise.

> **O que ele resolve?**  
> A resposta crua do NVD é extensa. Este cliente busca, **resume** e organiza os campos mais relevantes (ID do CVE, datas, descrição, CVSS, CWE e referências) e fornece funções utilitárias para diferentes consultas (por ID, por CPE, por palavra-chave, por datas, paginação e histórico de mudanças).

---

## 📝 Siglas e conceitos

- **NIST (National Institute of Standards and Technology)**  
  Instituição norte-americana responsável por desenvolver padrões, diretrizes e boas práticas em ciência e tecnologia, incluindo segurança da informação.

- **NVD (National Vulnerability Database)**  
  Banco de dados mantido pelo NIST que armazena informações sobre vulnerabilidades conhecidas em softwares e hardwares, fornecendo métricas e referências detalhadas.

- **CVE (Common Vulnerabilities and Exposures)**  
  Identificador único para cada vulnerabilidade conhecida. Permite referência padronizada entre diferentes bases de dados, ferramentas de segurança e relatórios.

- **CVSS (Common Vulnerability Scoring System)**  
  Sistema de pontuação que quantifica a gravidade de uma vulnerabilidade (baixa, média, alta, crítica), facilitando a priorização de correções.

- **CWE (Common Weakness Enumeration)**  
  Catálogo de tipos de falhas e vulnerabilidades de software, descrevendo padrões de código ou design que podem levar a vulnerabilidades exploráveis.

---

## 🎯 Objetivo geral do NIST e do NVD

O **NIST** visa melhorar a segurança e confiabilidade de sistemas, promovendo padrões, frameworks e dados de referência.  
O **NVD**, mantido pelo NIST, fornece **informações centralizadas e estruturadas** sobre vulnerabilidades conhecidas, permitindo que organizações monitorem riscos, priorizem correções e automatizem análises de segurança.

---

## 🛠️ Recursos

- 🔎 **Consultas**:
  - Por **ID de CVE**
  - Por **CPE** (com opção `isVulnerable`)
  - Por **palavra-chave** (com `keywordExactMatch`)
  - Por intervalo de **publicação** (`pubStartDate`/`pubEndDate`)
  - **Paginação** (`resultsPerPage`/`startIndex`)
  - **Histórico** de mudanças de um CVE (API `cvehistory`)
- 🧩 **Parsing amigável**: função `parse_cve` que extrai apenas os campos essenciais
  - Suporte a **CVSS v2** e **v3.1**
  - Campos opcionais (CVSS, CWE, referências) tratados automaticamente
- 🧮 **DataFrame do Pandas** pronto para análise
- 💾 **Exportação**: salvar DataFrame em Excel (`.xlsx`) usando `df.to_excel()`
- 📎 **Referências** (URLs) preservadas para investigação
- ✅ Código organizado em **funções** para reuso e testes

---

## 🗂️ Estrutura do código

O arquivo principal (script) contém:

- **Constantes**
  - `BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"`
  - `HISTORY_URL = "https://services.nvd.nist.gov/rest/json/cvehistory/2.0"`

- **Funções de busca**
  - `fetch_cves(params)` – _wrapper_ genérico
  - `fetch_cve_by_id(cve_id)`
  - `fetch_cves_by_cpe(cpe_name, is_vulnerable=False)`
  - `fetch_cves_by_keyword(keyword, exact_match=False)`
  - `fetch_cves_by_date(pub_start, pub_end)`
  - `fetch_paginated_cves(results_per_page=20, max_pages=1)`
  - `fetch_cve_history(cve_id=None, change_start=None, change_end=None)`

- **Funções de parsing/análise**
  - `parse_cve(cve)` – extrai campos úteis
  - `cves_to_dataframe(cves)` – gera um `pandas.DataFrame`

- **Bloco de exemplo (`if __name__ == "__main__":`)**
  - Demonstra busca por palavra-chave, conversão para DataFrame e impressão das primeiras linhas.

---

## 📋 Requisitos

- Python 3.8 ou superior  
- Bibliotecas Python:
  - `requests` – para fazer chamadas HTTP à API NVD  
  - `pandas` – para manipulação e análise de dados em DataFrames  
- Conexão com a internet para acessar a API NVD  
- Opcional: ambiente virtual para isolar dependências

---

## 🛠️ Instalação

```bash
pip install requests pandas
```

Se preferir, em um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # no Windows: .venv\Scripts\activate
pip install requests pandas
```

---

### ⚡ Como usar

> Copie o conteúdo do script para um arquivo, por exemplo `nvd_client.py`, e execute com `python nvd_client.py`.

---

## 🔍 Consultas

### 🔎 Buscar por palavra-chave

```python
raw = fetch_cves_by_keyword("Microsoft", exact_match=False)
cves = raw.get("vulnerabilities", [])
# 📝 Converte para DataFrame para análise
df = cves_to_dataframe(cves)
# 👀 Mostra as primeiras linhas
print(df.head())

# 💾 Exportar para Excel
df.to_excel("cves_microsoft.xlsx", index=False)
print("Arquivo 'cves_microsoft.xlsx' gerado com sucesso!")
```

#### ⚠️ Observações

- O DataFrame inclui apenas os campos extraídos pelo `parse_cve`:  
  `id`, `published`, `last_modified`, `description`, `cvss_score`, `severity`, `cwe_ids` e `references`.
- O script trata métricas **CVSS v2** e **v3.1** automaticamente.
- Campos opcionais (ex.: CVSS, CWE ou referências) podem não estar presentes para todos os CVEs,  
  mas `parse_cve` já faz o tratamento para não gerar erros.

### 🆔 Buscar por ID de CVE

```python
raw = fetch_cve_by_id("CVE-2019-1010218")
cves = raw.get("vulnerabilities", [])
if cves:
    # 🔍 Exibe detalhes simplificados do CVE
    print(parse_cve(cves[0]))
```

### 💻 Buscar por CPE (ex.: Microsoft Windows 10)

```python
raw = fetch_cves_by_cpe("cpe:2.3:o:microsoft:windows_10:1607:*:*:*:*:*:*:*", is_vulnerable=True)
cves = raw.get("vulnerabilities", [])
# 📊 Mostra quantidade de CVEs encontrados
print(len(cves), "registros")
```

### 📅 Buscar por intervalo de **publicação**

> Datas no formato ISO-8601 estendido (ver mais abaixo).

```python
# 🔹 Buscar CVEs publicados em janeiro de 2023
raw = fetch_cves_by_date("2023-01-01T00:00:00.000Z", "2023-01-31T23:59:59.999Z")
cves = raw.get("vulnerabilities", [])
```

### 📄 Paginar grandes coleções

```python
# 🔹 Baixar até 2 páginas de 100 itens cada (até 200 CVEs)
page = fetch_paginated_cves(results_per_page=100, max_pages=2)
print("📊 Itens recebidos:", len(page))
```

💡 Dica: use paginação para evitar sobrecarga e respeitar limites da API.

### 🕒 Histórico de mudanças de um CVE

Você pode consultar alterações de um CVE específico usando `fetch_cve_history`:

```python
# 🔹 Buscar histórico de um CVE
hist = fetch_cve_history(cve_id="CVE-2019-1010218")

# 🔹 Ver chaves principais do retorno
print(hist.keys())  # Ex.: 'cveChanges', 'resultsPerPage', 'totalResults', etc.
```

### 📈 Transformar em DataFrame

Depois de buscar CVEs (por exemplo, `raw.get("vulnerabilities", []))`, é possível analisar em um DataFrame:

```python
# 🔹 Converter lista de CVEs em DataFrame
df = cves_to_dataframe(cves)

# 🔹 Ver primeiras linhas
print(df.head())

# 🔹 Explorar colunas disponíveis
print(df.columns.tolist())
```

### 📊 Filtrar e ordenar no DataFrame

Após converter os CVEs em DataFrame (`cves_to_dataframe`), você pode facilmente filtrar e ordenar os dados para análises:

```python
# 🔹 Filtrar apenas CVEs com severidade HIGH ou CRITICAL
df_high = df[df["severity"].isin(["HIGH", "CRITICAL"])]

# 🔹 Top 10 CVEs por pontuação CVSS (decrescente)
top10 = df.sort_values("cvss_score", ascending=False).head(10)

# 🔹 Filtrar CVEs com CVSS >= 7.0
df_cvss7 = df[df["cvss_score"] >= 7.0]

# 🔹 Ordenar por data de publicação (mais recentes primeiro)
df_recent = df.sort_values("published", ascending=False)

# 🔹 Ver colunas disponíveis no DataFrame
print(df.columns.tolist())

# 🔹 Selecionar colunas específicas
df_subset = df[["id", "description", "cvss_score", "severity"]]
```

---

## 📅 Formato de datas (ISO-8601 estendido)

A API usa carimbos no formato `YYYY-MM-DDTHH:MM:SS[.mmm][Z|±HH:MM]`. Exemplos válidos:
- `2023-01-01T00:00:00.000Z`
- `2020-01-14T23:59:59.999-05:00`

> ⚠️ **Importante:** quando usar intervalo de datas (p. ex. `pubStartDate`/`pubEndDate`), o **máximo** de abrangência permitido é **120 dias**.

---

## 🏗️ Boas práticas e limites da API

- 📄 **Paginação:** a API é **paginada** (`resultsPerPage`, `startIndex`). O helper `fetch_paginated_cves` já controla isso por páginas sequenciais.
- ⏳ **Coleta incremental:** para manter-se atualizado, use os filtros por **data** (publicação ou última modificação) desde a última execução.
- ⚡ **Limites / rate-limit:** em cenários de alto volume, aplique espera entre requisições ou reduza `resultsPerPage`.
- 🔗 **CPE vs. Virtual Match:** este cliente usa `cpeName` diretamente. Para buscas mais amplas, a API oferece `virtualMatchString` (não implementado neste script, veja “Extensões”).

---

## ✨ Extensões sugeridas

Ideias para evoluir o cliente (mantendo a mesma arquitetura):

- 🔎 **Filtros adicionais**:
  - `cvssV3Severity` / `cvssV4Severity`
  - `cweId`
  - `hasKev`, `hasCertAlerts`, `hasCertNotes`, etc.
- ⏱️ **Parâmetros por última modificação** (`lastModStartDate` / `lastModEndDate`)
- 🧩 **Suporte a `virtualMatchString`** com faixas de versão (`versionStart` / `versionEnd`)
- 🔄 **Backoff exponencial** e tratamento específico para **HTTP 429**
- 🔐 **Suporte opcional a API key** do NVD para aumentar limites de uso

---

## ⚠️ Erros Comuns

- ❌ **`HTTPError: 4xx/5xx`**  
  ✔️ Verifique os parâmetros enviados, principalmente o formato das datas (`YYYY-MM-DDTHH:MM:SS:000 UTC+00:00`).

- ❌ **Intervalo de datas > 120 dias**  
  ✔️ A API da NVD rejeita consultas muito longas. Divida sua busca em intervalos menores.

- ❌ **Sem campo `"vulnerabilities"` na resposta**  
  ✔️ Isso significa que a consulta não trouxe resultados ou houve erro de parâmetros.

- ❌ **Rate limit da API**  
  ✔️ Muitas requisições em pouco tempo podem causar bloqueio temporário. Use `time.sleep()` entre chamadas ou configure uma API Key.

- ❌ **Campos opcionais ausentes**  
  ✔️ Nem todos os CVEs possuem CVSS v3.1, CWE ou referências. O código já trata isso, mas é bom sempre validar.

- ❌ **Erro de conexão**  
  ✔️ Pode ser causado por queda de rede ou indisponibilidade da NVD. Rode novamente mais tarde ou use `try/except` para capturar exceções.

---

## 📚 Documentação e links úteis

- **NVD API - Vulnerabilities**  
  [https://nvd.nist.gov/developers/vulnerabilities](https://nvd.nist.gov/developers/vulnerabilities)

- **Documentação oficial do Pandas** (manipulação e análise de dados em DataFrames)  
  [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)

- **Documentação Requests** (requisições HTTP para consumir APIs REST)  
  [https://requests.readthedocs.io/en/latest/](https://requests.readthedocs.io/en/latest/)

- **Especificação CVE (MITRE)**  
  [https://cve.mitre.org/](https://cve.mitre.org/)

- **Common Weakness Enumeration (CWE)**  
  [https://cwe.mitre.org/](https://cwe.mitre.org/)

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.
