import requests
import time  # Import para medir o tempo de execução

# Seu token do GitHub (crie um token em https://github.com/settings/tokens)
GITHUB_TOKEN = 'ghp_seutokenaqui'
# Nome do usuário no GitHub
GITHUB_USERNAME = 'nomedousuarioaqui'

# URL da API do GitHub para obter os repositórios
API_URL = f'https://api.github.com/users/{GITHUB_USERNAME}/repos'

# Cabeçalhos para autenticação com o token
headers = {
    'Authorization': f'token {GITHUB_TOKEN}'
}

# Constantes para extensões analisadas
CODE_EXTENSIONS = {".java", ".py", ".js", ".c", ".cpp", ".cs", ".html", ".css", ".php", ".rb", ".go", ".rs", ".ts", ".swift", ".kt", ".scala", ".sh", ".vbs", ".pas", ".dart"}
SQL_EXTENSION = ".sql"
MARKDOWN_EXTENSION = ".md"

def get_repositories():
    """Obtém a lista de repositórios do usuário."""
    try:
        response = requests.get(API_URL, headers=headers, params={'per_page': 100})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar os repositórios: {e}")
        return None

def fetch_file_content(file_url, file_path, repo_owner, repo_name):
    """Obtém o conteúdo de um arquivo do GitHub."""
    try:
        # Tentar buscar pelo link bruto primeiro
        raw_url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/main/{file_path}"
        raw_response = requests.get(raw_url, headers=headers)
        raw_response.raise_for_status()
        return raw_response.text  # Retorna o conteúdo bruto

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o arquivo bruto {file_path}: {e}")

    try:
        # Fallback para a API de blobs
        file_response = requests.get(file_url, headers=headers)
        file_response.raise_for_status()
        return file_response.json().get("content", "")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o arquivo {file_path}: {e}")
        return ""

def count_lines_in_repo(repo):
    """Conta as linhas de código e Markdown em um repositório."""
    BASE_URL = "https://api.github.com"
    
    repo_name = repo['name']
    repo_owner = repo['owner']['login']
    tree_url = f"{BASE_URL}/repos/{repo_owner}/{repo_name}/git/trees/main?recursive=1"
    
    try:
        response = requests.get(tree_url, headers=headers)
        response.raise_for_status()
        tree = response.json().get("tree", [])
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o repositório {repo_name}: {e}")
        return 0, 0, 0, 0, 0

    code_lines = 0
    java_lines = 0
    python_lines = 0
    sql_lines = 0
    markdown_lines = 0
    
    for file in tree:
        if file["type"] == "blob":
            file_path = file["path"]
            
            # Ignorar arquivos com extensões irrelevantes
            if not (file_path.endswith(tuple(CODE_EXTENSIONS)) or
                    file_path.endswith(SQL_EXTENSION) or
                    file_path.endswith(MARKDOWN_EXTENSION)):
                continue
            
            try:
                content = fetch_file_content(file["url"], file_path, repo_owner, repo_name)  # Obter o conteúdo
                lines = len(content.split("\n"))  # Contar as linhas uma vez
                print(f"Arquivo processado: {file_path}, Linhas contadas: {lines}")  # Diagnóstico
                
                if file_path.endswith(".java"):
                    java_lines += lines
                    code_lines += lines
                elif file_path.endswith(".py"):
                    python_lines += lines
                    code_lines += lines
                elif file_path.endswith(SQL_EXTENSION):
                    sql_lines += lines
                elif file_path.endswith(MARKDOWN_EXTENSION):
                    markdown_lines += lines
                elif any(file_path.endswith(ext) for ext in CODE_EXTENSIONS):
                    code_lines += lines
            except requests.exceptions.RequestException as e:
                print(f"Erro ao acessar o arquivo {file_path}: {e}")
    
    return code_lines, markdown_lines, java_lines, python_lines, sql_lines

def main():
    print("\n" + "*" * 150)
    print("Obtendo a lista de repositórios...")
    repos = get_repositories()
    
    if repos is None:
        print("Não foi possível obter a lista de repositórios.")
        return

    # Exibir a lista de extensões consideradas
    print("\nExtensões consideradas para análise:")
    print(f"  Código: {', '.join(CODE_EXTENSIONS)}")
    print(f"  SQL: {SQL_EXTENSION}")
    print(f"  Markdown: {MARKDOWN_EXTENSION}")
    
    total_code_lines = 0
    total_markdown_lines = 0
    total_java_lines = 0
    total_python_lines = 0
    total_sql_lines = 0
    
    print(f"\nTotal de repositórios encontrados: {len(repos)}")
    
    for repo in repos:
        print("\n" + "*" * 150)
        print(f"Processando repositório: {repo['name']}...")
        
        start_time = time.time()  # Começar a medir o tempo
        
        code_lines, markdown_lines, java_lines, python_lines, sql_lines = count_lines_in_repo(repo)
        
        end_time = time.time()  # Fim da medição do tempo
        elapsed_time = end_time - start_time  # Tempo total em segundos
        
        print(f"Tempo para processar {repo['name']}: {elapsed_time:.2f} segundos")
        if code_lines == 0 and sql_lines == 0 and markdown_lines == 0:
            print(f"Linguagem fora da lista no repositório {repo['name']}")
        elif sql_lines > 0:
            print(f"Linhas encontradas no repositório {repo['name']}:")
            print(f"  Linhas de código SQL: {sql_lines}")
            print(f"  Linhas de código: {code_lines}")
            print(f"  Linhas de Markdown: {markdown_lines}")
        else:
            print(f"Linhas encontradas no repositório {repo['name']}:")
            print(f"  Linhas de código: {code_lines}")
            print(f"  Linhas de Markdown: {markdown_lines}")
        
        total_code_lines += code_lines
        total_markdown_lines += markdown_lines
        total_java_lines += java_lines
        total_python_lines += python_lines
        total_sql_lines += sql_lines
    
    print("\n" + "*" * 150)
    print("\n--- Resultado Final ---")
    print(f"  Total de linhas de código: {total_code_lines}")
    print(f"  Total de linhas de Markdown: {total_markdown_lines}")
    print(f"  Total de linhas de código Java: {total_java_lines}")
    print(f"  Total de linhas de código Python: {total_python_lines}")
    print(f"  Total de linhas de código SQL: {total_sql_lines}")

if __name__ == "__main__":
    main()

# pip install requests
