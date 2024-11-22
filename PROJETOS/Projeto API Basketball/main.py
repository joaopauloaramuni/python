import requests

# Configuração da API
API_KEY = "seutokenaqui"
BASE_URL = "https://v2.nba.api-sports.io"

# Configuração dos cabeçalhos
HEADERS = {
    "x-rapidapi-host": "v2.nba.api-sports.io",
    "x-rapidapi-key": API_KEY
}

def get_games(date):
    """Obtém os jogos da NBA para uma data específica."""
    url = f"{BASE_URL}/games"
    params = {"date": date}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()  # Lança erro caso a requisição falhe
    games = response.json().get("response", [])
    return games

def display_games(games):
    """Exibe os jogos ordenados pela data mais próxima."""
    print("\nPróximos jogos da NBA:\n")
    for game in sorted(games, key=lambda x: x["date"]["start"]):
        date = game["date"]["start"]
        home_team = game["teams"]["home"]["name"]
        visitor_team = game["teams"]["visitors"]["name"]
        status = game["status"]["long"]
        arena = game["arena"]["name"]
        city = game["arena"]["city"]
        
        print(f"- {date} | {home_team} vs {visitor_team}")
        print(f"  Status: {status} | Local: {arena}, {city}\n")

def main():
    # Data dos jogos
    date = "2024-11-22"  # Pode ser ajustado para outra data
    
    # Obtém os jogos
    games = get_games(date)
    
    if games:
        display_games(games)
    else:
        print("Nenhum jogo encontrado para a data especificada.")

if __name__ == "__main__":
    main()
