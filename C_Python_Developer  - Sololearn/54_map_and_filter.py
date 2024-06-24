
from imprimir import espacio as aa


def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)


aa()


nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)
print(list(result))


aa()

# Definir una función que multiplica un número por 2
def doble(x):
    return x * 2

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Utilizar la función map para aplicar la función doble a cada elemento de la lista
resultado_iterable = map(doble, numeros)

# El resultado_iterable es un objeto iterable, no una lista real
print(resultado_iterable)
# Convertir el resultado_iterable a una lista si es necesario
resultado_lista = list(resultado_iterable)

# Imprimir la lista resultante
print(resultado_lista)


aa()


# La función filter filtra un iterable dejando sólo los
# elementos que coinciden con una condición (también llamada predicado).


nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

# Cómo map, el resultado tiene que ser convertido explícitamente en una lista si se quiere imprimir.


aa()

nums = [1, 2, 5, 8, 3, 0, 7]
res = list(filter(lambda x: x<5, nums))
print(res)

aa()


nums = [1, 2, 5, 8, 3, 0, 7]
res = list(map(lambda x: x<5, nums))
print(res)

aa()

nums = [1, 2, 5, 8, 3, 0, 7]
res = list(map(lambda x: x if x<5 else None, nums))
print(res)

aa()