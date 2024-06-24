from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1  # Disminuir las vidas en 1
        if self._lives == 0:
            print("Game Over")

# Creación del objeto Player y llamadas al método hit()
p = Player("Cyberpunk77", 3)
p.hit()  # 2 vidas restantes
p.hit()  # 1 vida restante
p.hit()  # 0 vidas restantes, debería imprimir "Game Over"
