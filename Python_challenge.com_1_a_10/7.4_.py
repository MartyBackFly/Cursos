import re
from PIL import Image
from io import BytesIO
import urllib.request
import requests

img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))
img.width
img.height
img.getpixel((0,0))

print (img.width, img.height)
print (img.getpixel((0,0)))
print() 

bandas = img.getbands()
print(bandas)

colors = img.getcolors()
print (colors)


#Para obtener la escala de grises, podemos tomar la fila central de píxeles:

row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]


print(row)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# reducimos ancho de pixel por que hay repetidos( creo que 7 veces cada uno)
row = row[::7]

print(row)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
ords = [r for r, g, b, a in row if r == g == b]

print (ords)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

# dado que RGB usa un número positivo en [0, 255] para cada color, podemos asumir que representa un carácter ASCII:
lettersascii = "".join(map(chr, ords))

print (lettersascii)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


nums = re.findall("\d+", "".join(map(chr, ords)))
nums = "".join(map(chr, map(int, nums)))


# Imprimimos los números encontrados
print(nums) 