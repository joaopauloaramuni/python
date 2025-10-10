import requests
import csv
import sys
import time
from urllib.parse import urlparse

# --- Configuração ---
# Seu Token de Acesso Pessoal (PAT) do GitHub.
# Recomenda-se armazená-lo como variável de ambiente ou usar bibliotecas de segredos.
# Para este exemplo, ele deve ser substituído por seu token real.
GITHUB_TOKEN = "ghp_####################################" # !! Substitua pelo seu PAT real !!

# URL base da API do GitHub
GITHUB_API_BASE = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# --------------------------------------------------------------------------------------
# 1. Funções de Utilitário e API
# --------------------------------------------------------------------------------------

def parse_repo_url(repo_url: str) -> tuple[str, str] | None:
    """
    Extrai o dono (owner) e o nome do repositório (repo_name) de uma URL do GitHub.
    Exemplo: https://github.com/ICEI-PUC-Minas-PMGES-TI/pmg-es-2025-2-ti3-9577100-repoexemplo
    -> ('ICEI-PUC-Minas-PMGES-TI', 'pmg-es-2025-2-ti3-9577100-repoexemplo')
    """
    try:
        path = urlparse(repo_url).path.strip('/')
        parts = path.split('/')
        if len(parts) >= 2:
            return parts[0], parts[1]
        else:
            print("ERRO: URL do repositório inválida.")
            return None
    except Exception as e:
        print(f"ERRO ao analisar a URL: {e}")
        return None

