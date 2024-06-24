from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz

# return se utiliza para devolver un valor y finalizar la ejecución de la función, 
# mientras que yield se utiliza para generar una serie de valores uno a la vez, conservando el estado de la función entre llamadas.






def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

aa()


def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(21)))

aa()
#generadores


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
    for i in range(f,t) :
      if isPrime(i) :           #if isPrime(i) == True:
        yield i 
        

f = int(input("desde-->"))
t = int(input('hasta -->'))

print(list(primeGenerator(f, t)))


aa()


def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))


aa()


def make_word():
  word = ""
  for ch in "spam":
    word =ch
    yield word

print(list(make_word()))