# mi ruta 
# C:\Users\fedeh\Desktop\channel\90052.txt
import re

def abrir_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(f"Contenido de '{ruta_archivo}':\n{contenido}")

            # Usamos una expresión regular para encontrar todos los números en el contenido del archivo
            numeros = re.findall(r'\d+', contenido)
            print("Números encontrados:", numeros)

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{ruta_archivo}'.")

def main():
    ruta_archivo = input("Ingrese la ruta del archivo que desea abrir: ")
    abrir_archivo(ruta_archivo)

if __name__ == "__main__":
    main()

