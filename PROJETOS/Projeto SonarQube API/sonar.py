import os
import subprocess
import requests
import shutil
import uuid
import time
import re
import fnmatch
from urllib.parse import urlparse

# Configurações globais do SonarQube: URL e token de autenticação
SONAR_HOST = "http://localhost:9000"
SONAR_TOKEN = "seu_token_aqui" # Substitua pelo seu token do SonarQube
SONAR_SCANNER_PATH = "sonar-scanner"

# Função responsável por compilar o repositório em Java (usando Maven, Gradle ou manualmente)
def compilar_java(caminho_repo):
    # Verifica se há um arquivo pom.xml (Maven)
    if os.path.isfile(os.path.join(caminho_repo, "pom.xml")):
        print("[+] Encontrado pom.xml, compilando com Maven...")
        # Executa mvn clean compile sem testes
        result = subprocess.run(
            ["mvn", "clean", "compile", "-DskipTests"],
            cwd=caminho_repo,
            capture_output=True,
            text=True
        )
        print("*" * 150)
        print("[DEBUG Maven STDOUT]:", result.stdout)
        print("[DEBUG Maven STDERR]:", result.stderr)
        print("*" * 150)
        # Verifica se a compilação foi bem-sucedida
        if result.returncode != 0:
            raise RuntimeError("Falha na compilação com Maven")
        
        classes_path = os.path.join(caminho_repo, "target", "classes")
        # Verifica se o diretório com classes compiladas existe
        if os.path.isdir(classes_path):
            # Percorre recursivamente os arquivos dentro do diretório
            for root, _, files in os.walk(classes_path):
                # Se encontrar qualquer arquivo .class, retorna a raiz
                if any(f.endswith(".class") for f in files):
                    print(f"[DEBUG] Diretório de classes Maven encontrado: {root}")
                    print("*" * 150)
                    return root
        print("*" * 150)
        print("[WARN] Diretório 'target/classes' não encontrado ou vazio após compilação Maven.")
        print("*" * 150)
        
        return None
    
    # Verifica se há um arquivo build.gradle (Gradle)
    elif os.path.isfile(os.path.join(caminho_repo, "build.gradle")):
        print("[+] Encontrado build.gradle, compilando com Gradle...")
         # Executa gradle build, ignorando testes
        result = subprocess.run(
            ["gradle", "build", "-x", "test"], cwd=caminho_repo, capture_output=True, text=True
        )
        print("*" * 150)
        print("[DEBUG Gradle STDOUT]:", result.stdout)
        print("[DEBUG Gradle STDERR]:", result.stderr)
        print("*" * 150)
        # Verifica se a compilação foi bem-sucedida
        if result.returncode != 0:
            raise RuntimeError("Falha na compilação com Gradle")
        
        # Procura por arquivos .class dentro da estrutura de build/classes
        for root, _, files in os.walk(caminho_repo):
            # Verifica se o diretório contém arquivos .class
            if "build/classes" in root.replace("\\", "/") and any(fnmatch.fnmatch(f, "*.class") for f in files):
                print(f"[DEBUG] Diretório com .class encontrado: {root}")
                print("*" * 150)
                return root
        print("*" * 150)
        print("[WARN] Não encontrou diretório válido com arquivos .class após compilação Gradle.")
        print("*" * 150)
        return None
    
    # Se não houver nem Maven nem Gradle, tenta compilar manualmente com javac
    else:
        arquivos_java = []
        # Coleta todos os arquivos .java no repositório
        for root, _, files in os.walk(caminho_repo):
            for file in files:
                if file.endswith(".java"):
                    arquivos_java.append(os.path.join(root, file))
        if arquivos_java:
            bin_dir = os.path.join(caminho_repo, "bin")
            os.makedirs(bin_dir, exist_ok=True)
            print("[+] Compilando arquivos Java manualmente (pode falhar)...")
            
            # Compila todos os arquivos .java com javac
            subprocess.run(["javac", "-d", bin_dir] + arquivos_java, check=True)
            for root, _, files in os.walk(bin_dir):
                if any(f.endswith(".class") for f in files):
                    print(f"[DEBUG] Diretório de classes manual encontrado: {root}")
                    print("*" * 150)
                    return root
            print("*" * 150)
            print("[WARN] Diretório 'bin' está vazio após compilação manual.")
            print("*" * 150)
            return None
        return None

# Consulta as métricas de qualidade do projeto no SonarQube
def get_sonar_metrics(project_key):
    print(f"[DEBUG] Consultando métricas para project_key: '{project_key}'")
    
    # Lista de métricas que queremos extrair do SonarQube
    metrics = [
        # Coverage
        "coverage", "new_coverage",
        "lines_to_cover", "new_lines_to_cover",
        "uncovered_lines", "new_uncovered_lines",
        "line_coverage", "new_line_coverage",
        "branch_coverage", "new_branch_coverage",
        "uncovered_conditions", "new_uncovered_conditions",
        "tests", "test_errors", "test_failures", "skipped_tests", "test_execution_time", "test_success_density",
        # "coverage_line_hist_data",
        # "branch_coverage_hits_data",
        # "conditions_by_line",
        # "covered_conditions_by_line",

        # Duplications
        "duplicated_lines_density", "new_duplicated_lines_density",
        "duplicated_lines", "new_duplicated_lines",
        "duplicated_blocks", "new_duplicated_blocks",
        "duplicated_files",

        # Size
        "new_lines", "ncloc", "lines", "statements", "functions", "classes", "files", "comment_lines", "comment_lines_density", "ncloc_language_distribution", "projects",

        # Complexity
        "complexity", "cognitive_complexity", "sqale_index",
        "code_smells", "bugs", "vulnerabilities"
    ]
    metric_keys = ",".join(metrics)

    url = f"{SONAR_HOST}/api/measures/component"
    params = {
        "component": project_key,
        "metricKeys": metric_keys
    }
    auth = (SONAR_TOKEN, "")

    response = requests.get(url, params=params, auth=auth)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("*" * 150)
        print(f"[ERROR] Falha na requisição HTTP: {response.status_code}")
        print(f"[ERROR] Conteúdo da resposta: {response.text}")
        print("*" * 150)
        raise

    data = response.json()
    return {m["metric"]: m["value"] for m in data["component"]["measures"] if "value" in m}

