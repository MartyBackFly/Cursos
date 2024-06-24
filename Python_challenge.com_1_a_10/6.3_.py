import re
import os

# mi ruta  inicial 
# C:\Users\fedeh\Desktop\channel\90052.txt


import re
import os

def abrir_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            numeros = re.findall(r'\d+', contenido)
            numeros_texto = ''.join(numeros)
            print(f"Números encontrados en '{ruta_archivo}': {numeros_texto}")
            return numeros_texto
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{ruta_archivo}'.")
        return None

def main():
    ruta_base = r"C:\Users\fedeh\Desktop\channel"
    ruta_archivo_inicial = input("Ingrese la ruta del archivo inicial que desea abrir: ")
    ruta_archivo_actual = ruta_archivo_inicial

    while ruta_archivo_actual:
        numeros_texto = abrir_archivo(ruta_archivo_actual)
        if numeros_texto is not None:
            # Generar la ruta del siguiente archivo automáticamente
            ruta_archivo_actual = os.path.join(ruta_base, f"{numeros_texto}.txt")
        else :
            print("no hay mas archivitos")
            break




if __name__ == "__main__":
    main()
