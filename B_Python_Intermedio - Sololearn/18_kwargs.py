from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz


#**kwargs (significa argumentos de palabras clave) 

# **kwargs se utiliza para pasar un número variable de argumentos de palabra clave a una función. 
# Los argumentos pasados a través de **kwargs se recogen como un diccionario dentro de la función. 
# Esto significa que los valores asociados a cada palabra clave se pueden acceder mediante la clave correspondiente en el diccionario.



def my_func(x, y=7, *args, **kwargs):
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)


aa()


# Ejemplo de **kwargs
def detalles_persona(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

detalles_persona(nombre="Juan", edad=30, ciudad="Ciudad de México")  # Output:
# nombre: Juan
# edad: 30
# ciudad: Ciudad de México


aa()


# Ejemplo de **kwargs
def detalles_producto(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave.capitalize()}: {valor}")

detalles_producto(nombre="Camisa", precio=25.99, color="Azul", talla="M")  # Output:
# Nombre: Camisa
# Precio: 25.99
# Color: Azul
# Talla: M

aa()


class Estudiante:
    def __init__(self, **valores):
        self.nombre = valores.get('nombre', 'Sin nombre')
        self.edad = valores.get('edad', None)
        self.notas = valores.get('notas', [])

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print("Notas:")
        for i, nota in enumerate(self.notas, 1):
            print(f"Nota {i}: {nota}")

# Crear instancia de Estudiante usando **valores
estudiante1 = Estudiante(nombre="Ana", edad=20, notas=[85, 90, 88, 5])

# Mostrar información del estudiante
estudiante1.mostrar_informacion()



aa()


def func(**kwargs):
  print(kwargs["zero"])

func(a = 0, zero = 8)