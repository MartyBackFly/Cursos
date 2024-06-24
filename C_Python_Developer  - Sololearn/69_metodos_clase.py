from imprimir import espacio as aa


class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def sayHi(cls):
        print("Hi")

# Crear una instancia de Person
person = Person("John")

# Llamar al método sayHi()
Person.sayHi()  # Esto imprimirá "Hi"


aa()



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def square(cls, side_length):
        return cls(side_length, side_length)

# Usando el método de clase para crear un cuadrado
square = Rectangle.square(5)
print("Square width:", square.width)  # Output: 5
print("Square height:", square.height)  # Output: 5



aa()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_string(cls, string):
        x, y = map(int, string.split(','))
        return cls(x, y)

# Usando el método de clase para crear un objeto Point desde una cadena
point = Point.from_string("3,4")
print("Point coordinates:", point.x, point.y)  # Output: 3 4


aa()

#length = longitud
#width = ancho
#heigth = altura

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def calculate_area(self):
    return self.width * self.height

  @classmethod
  def new_square(cls, side_length):
    return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(f"area is --> {square.calculate_area()}")