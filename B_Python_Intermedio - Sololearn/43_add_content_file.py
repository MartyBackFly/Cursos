from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

file = open("B_Python_Intermedio/newfile.txt", "a")

file.write("\n Ricardero ")
file.close()

file = open("B_Python_Intermedio/newfile.txt", "r")
print(file.read())
file.close()



msg = "Hello world!"
file = open("B_Python_Intermedio/newfile.txt", "a")
amount_written = file.write(msg)
print(amount_written)
file.close()

# amount = cantidad

# El código anterior escribirá en el archivo e imprimirá el número de bytes escritos.

#    file.write(msg) == len(msg)