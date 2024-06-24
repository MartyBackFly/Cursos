# obtenemos los valores de first y second y los imprimimos en consola 


import urllib.request
import urllib.error
from bs4 import BeautifulSoup, Comment

# Abrir la URL y leer su contenido
url = 'http://www.pythonchallenge.com/pc/return/good.html'

try:
    # Agregar encabezados de autenticación para superar el error de autorización
    username = 'huge'
    password = 'file'
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, username, password)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')  # Decodificar el contenido a UTF-8
except urllib.error.URLError as e:
    print("Error al abrir la URL:", e)

# Utilizar BeautifulSoup para analizar el HTML si la solicitud tuvo éxito
if 'html_content' in locals():
    soup = BeautifulSoup(html_content, 'html.parser')

    # Buscar en los comentarios del HTML
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    # Inicializar variables para almacenar los valores de first y second
    first = ""
    second = ""

    # Procesar los comentarios
    for comment in comments:
        # Reemplazar ':' con '=' en el comentario
        comment = comment.replace(':', '=')

       
print( comment)
    
