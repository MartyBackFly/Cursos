
#obtenemos los valores y los representamos en un dibujo , todo en el mismo codigo 



import re
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

    # Inicializar matrices para almacenar los valores de first y second
    first_matrix = []
    second_matrix = []

    # Expresión regular para encontrar solo números y comas
    regex = r'(\d+|,)'

    # Procesar los comentarios
    for comment in comments:
        # Verificar si el comentario contiene "first" o "second"
        if "first" in comment:
            # Extraer solo los números y comas de la cadena
            numbers = re.findall(regex, comment)
            # Eliminar las comas vacías y convertir los números a enteros
            numbers = [int(num) for num in numbers if num.isdigit()]
            first_matrix.append(numbers)
        elif "second" in comment:
            # Extraer solo los números y comas de la cadena
            numbers = re.findall(regex, comment)
            # Eliminar las comas vacías y convertir los números a enteros
            numbers = [int(num) for num in numbers if num.isdigit()]
            second_matrix.append(numbers)

    # Imprimir las matrices de first y second
    print("Matriz de first:")
    for row in first_matrix:
        print(row)

    print("\nMatriz de second:")
    for row in second_matrix:
        print(row)



from PIL import Image,ImageDraw
im = Image.new('RGB', (500,500))
draw = ImageDraw.Draw(im)
draw.polygon(row, fill='white')

im.show()