from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

# La lista de alumnos que creamos en el módulo anterior ahora debe ser un diccionario, en donde
# las claves serán nombres de alumnos y los valores sus respectivas cantidades de cursos.
# Para esto se debe modificar el código de las
# opciones 1 y 2 (agregar un nuevo alumno y ver la
# lista de alumnos).
# La tercera opción será “Ver la cantidad de cursos
# de un alumno”. Deberá solicitar el nombre de un
# alumno e imprimir en pantalla el número de
# cursos que tiene asociados como clave. La cuarta
# opción es la de salir, como en la versión anterior.
# Usar todo lo aprendido hasta el momento, el
# programa no debe de frenar de forma imprevista
# a causa de un error. Ya que en el material de
# lectura se vieron todas las posibles soluciones
# frente a los problemas que se puedan presentar. 

def validar(dato):
    while dato == "":
        print("Error campo vacio")
        dato = input("ingrese el dato nuevamente :")
    return dato

def convertir_valor(valor):
    while valor.isdecimal() == False:
        print("Error --> el valor tiene que ser numerico")
        valor = input("ingrese el valor :")
    return valor



alumnos = {}


while True:
    print("""Ingrese el número de la operación que desea ejecutar:"
     
     1 - Añadir un alumno a la lista.
     2 - Ver la lista de alumnos.
     3 - Ver la cantidad de cursos de un alumno
     4 - Salir."

     """)

    opcion = input("Ingrese el número de opción: ")
    print("############################")
    
    print("")

    if opcion == "1" : 
        nombre_alumno = input("Nombre del fulano >> : ")
        print("")
        nombre_alumno = validar(nombre_alumno)
        cursos = input("Ingrese cantidad de cursos >> :  ")
        print("")
        cursos = convertir_valor(cursos)
        alumnos[nombre_alumno] = cursos
        print("alumno ingresado exitosamente")
        print("")
    
    elif opcion == "2" : 
        print ("-- Lista de alumnos  // \n")
        print("")
        for alumno in alumnos:
            print(alumno + "\n")
        print("")
    
    elif opcion == "3" : 
        clave_alumno = input("Ingrese el nombre del fulano >> :")
        print("")
        
        clave_alumno = validar(clave_alumno)
        
        if clave_alumno in alumnos :
            print("-------------------------------")
            print(f"{clave_alumno} tiene {alumnos[clave_alumno]} cursos ")
            print("-------------------------------")
            print("")
        else:
            print(f"el fulano {clave_alumno} no tiene cursos asignados")
            print("----------------------")
    elif opcion == "4":
        print("Gracias por usar nuestros servicios")
        print("-----------------------------------")
        break
    else:
        print("La opcion no es valida.. pone un numero del 1 a 4 imbecil ... ")
        print("")
# mi_diccionario.update({'c': 3, 'd': 4})