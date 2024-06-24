from imprimir import espacio as aa


aa()

numero = int(input("numero her -->  "))

a = 1

while a < 11 :
    print(f"{numero} ^ {a:2}   = ", (numero ** a))
    a += 1


aa()

#► Solución 2: Bucle While

# Declaracion de variables
multiplicador = 1
resultado = 0
numero = 0
 
# Solicitud de Datos
numero = int(input('>>> Introduce el numero a potenciar: '))
 
while multiplicador > 0 and multiplicador < 11:
    resultado = numero ** multiplicador
    print("%d ^ %2d = %d" %(numero,multiplicador,resultado))
    multiplicador = multiplicador + 1


aa()


#► Solución : Bucle for in range

# Solicitud de Datos
numero = int(input('>>> Introduce el numero a potenciar: '))
potencia= int(input('>>> Introduce potenciar: '))
 
for multiplicador in range(1,potencia+1):
    resultado = numero ** multiplicador
    print("%d ^ %2d = %d" % (numero,multiplicador,resultado))
# Solicitud de Datos
numero = int(input('>>> Introduce el numero a  potenciar: '))
 
for multiplicador in range(1,11):
    resultado = numero ** multiplicador
    print(f"{numero} ^ {multiplicador:2} = {resultado}")
    