import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
import json

class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia_spider'
    start_urls = ['https://pt.wikipedia.org/wiki/Python']

    def __init__(self):
        self.data = []  # Inicializa uma lista para armazenar os dados

    def parse(self, response):
        title = response.css('h1 i::text').get()  # Captura o título da página
        
        # Utiliza BeautifulSoup para processar o HTML
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Captura todos os parágrafos não vazios
        paragraphs = soup.select('div.mw-parser-output > p:not(.mw-empty-elt)')
        
        # Concatena o texto de cada parágrafo, mantendo os espaços corretos
        summary_text = ' '.join([para.get_text(separator=' ', strip=True) for para in paragraphs if para.get_text(strip=True)])

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
