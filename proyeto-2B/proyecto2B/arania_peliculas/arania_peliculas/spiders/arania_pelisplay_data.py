import scrapy
import pandas as pd
import os

from arania_peliculas.items import DatosPelicula
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class arania_pelisplay_data(scrapy.Spider):
    
    title = []
    price = []
    urls = []

    name = "peliculas"

    def start_requests(self):
        path = open('./../../data/datos.csv')
        df = pd.read_csv(path)
        value = df['url'].values.tolist()
        for i in value:
            self.urls = [f'https://www.repelis24.live/pelicula/{i}']
            for url in self.urls:
                yield scrapy.Request(url = url)

    def parse(self, response):
        productos = response.css('div.movie-body')
        for producto in productos:
            detalles = producto.css('div.header')
            tiene_detalle = len(detalles) > 0
            if(tiene_detalle):
                producto_loader = ItemLoader(
                    item = DatosPelicula(),
                    selector = producto
                )

                producto_loader.add_css(
                    'titulo',
                    'div  > h1::text',
                )

                producto_loader.add_css(
                    'clasificacion',
                    'h4 > span.classification::text'
                )

                producto_loader.add_css(
                    'vistas',
                    'div.watch::text'
                )

                producto_loader.add_css(
                    'likes',
                    'div.like::text'
                )

                producto_loader.add_css(
                    'cometarios',
                    'div.comment::text'
                )

                producto_loader.add_css(
                    'categoria',
                    'div.category > a::text'
                )

                producto_loader.add_css(
                    'rating',
                    'div.progress-value > div::text'
                )

                

                yield producto_loader.load_item()
            
