from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz


class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)


print(felix.color, felix.legs)
print(f" felix es color {felix.color} y al dia de hoy tiene {felix.legs} patas ")

aa()

class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
print(felix.color)

aa()

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
print(fido.color)
fido.bark()
print(fido)


aa()


class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

#your code goes here


name = input("name-->")
level = input("level-->")

player_a = Player(name, level)

player_a.intro()

aa()


class Student:
  def __init__(self, name):
    self.name = name
  
  def sayHi(self):
    print("Hi from "+ self.name)
  
s1 = Student("Amy")
s1.sayHi()
