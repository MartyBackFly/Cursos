from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz

# filtrar 
# La función filter filtra un iterable dejando solo los elementos que 
# coinciden con una condición (también llamado predicado ).
aa()
nums = [11, 22, 33, 44, 55]

#sin convertir en list
res = (filter(lambda x: x%2==0, nums))
print(res)

zz()

# convertir en list
res = list(filter(lambda x: x%2==0, nums))
print(res)


aa()

nums = [1, 2, 5, 8, 3, 0, 7]
res = list(filter(lambda x: x < 5, nums))
print(res)