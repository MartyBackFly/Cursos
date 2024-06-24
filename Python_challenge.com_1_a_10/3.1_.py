# busqueda directamente en el html en la web 

# falta mejorar busqueda 


from string import ascii_letters
import re
import urllib.request
import urllib.error
import webbrowser as wb




def encontrar_letras_minusc_entre_mayusc(cadena):
    # Usamos una expresión regular para encontrar todas las letras minúsculas entre tres mayúsculas de cada lado
    # La expresión regular busca una mayúscula, luego una minúscula, y finalmente dos mayúsculas más
    patron = r'(?<=[A-Z]{3})([a-z])(?=[A-Z]{3})'
    # Usamos la función finditer para encontrar todas las ocurrencias del patrón en la cadena
    coincidencias = re.finditer(patron, cadena)
    letras_y_mayusc = []
    for match in coincidencias:
        letra_minusc = match.group(1)
        inicio = match.start() - 3  # Índice de inicio de las mayúsculas antes de la letra minúscula
        fin = match.end() + 3  # Índice de fin de las mayúsculas después de la letra minúscula
        mayusc_antes = cadena[inicio:inicio+3]
        mayusc_despues = cadena[fin-3:fin]
        letras_y_mayusc.append((letra_minusc, mayusc_antes, mayusc_despues))
    return letras_y_mayusc

# Abrir la URL y leer su contenido
url = 'http://www.pythonchallenge.com/pc/def/equality.html'
try:
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')  # Decodificar el contenido a UTF-8
except urllib.error.URLError as e:
    print("Error al abrir la URL:", e)

# Utilizar expresiones regulares para encontrar la cadena deseada
letras_y_mayusc = encontrar_letras_minusc_entre_mayusc(html_content)

letritas = []

for letra, _, _ in letras_y_mayusc:
    letritas.append(letra)



# Construir la URL utilizando los caracteres encontrados
final_url = 'http://www.pythonchallenge.com/pc/def/{}.html'.format(''.join(letritas))

# Abrir la URL en el navegador web
print(final_url)
wb.open(final_url)


