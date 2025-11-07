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

def obter_pib_nominal_por_uf(uf_sigla, ano=2021):
    """Retorna o PIB nominal (a preços correntes) de um estado (UF) em Mil Reais."""
    ufs = obter_ufs()
    uf_encontrada = next((uf for uf in ufs if uf["sigla"].upper() == uf_sigla.upper()), None)
    if not uf_encontrada:
        raise Exception(f"UF '{uf_sigla}' não encontrada.")

    uf_id = uf_encontrada["id"]
    url = f"{AGREGADOS_URL}/5938/periodos/{ano}/variaveis/37?localidades=N3[{uf_id}]"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        try:
            pib = dados[0]["resultados"][0]["series"][0]["serie"][str(ano)]
            nome_uf = dados[0]["resultados"][0]["series"][0]["localidade"]["nome"]
            return {"nome": nome_uf, "pib_mil_reais": int(pib)}
        except (KeyError, IndexError):
            raise Exception("Não foi possível extrair o PIB nominal dos dados retornados.")
    else:
        raise Exception(f"Erro ao buscar PIB: {response.status_code}, {response.text}")

def obter_populacao_por_sexo_uf(uf_sigla, ano=2022):
    """
    Retorna a população de homens e mulheres de uma UF em um determinado ano.
    """
    ufs = obter_ufs()
    uf_encontrada = next((uf for uf in ufs if uf["sigla"].upper() == uf_sigla.upper()), None)
    if not uf_encontrada:
        raise Exception(f"UF '{uf_sigla}' não encontrada.")
    
    uf_id = uf_encontrada["id"]
    populacao_sexo = {}
    for sexo_id, sexo_nome in [("4", "Homens"), ("5", "Mulheres")]:
        url = f"{AGREGADOS_URL}/10125/periodos/{ano}/variaveis/11852?localidades=N3[{uf_id}]&classificacao=2[{sexo_id}]|58[all]"
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            try:
                total = int(dados[0]["resultados"][0]["series"][0]["serie"][str(ano)])
                populacao_sexo[sexo_nome] = total
            except (KeyError, IndexError):
                populacao_sexo[sexo_nome] = None
        else:
            populacao_sexo[sexo_nome] = None
    return populacao_sexo

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

    # População estimada (2025)
    try:
        dados_pop = obter_populacao_estimada_por_uf(uf_sigla)
        print(f"\n👥 População residente estimada de {dados_pop['nome']} (2025): {dados_pop['populacao']:,} pessoas")
    except Exception as e:
        print(e)
    
    # PIB nominal (2021)
    try:
        dados_pib = obter_pib_nominal_por_uf(uf_sigla)
        print(f"💰 PIB nominal de {dados_pib['nome']} (2021): R$ {dados_pib['pib_mil_reais'] * 1000:,.2f}")
    except Exception as e:
        print(e)
    
    # População por sexo (2022)
    try:
        pop_sexo = obter_populacao_por_sexo_uf(uf_sigla)
        print(f"\n👨‍👩‍👧 População de {uf_sigla} em 2022 por sexo:")
        print(f"👨 Homens: {pop_sexo.get('Homens', 'N/A'):,}")
        print(f"👩 Mulheres: {pop_sexo.get('Mulheres', 'N/A'):,}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
