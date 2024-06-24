from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

az(1)

file = open("B_Python_Intermedio/books.txt")

num = int(input("numero de caracteres a leer : ")) 
print(file.read(num))

file.close()



az(2)

file = open("B_Python_Intermedio/books.txt") 
lines = file.readlines() 
print(lines) 
file.close()



az(3)
# Si no necesitas la lista para cada línea, simplemente puedes iterar sobre la variable del archivo:

file = open("B_Python_Intermedio/books.txt")

for line in file.readlines():
    print(line)
    
file.close()


az(4)



file = open("B_Python_Intermedio/books.txt", "r") 

cont = file.readlines()

print(cont[6])
file.close()