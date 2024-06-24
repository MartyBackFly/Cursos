import pickle
import urllib.request

url = "http://www.pythonchallenge.com/pc/def/banner.p"

# Descargar el contenido de la URL
response = urllib.request.urlopen(url)
data = response.read()

# Deserializar el contenido con pickle
unpickled = pickle.loads(data)

# Procesar los datos deserializados
for line in unpickled:
    print("".join([char * count for char, count in line]))


# Aquí hay un resumen de algunos de los modos más comunes utilizados en la función open():

# 'r': Abre el archivo en modo de lectura. El archivo debe existir, de lo contrario se generará un error.
# 'w': Abre el archivo en modo de escritura. Si el archivo no existe, se creará. Si el archivo existe, su contenido será truncado (borrado).
# 'a': Abre el archivo en modo de añadir (append). Si el archivo no existe, se creará. Si el archivo existe, los nuevos datos se agregarán al final del archivo.
# 'b': Abre el archivo en modo binario. Este modo debe combinarse con los otros modos, por ejemplo, 'rb' para lectura binaria y 'wb' para escritura binaria.


