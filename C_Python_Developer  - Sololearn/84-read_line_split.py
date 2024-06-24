msg = 'Harry Potter \nThe Hunger Games \nPride and Prejudice \nGone with the Wind'
file = open("B_Python_Developer/movies.txt", "w")
file.write(msg)
file.close()  # ¡No olvides cerrar el archivo después de escribir en él! si la lectura es sobre el final donde dejarste de escribirlo

with open("B_Python_Developer/movies.txt") as f:
  #tu código va aquí
  cont = f.readlines()
  dd = 0
  print(cont)
for line in cont :
  asd = len(line.split())
  dd += 1 
  print(f"Line {dd}: {asd} words" )

print("_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_# ")

with open("B_Python_Developer/movies.txt") as f:
    cont = f.readlines()
    for index, line in enumerate(cont, start=1):
        asd = len(line.split())
        print(f"Line {index}: {asd} words")