import numpy as np

# Função para calcular a pontuação composta
def calculate_scores(repos):
    # Extraindo estrelas e forks
    stars = np.array([repo['stars'] for repo in repos])
    forks = np.array([repo['forks'] for repo in repos])

    # Normalização
    stars_normalized = (stars - stars.min()) / (stars.max() - stars.min())
    forks_normalized = (forks - forks.min()) / (forks.max() - forks.min())

    # Cálculo da pontuação composta
    scores = 0.5 * stars_normalized + 0.5 * forks_normalized

    # Adicionando as pontuações aos repositórios
    for repo, score in zip(repos, scores):
        repo['score'] = score

    # Ordenando os repositórios pela pontuação composta
    repos_sorted = sorted(repos, key=lambda x: x['score'], reverse=True)
    return repos_sorted

# Main
if __name__ == "__main__":
    # Dados dos repositórios
    repos = [
        {"name": "nodebestpractices", "stars": 97090, "forks": 9864},
        {"name": "nest", "stars": 65393, "forks": 7447},
        {"name": "dubbo", "stars": 40191, "forks": 26331},
        {"name": "kong", "stars": 38213, "forks": 4747},
        {"name": "awesome-design-patterns", "stars": 37357, "forks": 2752},
        {"name": "istio", "stars": 35312, "forks": 7618},
        {"name": "system-design", "stars": 30105, "forks": 3095},
        {"name": "nacos", "stars": 29396, "forks": 12650},
        {"name": "apollo", "stars": 28908, "forks": 10186},
        {"name": "go-zero", "stars": 28063, "forks": 3826},
    ]

    # Calculando as pontuações e ordenando os repositórios
    repos_sorted = calculate_scores(repos)

    # Exibindo os resultados
    for repo in repos_sorted:
        print(f"Repository: {repo['name']}, Stars: {repo['stars']}, Forks: {repo['forks']}, Score: {repo['score']:.4f}")
