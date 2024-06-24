from imprimir import espacio as aa


Base = int(input("base del triangleee -- >>"))
Altura = int(input("altura del triangleee -- >>"))


Area = (Base*Altura)/2


print(f"el area del triangulo es  {Area}") 

aa()

# Declaracion de variables
int_Base = 0
int_Altura = 0
float_Area = 0.0
 
# Incio del programa
print("CALCULAR EL AREA DEL TRIANGULO")
 
# Solicitud de datos
int_Base = int(input('Introduzca el valor de la Base: '))
int_Altura = int(input('Introduzca el valor de la Altura:'))
 
# AREA DEL TRIANGULO
float_Area = (int_Base*int_Altura)/2
 
print("El area del triangulo es:  %0.2f"%(float_Area))