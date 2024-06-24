import os

#crear archivo desdepues de escanear y ver cxantidad de archivos 


# Directorio a escanear
directorio = 'B_Python_Intermedio/'

# Obtener una lista de archivos en el directorio
archivos = os.listdir(directorio)

print(len(archivos))

# Filtrar la lista para obtener solo archivos, no directorios
archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(directorio, archivo))]


# Imprimir los nombres de los archivos mientras se filtra la lista
for archivo in archivos:
    print(archivo)
    if os.path.isfile(os.path.join(directorio, archivo)):
        print(f"{archivo} es un archivo.")
    else:
        print(f"{archivo} es un directorio.")

print(len(archivos))

# Determinar el número de índice siguiente
if archivos:
    indices = []
    for archivo in archivos:
        partes = archivo.split('_')
        if len(partes) == 2 and archivo.endswith('.py'):
            try:
                indice = int(partes[0])
                indices.append(indice)
            except ValueError:
                pass
    indice_siguiente = max(indices) + 1 if indices else 1
else:
    indice_siguiente = 1  # Si no hay archivos, el índice siguiente será 1

# Crear el nuevo archivo con el número de índice siguiente
nuevo_archivo = f"{indice_siguiente}_Nuevo_Archivo.py"
with open(os.path.join(directorio, nuevo_archivo), 'w') as archivo:
    archivo.write("from aafuncionimprimir import espacio as aa")

print(f"Se ha creado el archivo {nuevo_archivo} con éxito.")


archivo.close()


# # if archivos:: Esta línea verifica si la lista archivos no está vacía. Si hay al menos un archivo en la lista, se procede a determinar 
# el número de índice siguiente. Si la lista está vacía (no hay archivos), el valor predeterminado para el siguiente índice será 1.

# # indices = []: Aquí se inicializa una lista vacía llamada indices que se utilizará para almacenar los números de índice extraídos de los nombres de los archivos.

# # for archivo in archivos:: Este bucle for itera sobre cada nombre de archivo en la lista archivos.

# # partes = archivo.split('_'): Esta línea divide el nombre del archivo en partes utilizando el carácter _ como separador. Esto es necesario 
# porque el nombre del archivo sigue el formato numero_descripcion.py, por lo que el número de índice está antes del primer _.

# # if len(partes) == 2 and archivo.endswith('.py'):: Esta línea verifica dos condiciones:

# # Si el archivo se divide en exactamente dos partes después de la división (es decir, si hay un número de índice y una descripción).
# # Si el archivo termina con la extensión .py, asegurando que solo se consideren los archivos con esa extensión.
# # try:: Aquí comienza un bloque try-except para manejar cualquier posible error al convertir el número de índice de cadena a entero.

# # indice = int(partes[0]): Esta línea convierte la primera parte del nombre del archivo (el número de índice) de cadena a entero.

# # indices.append(indice): Agrega el número de índice a la lista indices.

# # except ValueError:: Si ocurre un error al convertir el número de índice a entero (por ejemplo, si el número de índice no es un número válido), 
# este bloque except captura la excepción ValueError y lo omite.

# # indice_siguiente = max(indices) + 1 if indices else 1: Después de iterar sobre todos los archivos, se determina el número de índice siguiente. 
# Si la lista indices no está vacía (es decir, hay archivos con números de índice válidos), se toma el máximo número de índice de la lista indices, 
# se le suma 1 y se asigna a la variable indice_siguiente. Si la lista indices está vacía (no hay archivos válidos), el valor predeterminado para 
# el siguiente índice será 1. Esto garantiza que si no hay archivos existentes, el nuevo archivo se nombrará como 1_Nuevo_Archivo.py"






