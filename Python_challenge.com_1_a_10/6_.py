# http://www.pythonchallenge.com/pc/def/channel.html


# http://www.pythonchallenge.com/pc/def/channel.zip



#buscar directamente en la pagina dada --> read el html content 

import urllib.request
import urllib.error
from bs4 import BeautifulSoup

# Abrir la URL y leer su contenido
url = 'http://www.pythonchallenge.com/pc/def/channel.html'

try:
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')  # Decodificar el contenido a UTF-8
except urllib.error.URLError as e:
    print("Error al abrir la URL:", e)

# Utilizar BeautifulSoup para analizar el HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Obtener el título de la página
title = soup.title.string.strip()

# Obtener el contenido completo de la página
content = soup.text.strip()

# Obtener el contenido dentro del elemento <body> de la página
body_content = soup.body.get_text(separator='\n').strip()

# Obtener el contenido dentro del elemento <body> de la página
body_content1 = ""
for element in soup.body.children:
    if element.name == 'br':
        body_content += '\n'
    elif element.string:
        body_content += element.string


# Imprimir el título y el contenido
print("Título de la página:", title)
print("Contenido de la página:", content)
print("Contenido del cuerpo de la página:", body_content)
print(body_content1.strip())



