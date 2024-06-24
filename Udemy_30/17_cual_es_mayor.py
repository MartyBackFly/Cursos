from imprimir import espacio as aa


aa()

n1 = int(input("N1 = "))
n2 = int(input("N2 = "))
n3 = int(input("N3 = "))


if n1 > n2 and n1 > n3:
    print(f"n1 es amyor {n1}")
elif n2 > n1 and n2 > n3:
    print(f"n2 es mayor {n2}")
elif n3 > n1 and n3 > n2:
    print(f"n3 es mayor {n3}")
elif n1 == n2 and n1 == n3 and n2 == n3:
    print(f"n1 ,n2 y n3 iguales ")
elif n1 == n2 :
    print(f"n1 y n2 son iguales y mayores ")
elif n1 == n3 :
    print(f"n1 y n3 son iguales y mayores")

else :
    print(f"n2 y n3 son iguales y mayores ")



aa()

# # Declaracion de variables
# primer_numero  = 0.0
# segundo_numero = 0.0
# tercer_numero  = 0.0
 
# # Solicitud de datos
# primer_numero  = float(input('Introduce el primer  numero: '))
# segundo_numero = float(input('Introduce el segundo numero: '))
# tercer_numero  = float(input('Introduce el tercer  numero: '))
 
if n1 > n2:
    if n1 > n3:
        maximo = n1
    else:
        maximo = n3
else:
    if n2 > n3:
        maximo = n2
    else:
        maximo = n3
 
print(f'>>> El numero maximo es :', {maximo})

aa()