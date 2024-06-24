import re
import os


# mi ruta  inicial 
# C:\Users\fedeh\Desktop\channel\90052.txt

# abre archivo en ruta pedida por consola y itera abriendo archivos y cambiendo el nombre por el contenido numerico del anterior 
# hasta llegar al ultimo y mostra su contenido "collect the comments"
# junta los numeros  en una concatenacion
# junta los comentarios en una concatenacion e imprime uno debajo del otro 


def abrir_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            numeros = re.findall(r'\d+', contenido)
            numeros_texto = ''.join(numeros)
            print(f"Números encontrados en '{ruta_archivo}': {numeros_texto}")
            return numeros_texto, contenido  # Modificado para devolver el contenido completo del archivo
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{ruta_archivo}'.")
        return None, None  # Modificado para devolver None también para el contenido

def main():
    ruta_base = r"C:\Users\fedeh\Desktop\channel"
    ruta_archivo_inicial = input("Ingrese la ruta del archivo inicial que desea abrir: ")
    ruta_archivo_actual = ruta_archivo_inicial
    ultimo_contenido = None  # Variable para almacenar el contenido del último archivo
    todos_numeros = ''  # Variable para almacenar todos los números encontrados
    todo_contenido = ''  # Variable para almacenar el contenido de todos los archivos

    while ruta_archivo_actual:
        numeros_texto, contenido = abrir_archivo(ruta_archivo_actual)
        if numeros_texto is not None:
            # Generar la ruta del siguiente archivo automáticamente
            ruta_archivo_actual = os.path.join(ruta_base, f"{numeros_texto}.txt")
            todos_numeros += numeros_texto  # Concatena los números encontrados
            todo_contenido += contenido + '\n'  # Concatena el contenido del archivo y agrega un salto de línea
            ultimo_contenido = contenido  # Almacena el contenido del último archivo abierto
        else:
            print("No hay más archivos.")
            break

    # Imprimir el contenido del último archivo abierto
    if ultimo_contenido:
        print("\nContenido del último archivo:")
        print(ultimo_contenido)

    # Imprimir todos los números encontrados
    print("\nTodos los números encontrados:")
    print(todos_numeros)

    # Imprimir el contenido de todos los archivos con un salto de línea entre cada archivo
    print("\nContenido de todos los archivos:")
    print(todo_contenido.strip())  # Se imprime sin el último salto de línea

if __name__ == "__main__":
    main()
