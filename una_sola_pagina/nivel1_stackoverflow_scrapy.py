from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

# ABSTRACCION DE DATOS A EXTRAER - DETERMINA LOS DATOS QUE TENGO QUE LLENAR Y QUE ESTARAN EN EL ARCHIVO GENERADO
class Pregunta(Item):
    id = Field()
    pregunta = Field()
    descripcion = Field()

# CLASE CORE - SPIDER
class StackOverflowSpider(Spider):
    # nombre, puede ser cualquiera 
    name = "MiPrimerSpider" 
    # Forma de configurar el USER AGENT en scrapy
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }  
    # URL SEMILLA
    start_urls = ['https://stackoverflow.com/questions']
    
    # Funcion que se va a llamar cuando se haga el requerimiento a la URL semilla
    def parse(self, response):
        # Selectores: Clase de scrapy para extraer datos
        sel = Selector(response=response)
        # Selector de varias preguntas
        preguntas = sel.xpath("//div[@id='questions']//div[@class='s-post-summary    js-post-summary']")
        i = 0
        for pregunta in preguntas:
            # Instancio mi ITEM con el selector en donde estan los datos para llenarlo
            item = ItemLoader(Pregunta(), pregunta)
            # Lleno las propiedades de mi ITEM a traves de expresiones XPATH a buscar dentro del selector "pregunta"
            item.add_xpath('pregunta', './/h3/a/text()')
            item.add_xpath('descripcion', ".//div[@class='s-post-summary--content-excerpt']/text()")
            item.add_value('id', i)
            i += 1
            # Hago Yield de la informacion para que se escriban los datos en el archivo
            yield item.load_item()

# EJECUCION EN TERMINAL:
# scrapy runspider nivel1_stackoverflow_scrapy.py -o resultados_nivel1_stackoverflow_scrapy.csv
        
    
        