import requests

# Configuração da API
API_KEY = "seutokenaqui"
BASE_URL = "https://v3.football.api-sports.io"

# Configurações de cabeçalhos
HEADERS = {
    "x-rapidapi-host": "v3.football.api-sports.io",
    "x-rapidapi-key": API_KEY
}

# Ligas desejadas
DESIRED_LEAGUES = ["Serie A", "Serie B", "Copa Do Brasil", "Mineiro - 1"]

def get_brazilian_leagues():
    """Obtém ligas do Brasil e filtra pelas desejadas."""
    url = f"{BASE_URL}/leagues"
    params = {"country": "Brazil"}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    leagues = response.json()["response"]
    return [
        {
            "league_id": league["league"]["id"],
            "league_name": league["league"]["name"],
            "season": league["seasons"][-1]["year"]
        }
        for league in leagues
        if league["league"]["name"] in DESIRED_LEAGUES
    ]

def get_upcoming_fixtures(league_id):
    """Obtém os próximos jogos de uma liga específica."""
    url = f"{BASE_URL}/fixtures"
    params = {"league": league_id, "next": 10}  # Limita aos 10 próximos jogos
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    fixtures = response.json()["response"]
    return sorted(
        [
            {
                "date": fixture["fixture"]["date"],
                "home_team": fixture["teams"]["home"]["name"],
                "away_team": fixture["teams"]["away"]["name"]
            }
            for fixture in fixtures
        ],
        key=lambda x: x["date"]
    )

def main():
    leagues = get_brazilian_leagues()
    for league in leagues:
        print(f"Liga: {league['league_name']} ({league['season']})")
        
        fixtures = get_upcoming_fixtures(league["league_id"])
        print("Próximos jogos:")
        for fixture in fixtures:
            print(f"  {fixture['date']}: {fixture['home_team']} vs {fixture['away_team']}")
        print("\n")

if __name__ == "__main__":
    main()
