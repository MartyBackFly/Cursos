from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az



# Para leer solo una cierta cantidad de un archivo, puedes proporcionar el número de bytes a leer como argumento a la función read . 

# Cada carácter ASCII es 1 byte: 



file = open("B_Python_Intermedio/books.txt")
print(file.read(5))
aa()
print(file.read(7))
aa()
print(file.read(34))
aa()
print(file.read(74))
aa()
print(file.read())
file.close()


# Llamar al método read() sin un argumento devolverá el resto del contenido del archivo.


aa() 

file = open("B_Python_Intermedio/books.txt")
for i in range(21):
  print(file.read(4))
file.close()