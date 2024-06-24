#buscar directamente en la pagina dada --> read el html content 



from string import ascii_letters
import re
import urllib.request
import urllib.error
import webbrowser as wb

# Abrir la URL y leer su contenido
url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
try:
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')  # Decodificar el contenido a UTF-8
except urllib.error.URLError as e:
    print("Error al abrir la URL:", e)




print(html_content)
