# JSON Converter

O **JSON Converter** é uma aplicação Python que realiza conversões entre os formatos de arquivo JSON, XLSX e CSV. O objetivo do projeto é facilitar a manipulação e troca de dados entre diferentes formatos.

## Dependências

Este projeto utiliza as seguintes bibliotecas Python:

- **pandas**: Para manipulação de dados tabulares.
- **openpyxl**: Para leitura e escrita de arquivos XLSX.

### Instalação das Dependências

Certifique-se de que o Python 3 está instalado em sua máquina. Siga os passos abaixo para preparar o ambiente:

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

2. Ative o ambiente virtual:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Instale as dependências listadas no `requirements.txt`:
   ```bash
   pip install pandas openpyxl
   ```

## Como executar

Após instalar as dependências, execute o script principal `main.py` para criar e realizar as conversões entre os arquivos. No terminal, use o comando:

```bash
python main.py
```

O script gerará os arquivos de exemplo no diretório do projeto.

## Métodos disponíveis

### `json_to_xlsx(json_file, xlsx_file)`
Converte um arquivo JSON para XLSX. Utiliza o pandas para carregar os dados e salva o resultado no formato Excel.

### `json_to_csv(json_file, csv_file)`
Converte um arquivo JSON para CSV. Similar ao método anterior, mas salva o arquivo em formato CSV.

### `xlsx_to_json(xlsx_file, json_file)`
Lê um arquivo XLSX e o converte para JSON. Gera um arquivo JSON estruturado a partir dos dados do Excel.

### `csv_to_json(csv_file, json_file)`
Lê um arquivo CSV e o converte para JSON. Útil para transformar dados tabulares de texto em um formato JSON.

## Exemplo de execução

O script principal `main.py` cria um arquivo JSON de exemplo e executa as conversões automaticamente, gerando:

- `exemplo.json` (arquivo original)
- `exemplo.xlsx` (convertido do JSON)
- `exemplo.csv` (convertido do JSON)
- `from_xlsx.json` (convertido do XLSX)
- `from_csv.json` (convertido do CSV)

## Licença

Este projeto está licenciado sob a licença MIT.
