from aafuncionimprimir import espacio

# Tomar los pasos y los minutos como entradas
steps = int(input("Steps -->"))
active_minutes = int(input("active_minutes -->"))

# Almacenar el resultado de las operaciones en la variable
goal_achieved = ((steps > 10000) or (active_minutes > 30))

# Mostrar el resultado en la pantalla

print("goal achieved ---> ", goal_achieved)


if goal_achieved == True:
    print("buena gordito ")
else:
    print("tenes que mover mas el orto inmundo animal")

espacio()