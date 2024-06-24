
print("---------------------------------------------")

# Declaracion de variables:
int_Numero = 0
 
# Solicitud de Datos 
int_Numero = int(input('>>> Introduce un numero: '))

result = int(int_Numero / 3)
 
if int_Numero == (int_Numero // 3) * 3:
    print("El numero %d es multiplo de 3." %(int_Numero))
    print("---------------------------------------------")
    print (f"y si lo dividimos obtenemos { int_Numero }/3  =  {result}")
    print("---------------------------------------------")
else:
    print("El numero %d no es multiplo de 3." %(int_Numero))
    