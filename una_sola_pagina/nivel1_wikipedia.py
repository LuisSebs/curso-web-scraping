import requests
from lxml import html

encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://www.wikipedia.org//"

# Por defecto el encabezado es ROBOT (algunos sitios pueden alertarse por este encabezado)
# recomendable sobre escribirlo por el encabezado "user-agent"

respuesta = requests.get(url=url, headers=encabezados)
parser = html.fromstring(respuesta.text)

# Obtener elemento por id
# spanish = parser.get_element_by_id("js-link-box-es")
# Mostrar contenido:
# spanish.text_content()

# Obtener elemento usando XPATH
# spanish = parser.xpath("//a[@id='js-link-box-es']//strong/text()")
# Mostrar contenido:
# print(spanish)

# Obtener todos los idiomas
idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]")
for i in idiomas:
    print(i.text_content())

