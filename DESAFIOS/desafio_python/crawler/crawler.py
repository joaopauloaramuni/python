import scrapy


class GloboSpider(scrapy.Spider):
    name = "globo_spider"
    start_urls = ['https://g1.globo.com/']

    def parse(self, response):
        for artigo in response.css(".bastian-feed-item")[:3]:
            titulo = artigo.css(".feed-post-link::text ").extract_first()
            url_imagem = None
            if artigo.css(".bstn-fd-picture-image").extract_first() is not None:
                url_imagem = artigo.css(".bstn-fd-picture-image::attr(src)").extract_first()
            subtitulo = None
            if artigo.css(".feed-post-body-resumo").extract_first() is not None:
                subtitulo = artigo.css(".feed-post-body-resumo div::text").extract_first()
            if artigo.css(".bstn-relatedtext").extract_first() is not None:
                subtitulo = artigo.css(".bstn-relatedtext::text").extract_first()
            yield {'Título': titulo, 'Subtitulo': subtitulo, 'Url Imagem': url_imagem}
