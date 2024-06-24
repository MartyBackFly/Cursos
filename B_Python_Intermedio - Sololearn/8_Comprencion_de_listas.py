from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz


# a list comprehension
cubes = [i**3 for i in range(6)]

print(cubes)
zz()
# a list comprehension
cuadrado = [i**2 for i in range(6)]

print(cuadrado)
zz()
# a list comprehension
a = 1
cosita = [(a) for i in range(6)]

print(cosita)
zz()
# a list comprehension

cosa = [i for i in range(6)]

print(cosa)


aa()

nums = [i*2 for i in range(10)]
print(nums)


aa()


evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)


aa()

word = input("palabra a desvocalizar -- > ")
vocals = {'a','e','i','o','u'}


listita = [i for i in word if i not in vocals]
        


print (listita)
zz()
asd = set(listita)
print(asd)

zz()
# Convertir la lista en una cadena utilizando el método join()
resultado = ''.join(listita)
print(resultado)