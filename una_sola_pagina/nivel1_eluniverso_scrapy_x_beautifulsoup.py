from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

# ABSTRACCION DE DATOS A EXTRAER - DETERMINA LOS DATOS QUE TENGO QUE LLENAR Y QUE ESTARAN EN EL ARCHIVO GENERADO
class Noticia(Item):
    titular = Field()
    descripcion = Field()

# CLASE CORE - SPIDER
class ElUniversoSpider(Spider):
    # Nombre del spider
    name = "MiSegundoSpider"
    # Configuracion del USER AGENT en scrapy
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    # URL SEMILLA
    start_urls = ["https://www.eluniverso.com/deportes"]

    # Funcion que se va a llamar cuando se haga el requerimiento a la URL semilla
    def parse(self, response):
        # Selectores: Clase de scrapy para extraer datos
        sel = Selector(response=response)
        # Selector de varias noticias
        noticias = sel.xpath("//section[3]//div[contains(@class,'results')]//li")
        for noticia in noticias:
            # Selectores: Clase de scrapy para extraer datos
            item = ItemLoader(Noticia(), noticia)
            # Llenamos las propiedades del ITEM a partir de expresiones XPATH dentro del selector "noticia"
            item.add_xpath('titular', ".//div[contains(@class,'card-content')]//h2//a/text()")
            item.add_xpath('descripcion','.//p/text()')
            
            # Nota: Cuando no encuentra un elemento a partir de un XPATH
            # al momento de generar el resultado en un JSON no lo agrega
            # , es decir que Scrapy ya maneja el caso en el que algunos
            # elementos no cuenten con cierta informacion.

            # Hago Yield de la informacion para que se escriban los datos en el archivo
            yield item.load_item()

# EJECUCION EN TERMINAL:
# scrapy runspider nivel1_eluniverso_scrapy_x_beautifulsoup.py -o resultados_nivel1_eluniverso_scrapy_x_beautifulsoup.json


