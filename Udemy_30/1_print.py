



nombre = input("nombre -->")
apellido = input("apellido -->")

print(f"{nombre} - {apellido}")
 


print("---------------------------------")

# Declaracion de variables
nombre = ""
apellido = ""
 
# Solicitud de Datos
print(">>> Introduce tu nombre: ")
nombre = input("> ")
print(">>> Introduce tu apellido: ")
apellido= input("> ")
 
# Mensaje en Pantalla: Metodo .format()
print("Hola {0} {1}, gusto en conocerte!".format(nombre,apellido))

print("---------------------------------")
# Declaracion de variables
nombre = ""
apellido = ""
 
# Solicitud de Datos
print(">>> Introduce tu nombre: ")
nombre = input("> ")
print(">>> Introduce tu apellido: ")
apellido = input("> ")
 
# Mensaje en Pantalla: Operador de Formato %
print("Hola %s %s, gusto en conocerte!" %(nombre,apellido))

print("---------------------------------")



#forma mas nueva \


# Ejemplo 1: Insertar una cadena de texto
nombre = "Juan"
print(f"Hola, {nombre}")

# Ejemplo 2: Insertar un número entero
edad = 25
print(f"Tengo {edad} años")

# Ejemplo 3: Insertar un número de punto flotante
altura = 1.75
print(f"Mi altura es {altura:.2f} metros")

# Ejemplo 4: Insertar un número como representación hexadecimal
numero = 255
print(f"El número en hexadecimal es {numero:x}")