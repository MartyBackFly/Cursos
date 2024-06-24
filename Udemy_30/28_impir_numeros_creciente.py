from imprimir import espacio as aa


aa()


numero = int(input("numero her -->  "))

a = 1

while a < numero+1 :
    print(a)
    a += 1
    



aa()

numero = int(input("numero her -->  "))

a = 1

while a < numero+1 :
    if a % 2 == 0 : 
        print(a)
    a += 1
    


aa()


print('Imprimir los numeros pares entre 0 y 12 de forma Creciente')
aa()
 
for pares in range(0,13):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)





# Solicitud de Datos
numero = int(input('>>> Introduce un numero: '))
 
for pares in range(0,numero + 1):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)