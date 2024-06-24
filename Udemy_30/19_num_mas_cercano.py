


#numero mas cercano al 1ro

 
# Solicitud de datos
n1  = float(input('Introduce el Primer  numero: '))
n2 = float(input('Introduce el Segundo numero: '))
n3  = float(input('Introduce el Tercer  numero: '))
n4  = float(input('Introduce el Cuarto  numero: '))
n5  = float(input('Introduce el Quinto  numero: '))


resta1 = n1 - n2
resta2 = n1 - n3
resta3 = n1 - n4
resta4 = n1 - n5

16
menor_diferencia = resta1
 
if resta2 < menor_diferencia and resta2 >= 0:
   menor_diferencia = resta2
else:
    if resta2 > menor_diferencia and resta2 <= 0:
        menor_diferencia = resta2
 
if resta3 < menor_diferencia and resta3 >= 0:
   menor_diferencia = resta3
else:
    if resta3 > menor_diferencia and resta3 <= 0:
        menor_diferencia = resta3
 
if resta4 < menor_diferencia and resta4 >= 0:
   menor_diferencia = resta4
else:
    if resta4 > menor_diferencia and resta4 <= 0:
        menor_diferencia = resta4
 
numero_cercano = n1 - menor_diferencia
 
print(f'El numero mas cercano a { n1} es {numero_cercano}')



print("--------------------")


# Solicitud de datos
n1 = float(input('Introduce el Primer número: '))
n2 = float(input('Introduce el Segundo número: '))
n3 = float(input('Introduce el Tercer número: '))
n4 = float(input('Introduce el Cuarto número: '))
n5 = float(input('Introduce el Quinto número: '))

# Calcular las diferencias
diferencias = [abs(n1 - n) for n in [n2, n3, n4, n5]]

# Encontrar la diferencia mínima
menor_diferencia = min(diferencias)

# Encontrar el número más cercano
numero_cercano = n1 - diferencias[diferencias.index(menor_diferencia)]

print(f'El número más cercano a {n1} es {numero_cercano}')



