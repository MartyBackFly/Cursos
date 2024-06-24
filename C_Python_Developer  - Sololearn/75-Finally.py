from aafuncionimprimir import espacio as aa

try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")

   aa()



   
try:
   print("Hello")
   print(10 / 2)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")


aa()



try:
   print(1)
except ZeroDivisionError:
   print(2)
else:
   print(3)

try:
   print(1/0)
except ZeroDivisionError:
   print(4)
else:
   print(5)


aa()


x = 0
try:
  x+=1  # x = 1
  raise ValueError  # Lanza una excepción ValueError
except NameError:
  x+=1
except ValueError:
  x+=1  # Como la excepción ValueError es lanzada, se ejecuta este bloque y se incrementa x, x = 2
else:
  x+=1
finally:
  x+=1  # Independientemente de la excepción, se ejecuta el bloque finally y se incrementa x, x = 3

print(x)  # Imprime el valor final de x
