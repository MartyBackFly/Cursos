print(" http://www.pythonchallenge.com/pc/def/oxygen.html" )

import urllib.request
from bs4 import BeautifulSoup

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

# Iterar sobre las etiquetas de imagen y descargar y mostrar las imágenes PNG
for img in img_tags:
    src = img.get('src')
    if src.endswith('.png'):
        # Construir la URL completa de la imagen
        url_imagen = urllib.parse.urljoin(url_pagina, src)
        
        # Descargar la imagen desde la URL
        imagen_data = urllib.request.urlopen(url_imagen).read()
        
        # Decodificar la imagen
        imagen = Image.open(io.BytesIO(imagen_data))
        
        # Mostrar la imagen
        imagen.show()
# Decodificar la imagen
imagen = Image.open(io.BytesIO(imagen_data))

# Obtener el tamaño de la imagen
tamano = imagen.size
print("Tamaño de la imagen:", tamano)

# Obtener la descripción del formato de la imagen
descripcion_formato = imagen.format_description
print("Descripción del formato de la imagen:", descripcion_formato)

# Obtener las bandas de la imagen
bandas = imagen.getbands()
print("Bandas de la imagen:", bandas)

