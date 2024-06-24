def numeros_pares(maximo):
    pares = []
    for num in range(maximo + 1):
        if num % 2 == 0:
            pares.append(num)
    return pares

# Obtener la lista de números pares hasta el número 10
pares_hasta_10 = numeros_pares(10)

# Imprimir la lista de números pares
print(pares_hasta_10)

# Salida: [0, 2, 4, 6, 8, 10]

print("----------------------------------------------------------------")

def numeros_pares(maximo):
    for num in range(maximo + 1):
        if num % 2 == 0:
            yield num

# Crear un generador de números pares hasta el número 10
generador_pares = numeros_pares(10)

# Iterar sobre el generador para obtener los números pares
for numero in generador_pares:
    print(numero)

# Salida:
# 0
# 2
# 4
# 6
# 8
# 10
