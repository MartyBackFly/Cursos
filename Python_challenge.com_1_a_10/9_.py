import urllib.request
import urllib.error
from bs4 import BeautifulSoup
from bs4.element import Comment  # Importar Comment desde BeautifulSoup

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

    # Obtener el título de la página
    title = soup.title.string.strip()

    # Obtener el contenido completo de la página
    content = soup.text.strip()

    # Buscar en los comentarios del HTML
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    # Procesar los comentarios
    for comment in comments:
        print("Comentario encontrado:", comment)



