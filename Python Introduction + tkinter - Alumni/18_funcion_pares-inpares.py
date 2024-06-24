from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

# Hacer una función que reciba una lista con
# números enteros y devuelva en una “matriz”
# como primer elemento una lista con los números
# pares y como segunda lista los números
# impares de la lista recibida.
# Idea
# [pares , impares]


lista = [ 1,2,3,21,2,3,45,543,5,345,43,643,634,6,4356,43,634,634,6,436,34,6,346,436,43,6]

matriz=[]
a = []
b = []
def pares_inpares(lista):
    for i in lista:
        if i % 2 == 0:
            a.append(i)
        else : 
            b.append(i)
    matriz.append(a)
    matriz.append(b)
    print(matriz)


pares_inpares(lista)