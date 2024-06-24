from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz



# Usar *args como un parámetro de función te permite pasar un número arbitrario de
# argumentos a esa función. Los argumentos luego son accesibles como la tupla args en el cuerpo de la función.

# *args se utiliza para pasar un número variable de argumentos posicionales a una función. 
# Los argumentos pasados a través de *args se recogen como una tupla dentro de la función. 
# Esto significa que los elementos pasados como argumentos posicionales se pueden acceder mediante el índice dentro de la tupla.


def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)


aa()


#menor

def my_min(x, y, *args):
    return min(x, y, *args)

print(my_min(8, 13, 4, 42, 120, 7))  # Output: 4


aa()


#mayor

def my_max(x, *y):
    if x > max(y): 
        return x 
    else: 
        return max(y)

print(my_max(8, 13, 4, 42, 120, 7)) 

aa()


# Ejemplo de *args
def sumar_numeros(*args):
    suma = 0
    for num in args:
        suma += num
    return suma

print(sumar_numeros(1, 2, 3, 4, 5))  # Output: 15

aa()


# Ejemplo de *args
def promedio(*args):
    if not args:
        return None
    return sum(args) / len(args)

print(promedio(85, 90, 88, 92, 95))  # Output: 90.0

