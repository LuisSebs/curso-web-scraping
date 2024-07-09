from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

# Item
class Hotel(Item):
    nombre = Field()
    score = Field()
    descripcion = Field()
    amenities = Field()

# CrawSpider (para scraping vertical con varias paginas)
class TripAdvisor(CrawlSpider):
    name = "Hoteles"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',        
    }

    # Reduce el espectro de busqueda de URLs. No nos podemos salir de los dominios de esta lista
    allowed_domains = ['tripadvisor.com']
    
    # URL semilla
    start_urls = ['https://www.tripadvisor.com/Hotels-g303845-Guayaquil_Guayas_Province-Hotels']

    # Tiempo que se toma entre cada peticion para evitar ser detectados como web scraping
    download_delay = 2

    # Tupla de reglas para direccionar el movimiento de nuestro Crawler a traves de las paginas
    rules = (
        Rule( # Regla de movimiento VERTICAL hacia el detalle de los hoteles
            LinkExtractor(
                allow=r'/Hotel_Review-' # Si la URL contiene este patron, haz un requerimiento a esa URL
            ),
            follow=True, # Seguir url?
            callback="parse_hotel" # Funcion a ejecutar cuando se hace un requerimiento a los links que cumplen con el patron Hotel_Review-
        ),
    )

    def parse_hotel(self, response):
        sel = Selector(response=response)
        item = ItemLoader(Hotel(), sel)

        item.add_xpath('nombre', "//h1[@id='HEADING']")
        item.add_xpath(
            'score', 
            "//span[@class='kJyXc P']/text()",
            MapCompose(self.add_prefix_points) # Funcion para pre-procesar un valor
        )
        item.add_xpath('descripcion', "//div[@data-tab='TABS_ABOUT']//div[@class='fIrGe _T']/text()")
        # Al ser varios elementos los separa por comas
        item.add_xpath('amenities', "//div[@data-tab='TABS_ABOUT']//div[@class='Jevoh f K'][1]/div[@class='gFttI f ME Ci H3 _c']/text()")

        yield item.load_item()

    # Funcion a utilizar con MapCompose para realizar limpieza de datos
    def add_prefix_points(self, texto):
        return texto+" points"

# EJECUCION
# python -m scrapy runspider nivel2_tripadvisor.py -o nivel2_tripadvisor.csv