from imprimir import espacio as aa


aa()

numero = int(input("numero her -->  "))
print(f'Imprimir los números pares entre {numero} y 0 de forma decreciente')

for pares in range(numero, -1, -1):  # Rango de 50 a 0, decrementando de uno en uno
    if pares % 2 == 0:  # Verifica si el número es par
        print(pares)


# la función range() acepta hasta tres parámetros: inicio, fin y paso.

# Si solo proporcionas un parámetro, range(fin), el inicio se asume como 0 y el paso como 1.
# Si proporcionas dos parámetros, range(inicio, fin), el paso se asume como 1.
# Si proporcionas tres parámetros, range(inicio, fin, paso), especificas el valor del paso.
# Entonces, para sumar, solo necesitas proporcionar el valor final al que quieres llegar. Pero si quieres restar, necesitas especificar el paso como -1 para que vaya en reversa.

# Por ejemplo:

# Sumar de 0 a 60: range(0, 61)
# Restar de 60 a 0: range(60, -1, -1)
        
        # Solicitud de Datos
numero = int(input('>>> Introduce un numero: '))
 
for pares in range(0,numero + 1):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)


        
aa()
 
for pares in range(0,13):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)