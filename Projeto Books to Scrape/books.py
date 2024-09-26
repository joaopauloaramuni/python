import scrapy
from scrapy.crawler import CrawlerProcess
import json

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books_list = []
        for book in response.css('article.product_pod'):
            book_data = {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('p.price_color::text').get(),
                'availability': book.css('p.instock.availability::text').re_first('(\S+\s\S+)'),
            }
            books_list.append(book_data)
        
        # Salva os dados dos livros em um arquivo JSON
        with open('books.json', 'w') as f:
            json.dump(books_list, f, indent=4)

        # Caso haja próxima página
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# Executa o spider
process = CrawlerProcess()
process.crawl(BooksSpider)
process.start()
