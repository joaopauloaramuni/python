import pandas as pd
import json


def json_to_xlsx(json_file, xlsx_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        df = pd.DataFrame(data)
        df.to_excel(xlsx_file, index=False, engine='openpyxl')
        print(f"Arquivo JSON convertido para XLSX: {xlsx_file}")
    except Exception as e:
        print(f"Erro ao converter JSON para XLSX: {e}")


def json_to_csv(json_file, csv_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        df = pd.DataFrame(data)
        df.to_csv(csv_file, index=False)
        print(f"Arquivo JSON convertido para CSV: {csv_file}")
    except Exception as e:
        print(f"Erro ao converter JSON para CSV: {e}")


def xlsx_to_json(xlsx_file, json_file):
    try:
        df = pd.read_excel(xlsx_file, engine='openpyxl')
        data = df.to_dict(orient='records')
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Arquivo XLSX convertido para JSON: {json_file}")
    except Exception as e:
        print(f"Erro ao converter XLSX para JSON: {e}")


def csv_to_json(csv_file, json_file):
    try:
        df = pd.read_csv(csv_file)
        data = df.to_dict(orient='records')
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Arquivo CSV convertido para JSON: {json_file}")
    except Exception as e:
        print(f"Erro ao converter CSV para JSON: {e}")


if __name__ == "__main__":
    # Arquivos a serem gerados no próprio diretório do projeto
    json_file = "exemplo.json"
    xlsx_file = "exemplo.xlsx"
    csv_file = "exemplo.csv"

    # Criação de um JSON de exemplo diretamente no código
    example_data = [
        {"nome": "João", "idade": 30, "cidade": "Belo Horizonte"},
        {"nome": "Maria", "idade": 25, "cidade": "São Paulo"},
        {"nome": "José", "idade": 35, "cidade": "Rio de Janeiro"}
    ]

    # Salvando o JSON de exemplo na pasta do projeto
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(example_data, f, ensure_ascii=False, indent=4)
    print(f"Arquivo JSON de exemplo criado: {json_file}")

    # Realizando as conversões
    json_to_xlsx(json_file, xlsx_file)
    json_to_csv(json_file, csv_file)
    xlsx_to_json(xlsx_file, "from_xlsx.json")
    csv_to_json(csv_file, "from_csv.json")

# pip install pandas openpyxl