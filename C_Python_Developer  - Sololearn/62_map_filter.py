numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)  # Salida: [2, 4, 6, 8]

print ("-------------------------------")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 8, 8, 8, 8, 88]
numeros_pares = list(map(lambda x: x % 2 == 0, numeros))
print(numeros_pares)  # Salida: [2, 4, 6, 8]



#La función map() en Python se utiliza para aplicar una función a cada 
#elemento de un iterable (como una lista) y devolver un iterable que contiene los resultados de 
#aplicar la función a cada elemento en el mismo orden. Su sintaxis general es la siguiente:
#map(función, iterable)


#La diferencia clave entre filter() y map() es cómo se decide qué elementos se incluirán en el resultado:

# filter() incluye solo los elementos para los cuales la función dada devuelve True.
# map() aplica la función a cada elemento del iterable y devuelve el resultado de cada aplicación, 
#independientemente de si el resultado es True o False.