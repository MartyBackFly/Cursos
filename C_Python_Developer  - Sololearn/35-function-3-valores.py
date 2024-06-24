from aafuncionimprimir import espacio

def rect1(d1, d2):
  area = d1 * d2
  perimeter = 2 * d1 + 2 * d2
  price = 1000 * area
  return area, perimeter, price

a, b, c = rect1(2, 4)
print(a, b, c)


espacio()


def profitable(d1, d2):
  area = d1 * d2
  invest = area > 700
  return invest

buy = profitable(90, 120)
print(buy)
buy = profitable(90, 50)
print(buy)
buy = profitable(3, 120)
print(buy)





espacio()


#ejmeplo despues de return no se ejecuta nada mas 


def rect(d1, d2):
  area = 0
  return area
  #Fin de la ejecución de la función
  area = d1 * d2 #No se ejecuta

x = rect(50, 50)
print(x)