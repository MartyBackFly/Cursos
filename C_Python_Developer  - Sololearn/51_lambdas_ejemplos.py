from imprimir import espacio as aa

aa()

# Funciones de orden superior:



# Ejemplo con map()
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))


aa()

# Operaciones sencillas:



# Ejemplo con operación de suma
add = lambda x, y: x + y
print(add(3, 5))

# seria igual que 
def add(x, y):
    return x + y

print(add(3, 5))

aa()

# Callbacks:


def operacion_binaria(a, b, funcion):
    return funcion(a, b)

suma = operacion_binaria(5, 3, lambda x, y: x + y)
multiplicacion = operacion_binaria(5, 3, lambda x, y: x * y)


aa()

# Expresiones condicionales: con un argumento 


es_par = lambda x: True if x % 2 == 0 else False
print(es_par(4))  # True


aa()

# Expresiones condicionales: con dos argumentos 

funcion_con_dos_argumentos = lambda x, y: True if x % y == 0 else False



# Sort con criterios específicos:
# claves 'nombre' y 'edad'.

personas = [
    {'nombre': 'Alice', 'edad': 25},
    {'nombre': 'Bob', 'edad': 30},
    {'nombre': 'Charlie', 'edad': 20}
]

ordenado_por_edad = sorted(personas, key=lambda x: x['edad'])

print(ordenado_por_edad)
aa()

for raquelsaurio in ordenado_por_edad:
    print(f"Nombre: {raquelsaurio['nombre']}, Edad: {raquelsaurio['edad']}")


aa()

# Sin argumentos:


sin_argumentos = lambda: "Hola, mundo"

print(sin_argumentos)
print(sin_argumentos())


aa()

#Un argumento:

cuadrado = lambda x: x**2
print(cuadrado)
print(cuadrado(56))

aa()

#Varios argumentos:


suma = lambda x, y: x + y

resultadoparausarenlasiguientefuncion = (suma(332, 1))
# puedo solo hacer el print pero guardo el resultado para usarlo en la siguiente funcion 

print(resultadoparausarenlasiguientefuncion)


aa()

#Uso de expresiones condicionales:


es_par = lambda x: True if x % 2 == 0 else False

raquel = es_par(resultadoparausarenlasiguientefuncion)

print(raquel)

print(es_par(22))

#Recuerda que las funciones lambda son útiles para operaciones simples y expresiones cortas. 
#Si necesitas una lógica más compleja o funciones más extensas, es preferible usar funciones definidas con def.




#el (6) es el parametro x que se lo pasamos al final de la funcion
a = (lambda x: x * (x + 1))(6)
print(a, "lambdita")