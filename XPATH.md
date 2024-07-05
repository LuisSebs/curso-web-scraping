# XPATH

XPath es un lenguaje de navegación de grafos que se usa para seleccionar un conjunto de nodos de un documento XML.

## Probador de expresiones XPATH
http://xpather.com/

## Documentacion XPATH
https://devhints.io/xpath

# Overview

Expresiones básicas

## Ejes de busqueda

- **/**  -> busqueda en la raiz
- **//** -> busqueda en cualquier nivel
- **./** -> busqueda relativa

## Busqueda por atributos
**//<etiqueta\>[@<atributo\>]**

- //h1[@class = "titulo"]
- //h1[@class != "titulo"]

```html
<body>
    <h1 class="titulo">Hola mundo!</h1>
    <h1 class="subtitulo">XPATH</h1>
    <h2>Espot</h2>
</body>
```

## Operadores and or

- //h1[@class = "titulo" or @class = "subtitulo"]
- //h1[@class = "titulo" and @id = "subtitulo"]

```html
<body>
    <h1 class="titulo">Hola mundo!</h1>
    <h1 class="titulo" id="subtitulo">XPATH</h1>
    <h2>Espot</h2>
</body>
```

## Busquedas a profundidad

- //div[@class="article"]//button[@class="btn" or @class="btn toggle"]

```html
<body>
    <div class="article">
        <img src="" alt="perrito">
        <p>Lorem ipsum dolor sit amet.</p>
        <button class="btn">Read More</button>
    </div>
    <div class="article">
        <img src="" alt="perrito">
        <p>Lorem ipsum dolor sit amet.</p>
        <button class="btn toggle">Read More</button>
    </div>
    <button id="">Next</button>
</body>
```

## Indexacion y Funciones

**Indexacion:**
- //div[1]//li[@class = "item"][3]
- //div[1]//li[@class = "item"][last()]
- //div[1]//li[@class = "item"][position() = 3]

**Funciones**
- //div[contains(@class, "container-dos")]
- //div[starts-with(@class, "container")]
- //div[ends-with(@class, "uno")]
- //div[not(ends-with(@class, "uno"))]
- //a[contains(text(), "consectetur")]

```html
<body>
    <div class="container container-uno">
        <ul>
            <li class="item">
                <a href="">Lorem ipsum dolor sit amet.</a>
            </li>
            <li class="item">
                <a href="">Lorem ipsum dolor sit amet.</a>
            </li>
            <li class="item">
                <a href="">Lorem ipsum dolor sit amet.</a>
            </li>
        </ul>
    </div>
    <div class="container container-dos">
        <ul>
            <li class="item">
                <a href="">Lorem ipsum dolor sit amet consectetur.</a>
            </li>
            <li class="item">
                <a href="">Lorem ipsum dolor sit amet consectetur.</a>
            </li>
            <li class="item">
                <a href="">Lorem ipsum dolor sit amet consectetur.</a>
            </li>
        </ul>
    </div>
</body>
```

## Obtener información específica de los tags

- //p /  text()
- //p /  @class

```html
<body>
    <p class="texto">Hola mundo!</p>
</body>
```

# Probar expresiones en caliente

Abrir la consola del navegador en cualquier pagina web y ejecutar

```php
$x("<exprecion-xpath>")
```

Regresara todas las coincidencias de etiquetas y elementos en la pagina web actual.


https://maps.googleapis.com/maps/api/place/findplacefromtext/json?fields=formatted_address%2Cgeometry&input=chedraui%20la%20paz%20palacio&inputtype=textquery&key=AIzaSyBA1f9F9CjkesUO0HXYNcbYT1mmV9hXvSg


CHEDRAUI LA PAZ PALACIO





