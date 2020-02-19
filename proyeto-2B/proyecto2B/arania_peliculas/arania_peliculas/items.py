# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

def quitar_seccio_url(texto):
    caracter_a_borrar = 'https://www.pelisplay.co/pelicula/'
    caracter_reemplazar = ''
    return texto.replace(caracter_a_borrar,caracter_reemplazar)

def limpieza_texto(texto):
    texto = texto.replace("\t","")
    texto = texto.replace("\n","")
    texto = texto.replace(",",".")
    texto = texto.replace("\u00f3","o")
    texto = texto.replace("Me gusta","")
    texto = texto.replace(" ","")
    texto = texto.replace("Visitas","")
    texto = texto.replace("Comentarios","")
    return texto

def quitar_tildes(texto):
    texto = texto.replace("\u00e1","a")
    texto = texto.replace("\u00e9","e")
    texto = texto.replace("\u00ed","i")
    texto = texto.replace("\u00f3","o")
    texto = texto.replace("\u00fa","u")
    texto = texto.replace("\u00f1","ni")
    texto = texto.replace("\u00bf","¿")
    return texto

def quitar_punto(texto):
    texto = texto.replace("\t","")
    texto = texto.replace("\n","")  
    texto = texto.replace(" ","")
    texto = texto.replace("Visitas","")
    texto =  texto.replace(",","")
    return texto

class UrlPeliculas(scrapy.Item):
    url = scrapy.Field(
        input_processor = MapCompose(
            quitar_seccio_url
        ) 
    )

class DatosPelicula(scrapy.Item):
    titulo = scrapy.Field(
        input_processor = MapCompose(
            quitar_tildes
        )
    )
    clasificacion = scrapy.Field()
    vistas = scrapy.Field(
        input_processor = MapCompose(
            quitar_punto
        ) 
    )
    likes = scrapy.Field(
        input_processor = MapCompose(
            limpieza_texto
        ) 
    )
    cometarios = scrapy.Field(
        input_processor = MapCompose(
            limpieza_texto
        )
    )
    categoria = scrapy.Field(
        input_processor = MapCompose(
            limpieza_texto
        )
    )
    rating = scrapy.Field(
        input_processor = MapCompose(
            limpieza_texto
        )
    )
    

class AraniaPeliculasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
