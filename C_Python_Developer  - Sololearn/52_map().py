from imprimir import espacio as aa


#la función map() en Python es una función de orden superior que se utiliza para aplicar 
#una función a cada elemento de una iterable (como una lista) y devuelve un nuevo iterable con los resultados.

#La sintaxis básica de la función map() es la siguiente:


#    map(función, iterable)

#función: Una función que se aplicará a cada elemento del iterable. 
#Puede ser una función incorporada, una función definida por el usuario o una función lambda.
#iterable: La secuencia de elementos a los que se les aplicará la función.
#La función map() devuelve un objeto iterable. Puedes convertir este objeto iterable a una lista, 
#tupla u otro tipo de iterable según sea necesario.

#Supongamos que tienes una lista de números y quieres calcular el cuadrado de cada número:





aa()

def cuadrado(x):
    return x**2

numeros = [1, 2, 3, 4, 5]

resultado = map(cuadrado, numeros)

print( )

print (resultado)
print( )
print(list(resultado))


aa()



# En lugar de definir una función por separado, también 
# puedes usar una función lambda directamente en map():


numeros = [5, 6, 7, 8, 9]

resultado = map(lambda x: x**2, numeros)

print(list(resultado))


# En este caso, la función lambda lambda x: x**2 realiza la 
# misma operación de elevar al cuadrado cada elemento de la lista numeros.