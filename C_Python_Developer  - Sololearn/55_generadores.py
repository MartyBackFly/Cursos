from imprimir import espacio as aa

aa()

# Los Generadores son un tipo de iterable, como las listas o las tuplas.
# A diferencia de las listas, no permiten la indexación con índices 
# arbitrarios, pero pueden ser iterados con bucles for .
# Se pueden crear utilizando funciones y la declaración yield.


# para identificar la variable la llame e pero se llama i normalmente 

# yield = producir 


def countdown():
  e=5
  while e > 0:
    yield e
    e -= 1
    
for i in countdown():
  print(i)


aa()

# La función countdown() es una función generadora que utiliza la palabra clave yield. 
# Cuando se llama a esta función, devuelve un generador.

#La variable e se inicializa con el valor 5.

# Se utiliza un bucle while para generar valores en orden descendente. 

#Mientras e sea mayor que 0, la función genera el valor actual de e utilizando yield y luego decrementa e en 1.

# El bucle for utiliza la función generadora countdown() para iterar 
# sobre los valores generados. En cada iteración, el valor generado se almacena en la variable i, y luego se imprime.
# Cada número del 5 al 1 se imprime en líneas separadas, ya que la función generadora countdown() 
# se llama en el bucle for y produce esos valores uno a uno.


#ejemplo infinito 

""" def infinite_sevens():
   while True:
    yield 7
        
for i in infinite_sevens():
  print(i) """


aa()


def count_up():
    num = 1
    while num <= 15:
        yield num
        num += 1

# El bucle for itera sobre los valores generados por la función count_up
for i in count_up():
    print(i)
aa()

# En este caso, el argumento end=' ' hace que cada valor se imprima seguido por un espacio en 
# lugar de un salto de línea. Como resultado, los números se imprimirán uno al lado del otro en la misma línea.


for i in count_up():
    print(i, end=' ')

aa()

for i in count_up():
    print(i, end=' asd  ')

aa()




# para imprim los valores en un lista 


def count_up():
    num = 1
    numbers = []
    while num <= 15:
        numbers.append(num)
        num += 1
    return numbers

# Obtén la lista de valores generados por la función count_up
result_list = count_up()

# Imprime la lista completa
print(result_list)
print(count_up)


aa()


# En este ejemplo, generate_naturals es una función generadora que utiliza
# yield para producir números naturales de manera infinita. El bucle for en 
# el ejemplo de uso imprime los primeros 5 números naturales generados por 
# la función.


def generate_naturals():
    num = 1
    while True:
        yield num
        num += 1

# Imprimir los primeros 5 números naturales
natural_generator = generate_naturals()
for _ in range(5):
    print(next(natural_generator))


aa()


def count_up():
    num = 1
    while num <= 9:
        yield "RACATA"
        num += 1

# El bucle for itera sobre los valores generados por la función count_up
for i in count_up():
    print(i)
aa()



def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))


aa()

def make_word():
    word = ""
    for char in "spam":
        word += char
        yield word

print(list(make_word()))



aa()


def make_word():
    word = ""
    for jhkl in "raquel":
        word += jhkl
        yield word

print(list(make_word()))


aa()

# Si deseas imprimir las palabras sin convertirlas en una lista, 
# puedes iterar directamente sobre el generador devuelto por la función 
# generadora make_word. Aquí tienes el código modificado:


def make_word():
    word = ""
    for char in "spam":
        word += char
        yield word

# Iterar directamente sobre el generador e imprimir las palabras
for words in make_word():
    print(words)



aa()



def print_characters():
    for char in "spam":
        print(char)

# Llamada a la función para imprimir los caracteres
print_characters()



aa()



# ejercicio es primo ?


def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(a, b):
    #your code goes here
    for i in range(a, b):
      if isPrime(i):
        yield i  

f = int(input())
t = int(input())

  

print(list(primeGenerator(f, t)))