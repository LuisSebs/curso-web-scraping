import requests
from bs4 import BeautifulSoup

# URL a scrapear
url = "https://news.ycombinator.com/"

# Encabezado de la peticion
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Peticion a la URL
respuesta = requests.get(url, headers=headers)

# Extraemos el arbol HTML
soup = BeautifulSoup(respuesta.text, 'html.parser')

# Extraemos las noticias
lista_de_noticias = soup.find_all('tr', class_="athing")

# Por cada noticia
for noticia in lista_de_noticias:
    # Extrameos el titulo
    titulo = noticia.find('span', class_="titleline").text
    # Extraemos la url
    url = noticia.find('span', class_="titleline").find('a').get('href')
    # Extraemos la metadata
    metadata = noticia.find_next_sibling()

    # Puntuacion
    score = 0
    # Comentarios
    comentarios = 0

    # Intentamos
    try:
        # Extraemos el score (si hay)
        score_tmp = metadata.find('span', class_="score").text
        score_tmp = score_tmp.replace('points', '').strip()
        score = int(score_tmp)
    except:
        print('No hay score')
    
    try:
        # Extraemos los comentarios (si hay)
        comentarios_tmp = metadata.find('span', attrs={ 'class': 'subline'}).text
        comentarios_tmp = comentarios_tmp.split('|')[-1]
        comentarios_tmp = comentarios_tmp.replace('comments', '').strip()
        comentarios = int(comentarios_tmp)
    except:
        print('No hay comentarios')

    # Imprimimos la informacion
    print(titulo)
    print(url)
    print(score)
    print(comentarios)
    print()

