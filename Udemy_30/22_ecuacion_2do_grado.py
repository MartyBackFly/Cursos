
# Importacion de librerias
from math import sqrt
 
######################################################################
 
# Valores para Dibujar la Tabla
ANCHO = 55
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
######################################################################
 
MENSAJE_INICIAL = "ECUACION DE SEGUNDO GRADO: ax^2 + bx + c = 0"
 
######################################################################

# ► Variables

a = 0

b = 0

c = 0

x1 = 0

x2 = 0

discriminante = 0
######################################################################
 
# Encabezado del Programa
print(CADENA_VACIA.center(ANCHO,RELLENO1))
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
print(CADENA_VACIA.center(ANCHO,RELLENO1))


######################################################################
 
# Solicitud de Datos 
a = float(input(">>> Valor de a: "))
b = float(input(">>> Valor de b: "))
c = float(input(">>> Valor de c: "))

discriminante = b**2 - 4*a*c

try:
    x1 = (-b + sqrt(discriminante)) / (2 * a)
    x2 = (-b - sqrt(discriminante)) / (2 * a)

    print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
    if x1 == x2:
        print(">>> SOLUCION: x = {x1}" )
    else:
        print(f">>> SOLUCIONES: x1 = {x1} -- y -- x2 = {x2}")
 
except ZeroDivisionError:
 
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
    if b != 0:
        print("La ecuacion no tiene solucion.")
    else:
        print("La ecuacion tiene infinitas soluciones.")
 
except ValueError:
    # Casos:
    # 1) Se produce una division por cero.
    # 2) Se produce por calcular la raız cuadrada de un discriminante
    # negativo.
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
    print("No hay soluciones reales")
 
######################################################################
 
print(CADENA_VACIA.center(ANCHO,RELLENO1))


""" 
► Datos de Prueba.

a) a = 2 , b = 7, c = 2

b) a = 1 , b = 2, c = 3

c) a = 0 , b = 2, c = 3

d) a = 0 , b = 0, c = 3 

"""



