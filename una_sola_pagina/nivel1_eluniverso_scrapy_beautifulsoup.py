from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup

# Item
class Noticia(Item):
    id = Field() # Id
    titular = Field()
    descripcion = Field()

# Spider (solo para una pagina)
class ElUniversoSpider(Spider):
    name = "MiSegundoSpider"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'FEED_EXPORT_FIELDS': ['id', 'descripcion', 'titular'], # Como ordenar las columnas en el CSV?
        # 'CONCURRENT_REQUESTS': 1 # numero de requerimientos concurrentes 
        'FEED_EXPORT_ENCODING': 'utf-8' # Pone los acentos
    }
    start_urls = ["https://www.eluniverso.com/deportes/"]

    # Funcion que se llama al entrar a la pagina https://www.eluniverso.com/deportes/
    def parse(self, response):
        # Usamos soup para parsear el resultado
        soup = BeautifulSoup(response.body, 'html.parser')
        # Tenemos dos contenedores de noticias
        contenedores_noticias = soup.find_all('div', class_="results | space-y-3")
        # Index de la noticia
        i = 0
        for contenedor in contenedores_noticias:
            noticias = contenedor.find_all('div', class_="card-content | space-y-1")
            for noticia in noticias:
                item = ItemLoader(Noticia(), response.body)
                titular = noticia.find('h2').text
                descripcion = noticia.find('p').text
                item.add_value('id', i)
                item.add_value('titular', titular)
                item.add_value('descripcion', descripcion)
                i+=1
                yield item.load_item()

# EJECUCION EN TERMINAL
# python -m scrapy runspider nivel1_eluniverso_scrapy_beautifulsoup.py -o resultados_nivel1_eluniverso_scrapy_beautifulsoup.json -t json
        
# EJECUCION SIN LA TERMINAL
"""
process = CrawlerProcess(
    {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'resultados_nivel1_eluniverso_scrapy_beautifulsoup.csv'
    }
)

process.crawl(ElUniversoSpider)
process.start()
# Ejecuta el archivo
"""