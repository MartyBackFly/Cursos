from aafuncionimprimir import espacio as aa
from aafuncionimprimir import rayita as zz
from aafuncionimprimir import espacio_numero as az



class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)


aa()

# El método __add__ permite la definición de un comportamiento personalizado para el operador + en nuestra clase.

# Como puedes ver, suma los atributos correspondientes de los objetos y devuelve un nuevo objeto, que contiene el resultado.

# Una vez que está definido, podemos sumar dos objetos de la clase juntos.

# Más métodos mágicos para operadores comunes:

# __sub__ para -

# __mul__ para *

# __truediv__ para /

# __floordiv__ para //

# __mod__ para %

# __pow__ para **

# __and__ para &

# __xor__ para ^

# __or__ para |

# La expresión x + y se traduce en x.__add__(y).

# Sin embargo, si x no ha implementado __add__, y x e y son de diferentes tipos, entonces y.__radd__(x) es llamado.

# Existen métodos r equivalentes para todos los métodos mágicos mencionados anteriormente.


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!!!!!!!!!")
print(spam / hello)


az(2)

asd = SpecialString("ramon")
asdd = SpecialString("richard")
print(asd / asdd)

aa()

# Python también proporciona métodos mágicos para comparaciones.

# __lt__ para <

# __le__ para <=

# __eq__ para ==

# __ne__ para !=

# __gt__ para >

# __ge__ para >=

#  Si __ne__ no está implementado, devuelve lo opuesto de __eq__. 

# No hay otras relaciones entre los otros operadores.


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs-sssss")
spam > eggs


az(3)


# Hay varios métodos mágicos para hacer que las clases actúen como contenedores.

# __len__ para len()

# __getitem__ para indexar

# __setitem__ para asignar a valores indexados

# __delitem__ para eliminar valores indexados

# __iter__ para iterar sobre objetos (por ejemplo, en bucles for)

# __contains__ para in

# Hay muchos otros métodos mágicos que no vamos a cubrir aquí, tales como __call__ para llamar a objetos como
# funciones, y __int__, __str__, y similares, para convertir objetos en tipos integrados.

class MiClase:
    def __init__(self, datos):
        self.datos = datos

    def __getitem__(self, indice):
        return self.datos[indice]

# Creamos un objeto de la clase MiClase
objeto = MiClase([1, 2, 3, 4, 5])

# Ahora podemos indexar el objeto
print(objeto[2])  # Salida: 3


az(4)

#items al azar 

import random

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])