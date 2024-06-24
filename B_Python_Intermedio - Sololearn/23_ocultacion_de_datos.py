from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)


aa()
# En el código anterior, el atributo _hiddenlist está marcado como privado, pero aún se puede acceder en el código externo.

# El método mágico __repr__ se utiliza para la representación de cadena de la instancia.


# Los métodos con nombres enmascarados aún pueden ser accedidos externamente, pero con un nombre diferente. El método __privatemethod de la clase Spam podría ser accedido externamente con _Spam__privatemethod.


class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)


print(s.__egg) # sin esta linea no da error 


"""salida # 

7
7


Traceback (most recent call last):
  File "./Playground/file0.py", line 9, in <module>
    print(s.__egg)
AttributeError: 'Spam' object has no attribute '__egg'"""