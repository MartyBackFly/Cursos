file = open("B_Python_Developer/test.txt")
cont = file.read()
print(cont)

file.close()




print("####################################################")


# Para leer sólo una determinada cantidad de un archivo, puedes proporcionar el número de bytes a leer como argumento a la función read .
# Cada caracter ASCII es 1 byte:


file = open("B_Python_Developer/test.txt")
print(file.read(5))
print(file.read(7))
print(file.read())
file.close()

print("####################################################")

file = open("B_Python_Developer/test.txt")
for i in range(12):
    print(file.read(3))
file.close()

print("####################################################")



file = open("B_Python_Developer/test.txt")
#tu código va aquí
N = int(input("cantidad de caracteres a leer "))
cont = file.read()
print(cont[:N]) 

print("####################################################")


file = open("B_Python_Developer/test.txt")
N = int(input("cantidad de lineas a leer "))
cont = file.readlines()                  # Leer todas las líneas del archivo y almacenarlas en una lista
for line in cont[:N]:                 # Iterar sobre las primeras N líneas de la lista
    print(line.strip())              # Imprimir cada línea sin el carácter de nueva línea
file.close()                        # Cerrar el archivo después de usarlo