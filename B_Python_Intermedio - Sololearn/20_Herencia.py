from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz


class Animal: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
zz()
raquel=Cat("ricky", "red")
print(raquel.color)
print(raquel.name)
raquel.purr()

# Una clase que hereda de otra clase es llamada una subclase.

# Una clase de la que se hereda se llama una superclase.

# Si una clase hereda de otra con los mismos atributos o métodos, los sobrescribe. 


zz()
class Wolf: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof")

husky = Dog("Max", "grey")
husky.bark()


aa()


class A:
  def method(self):
    print(1)

class B(A):
  def method(self):
    print(2)

B().method()