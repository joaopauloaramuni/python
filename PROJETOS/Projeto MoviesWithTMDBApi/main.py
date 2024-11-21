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

def fetch_genres(api_key):
    """
    Busca todos os gêneros disponíveis.
    """
    genres_url = f"https://api.themoviedb.org/3/genre/movie/list"
    params = {
        'api_key': api_key,
        'language': 'en-US',
    }
    
    try:
        response = requests.get(genres_url, params=params, timeout=10)
        if response.status_code == 200:
            genres = response.json().get('genres', [])
            return {genre['id']: genre['name'] for genre in genres}
        else:
            print(f"Erro ao buscar gêneros: {response.status_code} - {response.reason}")
            return {}
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar gêneros: {e}")
        return {}

def fetch_similar_movies(api_key, genre_ids, min_vote_average=7.0):
    """
    Busca filmes similares com base no(s) gênero(s) e filtra pelos votos mínimos.
    """
    discover_url = f"https://api.themoviedb.org/3/discover/movie"
    params = {
        'api_key': api_key,
        'with_genres': ','.join(map(str, genre_ids)),
        'language': 'en-US',
        'page': 1,
    }
    
    try:
        response = requests.get(discover_url, params=params, timeout=10)  # Timeout para evitar longas esperas
        if response.status_code == 200:
            movies = response.json().get('results', [])
            # Filtrando filmes pela média de votos
            filtered_movies = [movie for movie in movies if movie['vote_average'] >= min_vote_average]
            return sorted(filtered_movies, key=lambda x: x['vote_average'], reverse=True)[:10]
        else:
            print(f"Erro ao buscar filmes similares: {response.status_code} - {response.reason}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar filmes similares: {e}")
        return []

def main():
    api_key = "636d05525b891098884fe79c594385e3"
    movie_name = input("Digite o nome do filme: ")
    min_vote_average = float(input("Digite a nota mínima para filtrar os filmes (por padrão 7.0): ") or 7.0)

    # Passo 1: Buscar detalhes do filme
    movie = fetch_movie_details(api_key, movie_name)
    if not movie:
        return
    
    print(f"Filme encontrado: {movie['title']} (ID: {movie['id']}) (GENRE_IDS: {movie['genre_ids']})")
    
    # Passo 2: Buscar todos os gêneros
    genres = fetch_genres(api_key)
    
    # Passo 3: Mapear os IDs dos gêneros para seus nomes
    genre_names = [genres.get(genre_id, "Desconhecido") for genre_id in movie['genre_ids']]
    print(f"Gêneros: {', '.join(genre_names)}")
    
    genre_ids = movie['genre_ids']
    
    # Passo 4: Buscar filmes similares
    similar_movies = fetch_similar_movies(api_key, genre_ids, min_vote_average)
    
    if similar_movies:
        print("\nTop 10 filmes populares e bem avaliados do mesmo gênero:")
        for idx, similar_movie in enumerate(similar_movies, start=1):
            print(f"{idx}. {similar_movie['title']} - Nota: {similar_movie['vote_average']}")
    else:
        print("Nenhum filme encontrado nos mesmos gêneros.")

if __name__ == "__main__":
    main()

# pip install requests
