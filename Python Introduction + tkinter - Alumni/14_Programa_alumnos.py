from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


aa()
az(1)


lista_alumnos = []


print("""Ingrese el número de la operación que desea ejecutar: 

1 - Ver la lista de alumnos.
2 - Añadir un alumno a la lista.
3 - Salir.""")
print("")


lista_alumnos = []

while True:
    
    opcion = int(input("opcion N : "))
    if opcion == 1:
        print(lista_alumnos)
        print("---------------")
    elif opcion == 2 :
        lista_alumnos.append(input("nombre_del_pibito/a : "))

    elif opcion == 3:
        print("¡Gracias por utilizar el programa!")
        break
    else:
        print("****************************" )
        print("   ERROR " )
        print("La opción ingresada no es correcta, vuelva aintentarlo.")
        print("****************************" )
        print("")
        print("""Ingrese el número de la operación que desea ejecutar: 
1 - Ver la lista de alumnos.
2 - Añadir un alumno a la lista.
3 - Salir.""")


az(2)

# solucion: 


# Crear una lista vacía.
alumnos = []

# Ejecutar el siguiente código infinitamente.
while True:
    print("Ingrese el número de la operación que desea ejecutar:")
    print("1 - Ver la lista de alumnos.")
    print("2 - Añadir un alumno a la lista.")
    print("3 - Salir.")

    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        print("Lista de alumnos:")
        for alumno in alumnos:
            nombre = alumno[0]
            cursos = alumno[1]
            print(nombre + " - " + str(cursos) + " cursos")
    elif opcion == "2":
        nombre_alumno = input("Ingrese el nombre del alumno: ")
        if nombre_alumno == "":
            print("Error: no ha ingresado un nombre válido.")
            continue
        # Es condición que la cantidad de cursos sea un número entero.
        cursos = int(input("Ingrese la cantidad de cursos: "))
        # Agregar un elemento al final de la lista "alumnos" que sea una lista con dos elementos: el nombre del alumno y la cantidad de cursos.
        alumnos.append([nombre_alumno, cursos])
        print("Has ingresado el alumno correctamente.")
    elif opcion == "3":
        # Forzar el bucle a que termine.
        break
    else:
        print("La opción ingresada no es correcta, vuelva a intentarlo.")

print("¡Gracias por utilizar el programa!")



# la lista se veria asi ---> alumnos = [["Juan", 3], ["María", 5], ["Pedro", 2]]


aa()
az(3)


# mejorado por chat : 


lista_alumnos = []

def mostrar_menu():
    print("""
Ingrese el número de la operación que desea ejecutar: 
1 - Ver la lista de alumnos.
2 - Añadir un alumno a la lista.
3 - Salir.
""")

mostrar_menu()

while True:
    try:
        opcion = int(input("Opción N: "))
        if opcion == 1:
            print("Lista de alumnos:", lista_alumnos)
            print("---------------")
        elif opcion == 2:
            nombre = input("Nombre del alumno/a: ")
            lista_alumnos.append(nombre)
            print(f"{nombre} ha sido añadido/a a la lista.")
            print("---------------")
        elif opcion == 3:
            print("¡Gracias por utilizar el programa!")
            break
        else:
            print("****************************")
            print("   ERROR ")
            print("La opción ingresada no es correcta, vuelva a intentarlo.")
            print("****************************")
    except ValueError:
        print("****************************")
        print("   ERROR ")
        print("Debe ingresar un número válido.")
        print("****************************")

    mostrar_menu()
