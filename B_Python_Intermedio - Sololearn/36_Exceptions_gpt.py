from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


# ejemplo de chat gpt 


def process_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            # Supongamos que queremos convertir el contenido a un entero
            number = int(data)
            print(f"El número es: {number}")
    except FileNotFoundError as fnf_error:
        print(f"Error: El archivo {filename} no se encontró.")
    except ValueError as val_error:
        print(f"Error: No se pudo convertir el contenido del archivo a un número. Detalles: {val_error}")
    except Exception as general_error:
        print(f"Ocurrió un error inesperado: {general_error}")
    else:
        print("El archivo se procesó correctamente.")

# Llamar a la función con un nombre de archivo
process_file("datos.txt")