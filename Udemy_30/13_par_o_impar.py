from imprimir import espacio as aa


aa()

numero = int(input("numerillo -->"))
 


if numero % 2 == 0 :
    print (f" es par... como peguntas si {numero} es par chaval ")
else :
    print (f" es impar... como peguntas si {numero} es impar chaval ") 



   #####  otra forma ---


    # Declaracion de variables:
int_Numero = 0
 
# Solicitud de Datos
int_Numero = int(input('>>> Introduce un numero: '))
 
if int_Numero == (int_Numero // 2) * 2:
    print(f"El numero {int_Numero} es par.")
else:
    print(f"El numero {int_Numero} es impar.")