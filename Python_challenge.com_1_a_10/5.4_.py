


# crea una imagen con el contenido de la url  WTF!!!!


import urllib.request
from PIL import Image, ImageDraw
import pickle

# Descargar los datos desde la URL
url = "http://www.pythonchallenge.com/pc/def/banner.p"
response = urllib.request.urlopen(url)
data = response.read()

# Cargar los datos con pickle
unpickled_data = pickle.loads(data)

# Crear una nueva imagen
im = Image.new("RGB", (95, 24), color="white")
draw = ImageDraw.Draw(im)

# Dibujar en la imagen
line = 0
for i in unpickled_data:
    xpos = 0
    for j in i:
        if j[0] == " ":
            draw.line([(xpos, line), (xpos + j[1], line)], fill="black")
        xpos += j[1]
    line += 1

# Guardar la imagen
im.save("banner.bmp")
