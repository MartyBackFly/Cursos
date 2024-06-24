from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

file = open("B_Python_Intermedio/newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("B_Python_Intermedio/newfile.txt", "r")
print(file.read())
file.close()


