from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


try:
    file = open("B_Python_Intermedio/books.txt")
    cont = file.read()
    print(cont)
    file.close()
except:
    print("el libro no esta en este directorio ")

aa()


try:
    file = open("B_Python_Intermedioasdasdad/books.txt")
    cont = file.read()
    print(cont)
    file.close()
except:
    print("el libro no esta en este directorio ")