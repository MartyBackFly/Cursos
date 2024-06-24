from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz
from aafuncionimprimir import espacio_numero as az



# La función super es una función útil relacionada con la herencia que se refiere a la clase padre. 
# Se puede utilizar para encontrar el método con un nombre determinado en la superclase de un objeto.


class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()

# super().spam() llama al método spam de la superclase.


az(1)

class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(f"area: {self.width*self.height}")

class Rectangle(Shape):
    #your code goes here
    def perimeter(self):
        print(f"perimeter: {2*(w+h)}")



w = int(input("weight-->"))
h = int(input("height-->"))

r = Rectangle(w, h)
r.area()
r.perimeter()

zz()