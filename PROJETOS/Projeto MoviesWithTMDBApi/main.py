import requests

def fetch_movie_details(api_key, movie_name):
    """
    Busca informações do filme com base no nome fornecido.
    """
    search_url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': api_key,
        'query': movie_name,
        'language': 'en-US',
    }
    
    try:
        response = requests.get(search_url, params=params, timeout=10)  # Timeout para evitar longas esperas
        if response.status_code == 200:
            results = response.json().get('results', [])
            if results:
                return results[0]  # Retorna o primeiro filme encontrado
            else:
                print("Nenhum filme encontrado com esse nome.")
                return None
        else:
            print(f"Erro ao buscar o filme: {response.status_code} - {response.reason}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar o filme: {e}")
        return None

def fetch_similar_movies(api_key, genre_ids):
    """
    Busca filmes similares com base no(s) gênero(s).
    """
    discover_url = f"https://api.themoviedb.org/3/discover/movie"
    params = {
        'api_key': api_key,
        'with_genres': ','.join(map(str, genre_ids)),
        'sort_by': 'popularity.desc',
        'vote_average.gte': 7.0,  # Apenas filmes bem avaliados
        'language': 'en-US',
        'page': 1,
    }
    
    try:
        response = requests.get(discover_url, params=params, timeout=10)  # Timeout para evitar longas esperas
        if response.status_code == 200:
            return sorted(response.json().get('results', []), key=lambda x: x['vote_average'], reverse=True)[:10]
        else:
            print(f"Erro ao buscar filmes similares: {response.status_code} - {response.reason}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar filmes similares: {e}")
        return []

def main():
    api_key = "636d05525b891098884fe79c594385e3"
    movie_name = input("Digite o nome do filme: ")
    
    # Passo 1: Buscar detalhes do filme
    movie = fetch_movie_details(api_key, movie_name)
    if not movie:
        return
    
    print(f"Filme encontrado: {movie['title']} (ID: {movie['id']}) {movie['genre_ids']}")
    genre_ids = movie['genre_ids']
    
    # Passo 2: Buscar filmes similares
    similar_movies = fetch_similar_movies(api_key, genre_ids)
    
    if similar_movies:
        print("\nTop 10 filmes populares e bem avaliados do mesmo gênero:")
        for idx, similar_movie in enumerate(similar_movies, start=1):
            print(f"{idx}. {similar_movie['title']} - Nota: {similar_movie['vote_average']}")
    else:
        print("Nenhum filme encontrado nos mesmos gêneros.")

if __name__ == "__main__":
    main()
