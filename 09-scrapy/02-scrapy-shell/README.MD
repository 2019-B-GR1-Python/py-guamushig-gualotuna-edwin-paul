# SCRAPY    

## Scrapy instalacion

Ejecutar en la **terminal** de Linux.

```
$ pip install scrapy
```

## Comandos genereales

Da las caracteristicas para poder hacer Web Scraping o Web Crawling de ese computador.
```
$ scrapy bench
```

Visualizar configuraciones extras.
```
$ scrapy settings
```

Visualizamos la version de scrapy con la que estamos trabajando.

```
$ scrapy version 
```


## Scrapy view

Depende la forma en la que se carga el contenido para poder visualizar.  Cuando el contenido utiliza JS y carga
su contenido desde otro servicios no se va a poder realizar scrapy.

```
$ scrapy view <url de la pagina> 
```

### Scrapy shell <url>

Permite interactuar con la respuesta del scrapy mediante un shell.

```
$ scrapy shell <url>
```


## Metodos utilizados:

```
$ response.xpath('/html/head/title').extract()
$ response.xpath('//title').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath("//div[@class='quote']/span[@class='text']").extract_first()
$ response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()
$ //div[@class='quote']/span/a/@href").extract_first()
```

## Scrapy startpoject <nombre_proyecto>

```
$ scrapy startproject arania_basica
```