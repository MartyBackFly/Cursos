from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

# # Ejercicio 10

# # Armar una frase con las 3 variables dadas y
# # mostrarla por pantalla.
# # Es obligatorio usar las 3 variables, pero también
# # podés agregar palabras vos para generar una
# # frase. No importa el orden que elijas para las
# # variables.


import random
import string


palabras = []

num = int(input("ingresa un numero --> : "))
for i in range (num):
    palabras.append(input("palabra : "))
print(palabras)

frase_random = []
for _ in range(num):
    p_elegida = random.choice(palabras)
    
    frase_random.append(p_elegida)
    
    palabras.remove(p_elegida)
    
print(frase_random)




