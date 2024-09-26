import scrapy
from scrapy.crawler import CrawlerProcess
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes_list = []
        for quote in response.css('div.quote'):
            quote_data = {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }
            quotes_list.append(quote_data)
        
        # Salva as citações em um arquivo JSON
        with open('quotes.json', 'w') as f:
            json.dump(quotes_list, f, indent=4)

        # Caso haja próxima página
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# Executa o spider
process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()
