
# Books Spider

Este projeto é um web scraper que coleta dados sobre livros do site [Books to Scrape](http://books.toscrape.com/). Utiliza a biblioteca Scrapy para realizar a raspagem dos dados.

## Funcionalidades

- Coleta o título, preço e disponibilidade de cada livro.
- Navega por todas as páginas do site e acumula os dados.
- Salva os dados coletados em um arquivo JSON chamado `books.json`.

## Dependências

Este projeto utiliza as seguintes bibliotecas:

- `scrapy`

As dependências do projeto podem ser instaladas utilizando pip com o seguinte comando:

```bash
pip install scrapy
```

## Estrutura do Projeto

A estrutura básica do projeto é a seguinte:

```
scrapy-books/
├── books.py
└── books.json
```

## Executando o Projeto

Para executar o projeto, use o seguinte comando:

```bash
scrapy crawl books
```

Os dados raspados serão salvos no arquivo `books.json`.

## Resultados

Os dados coletados terão a seguinte estrutura no arquivo `books.json`:

```json
[
    {
        "title": "Book Title 1",
        "price": "£50.00",
        "availability": "In stock"
    },
    {
        "title": "Book Title 2",
        "price": "£35.99",
        "availability": "In stock"
    }
]
```

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
