from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


name = str(input("cual es tu nombre "))

while len(name) < 3:
    print("¡Error de ingreso!")
    name = input("Ingrese el nombre nuevamente: ")

print(f"no era tan dificl {name}")
 