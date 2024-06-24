from imprimir import espacio as aa


aa()




# Solicitud de datos
# Solicitud de datos
n1 = float(input('Introduce el Primer número: '))
n2 = float(input('Introduce el Segundo número: '))
n3 = float(input('Introduce el Tercer número: '))
n4 = float(input('Introduce el Cuarto número: '))
n5 = float(input('Introduce el Quinto número: '))
print("---------------------")
# Calcular las diferencias
diferencias = [abs(n1 - n) for n in [n2, n3, n4, n5]]


print("---------------------")
# Encontrar la diferencia mínima
print(f"Las diferencias son {diferencias}")
menor_diferencia = min(diferencias)

# Encontrar el índice de la diferencia mínima
indice_menor_diferencia = diferencias.index(menor_diferencia)
print(f"el indice de la lista con menor dif es   {indice_menor_diferencia} ")

# Determinar el número más cercano
numero_cercano = [n2, n3, n4, n5][indice_menor_diferencia]
print("---------------------")
print(f'El número más cercano a {n1} es {numero_cercano} con una diferencia de {menor_diferencia}')
print("---------------------")



#La función abs() en Python devuelve el valor absoluto de un número. El valor absoluto de un número es su distancia 
# desde el cero en la recta numérica, sin tener en cuenta su dirección.

# Por ejemplo:

# abs(5) devuelve 5.
# abs(-5) también devuelve 5.

# La función min() en Python se utiliza para encontrar el valor mínimo de un iterable, como una lista, una tupla o 
# cualquier otro objeto iterable. Devuelve el valor más pequeño dentro del iterable.
numbers = [5, 2, 8, 1, 9]
min_value = min(numbers)
print(min_value)  # Output: 1
