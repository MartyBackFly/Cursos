from aafuncionimprimir import espacio as aa


# Conjuntos 
# Los Conjuntos son similares a las listas o diccionarios. 

# Se crean usando llaves, y son desordenados, lo que significa que no pueden ser indexados. 

# Debido a la forma en que se almacenan, es más rápido verificar si un elemento es parte de un conjunto usando el operador in, en lugar de ser parte de una lista.

# CODE PLAYGROUND: PY

num_set = {1, 2, 3, 4, 5}

print(3 in num_set)

aa()

letters = {"a", "b", "c", "d"}
if "e" not in letters:
  print(1)
else: 
  print(2)


aa()

nums = {1, 2, 1, 3, 1, 4, 5, 6, 6, 6, 6, 6, 7}
print(len(nums))
print(nums)
nums.add(-7)
print(len(nums))

nums.remove(3)

print(nums)
print(len(nums))

