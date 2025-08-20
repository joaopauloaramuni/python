# Quotes Spider

Este projeto é um spider simples feito com Scrapy para coletar citações do site [Quotes to Scrape](http://quotes.toscrape.com/). O spider extrai o texto da citação, o autor e as tags associadas, salvando todos os dados em um arquivo JSON.

## Estrutura do Projeto

```
scrapy-quotes/
├── quotes.py
└── quotes.json
```

### Dependências

Certifique-se de que você tenha o Python e o Scrapy instalados. Você pode instalar o Scrapy usando o seguinte comando:

```bash
pip install scrapy
```

## Como Usar

1. **Clone o repositório**:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd scrapy-quotes
   ```

2. **Execute o spider**:

   Para executar o spider, você pode usar o seguinte comando:

   ```bash
   scrapy runspider quotes.py  # roda um spider diretamente de um arquivo Python
   scrapy crawl quotes         # roda um spider dentro de um projeto Scrapy
   ```

   O spider irá coletar as citações de todas as páginas disponíveis no site e salvar os dados em `quotes.json`.

## Resultados

Após a execução do spider, você encontrará um arquivo chamado `quotes.json` na pasta do projeto. Este arquivo conterá as citações coletadas em formato JSON. O conteúdo do arquivo terá a seguinte estrutura:

```json
[
    {
        "text": "Citação 1",
        "author": "Autor 1",
        "tags": ["tag1", "tag2"]
    },
    {
        "text": "Citação 2",
        "author": "Autor 2",
        "tags": ["tag3", "tag4"]
    }
]
```

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests se você tiver sugestões de melhorias!

## Licença

Este projeto está licenciado sob a MIT License.
