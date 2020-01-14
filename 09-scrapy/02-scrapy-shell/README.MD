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