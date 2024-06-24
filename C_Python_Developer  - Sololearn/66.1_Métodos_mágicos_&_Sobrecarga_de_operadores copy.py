from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az



"""Sobrecarga de Operadores 
Estamos mejorando nuestra aplicación de dibujo.

Nuestra aplicación necesita soportar la adición y comparación de dos objetos Shape  .

Agrega los métodos correspondientes para habilitar la adición + y la comparación utilizando el operador mayor que > para la clase Shape.

La adición debería devolver un nuevo objeto con la suma de los anchos y las alturas de los operandos, mientras que la comparación debería devolver el resultado de comparar las áreas de los objetos.

El código proporcionado crea dos objetos Shape a partir de la entrada del usuario, muestra el área() de su suma y los compara.
"""

# micodigo malito ,,, faltan cosas 

# class Shape: 
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h

#     def area(self):
#         return self.width*self.height

#     #your code goes here
#     def __gt__(self,other):
#         return self.area() > other.area()

#     def __add__(self, other):
#         result =  self.area() + other.area()

# w1 = int(input())
# h1 = int(input())
# w2 = int(input())
# h2 = int(input())

# s1 = Shape(w1, h1)
# s2 = Shape(w2, h2)
# result = s1 + s2

# print(result.area())
# print(s1 > s2)

   

az(1)
# Aquí tienes el código completo con los métodos __add__ y __gt__ implementados para la clase Shape:

# python  código



class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.area() > other.area()

    def __add__(self, other):
        # Sumar anchos y alturas para crear un nuevo objeto Shape
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Shape(new_width, new_height)

# Entrada del usuario para los tamaños de los objetos Shape
w1 = int(input("Ancho de la figura 1: "))
h1 = int(input("Altura de la figura 1: "))
w2 = int(input("Ancho de la figura 2: "))
h2 = int(input("Altura de la figura 2: "))

# Crear los objetos Shape
s1 = Shape(w1, h1)
s2 = Shape(w2, h2)

# Sumar los objetos Shape
result = s1 + s2

# Mostrar el área de la suma de los objetos Shape
print("Área de la suma de las dos figuras:", result.area())

# Comparar las áreas de los objetos Shape
print("¿La figura 1 tiene un área mayor que la figura 2?", s1 > s2)


# Este código ahora permitirá la adición de dos objetos Shape usando el operador +, devolviendo un nuevo objeto Shape con las 
# dimensiones sumadas. Además, la comparación > compara las áreas de los objetos Shape en lugar de sus dimensiones directas.

az(2)


class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width*self.height

    #your code goes here
    

    def __add__(self, other):
        return Shape(self.width + other.width, self.height + other.height)
        

    def __gt__(self,other):
        return self.area() > other.area()

w1 = int(input("Ancho de la figura 3: "))
h1 = int(input("Altura de la figura 3: "))
w2 = int(input("Ancho de la figura 4: "))
h2 = int(input("Altura de la figura 4: "))

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)



 
"""
ChatGPT
La función __add__ que has proporcionado está sobrecargando el operador de suma (+) para la clase Shape. Esto significa que cuando utilizas el operador + entre dos objetos Shape, Python invocará automáticamente este método y retornará un nuevo objeto Shape que representa la suma de las dos formas originales.

Veamos más de cerca cómo funciona esta función:

self.width + other.width: Aquí, estamos sumando los anchos (width) del objeto self (el primer objeto Shape) y other (el segundo objeto Shape). Esto da como resultado el ancho de la nueva forma.

self.height + other.height: Similar al paso anterior, estamos sumando las alturas (height) de self y other, lo que resulta en la altura de la nueva forma.

return Shape(self.width + other.width, self.height + other.height): Finalmente, utilizamos los valores calculados del ancho y la altura para crear un nuevo objeto Shape con estos valores y lo retornamos. Este nuevo objeto Shape representa la suma de las dos formas originales.

En resumen, esta función crea un nuevo objeto Shape cuyas dimensiones son la suma de las dimensiones de los objetos Shape originales sobre los cuales se aplicó el operador +.

si yo no creo el metodo __add__ no podria sumar result = s1 + s2 ??
ChatGPT
Correcto, si no creas el método __add__ en la clase Shape, no podrías sumar dos instancias de Shape usando el operador +. En Python, el operador + no sabe cómo manejar objetos personalizados a menos que se le indique específicamente cómo hacerlo mediante la sobrecarga de operadores.

Aquí tienes una explicación más detallada:

Sobrecarga de Operadores
La sobrecarga de operadores permite definir o redefinir cómo los operadores (+, -, *, >, <, etc.) funcionan con objetos de una clase personalizada. Esto es útil cuando quieres que tus objetos se comporten de manera similar a los tipos de datos integrados de Python (como números y cadenas).

Sin Sobrecarga de Operadores
Si no defines el método __add__, el intento de usar + con dos objetos Shape resultará en un error:"""

# python  código

az(3)


class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

# No se define __add__ aquí

w1 = 3
h1 = 4
w2 = 5
h2 = 6

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)

# result = s1 + s2  # Esto lanzará un TypeError


# Este código producirá un TypeError como:
#  TypeError: unsupported operand type(s) for +: 'Shape' and 'Shape'



# Con Sobrecarga de Operadores

""" Al definir el método __add__, le estás diciendo a Python cómo debe comportarse el operador + cuando se utiliza con instancias de tu clase Shape: """

# python código

az(4)


class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        return Shape(self.width + other.width, self.height + other.height)

    def __gt__(self, other):
        return self.area() > other.area()

# Crear instancias de Shape
w1 = 2
h1 = 2
w2 = 2
h2 = 2

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)

result = s1 + s2  # Esto funciona correctamente ahora

print(result.area())  # Imprime el área de la nueva forma sumada
print(f"s1 es mayor que s2 : {s1 > s2}")        # Compara las áreas de las dos formas



"""Explicación de __add__
El método __add__ define la lógica para sumar dos objetos Shape. La función toma dos argumentos, self y other, donde self es el primer operando y other es el segundo operando de la operación de suma. En este método:

Se suman las anchuras de los dos objetos Shape (self.width + other.width).
Se suman las alturas de los dos objetos Shape (self.height + other.height).
Se crea y retorna un nuevo objeto Shape con las dimensiones resultantes de estas sumas.
Esto permite que la operación s1 + s2 sea válida y produzca un nuevo objeto Shape con las dimensiones correctas."""