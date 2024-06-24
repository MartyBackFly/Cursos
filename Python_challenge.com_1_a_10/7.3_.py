from PIL import Image
from io import BytesIO
import requests

# Carga la imagen desde la URL
response = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png')
img = Image.open(BytesIO(response.content))

# Obtiene las dimensiones de la imagen
width, height = img.size

print("Ancho de la imagen:", width)
print("Alto de la imagen:", height)
print()

# Obtiene el color del píxel en la esquina superior izquierda
top_left_pixel = img.getpixel((0, 0))
print("Color del píxel en la esquina superior izquierda:", top_left_pixel)
print()

# Obtiene las bandas de la imagen
bandas = img.getbands()
print("Bandas de la imagen:", bandas)
print()

# Obtiene todos los colores presentes en la imagen junto con sus recuentos
colors = img.getcolors()
print("Colores presentes en la imagen:", colors)
print()

# Obtiene los colores de la fila central de píxeles
row = [img.getpixel((x, int(height / 2))) for x in range(width)]

# Define una función para determinar si un color es gris
def es_gris(color):
    # Verifica si los componentes RGB están dentro de un rango específico
    return all(50 <= value <= 200 for value in color)

# Filtra los colores grises
grises = [color for color in row if es_gris(color)]

# Imprime los colores grises encontrados
for color in grises:
    print("Color gris:", color)

# Muestra la cantidad de colores grises encontrados
cantidad_grises = len(grises)
print("Cantidad de colores grises:", cantidad_grises)
