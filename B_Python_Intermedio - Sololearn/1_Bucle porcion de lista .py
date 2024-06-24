n = [2, 4, 6, 8]
res = 1

# Bucle sobre la porción de la lista n, desde el segundo elemento (índice 1) hasta el tercer elemento (índice 2).
for x in n[1:3]:
    res *= x  # Multiplica el elemento actual x al resultado acumulado.

print(res)  # Imprime el resultado final de la multiplicación.


""" Desglose paso a paso:

Se define una lista n con los elementos [2, 4, 6, 8].
Se inicializa una variable res con el valor 1. Esta variable 
se utilizará para acumular el resultado de la multiplicación.
Se ejecuta un bucle for sobre la porción de la lista n que va 
desde el segundo elemento (índice 1) hasta el tercer elemento (índice 2). La porción es [4, 6].
En cada iteración del bucle, el valor actual x se multiplica con 
el valor acumulado en res.
Después del bucle, se imprime el resultado final de la multiplicación, 
que es el producto de los elementos en la porción [4, 6], es decir, 4 * 6 = 24.
En resumen, el código calcula el producto de los elementos en la
porción específica de la lista n y lo imprime. En este caso, el resultado final es 24. """


n = [2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
res = 1

# Bucle sobre la porción de la lista n, desde el segundo elemento (índice 1) hasta el tercer elemento (índice 2).
for x in n[1:6]:
    res *= x  # Multiplica el elemento actual x al resultado acumulado.

print(res)  # Imprime el resultado final de la multiplicación.