from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz
from aafuncionimprimir import espacio_numero as az

# Las funciones incorporadas map y filter son funciones de orden superior muy útiles que operan en listas (u objetos similares llamados iterables ). 

# La función map toma una función y un iterable como argumentos, y devuelve un nuevo iterable con la función aplicada a cada argumento.


def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)


az(1)

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x + 5 , nums ))
print(result)


az(2)

salaries = [2000, 1800, 3100, 4400, 1500]
print(salaries)
bonus = int(input("aumentillo --->"))

salariess = list(map(lambda x: x + bonus, salaries))

print(salariess)



az(3)

# con for 

salaries = [2000, 1800, 3100, 4400, 1500]

bonus = int(input("aumentillo --->"))

salariess = []
print(salaries)
for salary in salaries:
    salariess.append(salary + bonus)

print(salariess)
