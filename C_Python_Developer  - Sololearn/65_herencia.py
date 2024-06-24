from imprimir import espacio as aa


aa()

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
print(fido.name)

aa()

amy = Cat("amy", "pink")
print(amy.color)
amy.purr()


aa()


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
ramy = Wolf("Ramy", "grey")
ramy.bark()


aa()


class A:
  def method(self):
    print(1)

class B(A):
  def method(self):
    print(2)

B().method()

#este código demuestra el concepto de herencia y el comportamiento de sobrescribir métodos en Python. 
#Cuando una clase hereda de otra y redefine un método con el mismo nombre, el método de la clase hija se 
#ejecutará en lugar del método de la clase padre cuando se llame en una instancia de la clase hija.


aa()


class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2)
    super().spam()
            
B().spam()


# Primero, imprimirá 2, ya que es lo que hace el método spam() de la clase B.
# Luego, llama a super().spam(), que llama al método spam() de la clase base A, lo que imprime 1.

aa()

class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2)
    

class C(B):
  def spam(self):
    print(3)
    super().spam()
            
C().spam()


# super().spam() llama a la clase padre en este caso B e imprime 2 . Si cambiamos -class C(B):- por -class C(A):- 
# entonces imprimira 1 por que su clase padre sera la primera 

 
