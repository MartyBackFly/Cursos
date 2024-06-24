from imprimir import espacio as aa


#creoacion de objeto 


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Acceder a los atributos de la instancia
print("Nombre:", persona1.nombre)
print("Edad:", persona1.edad)



aa() 


#creacion de @classmethod 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def crear_persona(cls, nombre, edad):
        return cls(nombre, edad)

# Crear una instancia de la clase Persona usando el método de clase
persona2 = Persona.crear_persona("María", 25)

# Acceder a los atributos de la instancia
print("Nombre:", persona2.nombre)
print("Edad:", persona2.edad)
