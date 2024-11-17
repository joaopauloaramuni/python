import requests
import threading

# Configuração do alvo
TARGET_URL = "https://httpbin.org/get"  # Alvo seguro para testes
REQUEST_COUNT = 50  # Número de requisições

# Função para enviar uma requisição ao alvo
def send_request():
    try:
        response = requests.get(TARGET_URL)
        print(f"Status: {response.status_code}, Response: {response.json()}")
    except Exception as e:
        print(f"Erro ao enviar requisição: {e}")

# Threading para enviar múltiplas requisições simultâneas
def simulate_ddos():
    threads = []
    for _ in range(REQUEST_COUNT):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print(f"Iniciando ataque controlado para {TARGET_URL} com {REQUEST_COUNT} requisições.")
    simulate_ddos()
    print("Teste finalizado.")

# pip install requests