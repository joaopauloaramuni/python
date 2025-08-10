import requests
import time

# ========================================
# CONFIGURAÇÕES
# ========================================
GITHUB_TOKEN = "SEU_TOKEN_AQUI"  # Crie em https://github.com/settings/tokens
NUM_REQUISICOES = 10

REST_URL = "https://api.github.com/repos/torvalds/linux"
GRAPHQL_URL = "https://api.github.com/graphql"

# ========================================
# FUNÇÕES DE REQUISIÇÃO
# ========================================

def request_rest():
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    response = requests.get(REST_URL, headers=headers)
    response.raise_for_status()
    return response.json()

def request_graphql():
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    query = """
    {
      repository(owner: "torvalds", name: "linux") {
        name
        owner {
          login
        }
        stargazerCount
        forksCount
      }
    }
    """
    response = requests.post(GRAPHQL_URL, json={"query": query}, headers=headers)
    response.raise_for_status()
    return response.json()

# ========================================
# FUNÇÕES DE TESTE DE PERFORMANCE
# ========================================

def medir_tempo(func, n=1):
    tempos = []
    for _ in range(n):
        inicio = time.perf_counter()
        func()
        fim = time.perf_counter()
        tempos.append(fim - inicio)
    return tempos

def calcular_media(tempos):
    return sum(tempos) / len(tempos)

# ========================================
# MAIN
# ========================================

def main():
    print(f"Executando {NUM_REQUISICOES} requisições REST...")
    tempos_rest = medir_tempo(request_rest, NUM_REQUISICOES)
    media_rest = calcular_media(tempos_rest)

    print(f"Executando {NUM_REQUISICOES} requisições GraphQL...")
    tempos_graphql = medir_tempo(request_graphql, NUM_REQUISICOES)
    media_graphql = calcular_media(tempos_graphql)

    print("\n--- RESULTADOS ---")
    print(f"Tempo médio REST: {media_rest:.4f} segundos")
    print(f"Tempo médio GraphQL: {media_graphql:.4f} segundos")

    if media_rest < media_graphql:
        print("✅ REST foi mais rápido.")
    elif media_graphql < media_rest:
        print("✅ GraphQL foi mais rápido.")
    else:
        print("⚖️ Empate técnico.")

if __name__ == "__main__":
    main()