# Aguarda o processamento assíncrono da análise no SonarQube
def aguardar_processamento(task_id):
    print("[+] Aguardando processamento da análise no SonarQube...")
    url = f"{SONAR_HOST}/api/ce/task"
    auth = (SONAR_TOKEN, "")
    while True:
        response = requests.get(url, params={"id": task_id}, auth=auth)
        response.raise_for_status()
        status = response.json()["task"]["status"]
        if status == "SUCCESS":
            return
        elif status in ("PENDING", "IN_PROGRESS"):
            time.sleep(2)
        else:
            raise RuntimeError(f"A análise falhou com status: {status}")

# Gera e executa o sonar-scanner no repositório
def run_sonar_scanner(repo_path, project_key):
    # Compila o código e obtém caminho para os .class
    binaries_path = compilar_java(repo_path)

    # Monta o conteúdo do arquivo sonar-project.properties
    sonar_project_properties = f"""
    sonar.projectKey={project_key}
    sonar.sources=.
    sonar.host.url={SONAR_HOST}
    sonar.login={SONAR_TOKEN}
    """

    # Define onde estão os arquivos .class, ou exclui tudo se não encontrar
    if binaries_path:
        rel_path = os.path.relpath(binaries_path, repo_path)
        sonar_project_properties += f"sonar.java.binaries={rel_path}\n"
    # else:
        # sonar_project_properties += "sonar.exclusions=**/*.java\n"

    with open(os.path.join(repo_path, "sonar-project.properties"), "w") as f:
        f.write(sonar_project_properties)

    print("[+] Executando sonar-scanner...")

    # Executa o sonar-scanner com subprocess
    result = subprocess.run(
        [SONAR_SCANNER_PATH],
        cwd=repo_path,
        capture_output=True,
        text=True
    )
    
    print("*" * 150)
    print("[DEBUG] STDOUT:\n", result.stdout)
    print("[DEBUG] STDERR:\n", result.stderr)
    print("*" * 150)

    result.check_returncode()
    
    # Extrai o task ID da saída do sonar-scanner
    match = re.search(r"task\?id=([a-f0-9\-]+)", result.stdout)
    if match:
        return match.group(1)
    else:
        raise RuntimeError("Não foi possível extrair o task ID da saída do sonar-scanner.")

# Clona o repositório GitHub em um diretório temporário
def clone_repo(github_url):
    url_clean = github_url.rstrip("/")
    repo_name = urlparse(url_clean).path.split("/")[-1].replace(".git", "")
    if not repo_name:
        raise ValueError(f"Não foi possível extrair o nome do repositório da URL: {github_url}")
    
    # Diretório atual do projeto
    current_dir = os.getcwd()
    temp_dir = os.path.join(current_dir, f"temp_clone_{uuid.uuid4().hex}_{repo_name}")
    
    # Clona o repositório na pasta temporária dentro do projeto
    subprocess.run(["git", "clone", github_url, temp_dir], check=True)
    
    return temp_dir, repo_name

# Função principal que orquestra toda a análise
def analisar_repositorio(github_url):
    repo_path, repo_name = clone_repo(github_url)
    project_key = repo_name.replace("-", "_").lower()
    if not project_key:
        raise ValueError(f"Não foi possível gerar um project_key válido a partir do nome do repositório '{repo_name}'. Resultado vazio.")
    if not any(c.isalpha() for c in project_key):
        raise ValueError(f"O project_key '{project_key}' gerado a partir do nome do repositório '{repo_name}' não contém letras e é inválido.")

    try:
        print("*" * 150)
        print("[+] Rodando análise com SonarQube...")
        task_id = run_sonar_scanner(repo_path, project_key)
        aguardar_processamento(task_id)
        
        print("*" * 150)
        print("[+] Obtendo métricas...")
        metrics = get_sonar_metrics(project_key)
        
        print("*" * 150)
        print("[+] Resultado:")
        for key, value in metrics.items():
            print(f"{key}: {value}")

    finally:
        print("*" * 150)
        print("[+] Limpando repositório clonado.")
        print("*" * 150)
        shutil.rmtree(repo_path)

# Ponto de entrada do script
if __name__ == "__main__":
    print("************ Projeto de Análise de Repositórios Java com SonarQube ************")
    url = input("Informe a URL do repositório GitHub: ")
    analisar_repositorio(url)
    print("************ Análise concluída! ************")

# pip install requests
# brew install sonar-scanner
# brew install maven
# brew install gradle
# Fazer o download do SonarQube e iniciar o servidor localmente: ./sonar.sh start
# Gerar o token em http://localhost:9000/account/security