from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

# Ejercicio 6

# Escriba un programa que permita crear una lista
# de nombres.
# Para ello, el programa tiene que pedir un número
# y luego solicitar esa cantidad de nombres para
# crear la lista. Por último, el programa tiene que
# mostrar la lista creada.

nombres = []

num = int(input('cantidad de nombres : '))

for i in range (0, num):
    nombres.append(input("agregar nombre--> "))

print(nombres)

aa()

# solucion 


#Ingreso por teclado de la cantidad de nombres
cantidad = input("¿Cuantos nombres desea ingresar?: ")
#Convertimos
cantidad = int(cantidad)
#Arranca la lista vacia
nombres = []
#Variable contador = 0
contador = 0

#Este bucle generara el ingreso de los nombres segun cantidad
while contador < cantidad:
#Variable name para que sea auxiliar para guardar ingresos
    name = input("Ingrese un nombre: ")
#el append siempre agrega al final de las listas
    nombres.append(name)
#variable contador(de vueltas) se usara para comparar con cantidad
    contador = contador + 1
print(nombres)