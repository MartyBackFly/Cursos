from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


"""
Es una buena práctica evitar el desperdicio de recursos asegurándose de que los archivos siempre se
 cierren después de haber sido utilizados. Una forma de hacer esto es usar try y finally.
"""


try:
  f = open("B_Python_Intermedio/lista_num.txt", "r")
  cont = f.read()
  print(cont)
finally:
 f.close()


 aa()

"""
Una manera alternativa de hacer esto es utilizando las declaraciones with . 
Esto crea una variable temporal (a menudo llamada f),  
que solo es accesible en el bloque indentado de la declaración with . 
"""


with open("B_Python_Intermedio/lista_num.txt") as f:
  print(f.read())


# El archivo se cierra automáticamente al final de la declaración with , incluso si ocurren excepciones dentro de ella.