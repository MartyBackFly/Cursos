from aafuncionimprimir import espacio


def rect(length, width):
  area = length * width
  perimeter = 2 * length + 2 * width
  return area, perimeter #2 valores

x, y = rect(50, 100) #2 variables
print(x, y)


espacio()

