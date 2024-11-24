import os
import requests

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

# Função para baixar o repositório
def download_repo(repo_url, repo_name):
    
    print(f'Baixando o repositório {repo_name}...')
    print(f'URL: {repo_url}')
    os.makedirs(repo_name, exist_ok=True)
    os.system(f'git clone {repo_url} {repo_name}')    
    print(f'Repositório {repo_name} baixado com sucesso!')

# Função para baixar o repositório em formato ZIP
def download_repo_zip(repo_url, repo_name):
    print(f'Baixando o repositório {repo_name} como arquivo ZIP...')
    print(f'URL: {repo_url}')
    
    # Remove a parte final .git da URL, se presente
    repo_url = repo_url[:-4] if repo_url.endswith('.git') else repo_url
    print(f'Nova URL: {repo_url}')
    
    # Formato de URL para download do ZIP
    zip_url = f'{repo_url}/archive/refs/heads/main.zip'
    print(f'Zip URL: {zip_url}')

    # Fazendo o download do arquivo ZIP
    response = requests.get(zip_url)
    
    if response.status_code == 200:
        print(f'Conexão bem-sucedida! Status: {response.status_code}')
        
        # Cria o diretório para salvar o arquivo ZIP
        # print(f'Criando o diretório {repo_name} para salvar o arquivo ZIP...')
        # os.makedirs(repo_name, exist_ok=True)
        
        # Caminho para salvar o arquivo ZIP
        # zip_file_path = os.path.join(repo_name, f'{repo_name}.zip')
        # print(f'Caminho para salvar o arquivo ZIP: {zip_file_path}')
        
        # Caminho para salvar o arquivo ZIP diretamente no diretório atual
        zip_file_path = f'{repo_name}.zip'
        print(f'Caminho para salvar o arquivo ZIP: {zip_file_path}')
        
        # Salva o conteúdo no arquivo ZIP
        print(f'Salvando o conteúdo no arquivo ZIP...')
        with open(zip_file_path, 'wb') as file:
            file.write(response.content)
        
        print(f'Repositório {repo_name} baixado com sucesso em formato ZIP!')
    else:
        print(f'Erro ao baixar o repositório {repo_name}: {response.status_code}')

# Função principal para pegar todos os repositórios e fazer o download
def main():
    # Pega a lista de repositórios
    # Definir o parâmetro per_page para 100, que é o máximo de repositórios retornados em uma requisição
    response = requests.get(API_URL, headers=headers, params={'per_page': 100})
    
    if response.status_code == 200:
        repos = response.json()
        
        # Imprime o total de repositórios
        total_repos = len(repos)
        print(f'Total de repositórios: {total_repos}')
        
        for repo in repos:
            repo_name = repo['name']
            repo_url = repo['clone_url']
            # download_repo(repo_url, repo_name)
            download_repo_zip(repo_url, repo_name)
    else:
        print(f'Erro ao acessar os repositórios: {response.status_code}')
    
if __name__ == '__main__':
    main()

# pip install requests
