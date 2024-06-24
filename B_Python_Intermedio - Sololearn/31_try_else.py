from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


try:
  print(1)
  print(1 + "1" == 2)
  print(2)
except TypeError:
  print(3)
else:
  print(4)

aa()


try:
  print(1)
  #print(1 + "1" == 2)
  print(2)
except TypeError:
  print(3)
else:
  print(4)