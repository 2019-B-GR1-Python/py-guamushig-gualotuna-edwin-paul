import scrapy
from arania_peliculas.items import UrlPeliculas
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class IntroSpider(scrapy.Spider):
    name = 'arania_peliculas'    
    images_url = []
    
    def start_requests(self):
        for i in range(1,80):
            self.urls = [f'https://www.repelis24.live/pelicula/{i}']
            for url in self.urls:
                yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedora = response.css('div.movie')
        for producto in etiqueta_contenedora:
            producto_loader = ItemLoader(
                item = UrlPeliculas(),
                selector = producto
            )

            producto_loader.add_css(
                'url',
                'div.posterpie > a::attr(href)'
            )

            yield producto_loader.load_item()
