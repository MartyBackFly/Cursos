from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
    
    #your code goes here
    @property 
    def isAlive(self): 
        if self._lives > 0: 
            return True

aa()
az(1)
print(f"esta con vida ? {Player.isAlive} ")

p = Player("Cyberpunk77", int(input("salud --> ")))
i = 1
az(2)
print(f"esta con vida --> ? {p.isAlive} ")

az(3)
while True:
    p.hit()
    print("Hit # " + str(i))
    i += 1
    if not p.isAlive:
        print("Game Over")
        break