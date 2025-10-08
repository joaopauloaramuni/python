import csv
import json
from faker import Faker
import os
from typing import List, Dict, Any

# Define a quantidade de registros a serem gerados
NUM_REGISTROS = 100
# Define o nome base do arquivo de saída (será usado para .csv e .json)
NOME_BASE_ARQUIVO = 'dados_falsos'

def configurar_faker(locale: str = 'pt_BR') -> Faker:
    """
    Configura e retorna uma instância do Faker.
    
    Args:
        locale (str): O local/idioma para gerar os dados (ex: 'pt_BR', 'en_US').
        
    Returns:
        faker.Faker: Uma instância configurada do gerador de dados.
    """
    # Cria uma instância do Faker com o local especificado
    fake = Faker(locale)
    return fake

def gerar_dados_usuario(fake_instance: Faker) -> Dict[str, Any]:
    """
    Gera um único dicionário com dados de usuário falsos.
    
    Args:
        fake_instance (faker.Faker): A instância do Faker configurada.
        
    Returns:
        dict: Um dicionário contendo os dados do usuário.
    """
    # Usa os métodos do Faker para gerar dados realistas e variados
    dados = {
        'ID': fake_instance.unique.random_int(min=1000, max=9999),
        'Nome Completo': fake_instance.name(),
        'Email': fake_instance.unique.email(),
        'CPF': fake_instance.cpf(),
        'Endereço': fake_instance.address(),
        # Formata a data para uma string padronizada
        'Data de Nascimento': fake_instance.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d'),
        'Cargo': fake_instance.job(),
        'Empresa': fake_instance.company(),
        # Gera um número com 2 casas decimais
        'Salário (BRL)': round(fake_instance.random_number(digits=5) / 100, 2)
    }
    return dados

def salvar_dados_csv(dados_lista: List[Dict], nome_arquivo: str):
    """
    Salva uma lista de dicionários em um arquivo CSV.
    
    Args:
        dados_lista (list): Uma lista de dicionários, onde cada dicionário é um registro.
        nome_arquivo (str): O nome do arquivo CSV para salvar.
    """
    if not dados_lista:
        print("A lista de dados está vazia. Não é possível criar o CSV.")
        return
        
    # Obtém os nomes das colunas (chaves do primeiro dicionário)
    campos = list(dados_lista[0].keys())
    
    try:
        # Abre o arquivo para escrita ('w')
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            
            # Escreve o cabeçalho e os registros
            writer.writeheader()
            writer.writerows(dados_lista)
            
        print(f"-> CSV criado com sucesso: {os.path.abspath(nome_arquivo)}")
        
    except IOError as e:
        print(f"ERRO ao salvar o CSV em {nome_arquivo}. Detalhes: {e}")

def salvar_dados_json(dados_lista: List[Dict], nome_arquivo: str):
    """
    Salva uma lista de dicionários em um arquivo JSON.
    
    Args:
        dados_lista (list): Uma lista de dicionários, onde cada dicionário é um registro.
        nome_arquivo (str): O nome do arquivo JSON para salvar.
    """
    try:
        # Abre o arquivo para escrita ('w')
        with open(nome_arquivo, 'w', encoding='utf-8') as jsonfile:
            # Usa json.dump para escrever a lista de dicionários.
            # 'indent=4' é usado para formatar o JSON de forma legível.
            json.dump(dados_lista, jsonfile, indent=4, ensure_ascii=False)
            
        print(f"-> JSON criado com sucesso: {os.path.abspath(nome_arquivo)}")
        
    except IOError as e:
        print(f"ERRO ao salvar o JSON em {nome_arquivo}. Detalhes: {e}")


def main():
    """
    Função principal que orquestra a geração e o salvamento dos dados em CSV e JSON.
    """
    print("Iniciando o Gerador de Dados Falsos (CSV e JSON)...")
    
    # 1. Configura o Faker (usando pt_BR para dados brasileiros)
    fake = configurar_faker(locale='pt_BR')
    
    # Lista para armazenar todos os registros gerados
    registros: List[Dict] = []
    
    # 2. Gera os dados
    print(f"\nGerando {NUM_REGISTROS} registros...")
    for i in range(NUM_REGISTROS):
        registro = gerar_dados_usuario(fake)
        registros.append(registro)
        # Feedback de progresso
        if (i + 1) % (NUM_REGISTROS // 10 or 1) == 0:
             print(f"Progresso: {i + 1}/{NUM_REGISTROS}...")

    # 3. Salva os dados nos formatos
    print("\n--- Processo de Salvamento ---")
    
    # Salva em CSV
    nome_csv = f"{NOME_BASE_ARQUIVO}.csv"
    salvar_dados_csv(registros, nome_csv)
    
    # Salva em JSON
    nome_json = f"{NOME_BASE_ARQUIVO}.json"
    salvar_dados_json(registros, nome_json)
    
    print(f"\n--- FIM ---")
    print(f"Total de {len(registros)} registros criados com sucesso.")

# Inicia a execução do script
if __name__ == "__main__":
    # Lembre-se de instalar a dependência:
    # pip install faker
    main()

# pip install faker