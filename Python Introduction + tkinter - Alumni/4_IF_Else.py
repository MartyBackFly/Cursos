from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

# Ejercicio 4

# Se preguntará el tipo de rol que desempeña una
# persona en una institución por una entrada del
# tipo input. Los valores posibles son “admin” o
# “profesor”.

# Luego si la persona es “admin” o “profesor”, se
# debería pedirla contraseña, siendo la única válida
# “1234” (la contraseña se toma como string). Si
# la contraseña ingresada es válida, se procederá a
# pedir el nombre de la persona, y si no es vacío, se
# lo saludará.
# Contemplar los casos donde no se cumple como
# corresponde y mostrar un mensaje en pantalla.

rol = str(input("eres admin o profesor ?   : "))



if rol == str("admin") or str("profesor"):
    password = input("digite la clave :")
    if password == "1234" : 
            name = input("what is your name mdf :")
            print(f"Hello {name} mdf! ")
    else :
        print("clave erronea")
else:
     print("vo quien so ")





aa()


#solucion : 



rol = input("Ingrese su rol: ")
if rol == "admin" or rol == "profesor":
        clave = input("Ingrese clave: ")
        if clave == "1234":
           nombre = input("Ingrese su nombre: ")
           if nombre == "":
                 print("¡Error, nombre vacio!")
           else:
                print("Hola, " + nombre)
        else:
                print("¡Clave incorarecta!")
else:
        print("¡Ese rol no existe!")