from imprimir import espacio as aa


aa()


numero = int(input("numero her -->  "))

a = -1

while a < numero :
    print(numero)
    numero -= 1
    



aa()

numero = int(input("numero her -->  "))

a = -1

while a < numero :
    if numero % 2 == 0 : 
        print(numero)
    numero -= 1



aa()

numero = int(input("numero her -->  "))
print(f'Imprimir los números pares entre {numero} y 0 de forma decreciente')

for pares in range(numero, -1, -1):  # Rango de 50 a 0, decrementando de uno en uno
    if pares % 2 == 0:  # Verifica si el número es par
        print(pares)



