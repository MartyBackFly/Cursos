from imprimir import espacio as aa

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad no puede ser negativa.")

# Crear una instancia de la clase Persona
persona = Persona("Juan", 30)

# Acceder a la propiedad 'nombre' (solo lectura)
print("Nombre:", persona.nombre)

# Intentar modificar la propiedad 'nombre' (debería dar error)
# persona.nombre = "Pedro"

# Acceder y modificar la propiedad 'edad' (lectura y escritura)
print("Edad:", persona.edad)
persona.edad = 35
print("Nueva edad:", persona.edad)

# Intentar modificar la edad a un valor negativo
persona.edad = -5  # Esto debería imprimir "La edad no puede ser negativa."


aa()


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True
# si intentamos cambiar este valor con la linea anterior  el codigo dara error
