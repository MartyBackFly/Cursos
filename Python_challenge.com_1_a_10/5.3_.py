
import sys
import pickle
import urllib.request 

data = pickle.loads(urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read())
for line in data:
    for char, count in line: sys.stdout.write(char * count)
    sys.stdout.write("\n")



#     for char, count in line:: Esta línea itera sobre cada elemento en la lista line, que consiste en tuplas. 
#     Para cada iteración, char tomará el primer valor de la tupla (el carácter) y count tomará el segundo valor (la cantidad).

# sys.stdout.write(char * count): Esta línea escribe en la salida estándar (normalmente la consola) el carácter 
# char repetido count veces. Esto se logra multiplicando el carácter por la cantidad, lo que genera una cadena 
# más larga con el carácter repetido tantas veces como indique la cantidad.

# sys.stdout.write("\n"): Después de escribir todos los caracteres de una línea, se escribe un salto de línea ("\n") para pasar a la siguiente línea.

# En resumen, estas líneas se encargan de escribir en la salida estándar la representación visual de la
# estructura de datos cargada desde el archivo pickle. Cada línea consiste en caracteres repetidos según la 
# cantidad especificada en las tuplas dentro de la lista line, seguido de un salto de línea para pasar a la siguiente línea.