from imprimir import espacio as aa

grados_F = int(input("ïngrese los grados F -->"))
celcius = 0.0

celcius = (grados_F - 32.0) * 5.0 / 9.0


print (f"{grados_F} grados F son iguales a {celcius} grados C")



aa()

# Declaracion de Variables
int_farenheit = 0
float_celcius = 0.0
 
# Incio del programa
print("LLEVAR GRADOS FARENHEIT A CELCIUS")
 
# SOLICITUD de Datos 
int_farenheit = int(input('Introduzca los grados Farenheit: '))
 
# FAHRENHEIT A CELCIUS
float_celcius = (int_farenheit-32.0)*5.0/9.0
 
print("Grados Celsius:  %0.2f"%(float_celcius))

aa()

grados_F = float(input("Ingrese los grados Fahrenheit: "))
celcius = (grados_F - 32.0) * 5.0 / 9.0
print(f"{grados_F} grados Fahrenheit son iguales a {celcius:.2f} grados Celsius")



# .: Indica que se especificará el número de decimales.
# 2: Indica que se mostrarán dos dígitos después del punto decimal.
# f: Indica que el valor a formatear es un número de punto flotante (float).