#buscar directamente en la pagina dada --> read el html content 



from string import ascii_letters
import re
import urllib.request
import urllib.error
import webbrowser as wb

# Abrir la URL y leer su contenido
url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
try:
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')  # Decodificar el contenido a UTF-8
except urllib.error.URLError as e:
    print("Error al abrir la URL:", e)

# Utilizar expresiones regulares para encontrar la cadena deseada
result = re.findall(r'<!--(.*?)-->', html_content, re.S)[-1]
characters = [char for char in result if char in ascii_letters]

# Construir la URL utilizando los caracteres encontrados
final_url = 'http://www.pythonchallenge.com/pc/def/{}.html'.format(''.join(characters))

# Abrir la URL en el navegador web
print(final_url)
wb.open(final_url)
