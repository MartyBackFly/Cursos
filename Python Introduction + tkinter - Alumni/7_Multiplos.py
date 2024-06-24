from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

# Ejercicio 7

# Múltiplos
# Se quiere buscar los múltiplos de 3 y de 5 en un
# rango que ingrese el usuario. Guardar los
# múltiplos en una lista.
# Se debe usar for asociado a un range como se
# vio en la teoría. 

numero = int(input("buscar N multiplos de 3 y 5 : "))
mult =  []
for i in range(0,numero):
    if i % 3 ==0  and i % 5 == 0:
        mult.append(i)

print(mult)


aa()







#Resolución del ejercicio 7

inicio = input("Ingrese el numero de incio del rango: ")
inicio = int(inicio)
final = input("Ingrese el numero del final del rango: ")
final = int(final)
multiplos = []
for n in range(inicio,final+1,1):
    if n%3 == 0 and n%5 == 0:
        multiplos.append(n)
print("Los multiplos de 3 y de 5 en ese rango son: ")
print(multiplos)