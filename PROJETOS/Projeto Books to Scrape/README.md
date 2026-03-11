
# Books Spider

Este projeto é um web scraper que coleta dados sobre livros do site [Books to Scrape](http://books.toscrape.com/). Utiliza a biblioteca Scrapy para realizar a raspagem dos dados.

## Funcionalidades

- Coleta o título, preço e disponibilidade de cada livro.
- Navega por todas as páginas do site e acumula os dados.
- Salva os dados coletados em um arquivo JSON chamado `books.json`.

## Estrutura do Projeto

A estrutura básica do projeto é a seguinte:

```
scrapy-books/
├── books.py
└── books.json
```

## Como Usar

1. **Clone o repositório**:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd nome-da-pasta
   ```
   
2. **Crie e ative o ambiente virtual:**

   É recomendável usar um ambiente virtual para gerenciar suas dependências.  
   Siga os passos abaixo para configurar um ambiente virtual:

   a. Crie um ambiente virtual usando o seguinte comando:

   ```bash
   python3 -m venv .venv
   ```
   
   b. Ative o ambiente virtual:

   - No macOS e Linux:

     ```bash
     source .venv/bin/activate
     ```
     
   - No Windows:

     ```bash
     .venv\Scripts\activate
     ```
     
3. **Instale as dependências:**

   Certifique-se de que você tenha o Python e o Scrapy instalados.  
   Você pode instalar o Scrapy usando o seguinte comando:

   ```bash
   pip install scrapy
   ```
   
4. **Execute o spider**:

   Para executar o spider, você pode usar o seguinte comando:

   ```bash
   scrapy runspider books.py  # roda um spider diretamente de um arquivo Python
   scrapy crawl books         # roda um spider dentro de um projeto Scrapy
   ```

   O spider irá coletar as citações de todas as páginas disponíveis no site e salvar os dados em `books.json`.

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
