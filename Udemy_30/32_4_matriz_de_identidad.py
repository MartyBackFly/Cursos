# Pedimos la dimensión de la matriz,
dimension = int(input("Dimension de la matriz: "))
 
# Creamos una matriz nula...
Matriz = []
 
for elemento in range(dimension):
    Matriz.append ([0] * dimension)
 
# ... y leemos su contenido
for fila in range(dimension):
    for columna in range(dimension):
        # Si el numero de fila y columna es igual
        if fila == columna:
        # Guarda el número 1 en la posición
            Matriz[fila][columna] = 1

print(Matriz)


#########################################################

# Declaracion de Variables:
M = []
longitud = 0
dimension = 0
 
######################################################################
 
# Pedimos la dimensión de la matriz,
dimension = int(input(">>> Dimension de la matriz de tamaño n x n: "))
 
# Creamos una matriz nula...
for elemento in range(dimension):
        M.append ([0] * dimension)
 
# ... y leemos su contenido
for fila in range(dimension):
    for columna in range(dimension):
        # Si el numero de fila y columna es igual
        if fila == columna:
             # Guarda el número 1 en la posición
             M[fila][columna] = 1
 
######################################################################
 
print(f"\n>>> MATRIZ M({dimension}x{dimension}): {M}\n")
 
longitud = len(M)
long_cel = len(M[0])
print(f"longitud matriz {longitud}" )
print(f"longitud celdas matriz {long_cel}" )
print("  ")

print(M[longitud-1])
print("---------")

# Se imprime cada fila de la matriz
for i in range(longitud):
    print(M[i])