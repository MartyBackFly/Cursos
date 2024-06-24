from imprimir import espacio as aa


aa()

matriz= [[7,8,9],[4,5,6],[1,2,3]]
print(matriz)


aa()

#FILA 1: [7, 8, 9]
#FILA 2: [4, 5, 6]
#FILA 3: [1, 2, 3]


#print (matriz[0],'\n',matriz[1],'\n',matriz[2])
print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")
aa()
print(matriz[1])
aa()
print(matriz[2][0])
aa()
print("tamaño matriz- filas", len(matriz))
print("tamaño matriz- columna 1--   ", len(matriz[0]))
print("tamaño matriz- columna 2--   ", len(matriz[1]))
print("tamaño matriz- columna 3--   ", len(matriz[2]))
################################################################
aa()


# Declaracion de Variables:
Matriz = []
Longitud = 0
 
# Creacion de la matriz 
Matriz = [[7, 8, 9], [4, 5, 6,], [1, 2, 3]]
 
# Longitud de la Matriz
Longitud = len(Matriz)
 
print(f">>> MATRIZ:  {Matriz}")
aa()
# Se imprime cada fila de la matriz
for fila in range(Longitud):
    print(F">>> FILA :  {fila+1, Matriz[fila]}")
