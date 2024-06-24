# Para recuperar cada línea de un archivo, puedes utilizar el método readlines() para devolver una lista en la que cada elemento es una línea del archivo.

# Por ejemplo:
file = open("C_Python_Developer/test.txt")

for line in file.readlines():
    print(line)
    
file.close()

print(len(line))


# Haz clic para ejecutar
# Si no necesitas la lista para cada línea, puede simplemente iterar sobre la variable file:
print("------------------------------------------------------------------")



file = open("C_Python_Developer/test.txt")

for line in file:
    print(line)
    
file.close()


# Haz clic para ejecutar
# En la salida, las líneas están separadas por líneas en blanco, ya que la función print añade automáticamente una nueva línea al final de su salida.
# y no carga toda la informacion en memoria 