def fetch_contributors_stats(owner: str, repo_name: str) -> list | None:
    """
    Busca as estatísticas de contribuição do repositório usando a API do GitHub.
    Implementa um loop de retentativa (pooling) para lidar com o status 202 (Accepted).
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo_name}/stats/contributors"
    
    # Define o número máximo de tentativas e o tempo de espera
    MAX_TRIES = 6
    WAIT_TIME = 10 # segundos

    # Tenta buscar os dados até MAX_TRIES vezes
    for attempt in range(1, MAX_TRIES + 1):
        print(f"Buscando estatísticas (Tentativa {attempt}/{MAX_TRIES}) de: {url}")
        
        # Faz a requisição
        response = requests.get(url, headers=HEADERS)

        # Caso 1: Sucesso (Dados Prontos)
        if response.status_code == 200:
            print("Dados de contribuição recebidos com sucesso.")
            return response.json()
        
        # Caso 2: Processando (Precisa Tentar Novamente)
        elif response.status_code == 202:
            if attempt < MAX_TRIES:
                print(f"A API do GitHub está processando as estatísticas. Aguardando {WAIT_TIME} segundos...")
                # Espera o tempo definido antes de tentar novamente
                time.sleep(WAIT_TIME)
                continue # Vai para a próxima tentativa
            else:
                # Se for a última tentativa e ainda estiver 202
                print("ERRO: O processamento demorou muito e o tempo limite foi atingido.")
                return None
        
        # Caso 3: Outros Erros (Permissão, Repositório Inexistente, etc.)
        else:
            print(f"ERRO {response.status_code}: Falha crítica ao buscar dados do repositório.")
            print(f"Mensagem da API: {response.json().get('message', 'Nenhuma mensagem adicional.')}")
            return None

    # Este ponto só é atingido se o loop de retentativa falhar
    return None

# --------------------------------------------------------------------------------------
# 2. Funções de Análise e Geração de Saída
# --------------------------------------------------------------------------------------

def generate_ranking(contributors_data: list) -> list:
    """
    Processa os dados brutos da API para criar um ranking ordenado e sumarizado.
    Métricas consideradas: total de commits, adições (linhas inseridas) e deleções.
    """
    ranking = []
    
    for contributor in contributors_data:
        # Pega as informações do usuário
        username = contributor['author']['login']
        user_profile_url = contributor['author']['html_url']
        
        # O total de 'weeks' contém a soma total de commits, adições e deleções
        total_commits = contributor['total']
        total_additions = sum(week['a'] for week in contributor['weeks'])
        total_deletions = sum(week['d'] for week in contributor['weeks'])
        
        # Calcula o impacto líquido das linhas
        net_impact = total_additions - total_deletions

        ranking.append({
            'Nome de Usuário': username,
            'URL Perfil': user_profile_url,
            'Commits Totais': total_commits,
            'Linhas Inseridas': total_additions,
            'Linhas Deletadas': total_deletions,
            'Impacto Líquido (Ins - Del)': net_impact
        })

    # Ordena o ranking usando o número de commits como métrica principal e o impacto líquido como desempate.
    ranking.sort(key=lambda x: (x['Commits Totais'], x['Impacto Líquido (Ins - Del)']), reverse=True)
    
    # CÓDIGO ALTERNATIVO (prioriza impacto líquido)
    # ranking.sort(key=lambda x: (x['Impacto Líquido (Ins - Del)'], x['Commits Totais']), reverse=True)

    return ranking

def export_to_csv(ranking: list, repo_name: str):
    """
    Exporta o ranking de contribuições para um arquivo CSV.
    """
    if not ranking:
        print("Nenhum dado de ranking para exportar.")
        return

    csv_filename = f"ranking_contribuicao_{repo_name}.csv"
    
    # Define os cabeçalhos (baseado nas chaves do dicionário de ranking)
    fieldnames = list(ranking[0].keys())
    
    try:
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            
            writer.writeheader()
            writer.writerows(ranking)
        
        print(f"\n✅ Sucesso! Ranking exportado para: {csv_filename}")
        print("As métricas são: Commits Totais, Linhas Inseridas, Linhas Deletadas e Impacto Líquido.")

    except Exception as e:
        print(f"ERRO ao escrever o arquivo CSV: {e}")

# --------------------------------------------------------------------------------------
# 3. Função Principal
# --------------------------------------------------------------------------------------

def main(repo_url: str):
    """
    Função principal que orquestra a análise de contribuições.
    """
    # 1. Verifica se o token foi substituído
    if GITHUB_TOKEN == "SEU_TOKEN_AQUI":
        print("ERRO: Por favor, substitua 'SEU_TOKEN_AQUI' no script pelo seu Token de Acesso Pessoal do GitHub.")
        sys.exit(1)
        
    # 2. Analisa a URL
    owner_repo = parse_repo_url(repo_url)
    if not owner_repo:
        sys.exit(1)
        
    owner, repo_name = owner_repo
    
    # 3. Busca os dados na API
    data = fetch_contributors_stats(owner, repo_name)
    if data is None:
        print("\nProcesso interrompido. Verifique o erro acima (permissão ou processamento).")
        sys.exit(1)
        
    # 4. Gera o Ranking
    ranking = generate_ranking(data)
    
    # 5. Exporta para CSV
    export_to_csv(ranking, repo_name)
    
    # 6. Exibe o Top 10 no console para visualização rápida
    print("\n--- TOP 10 Contribuidores (Console) ---")
    for i, contributor in enumerate(ranking[:10]):
        print(f"{i+1}. {contributor['Nome de Usuário']} ({contributor['URL Perfil']})")
        print(f"   -> Commits: {contributor['Commits Totais']} | Inseridas: {contributor['Linhas Inseridas']} | Deletadas: {contributor['Linhas Deletadas']} | Impacto Líquido: {contributor['Impacto Líquido (Ins - Del)']}")

# --------------------------------------------------------------------------------------
# Execução
# --------------------------------------------------------------------------------------

if __name__ == "__main__":
    # URL do repositório
    repo_to_analyze = "https://github.com/ICEI-PUC-Minas-PMGES-TI/pmg-es-2025-2-ti3-9577100-repoexemplo"
    
    # Caso o usuário queira passar a URL como argumento de linha de comando
    if len(sys.argv) > 1:
        repo_to_analyze = sys.argv[1]
    
    main(repo_to_analyze)

# pip install requests
