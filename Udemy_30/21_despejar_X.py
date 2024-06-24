# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
# Mensaje inicial
MENSAJE_INICIAL = "ECUACION DE PRIMER GRADO: ax + b = 0"
 
# Formato de Salida Final en Pantalla
Formato_Ecuacion = "ECUACION: {}x + {} = 0"
 
# Encabezado del Programa
print(CADENA_VACIA.center(ANCHO, RELLENO1))
print(MENSAJE_INICIAL.center(ANCHO, RELLENO2))
print(CADENA_VACIA.center(ANCHO, RELLENO1))
 
# Declaración de variables
a = float(input(">>> Valor de a: "))
b = float(input(">>> Valor de b: "))
 
print(CADENA_VACIA.center(ANCHO, RELLENO1))
print(Formato_Ecuacion.format(a, b))
print(CADENA_VACIA.center(ANCHO, RELLENO1))
 
# Cálculo de la solución
try:
    x = -b / a
    print(">>> SOLUCION: x =", x)
except ZeroDivisionError:
    if b != 0:
        print("La ECUACION no tiene solucion.")
    else:
        print("La ECUACION tiene infinitas soluciones.")
 
print(CADENA_VACIA.center(ANCHO, RELLENO1))
