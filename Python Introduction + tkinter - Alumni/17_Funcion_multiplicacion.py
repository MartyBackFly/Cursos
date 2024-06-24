from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

# Ejercicio 
# Escribir una función que sirva para multiplicar
# cada elemento de una lista numérica por un
# valor (ambos deben ser parámetros de función);
# y devuelva la nueva lista con cada elemento en
# su respectiva posición, pero ya multiplicado. 


def mult(elemento, desde, hasta):
    
    lista = []
  
    for i in range(desde,hasta+1):
        lista.append(elemento*i)
        desde +=1
    
    print(lista)

#mult(3,6,44)
def input_int(entrada):
    while True:
        try:
            value = int(input(entrada))
            return value
        except ValueError:
            print("tenes que poner numeros si o si ")
        




elemento = input_int("Valor a multiplicar ")
desde = input_int("Desde  ")
hasta = input_int("Hasta ")
    

# Llamar a la función con las entradas del usuario
mult(elemento, desde, hasta)