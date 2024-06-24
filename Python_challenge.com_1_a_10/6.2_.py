import re
import os

# mi ruta  inicial 
# C:\Users\fedeh\Desktop\channel\90052.txt



def abrir_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            # Usamos una expresión regular para encontrar todos los números en el archivo
            numeros = re.findall(r'\d+', contenido)
            # Convertimos los números encontrados a enteros
            numeros_enteros = [int(num) for num in numeros]
            print(f"Números encontrados en '{ruta_archivo}': {numeros_enteros}")
            return numeros_enteros
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{ruta_archivo}'.")
        return None

def abrir_archivos_con_numeros(numeros):
    if numeros:
        for num in numeros:
            nombre_archivo = (f"C:/Users/fedeh/Desktop/channel/{num}.txt")
            if os.path.isfile(nombre_archivo):
                print(f"Contenido de '{nombre_archivo}':")
                with open(nombre_archivo, 'r') as archivo:
                    contenido = archivo.read()
                    print(contenido)
            else:
                print(f"No se encontró el archivo '{nombre_archivo}'.")

def main():
    ruta_archivo_inicial = input("Ingrese la ruta del archivo inicial que desea abrir: ")
    ruta_archivo_actual = ruta_archivo_inicial

    while ruta_archivo_actual:
        numeros = abrir_archivo(ruta_archivo_actual)
        abrir_archivos_con_numeros(numeros)
        
        # Pedimos al usuario el nombre del siguiente archivo a abrir
        ruta_archivo_siguiente = input("Ingrese la ruta del siguiente archivo que desea abrir (o presione Enter para salir): ")
        
        # Si no se proporciona una ruta, salimos del bucle
        if not ruta_archivo_siguiente:
            break
        
        # Actualizamos la ruta del archivo actual para la próxima iteración
        ruta_archivo_actual = ruta_archivo_siguiente

if __name__ == "__main__":
    main()