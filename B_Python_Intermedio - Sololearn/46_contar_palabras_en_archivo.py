from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

aa()


with open("B_Python_Intermedio/books.txt") as f:
   #your code goes here
   cont = f.readlines()          
   print (cont )   # ejemplo para mostrar que  hay en variable count 
   lala = 0        # variale para sumar lineas -- las dos primeras estan vacias , arranca contando de la 3 como primera 
   
for lineaaa in cont:
      lala+=1
      numero_espacios = lineaaa.count(' ') + 1            # variable que cuenta espacios , se le suma uno para que cuente la ultima palabra que no tiene espacio 
      print(f"Line {lala}: {numero_espacios} words")