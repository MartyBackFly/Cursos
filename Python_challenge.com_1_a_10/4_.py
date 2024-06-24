import re
import urllib.request
import urllib.error

def encontrar_numero(url):
    # Abre la URL y lee su contenido
    try:
        response = urllib.request.urlopen(url)
        html_content = response.read().decode('utf-8')  # Decodificar el contenido a UTF-8
    except urllib.error.URLError as e:
        print("Error al abrir la URL:", e)
        return None
    
    # Busca el número en el contenido HTML
    patron = r"\d+"
    match = re.search(patron, html_content)
    if match:
        return match.group()
    else:
        return None

# URL inicial
url_base = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'

# Número máximo de iteraciones
max_iteraciones = 200
iteracion_actual = 1
while iteracion_actual <= max_iteraciones:
    numero = encontrar_numero(url_base)
    if numero:
        # Construir la URL utilizando el número encontrado
        url_base = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(numero)
        print("Iteración {}: {}".format(iteracion_actual, url_base))
        iteracion_actual += 1
    else:
        print("No se encontró ningún número en el contenido HTML.")
        break

print("Fin del proceso.")


