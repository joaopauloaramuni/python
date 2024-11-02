import scrapy
from scrapy.crawler import CrawlerProcess
import json

class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia_spider'
    start_urls = ['https://pt.wikipedia.org/wiki/Python']

    def __init__(self):
        self.data = []  # Inicializa uma lista para armazenar os dados

    def parse(self, response):
        title = response.css('h1 i::text').get()  # Captura o título da página
        paragraphs = response.css('div.mw-parser-output > p:not(.mw-empty-elt)')  # Captura todos os parágrafos não vazios

        # Concatena o texto de cada parágrafo, mantendo a formatação HTML
        summary_text = ' '.join([para.get() for para in paragraphs if para.get().strip()])  # Mantém a formatação HTML

        # Estrutura de dados
        item = {
            'title': title if title else 'Título não encontrado',  # Valida se o título está vazio
            'summary': summary_text if summary_text else 'Resumo não encontrado'
        }

        self.data.append(item)  # Adiciona o item à lista de dados

        # Salva os dados em JSON
        self.save_to_json()

    def save_to_json(self):
        # Salvar os dados coletados em um arquivo JSON
        with open('python_wikipedia.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
            self.log(f'Dados salvos em python_wikipedia.json.')

# Configurar e iniciar o crawler
process = CrawlerProcess()

# Iniciar o spider
process.crawl(WikipediaSpider)
process.start()
