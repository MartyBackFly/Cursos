from aafuncionimprimir  import espacio
#Cuándo utilizar un diccionario:

#Cuando necesites una asociación lógica entre un par key:value.
#Cuando necesites una búsqueda rápida de tus datos, basada en una clave personalizada.
#Cuando tus datos se modifican constantemente. Recuerda que los diccionarios son mutables.

#------------

#Cuándo utilizar los otros tipos:

#Usa listas si tienes una colección de datos que no necesitan acceso aleatorio. 
#Intenta elegir listas cuando necesites una colección simple e iterable que se modifique con frecuencia.

#Usa un conjunto si necesitas que los elementos sean únicos.

#Usa tuplas cuando tus datos no pueden/deben cambiar.INMUTABLES




#---LISTAS--------

# Lista de números
numbers = [1, 2, 3, 4, 5]

# Lista de cadenas
fruits = ['apple', 'banana', 'orange']

# Lista mixta
mixed_list = [1, 'hello', 3.14, True]

# Acceder a elementos
print(numbers[0])  # Salida: 1
print(fruits[1])   # Salida: banana

# Modificar elementos
numbers[2] = 6
print(numbers)     # Salida: [1, 2, 6, 4, 5]

# Agregar elementos
fruits.append('grape')
print(fruits)      # Salida: ['apple', 'banana', 'orange', 'grape']

espacio()

#---DICCIONARIOS-------

# Diccionario de persona
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# Acceder a valores
print(person['name'])  # Salida: John
print(person['age'])   # Salida: 30

# Modificar valores
person['age'] = 31
print(person)          # Salida: {'name': 'John', 'age': 31, 'city': 'New York'}

# Agregar nuevos pares clave-valor
person['occupation'] = 'engineer'
print(person)          # Salida: {'name': 'John', 'age': 31, 'city': 'New York', 'occupation': 'engineer'}


espacio()

#---TUPLAS-------


# Tupla de coordenadas
coordinates = (3, 4)

# Acceder a elementos
x, y = coordinates
print(x, y)  # Salida: 3 4

# Tupla de elementos mixtos
mixed_tuple = (1, 'hello', 3.14)

# Acceder a elementos
print(mixed_tuple[1])  # Salida: hello



espacio()

#---CONJUNTOS-------


# Conjunto de números
numbers_set = {1, 2, 3, 4, 5, 67}

# Conjunto de cadenas
fruits_set = {'apple', 'banana', 'orange'}

# Agregar elementos
numbers_set.add(6)
print(numbers_set)  # Salida: {1, 2, 3, 4, 5, 6}

# Operaciones de conjuntos
common_elements = numbers_set.intersection({2, 4, 6, 8})
print(common_elements)  # Salida: {2, 4, 6}

# Operaciones de conjuntos sin resultado 
common_elements = numbers_set.intersection({7})
print(common_elements)  # set()

# Operaciones de conjuntos  
common_elements = numbers_set.intersection({4, 7, 32, 33, 34, 35, 67})
print(common_elements)  # Salida: {}

# En resumen, la salida {67, 4} y {4, 67} son esencialmente equivalentes, ya que ambos 
# representan el conjunto que contiene los elementos 4 y 67. Puedes considerar que el orden no importa en los conjuntos.


espacio()



