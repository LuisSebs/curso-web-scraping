from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Articulo(Item):
    titulo = Field()
    precio = Field()
    descripcion = Field()

class MercadoLibreCrawler(CrawlSpider):
    name = "mercadolibre"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 20
    }

    download_delay = 1

    allowed_domains = ['listado.mercadolibre.com.ec', 'articulo.mercadolibre.com.ec']

    start_urls = ['https://listado.mercadolibre.com.ec/animales-mascotas/perros/']

    rules = (
        # Paginacion
        Rule(

        ),
        # Detalle de los productos
        Rule(
            LinkExtractor(
                allow=r'/MEC-'
            ),
            follow=True,
            callback='parse_items'
        )
    )

    def parse_itms(self, response):
        None

# Precio retail (precio con descuento)
# Precio original (precio tachado)
# Modelo
# Marca
# Alto
# Ancho 
# Fondo
# Tipo de vehiculo
# Rin
# Todos los campos que se puedan