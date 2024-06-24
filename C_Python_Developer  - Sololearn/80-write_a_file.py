file = open("C_Python_Developer/newfile.txt", "w")
file.write("This has been written to a file")
file.close()


# En caso de que el archivo ya exista, todo su contenido será reemplazado cuando lo abra en modo de escritura usando "w".


try:
    with open("test.txt") as f:
        print(f.read())
except:
    print("Error")
