from imprimir import espacio as aa


aa()

# matriz  4 x 4 

matriz = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]

print(matriz)

aa()


print(matriz[3])

aa()

print(matriz[3][0])


################################################################
aa()




# Declaracion de Variables:
Matriz = []
Fila = 3
Columna = 0
 
# Creacion de la matriz del teclado Matricial 4x4
Matriz = [['1', '2', '3', 'A'],
          ['4', '5', '6', 'B'],
          ['7', '8', '9', 'C'],
          ['*', '0', '#', 'D']]
 
# Se imprime la matriz en pantalla
print(">>> IMPRIMIR MATRIZ  : %s" %(Matriz))
print(">>> FILA A IMPRIMIR  : %s" %(Matriz[Fila]))
print(">>> DATO A IMPRIMIR  : %s" %(Matriz[Fila][Columna]))