class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width*self.height

    #tu código va aquí
    def __add__(self, other):
        return Shape(self.width + other.width, self.height + other.height)

    def __gt__(self, other):
        return self.area() > other.area()

w1 = int(input("w1 ="))
h1 = int(input("h1 ="))
w2 = int(input("w2 ="))
h2 = int(input("h2 ="))

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)


  # Clase Shape: Define una clase llamada Shape, que tiene los siguientes métodos:

#__init__(self, w, h): El constructor de la clase Shape inicializa los atributos de instancia width y height con los valores 
# proporcionados w y h, respectivamente.

# area(self): Este método calcula y devuelve el área de la forma multiplicando el ancho (width) por la altura (height).

# __add__(self, other): Sobrecarga el operador de suma (+) para permitir la adición de dos instancias de Shape. Esta operación 
# crea una nueva instancia de Shape cuyo ancho y altura son la suma de los anchos y alturas de las dos instancias originales.

# __gt__(self, other): Sobrecarga el operador de comparación mayor que (>) para comparar dos instancias de Shape basándose en sus áreas. 
# Devuelve True si el área de la instancia actual es mayor que el área de la otra instancia.

# Entrada de usuario: El código solicita al usuario que ingrese el ancho (w1) y la altura (h1) de la primera forma, y el ancho (w2) y la 
# altura (h2) de la segunda forma.

# Creación de instancias de Shape: Se crean dos instancias de la clase Shape, s1 y s2, utilizando los valores proporcionados por el usuario.

# Operación de suma: Se suma (+) s1 y s2, lo que invoca el método __add__ definido en la clase Shape. El resultado se asigna a la variable result.

# Impresión del área del resultado: Se imprime el área del resultado (result.area()).

# Comparación de áreas: Se compara las áreas de las dos instancias de Shape (s1 y s2) utilizando el operador mayor que (>). La impresión 
# de print(s1 > s2) devolverá True si el área de s1 es mayor que el área de s2, y False de lo contrario.

# Cuando se ejecuta result.area(), Python busca el método area() dentro de la clase Shape porque result es una instancia de esta clase.

# El método area() definido en la clase Shape se ejecuta. Este método toma los valores de ancho (width) y altura (height) de la instancia 
# result y los utiliza para calcular el área de la forma representada por result.

# El área se calcula multiplicando el ancho (width) por la altura (height) de la forma representada por result.

# El resultado del cálculo se devuelve como resultado de la llamada al método area().

# Aquí tienes un ejemplo con valores concretos:

# Supongamos que tenemos dos instancias de Shape llamadas s1 y s2 con las siguientes dimensiones:

# s1: Ancho (width) = 3, Altura (height) = 4
# s2: Ancho (width) = 5, Altura (height) = 2
# Después de realizar la suma (result = s1 + s2), result tendría las siguientes dimensiones:

# result: Ancho (width) = 8 (3 + 5), Altura (height) = 6 (4 + 2)
# Entonces, cuando llamamos a result.area(), se realizará el siguiente cálculo:

# python
# Copy code
# result.area() = result.width * result.height
#               = 8 * 6
#               = 48
# Por lo tanto, result.area() devolverá 48 como resultado.