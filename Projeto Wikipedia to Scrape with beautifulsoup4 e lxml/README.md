
# Wikipedia Spider

Este projeto é um spider simples feito com Scrapy para coletar dados da página da Wikipedia sobre Python. O spider extrai o título da página e o texto dos parágrafos, salvando todos os dados em um arquivo JSON.

## Estrutura do Projeto

```
scrapy-wikipedia/
├── wikipedia.py
└── python_wikipedia.json
```

### Dependências

Certifique-se de que você tenha o Python e o Scrapy instalados. Você pode instalar o Scrapy usando o seguinte comando:

```bash
pip install scrapy
pip install beautifulsoup4 lxml 
```

## Como Usar

1. **Clone o repositório**:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd scrapy-wikipedia
   ```

2. **Execute o spider**:

   Para executar o spider, você pode usar o seguinte comando:

   ```bash
   scrapy runspider wikipedia.py
   ```

   O spider irá coletar os dados da página da Wikipedia e salvar os dados em `python_wikipedia.json`.

## Resultados

Após a execução do spider, você encontrará um arquivo chamado `python_wikipedia.json` na pasta do projeto. Este arquivo conterá os dados coletados em formato JSON. O conteúdo do arquivo terá a seguinte estrutura:

```json
{
    "title": "Título da página",
    "summary": "Texto concatenado dos parágrafos da página"
}
```

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests se você tiver sugestões de melhorias!

## Licença

Este projeto está licenciado sob a MIT License.

