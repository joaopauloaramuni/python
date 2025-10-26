import requests

BASE_URL = "https://servicodados.ibge.gov.br/api/v1/localidades"

def obter_ufs():
    """Retorna uma lista de todos os estados (UFs) do Brasil."""
    url = f"{BASE_URL}/estados"
    response = requests.get(url)
    if response.status_code == 200:
        ufs = response.json()
        return [{"id": uf["id"], "sigla": uf["sigla"], "nome": uf["nome"]} for uf in ufs]
    else:
        raise Exception(f"Erro ao buscar UFs: {response.status_code}")

def obter_municipios(uf_sigla):
    """Retorna todos os municípios de um estado específico (UF)."""
    url = f"{BASE_URL}/estados/{uf_sigla}/municipios"
    response = requests.get(url)
    if response.status_code == 200:
        municipios = response.json()
        return [{"id": m["id"], "nome": m["nome"]} for m in municipios]
    else:
        raise Exception(f"Erro ao buscar municípios para {uf_sigla}: {response.status_code}")

def main():
    # Buscar e exibir todos os estados
    print("Buscando todos os estados...")
    ufs = obter_ufs()
    for uf in ufs:
        print(f"{uf['sigla']} - {uf['nome']}")

    # Solicitar ao usuário a sigla do estado para buscar municípios
    uf_escolhido = input("\nDigite a sigla do estado para listar seus municípios: ").upper()
    
    # Buscar e exibir municípios
    try:
        municipios = obter_municipios(uf_escolhido)
        print(f"\nMunicípios de {uf_escolhido}:")
        for m in municipios:
            print(m["nome"])
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

# pip install requests