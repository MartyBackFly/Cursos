from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az



n = int(input("cuantos num la lista capo ? : "))

file = open("B_Python_Intermedio/lista_num.txt", "w+")
#your code goes here
for i in range(1, n+1):
    file.write(str(i)+"\n")
file.close()

f = open("B_Python_Intermedio/lista_num.txt", "r")
print(f.read())
f.close()