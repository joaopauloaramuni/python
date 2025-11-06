import requests

BASE_URL = "https://servicodados.ibge.gov.br/api/v1/localidades"
AGREGADOS_URL = "https://servicodados.ibge.gov.br/api/v3/agregados"

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

def obter_populacao_estimada_por_uf(uf_sigla, ano=2025):
    """
    Retorna a população residente estimada de um estado (UF) pela sua sigla.
    Exemplo: obter_populacao_estimada_por_uf("MG", 2025)
    """
    # Primeiro, obtemos a lista de UFs e o ID correspondente à sigla
    ufs = obter_ufs()
    uf_encontrada = next((uf for uf in ufs if uf["sigla"].upper() == uf_sigla.upper()), None)
    if not uf_encontrada:
        raise Exception(f"UF '{uf_sigla}' não encontrada.")

    uf_id = uf_encontrada["id"]
    url = f"{AGREGADOS_URL}/6579/periodos/{ano}/variaveis/9324?localidades=N3[{uf_id}]"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        try:
            populacao = dados[0]["resultados"][0]["series"][0]["serie"][str(ano)]
            nome_uf = dados[0]["resultados"][0]["series"][0]["localidade"]["nome"]
            return {"nome": nome_uf, "populacao": int(populacao)}
        except (KeyError, IndexError):
            raise Exception("Não foi possível extrair a população estimada dos dados retornados.")
    else:
        raise Exception(f"Erro ao buscar população estimada: {response.status_code}")

def main():
    print("Buscando todos os estados...")
    ufs = obter_ufs()
    for uf in ufs:
        print(f"{uf['sigla']} - {uf['nome']}")

    uf_sigla = input("\nDigite a sigla do estado para listar seus municípios: ").upper()

    try:
        municipios = obter_municipios(uf_sigla)
        print(f"\nMunicípios de {uf_sigla}:")
        for m in municipios:
            print(m["nome"])
    except Exception as e:
        print(e)
        return

    # Buscar e exibir a população estimada
    try:
        dados_pop = obter_populacao_estimada_por_uf(uf_sigla)
        print(f"\nPopulação residente estimada de {dados_pop['nome']} (2025): {dados_pop['populacao']:,} pessoas")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
