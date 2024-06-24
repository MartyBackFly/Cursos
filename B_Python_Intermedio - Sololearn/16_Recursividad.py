from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz


def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)

print(factorial(5))



aa()



def funcion_uno(n):
    if n > 0:
        print("En funcion_uno, n =", n)
        funcion_dos(n - 1)
    else:
        return

def funcion_dos(n):
    if n > 0:
        print("En funcion_dos, n =", n)
        funcion_uno(n - 1)
    else:
        return

# Llamada inicial
funcion_uno(3)



aa()

def is_even(x):   #par
    if x == 0:
        return True
    else:
        return is_odd(x-1)
 
def is_odd(x):  # impar
    return not is_even(x)


print(is_odd(17))
print(is_even(23))

print(is_even(4))
print(is_even(5))


# Para is_even(4):

# is_even(4) llama a is_odd(3) (ya que 4 - 1 = 3).
# is_odd(3) llama a is_even(2) (ya que 3 - 1 = 2).
# is_even(2) llama a is_odd(1) (ya que 2 - 1 = 1).
# is_odd(1) llama a is_even(0) (ya que 1 - 1 = 0).
# is_even(0) devuelve True.



# Para is_even(5):

# is_even(5) llama a is_odd(4) (ya que 5 - 1 = 4).
# is_odd(4) llama a is_even(3) (ya que 4 - 1 = 3).
# is_even(3) llama a is_odd(2) (ya que 3 - 1 = 2).
# is_odd(2) llama a is_even(1) (ya que 2 - 1 = 1).
# is_even(1) llama a is_odd(0) (ya que 1 - 1 = 0).
# is_odd(0) llama a is_even(0).
# is_even(0) devuelve True.

# Ambas secuencias de llamadas terminan en is_even(0), lo que devuelve True. La diferencia radica en cómo
# se llega a ese punto: para is_even(4), se hacen cuatro llamadas a is_odd antes de llegar a is_even(0), 
# mientras que para is_even(5), se hacen cinco llamadas a is_odd.





aa()


# ejercicio solo learn decimal a binario 

def convert(num): 
   if num == 0 :
      return num 
   else:
     return (num % 2 + 10 * convert(num // 2)) 



asd = int(input("put the number mtf -->"))
qwe = convert(asd)


print(f"tu numero {asd} en binario es {qwe}")



aa()


def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))


aa()

def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
		
print(power(2, 3))

# en la respuesta va sumando llamadas hasta llegar a y == 0 luego cuando llega vuelve devolviendo las llamadas y multiplicando por dos ... 
# ultimo return da 1.. entonces 2x1 = 2 ... luego retorna el 2 .. 2x2=4 .. luego retorna el 4 .. 2x4 = 8 .. ahi devolvio las 3 llamadas recursivas 

aa()

# con yiend 
def power(x, y):
    result = 1
    for _ in range(y):  # Iteramos y veces
        result *= x
        yield result  # Devolvemos el resultado actual como un valor del generador

# Ejemplo de uso del generador
for value in power(2, 5):
    print(value)