Matriz = []
# Se agregan los elementos a la Matriz

m = int(input("filas-->"))
n = int(input("columnas-->"))


for elemento in range(m):
    Matriz.append ([0] * n)
print(Matriz)




####################################################
# Declaracion de Variables:
Longitud = 0
m_filas = 0
n_columnas = 0
 
######################################################################
 
# Pedimos la dimensión de la matriz:
m_filas    = int(input(">>> Numero de filas (m): "))
n_columnas = int(input(">>> Numero de columnas (n): "))
 
# Se crea la matriz nula
M = []
 
# Se agregan los elementos a la Matriz
for elemento in range(m_filas):
    M.append ([0] * n_columnas)
 
# Longitud de la Matriz
Longitud = len(M)
 
######################################################################
 
print(f"\n>>> MATRIZ M({m_filas}x{n_columnas}): \n\n {M}")
 

print("##############")
# Se imprime cada fila de la matriz
for fila in range(Longitud):
    print(M[fila])