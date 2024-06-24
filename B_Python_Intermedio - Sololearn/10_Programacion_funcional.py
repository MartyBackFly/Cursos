from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5 

print(apply_twice(add_five, 10))


aa()


def apply_one(func, arg):
    return func(arg)

def add_six(x):
    return x + 6

print(apply_one(add_six, 10))

aa()

def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 3))

aa()



# pura 

def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)
print(pure_function(10, 10))

aa()

def func(x):
  y = x**2
  z = x + y
  return z
print(func(122))

aa()

# impura 

some_list = []

def impure(arg):
  some_list.append(arg)

print(impure(10))
print(some_list)
aa()


