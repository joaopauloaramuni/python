import scrapy
from scrapy.crawler import CrawlerProcess
import json

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['http://books.toscrape.com/']

    # Inicializamos uma lista para acumular os dados de todos os livros de todas as páginas
    books_list = []

    def parse(self, response):
        # Extrai os dados dos livros da página atual
        for book in response.css('article.product_pod'):
            book_data = {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('p.price_color::text').get(),
                'availability': book.css('p.instock.availability::text').re_first('(\S+\s\S+)'),
            }
            self.books_list.append(book_data)

        # Caso haja próxima página
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # Segue para a próxima página
            yield response.follow(next_page, self.parse)
        else:
            # Quando não houver mais páginas, salva os dados acumulados em um arquivo JSON
            with open('books.json', 'w', encoding='utf-8') as f:
                json.dump(self.books_list, f, ensure_ascii=False, indent=4)

# Executa o spider
process = CrawlerProcess()
process.crawl(BooksSpider)
process.start()
