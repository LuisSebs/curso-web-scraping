import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = 'https://stackoverflow.com/questions'

respuesta = requests.get(url, headers=headers)

soup  = BeautifulSoup(respuesta.text, 'html.parser')

# Unica coincidencia
contenedor_de_preguntas = soup.find(id="questions")

# Lista de coincidencias
lista_de_preguntas = contenedor_de_preguntas.find_all('div', class_="s-post-summary js-post-summary")

def forma1():
    # Forma uno de obtener el titulo de las preguntas y su descipcion
    for pregunta in lista_de_preguntas:
        texto_pregunta = pregunta.find('h3').text
        descripcion_pregunta = pregunta.find('div',class_="s-post-summary--content-excerpt").text
        descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r', '').strip()
        print(texto_pregunta)
        print(descripcion_pregunta)

def forma2():
    # Forma uno de obtener el titulo de las preguntas y su descipcion usando siblings
    for pregunta in lista_de_preguntas:
        elemento_texto_pregunta = pregunta.find('h3')
        texto_pregunta = elemento_texto_pregunta.text
        descripcion_pregunta = elemento_texto_pregunta.find_next_sibling().text
        descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r', '').strip()
        print(texto_pregunta)
        print(descripcion_pregunta)



