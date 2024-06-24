# http://www.pythonchallenge.com/pc/def/integrity.html

import bz2





 # La "b" antes de una cadena de texto en Python indica que es una cadena de bytes en lugar de una cadena de texto Unicode. 
 # Las cadenas de bytes se utilizan comúnmente para representar datos binarios, como en este caso, donde los datos parecen ser una secuencia de bytes comprimidos.

# Datos comprimidos
data_un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
data_pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# Descomprimir los datos
uncompressed_un = bz2.decompress(data_un)
uncompressed_pw = bz2.decompress(data_pw)

# Imprimir los resultados
print("un:", uncompressed_un.decode())
print("pw:", uncompressed_pw.decode())

# usuario y password :D 
# click img "bee"