import urllib.request
from bs4 import BeautifulSoup
from PIL import Image
import io

# Descargar el HTML de la página
url_pagina = "http://www.pythonchallenge.com/pc/def/oxygen.html"
response = urllib.request.urlopen(url_pagina)
html = response.read()

# Analizar el HTML
soup = BeautifulSoup(html, 'html.parser')

# Buscar la etiqueta de imagen
img_tags = soup.find_all('img')

# Iterar sobre las etiquetas de imagen y descargar y procesar las imágenes PNG
for img in img_tags:
    src = img.get('src')
    if src.endswith('.png'):
        # Construir la URL completa de la imagen
        url_imagen = urllib.parse.urljoin(url_pagina, src)
        
        # Descargar la imagen desde la URL
        imagen_data = urllib.request.urlopen(url_imagen).read()
        
        # Decodificar la imagen
        imagen = Image.open(io.BytesIO(imagen_data))
        
        # Definir una lista de caracteres ASCII, ordenados por su densidad (de oscuro a claro)
        ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
        
        # Obtener los valores de los píxeles de la imagen
        pixels = list(imagen.getdata())

        # Convertir las tuplas de píxeles en valores de píxeles individuales
        pixels = [pixel[0] for pixel in pixels]  # Aquí asumimos que solo necesitamos el primer valor de la tupla

        # Convertir los valores de los píxeles en caracteres ASCII
        ascii_art = ''.join([ascii_chars[pixel // 25] for pixel in pixels])

        
        # Obtener el ancho de la imagen y ajustar la longitud del texto al ancho de la imagen
        ancho_imagen = imagen.size[0]
        ascii_art = [ascii_art[i:i + ancho_imagen] for i in range(0, len(ascii_art), ancho_imagen)]
        ascii_art = '\n'.join(ascii_art)
        
        # Imprimir el arte ASCII
        print(ascii_art)
