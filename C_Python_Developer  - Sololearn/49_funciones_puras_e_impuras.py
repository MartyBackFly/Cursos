from imprimir import espacio as aa 
aa()


#funcion pura no cambia ningun valor 

def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)
  

print(pure_function(6, 12))


aa()


#funcion impura cambia el valor de some_list

some_list = []

def impure(arg):
  some_list.append(arg)
    
impure(12)

print(some_list)