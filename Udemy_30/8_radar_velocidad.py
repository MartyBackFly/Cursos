from imprimir import espacio as aa

aa()

Velocidad = 0

F0= 0

F1= 0


sec = 0


F0 = 2*(10 ** -10)

F1 = (2.0000004 * (10 ** -10))

V = (6.685*(10**8))*(F1 - F0)/(F1 + F0)


print (f"la velocidad es {V} millas per hora")

aa()



# Valores para Dibujar la Tabla
ANCHO = 50
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
######################################################################
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "RADAR DE VELOCIDAD"
 
######################################################################
 
# Declaracion de variables
Velocidad   = 0.0
Frecuencia0 = 2e-10            
Frecuencia1 = 2.0000004e-10    
 
# Formato de Salida Final en Pantalla
Formato_Respuesta = ">>> La Velocidad es: %0.2f millas/hora."
 
######################################################################
 
# Encabezado del Programa
# LINEA 1: Parte superior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
# Mensaje Centrado
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
 
######################################################################
 
# Inicio del Programa:
# Calculo de la VELOCIDAD del radar
# velocidad = 6.685x10^8 x (f1 - f0) / (f1 + f0)
Velocidad=6.685e8*(Frecuencia1-Frecuencia0)/(Frecuencia1+Frecuencia0)
 
# LINEA 2: Separador de la tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
# Se muestra el mensaje en Pantalla
print(Formato_Respuesta.center(ANCHO,RELLENO2) % (Velocidad))
 
######################################################################
 
# LINEA 3: Parte Inferior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))




aa()

Velocidad = 0

F0 = 0

F1 = 0

sec = 0

F0 = 2 * (10 ** -10)

F1 = (2.0000004 * (10 ** -10))

V = (6.685 * (10 ** 8)) * (F1 - F0) / (F1 + F0)

# Formateo del resultado centrado en una cadena
resultado_formateado = f"La velocidad es {V} millas por hora"

# Imprimir el resultado centrado
print(resultado_formateado.center(60))  # Ajusta el ancho según lo necesites


aa()
