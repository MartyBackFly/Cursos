

numero = int(input("numero her -->  "))

a = 1

while a < 11 :
    print(f"{numero} x {a:2}   = ", (numero * a))
    a += 1


#► Solución 2: Bucle While

# Declaracion de variables
multiplicador = 1
resultado = 0
numero = 0
 
# Solicitud de Datos
numero = int(input('>>> Introduce el numero a multiplicar: '))
 
while multiplicador > 0 and multiplicador < 11:
    resultado = numero * multiplicador
    print("%d x %2d = %d" %(numero,multiplicador,resultado))
    multiplicador = multiplicador + 1


#► Solución : Bucle for in range

# Solicitud de Datos
numero = int(input('>>> Introduce el numero a multiplicar: '))
 
for multiplicador in range(1,11):
    resultado = numero * multiplicador
    print("%d x %2d = %d" % (numero,multiplicador,resultado))
# Solicitud de Datos
numero = int(input('>>> Introduce el numero a multiplicar: '))
 
for multiplicador in range(1,11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador:2} = {resultado}")
    