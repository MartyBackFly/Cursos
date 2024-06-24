from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz


def my_func(f, arg):
  return f(arg)

print(my_func(lambda x: 2*x*x, 5))


# my_func toma una función como primer argumento y un argumento para esa función. 
#En el segundo caso, se pasa una función lambda como argumento a my_func, lo que resulta 
#en la evaluación de lambda x: 2*x*x con arg = 5, devolviendo 50.


aa()
#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-5))

#lambda


print((lambda x: x**2 + 5*x + 4) (-5))


aa()


price = int(input("price : "))
perc = int(input("perc : "))

res = (lambda x,y: (x*y)/100)(price, perc)

print(res)



aa()

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input("pone aumento here -->"))

salariess = list(map(lambda x: x + bonus, salaries))

print(salariess)

aa()





nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
print(nums)
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))


#Primero, se crea un conjunto nums con los elementos {1, 2, 3, 4, 5, 6}.
#Luego, se realiza una operación de intersección (&) entre dos conjuntos: {0, 1, 2, 3} y nums. 
# La intersección de estos dos conjuntos resulta en {1, 2, 3}. Como nums es reasignado, ahora nums contiene {1, 2, 3}.
#Se imprime el conjunto nums, que ahora contiene {1, 2, 3}.
#Después, se aplica la función filter() sobre el conjunto nums. La función filter() filtra los elementos del 
#conjunto nums según la condición especificada en la función lambda. La función lambda lambda x: x > 1 devuelve 
#True si x es mayor que 1 y False de lo contrario.
#La función filter() devuelve un iterador que contiene los elementos del conjunto nums que cumplen la condición 
#especificada. Sin embargo, en este punto, la función filter() no se ha ejecutado realmente. Todavía es un objeto de tipo filter.
#Se convierte el iterador resultante de filter() en una lista usando list(), lo que efectivamente ejecuta
# la función filter() y se obtiene una lista con los elementos filtrados.
#Se obtiene la longitud de la lista resultante usando len() y se imprime. En este caso, la lista filtrada 
# contiene los elementos {2, 3}, por lo tanto, la longitud de la lista es 2. Por lo tanto, se imprime 2.



aa()


a = (lambda x: x *(x+1)) (6)
print(a)



aa()


nums = [1, 2, 8, 3, 7]
res = list(filter(lambda x: x%2==0, nums))
print(res)