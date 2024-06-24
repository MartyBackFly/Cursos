


# isinstance() es una función incorporada en Python que se utiliza para 
# comprobar si un objeto es una instancia o subclase de una clase específica. La sintaxis general de isinstance() es la siguiente:

# python
# Copy code
# isinstance(objeto, clase)
# objeto: El objeto que se va a comprobar.
# clase: La clase o el tipo de datos que se quiere comprobar si el objeto es una instancia de ella.
# La función devuelve True si el objeto es una instancia o subclase de la clase especificada, y False en caso contrario.

# Aquí tienes algunos ejemplos de uso de isinstance():


x = 5
if isinstance(x, int):
    print("x es un entero")

y = "Hola"
if isinstance(y, str):
    print("y es una cadena de caracteres")

z = [1, 2, 3]
if isinstance(z, list):
    print("z es una lista")


#En cada uno de estos ejemplos, isinstance() se utiliza para comprobar si el objeto dado (x, y o z) 
    # es una instancia del tipo de datos especificado (int, str o list, respectivamente). Si lo es, se imprime un mensaje apropiado.