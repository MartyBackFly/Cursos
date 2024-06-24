from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

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
print(square.calculate_area())


# new_square es un método de clase y se llama en la clase, en lugar de en una instancia de la clase. Devuelve un nuevo objeto de la clase cls.

# Técnicamente, los parámetros self y cls son solo convenciones; podrían cambiarse a cualquier otra cosa. Sin embargo, se siguen universalmente,

# por lo que es prudente seguir utilizándolos.


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)


print(pizza.toppings)
print(f" zarasa pizza con // {pizza.toppings}")


aa()



class Shape :
    def  __init__(self,w,h):
        self.h = h
        self.w = w


    @staticmethod
    def area (w,h):
        return w * h


w = int(input("--> "))
h = int(input("--> "))

print(Shape.area(w, h))