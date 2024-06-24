

# num = 102
# if num > 100:
#   raise ValueError


# name = "123"
# raise NameError("Invalid name!")


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

try:
    resultado = dividir(10, 0)
except ValueError as error:
    print("Se produjo un error:", error)
else:
    print("El resultado de la división es:", resultado)

 
print("#############################################################################")

#ejercicio rancio tweet = input()
tweet = input("posted here ---> ")

try:
    # Verificar si la longitud del tweet es mayor que 42 caracteres
    if len(tweet) > 42:
        raise ValueError()
except ValueError as error:
    print("Error")
else:
    print("Posted")


"""
Bloque try: El bloque try, que es utilizado para envolver el código que puede causar una excepción.

Verificar la longitud del tweet: Se verifica si la longitud del tweet es mayor que 42 caracteres.

python
Copiar código
if len(tweet) > 42:
    raise ValueError()
len(tweet) > 42: Comprueba si la longitud del tweet es mayor que 42.
raise ValueError(): Si la condición es verdadera (es decir, si el tweet tiene más de 42 caracteres), se lanza un ValueError.
Bloque except: Si se lanza un ValueError en el bloque try, se ejecutará este bloque.

python
Copiar código
except ValueError as error:
    print("Error")
except ValueError as error: Captura el ValueError que se lanzó en el bloque try.
print("Error"): Imprime "Error" para indicar que hubo un problema (es decir, que el tweet es demasiado largo).
Bloque else: Si no se lanza ninguna excepción en el bloque try, se ejecutará el bloque else.

python
Copiar código
else:
    print("Posted")
print("Posted"): Imprime "Posted" para indicar que el tweet ha sido aceptado y "publicado" (o al menos pasó la verificación de longitud).
Resumen del flujo del código:
Se pide al usuario que ingrese un tweet.
Si el tweet tiene más de 42 caracteres, se lanza un ValueError y se imprime "Error".
Si el tweet tiene 42 caracteres o menos, se imprime "Posted".
Ejemplos:
Tweet válido (menor o igual a 42 caracteres):

Entrada: "This is a short tweet"
Salida: "Posted"
Tweet no válido (mayor a 42 caracteres):

Entrada: "This is a very long tweet that definitely exceeds the 42 character limit"
Salida: "Error"
Este código es una forma de asegurar que los tweets no excedan una longitud máxima permitida de 42 caracteres, utilizando manejo de excepciones para controlar el flujo del programa basado en esta condición."""




