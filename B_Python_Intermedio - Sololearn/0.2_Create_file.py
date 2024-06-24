import os

def obtener_indice_siguiente(directorio):
    archivos = os.listdir(directorio)
    archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(directorio, archivo))]
    indices = []
    for archivo in archivos:
        partes = archivo.split('_')
        #if len(partes) == 2 and archivo.endswith('.py'):
        try:
                indice = int(partes[0])
                indices.append(indice)
        except ValueError:
                pass
    return max(indices) + 1 if indices else 1

directorio = 'B_Python_Intermedio/'
indice_siguiente = obtener_indice_siguiente(directorio)

nuevo_archivo = f"{indice_siguiente}_N.py"
with open(os.path.join(directorio, nuevo_archivo), 'w') as archivo:
    archivo.write("from aafuncionimprimir import espacio as aa \nfrom aafuncionimprimir import rayita as zz \nfrom aafuncionimprimir import espacio_numero as az")



print(f"Se ha creado el archivo {nuevo_archivo} con éxito.")