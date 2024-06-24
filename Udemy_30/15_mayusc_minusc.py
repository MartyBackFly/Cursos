from imprimir import espacio as aa

aa()

# Declaracion de variables
letra = ''
 
# Solicitud de Datos
letra = input('>>> Introduce una letra: ')
 
if letra <= 'z'  and letra >= 'a':  # a-z (97-122)
    print('La letra es minuscula.')
 
elif letra <= 'Z' and letra >= 'A':  # A-Z (65-90)
    print('La letra es Mayuscula.')
else:
    print('El valor introducido no es una letra.')


aa()


if 'a' < 'b':
    print("a es menor que b")
else:
    print("a no es menor que b")



if 'c' < 'b':
    print("c es menor que b")
else:
    print("c no es menor que b")

print ('a' == 97 )



aa()


print (ord("a") == 97 )


cadena = (" - zarasa - @ - \" \ ")
for letra in cadena:
    valor_ascii = ord(letra)
    print(f"El valor ASCII de '{letra}' es: {valor_ascii}")


