from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

x = 0
try:
  x += 1  # x es incrementado a 1
  raise ValueError  # Se lanza una excepción de tipo ValueError
except NameError:
  x += 1  # Este bloque no se ejecuta porque la excepción no es de tipo NameError
except ValueError:
  x += 1  # Este bloque se ejecuta porque la excepción es de tipo ValueError
else:
  x += 1  # Este bloque no se ejecuta porque hubo una excepción
finally:
  x += 1  # Este bloque siempre se ejecuta
  print(x)


aa()

x = 0
try:
  x += 3  # x es incrementado a 1
  raise ValueError  # Se lanza una excepción de tipo ValueError
except NameError:
  x += 8  # Este bloque no se ejecuta porque la excepción no es de tipo NameError
except ValueError:
  x += 4  # Este bloque se ejecuta porque la excepción es de tipo ValueError
else:
  x += 56  # Este bloque no se ejecuta porque hubo una excepción
finally:
  x += 1  # Este bloque siempre se ejecuta
print(x)



aa()

x = 0
try:
  x += 3  # x es incrementado a 1
  # raise ValueError  # Se lanza una excepción de tipo ValueError
except NameError:
  x += 8  # Este bloque no se ejecuta porque la excepción no es de tipo NameError
except ValueError:
  x += 4  # Este bloque no se ejecuta porque la excepción es de tipo ValueError
else:
  x += 56  # Este bloque  se ejecuta 
finally:
  x += 5  # Este bloque siempre se ejecuta
print(x)