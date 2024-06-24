
from imprimir import espacio as aa





# Un método estático en Python es un método que se define dentro de una clase pero que no tiene acceso a la 
# instancia de la clase (self) ni a la clase misma (cls) como parámetro. 
# Se utilizan para definir funciones que no necesitan acceder ni modificar ningún atributo o método de la clase.




class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            return "Error: división por cero"
        return a / b

# No es necesario crear una instancia de la clase Calculadora para usar los métodos estáticos
resultado_suma = Calculadora.sumar(5, 3)
resultado_resta = Calculadora.restar(5, 3)
resultado_multiplicacion = Calculadora.multiplicar(5, 3)
resultado_division = Calculadora.dividir(5, 3)

print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_multiplicacion)
print("División:", resultado_division)



aa()


class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @staticmethod
  def validate_topping(topping):
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True

  def __str__(self):
        return f"Pizza with toppings: {', '.join(self.toppings)}"


ingredients = ["cheese", "onions", "spam", ]
#ingredients = ["cheese", "onions", "spam", "pineapple"]
if all(Pizza.validate_topping(i) for i in ingredients):
  pizza = Pizza(ingredients)

print(f" zarasa pizza son // {pizza}")



aa()




#sololearn ejercicio 


#tu código va aquí

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