


try:
  f = open("B_Python_Developer/newfilesita.txt")
  cont = f.read()
  print(cont)
finally:
    f.close()



    with open("B_Python_Developer/books.txt") as f:
        print(f.read())

# El archivo se cierra automáticamente al final de la declaración with, incluso si las excepciones se producen en su interior.