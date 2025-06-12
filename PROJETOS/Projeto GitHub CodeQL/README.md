# 🔍 Análise Estática com CodeQL para Projetos Java

Este projeto automatiza a análise de repositórios Java utilizando o **CodeQL**, uma poderosa ferramenta de análise estática mantida pelo GitHub. Através de um script em Python, é possível clonar um repositório, criar um banco de dados CodeQL e executar múltiplas *query suites* para identificar vulnerabilidades, problemas de qualidade e padrões inseguros no código.

---

## 📘 O que é o CodeQL?

O **CodeQL** transforma o código-fonte em um banco de dados que pode ser consultado com queries escritas em uma linguagem lógica baseada em Datalog. Ele é amplamente utilizado para encontrar vulnerabilidades, code smells e erros comuns em código de forma automatizada.

> 🔗 [Sobre o CodeQL – Documentação oficial](https://codeql.github.com/docs/codeql-overview/about-codeql/)

---

## ☕ Análise de Projetos Java

Este projeto foi feito especificamente para analisar repositórios Java. O processo inclui:

1. Clonagem do repositório.
2. Compilação via Maven.
3. Criação de banco de dados com o CodeQL.
4. Execução de várias *query suites* para detectar problemas.

---

## 🖼️ Captura de Tela

| ![CodeQL](https://joaopauloaramuni.github.io/python-imgs/GitHub_CodeQL/imgs/codeql.png) |
|:-----------------------------:|
|         GitHub CodeQL         |

---

## 📦 Query Suites utilizadas

As *query suites* são conjuntos de queries CodeQL agrupadas por propósito. As seguintes suites são utilizadas neste projeto:

```python
QUERY_SUITES = [
    "java-code-quality.qls",
    "java-code-scanning.qls",
    "java-lgtm-full.qls",
    "java-lgtm.qls",
    "java-security-and-quality.qls",
    "java-security-experimental.qls",
    "java-security-extended.qls"
]
```

Cada uma cobre diferentes aspectos da análise de código, como qualidade, segurança e verificações experimentais.

---

## 🧠 Explicação das Funções

- `clone_repo(repo_url, local_path)`: Clona um repositório Git no diretório especificado.
- `create_codeql_database(source_path, db_path)`: Cria o banco de dados CodeQL compilando o projeto com Maven.
- `run_codeql_analysis(db_path, query_suite_path, output_file)`: Executa uma análise CodeQL com a query suite e salva o resultado no formato SARIF.
- `run_all_analyses(db_path, base_query_path, query_suites)`: Executa todas as análises usando as suites listadas.
- `cleanup(path)`: Remove diretórios antigos, evitando conflitos nas análises.
- `main()`: Orquestra todo o processo: limpeza, clonagem, criação do banco de dados e execução das análises.

---

## 🔍 Explicando o comando codeql

```python
print(f"[INFO] Rodando análise CodeQL com {query_suite_path}...")
subprocess.run([
    "codeql", "database", "analyze", db_path,
    query_suite_path,
    "--format=sarifv2.1.0",
    f"--output={output_file}",
    '--ram=8192'
], check=True)
```

Esse trecho executa a análise CodeQL:
- `codeql database analyze`: comando que executa a análise sobre o banco de dados.
- `--format=sarifv2.1.0`: define o formato de saída (SARIF, padrão para scanners de segurança).
- `--output`: arquivo onde os resultados serão salvos.
- `--ram=8192`: usa 8 GB de RAM para evitar falhas durante a análise.

---

## 📁 Estrutura de diretórios e arquivos

Durante a execução do projeto, os seguintes diretórios são utilizados ou criados automaticamente:

- `./repo_temp/`  
  Diretório temporário onde o repositório Java será clonado antes da análise.

- `./codeql-db/`  
  Diretório onde o banco de dados CodeQL será criado. Ele armazena uma versão compilada do código-fonte, necessária para que o CodeQL realize a análise.

- `./results/`  
  Diretório onde serão salvos os arquivos de saída no formato [SARIF](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/sarif-output), contendo os resultados da análise.

- As Query Suites (`.qls`) utilizadas nas análises devem estar localizadas no seguinte caminho relativo:

  ```python
  base_query_path = os.path.join("codeql", "java", "ql", "src", "codeql-suites")
  ```

> ⚠️ Certifique-se de que o diretório `codeql/java/ql/src/codeql-suites/` exista e contenha os arquivos `.qls` necessários antes de rodar o script.

Essa estrutura pressupõe que você **clonou o repositório oficial do CodeQL** diretamente do GitHub:

```bash
git clone https://github.com/github/codeql.git
```

Alternativamente, você pode usar o comando abaixo para **baixar os pacotes oficiais via CLI**, sem clonar o repositório:

```bash
codeql pack install
```

Esse comando resolve automaticamente as dependências e instala os pacotes CodeQL referenciados no arquivo `qlpack.yml`. Essa abordagem é recomendada quando você está usando a CLI em um projeto configurado com `qlpack.yml` e deseja evitar o clone manual do repositório.

🔧 Exemplo de `qlpack.yml` mínimo para análise com Java:

```yaml
name: meu-org/minha-analise-java
version: 0.0.1
dependencies:
  codeql/java-queries: "*"
extractor: java
```

Esse arquivo indica que você deseja usar as queries do pacote oficial `codeql/java-queries` e que o extrator utilizado será o de **Java**. Após isso, basta rodar `codeql pack install` para que tudo seja baixado automaticamente.

---

## 📦 Dependências

Este projeto depende dos seguintes requisitos para funcionar corretamente:

- **Python 3.9+**  
  Utilizado para automatizar a análise de código com CodeQL via scripts Python.

- **[CodeQL CLI](https://github.com/github/codeql-cli-binaries/releases)**  
  Ferramenta de análise estática desenvolvida pela GitHub, usada para identificar vulnerabilidades, bugs e problemas de qualidade em código-fonte.

- **Pacotes e Query Suites do CodeQL**  
  Os arquivos `.qls` contendo as consultas devem estar disponíveis. Isso pode ser feito de duas formas:
  
  - Clonando o repositório oficial do CodeQL (estrutura esperada: `codeql/java/ql/src/codeql-suites/`), **ou**
  - Utilizando o comando `codeql pack install`, que baixa os pacotes automaticamente com base no `qlpack.yml`.

> Certifique-se de que o CodeQL CLI esteja instalado corretamente e disponível no terminal com:

```bash
codeql --version
```

---

## 🛠️ Instalação do CodeQL CLI

### macOS (via Homebrew)

```bash
brew install codeql
```

> Se não tiver o Homebrew instalado, acesse: [https://brew.sh](https://brew.sh)

---

### Linux (Ubuntu/Debian)

```bash
# Acesse a página de releases oficiais:
https://github.com/github/codeql-cli-binaries/releases

# Baixe o arquivo apropriado para Linux, por exemplo:
# codeql-linux64.zip

# Extraia o conteúdo:
unzip codeql-linux64.zip

# Mova para um diretório de sua preferência:
sudo mv codeql /opt/

# Adicione ao PATH (exemplo para bash):
echo 'export PATH=$PATH:/opt/codeql' >> ~/.bashrc
source ~/.bashrc
```

---

### Windows

1. Acesse: [CodeQL CLI Releases](https://github.com/github/codeql-cli-binaries/releases)
2. Baixe o arquivo `.zip` correspondente ao Windows (ex: `codeql-win64.zip`)
3. Extraia para um diretório, como `C:\codeql`
4. Adicione `C:\codeql` à variável de ambiente `Path`
5. No terminal (CMD ou PowerShell), execute:

```bash
codeql --version
```

Se a versão aparecer, o CodeQL está instalado corretamente.

---

## ⚙️ Ambiente virtual

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

---

## 📄 Sobre o Formato SARIF

O SARIF (Static Analysis Results Interchange Format) é um formato padrão para a troca de resultados de análise estática. Ele é compatível com ferramentas como Visual Studio Code, GitHub Advanced Security, e outras plataformas.

> 🔗 [Saiba mais sobre o SARIF Output](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/sarif-output)

---

## 📚 Documentação e Links Úteis

- [Documentação Geral do CodeQL](https://codeql.github.com/docs/)  
  Página principal com toda a documentação oficial do CodeQL.

- [Sobre o CodeQL](https://codeql.github.com/docs/codeql-overview/about-codeql/)  
  Visão geral do CodeQL: o que é, para que serve e como funciona.

- [Sobre Queries CodeQL](https://codeql.github.com/docs/writing-codeql-queries/about-codeql-queries/)  
  Introdução à escrita de consultas em CodeQL e à linguagem em si.

- [CodeQL CLI – Introdução](https://docs.github.com/pt/enterprise-server@3.13/code-security/codeql-cli/getting-started-with-the-codeql-cli/about-the-codeql-cli)  
  Visão geral da CLI do CodeQL.

- [CodeQL CLI - pack install](https://docs.github.com/pt/code-security/codeql-cli/codeql-cli-manual/pack-install)  
  Comando `codeql pack install` e como usá-lo para gerenciar pacotes CodeQL.

- [CodeQL CLI - Criando e Trabalhando com CodeQL Packs](https://docs.github.com/pt/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/creating-and-working-with-codeql-packs)  
  Explica como criar, estruturar e gerenciar pacotes (`packs`) personalizados no CodeQL.

- [Preparando Código para CodeQL](https://docs.github.com/pt/enterprise-server@3.13/code-security/codeql-cli/getting-started-with-the-codeql-cli/preparing-your-code-for-codeql-analysis)  
  Como preparar seu projeto para análise com CodeQL.

- [Formato SARIF – Detalhes](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/sarif-output)  
  Informações detalhadas sobre o formato de saída SARIF utilizado nas análises.

---

## ⚖️ Licença

Este projeto está licenciado sob a **MIT License**.
