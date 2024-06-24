
# esto nos crea un archivo python en la ruta, con el nombre y extencion dados y escribe la linea para tener importada la funcion para hacer  espacios


file = open("B_Python_Intermedio/NewFile.py", "w")
file.write("from aafuncionimprimir import espacio as aa")
file.close()


# En caso de que el archivo ya exista, todo su contenido será reemplazado cuando lo abra en modo de escritura usando "w".


try:
    with open("NewFile.py") as f:
        print(f.read())
except:
    print("Error")