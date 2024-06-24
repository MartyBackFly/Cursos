from imprimir import espacio as aa


class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

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
fido.bark()


aa()

class Student:
  def __init__(self, name):
    self.name = name
  
  def sayHi(self):
    print("Hi from "+ self.name)
  
  def areyouok(self):
    print ("are you ok mtf ? ")


s1 = Student("Amy")
s1.sayHi()
s1.areyouok()


aa()


class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

#tu código va aquí


name = input("name")
level = input("level ricard")

player1 = Player(name, level)

player1.intro()