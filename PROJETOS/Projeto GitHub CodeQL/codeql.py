import subprocess
import os
import shutil

# Constante global com os nomes das suites de queries CodeQL
QUERY_SUITES = [
    "java-code-quality.qls",
    "java-code-scanning.qls",
    "java-lgtm-full.qls",
    "java-lgtm.qls",
    "java-security-and-quality.qls",
    "java-security-experimental.qls",
    "java-security-extended.qls"
]

def clone_repo(repo_url: str, local_path: str):
    """
    Clona um repositório Git em um diretório local.

    Parâmetros:
    - repo_url: URL do repositório Git a ser clonado.
    - local_path: Caminho local onde o repositório será salvo.

    Esta função usa o comando `git clone` para obter o código-fonte que será analisado.
    """
    print(f"[INFO] Clonando repositório: {repo_url}")
    subprocess.run(["git", "clone", repo_url, local_path], check=True)

def create_codeql_database(source_path: str, db_path: str):
    """
    Cria um banco de dados CodeQL a partir do código-fonte de um projeto Java.

    Parâmetros:
    - source_path: Caminho para o código-fonte do projeto.
    - db_path: Caminho onde o banco de dados será criado.

    O CodeQL precisa de um banco de dados construído a partir do código-fonte.
    Aqui usamos o comando `mvn compile` para compilar o projeto Java com Maven
    antes da análise.
    """
    print(f"[INFO] Criando banco de dados CodeQL em: {db_path}")
    subprocess.run([
        "codeql", "database", "create", db_path,
        "--language=java",
        "--source-root", source_path,
        "--command", "mvn compile"
    ], cwd=".", check=True)

def run_codeql_analysis(db_path: str, query_suite_path: str, output_file: str):
    """
    Executa a análise CodeQL com uma suite de queries e salva os resultados.

    Parâmetros:
    - db_path: Caminho para o banco de dados CodeQL.
    - query_suite_path: Caminho para o arquivo .qls com as queries da suite.
    - output_file: Nome do arquivo de saída no formato SARIF.

    A análise é feita com uso de memória extra (--ram=8192) para evitar erros.
    O resultado é salvo no formato SARIF, que é compatível com ferramentas de segurança.
    """
    print(f"[INFO] Rodando análise CodeQL com {query_suite_path}...")
    subprocess.run([
        "codeql", "database", "analyze", db_path,
        query_suite_path,
        "--format=sarifv2.1.0",
        f"--output={output_file}",
        '--ram=8192'
    ], check=True)
    print(f"[INFO] Resultados salvos em {output_file}")

def run_all_analyses(db_path: str, base_query_path: str, query_suites: list):
    """
    Executa várias análises CodeQL com diferentes suites de queries.

    Parâmetros:
    - db_path: Caminho para o banco de dados CodeQL.
    - base_query_path: Caminho base onde estão as query suites (.qls).
    - query_suites: Lista de arquivos .qls a serem usados.

    Esta função percorre cada suite de queries e chama `run_codeql_analysis` para cada uma.
    Cada resultado é salvo com um nome correspondente à suite usada.
    """
    for suite in query_suites:
        query_suite_path = os.path.join(base_query_path, suite)
        output_file = f"results-{suite.replace('.qls', '')}.sarif"
        output_file = os.path.join("results", f"results-{suite.replace('.qls', '')}.sarif")
        run_codeql_analysis(db_path, query_suite_path, output_file)

def cleanup(path: str):
    """
    Remove diretórios temporários usados no processo.

    Parâmetro:
    - path: Caminho do diretório a ser removido.

    Isso garante que repositórios anteriores e bancos de dados não interfiram
    em novas execuções da análise.
    """
    if os.path.exists(path):
        print(f"[INFO] Limpando {path}")
        shutil.rmtree(path)

def main():
    """
    Função principal que orquestra todo o processo de análise com CodeQL:

    1. Define o repositório alvo a ser analisado.
    2. Define os caminhos locais temporários.
    3. Remove dados antigos (cleanup).
    4. Clona o repositório remoto.
    5. Cria o banco de dados CodeQL a partir do código-fonte.
    6. Executa todas as análises com as suites especificadas.
    """
    repo_url = "https://github.com/apache/commons-lang"  # Repositório Java de exemplo
    local_path = "./repo_temp"  # Diretório local temporário para o repositório
    db_path = "./codeql-db"     # Caminho onde o banco de dados será criado

    # Caminho base para as suites de queries CodeQL
    base_query_path = os.path.join("codeql", "java", "ql", "src", "codeql-suites")

    # Limpeza de dados antigos
    cleanup(local_path)
    cleanup(db_path)

    # Execução do pipeline de análise
    clone_repo(repo_url, local_path)                            # Clona o repositório Java para o diretório local
    create_codeql_database(local_path, db_path)                 # Cria o banco de dados CodeQL a partir do código-fonte clonado
    os.makedirs("results", exist_ok=True)                       # Garante que o diretório 'results/' exista para armazenar os arquivos SARIF
    run_all_analyses(db_path, base_query_path, QUERY_SUITES)    # Executa todas as análises CodeQL usando as suites definidas

# Ponto de entrada do script
if __name__ == "__main__":
    main()

# brew install codeql