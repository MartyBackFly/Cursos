from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

# Ejercicio 12

# Lista de nombres
# Se tiene la siguiente lista de nombres:
nombres = ["Susana","Alejandro","Roberto"]

# Insertar entre Alejandro y Roberto a Paula. Y luego

# agregar al final a Silvina.

# Para finalizar, hay que recorrer la lista y mostrar a
# todos los nombres por pantalla.

nombres.append("Silvina")
nombres.insert(2,"Paula")


for i in nombres :
    print(i)



aa()

nombres = ["Susana","Alejandro","Roberto"]
nombres.insert(2,"Paula")
nombres.append("Silvina")
indice = 0
while indice < len(nombres):
    print(nombres[indice])
    indice = indice + 1