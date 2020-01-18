import scrapy
import csv
from urllib.parse import urljoin

nombre_archivo = 'libros.csv'


def guardar_archivo(titulos, precios, links):
    with open(nombre_archivo, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        data = list(zip(titulos, precios, links))
        for row in data:
            row = list(row)
            spamwriter.writerow(row)
    print("Listo :)")



def precio_float(precios):
    return float(precios[1:])


class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url = url) # palabra clave para esperar que se complete esa linea


    def parse(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        titulos = etiqueta_contenedora.css('h3 > a::text').extract()
        precios = response.css('article > div > p.price_color::text').extract()
        links = response.css('article > div > a > img::attr(src)').extract()
        
        url_completa = []
        for url in links:
            url_completa.append(response.urljoin(url))


        precios_float = list(map(precio_float, precios))
        guardar_archivo(titulos, precios_float, url_completa)

        print(titulos)
        print(url_completa)
        print(precios_float)