from imprimir import espacio as aa

aa()

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


#   Más métodos mágicos para operadores comunes:
#   __sub__ for -
#   __mul__ for *
#   __truediv__ for /
#   __floordiv__ for //
#   __mod__ for %
#   __or__ for |
#   __pow__ for **
#   __and__ for &
#   __xor__ for ^


# La expresión x + y se traduce en x.__add__(y).
# Sin embargo, si x no ha implementado __add__, y x e y son de tipos diferentes, entonces y.__radd__(x) es llamado.
# Existen métodos r equivalentes para todos los métodos mágicos que acabamos de mencionar.

aa()


class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world ! ! ! ! ")
print(spam / hello)

aa()



class Specialcooking:
    def __init__(self, comida):
        self.comida = comida

    def __add__(self, asd):
        line = "_" * len(asd.comida)
        return "  ++  ".join([self.comida, line, asd.comida])
  

ingrediente1 = (input("ingrediente 1 -- >"))
ingrediente2 = input("ingrediente 1 -- >")
  
recipe = Specialcooking(ingrediente1) 

result = recipe + Specialcooking(ingrediente2)  

print (result)



a1 = Specialcooking("ajo")
a2 = Specialcooking("derse")
print(a1 + a2)



#  Python también proporciona métodos mágicos para las comparaciones.
#  __lt__ for <
#  __le__ for <=
#  __eq__ for ==
#  __ne__ for !=
#  __gt__ for >
#  __ge__ for >=
 
#  Si __ne__ no está implementado, devuelve lo contrario de __eq__.
#  No hay otras relaciones entre los otros operadores.

aa()


class SpecialStringui:
  def __init__(self, conte):
    self.conte = conte

  def __gt__(self, other):
    for index in range(len(other.conte)+1):
      result = other.conte[:index] + ">" + self.conte
      result += ">" + other.conte[index:]
      print(result)

spam = SpecialStringui("spam")
eggs = SpecialStringui("eggs")
spam > eggs


# Hay varios métodos mágicos para hacer que las clases actúen como contenedores.

# __len__ para len()
# __getitem__ para indexar
# __setitem__ para asignar a los valores indexados
# __delitem__ para borrar los valores indexados
# __iter__ para la iteración sobre objetos (por ejemplo, en los bucles for)
# __contains__ para in
# 
# Hay muchos otros métodos mágicos que no cubriremos aquí, como __call__ para llamar a los objetos como 
# funciones, y __int__, __str__, y similares, para convertir objetos en tipos incorporados.


aa()

class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __len__(self):
        return len(self.elementos)

    def __getitem__(self, indice):
        return self.elementos[indice]

    def __setitem__(self, indice, valor):
        self.elementos[indice] = valor

    def __delitem__(self, indice):
        del self.elementos[indice]

    def __iter__(self):
        return iter(self.elementos)

    def __contains__(self, elemento):
        return elemento in self.elementos

# Crear una instancia de MiLista
mi_lista = MiLista([1, 2, 3, 4, 5])  # Se define la clase MiLista que implementa los métodos mágicos necesarios para simular una lista.

# Usar las operaciones definidas
print(len(mi_lista))      # Salida: 5    # __len__ devuelve la longitud de la lista.

print(mi_lista[0])        # Salida: 1    # __getitem__ permite indexar la lista.

mi_lista[0] = 10
print(mi_lista[0])        # Salida: 10   # __setitem__ permite asignar valores a elementos indexados.

del mi_lista[0]
print(len(mi_lista))      # Salida: 4    # __delitem__ permite eliminar elementos de la lista.

print(2 in mi_lista)      # Salida: True   # __contains__ permite verificar si un elemento está presente en la lista usando el operador in.

print(6 in mi_lista)      # Salida: False

# Iterar sobre la lista   __iter__ permite iterar sobre la lista.  usando un bucle for.
for elemento in mi_lista:
    print(f"iteracion {elemento}")




  






