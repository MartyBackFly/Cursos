
#se crea otra lista con los valores seleccionados 

animals =["cat", "dog", "bird", "cow"]
print(animals[1:4])
print("")
print("-----------------------")

animals =["cat", "dog", "bird", "cow"]
print(animals[1:3])

print("")
print("-----------------------")
#El rebanado también funciona con cadenas de texto.

#Completa el código para imprimir la palabra "air".

vehicle = "airplane"
print(vehicle[0:3])

print("")
print("-----------------------")


vehicle = "airplane"
print(vehicle[3:8])


print("")
print("-----------------------")


animals = ["cad", "tiger", "monkey"]
animal = list(animals[0])
animal[2] = "t"
animal = "".join(animal)
print(animal)
print(animals)
animals[0]= animal 
print(animals)
print("")


print("-----------------------")

players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

# Crear 3 listas con 2 jugadores cada una
# Usar el rebanado para crear una lista para el Group 1
g1 = players[0:2]

# Usar el rebanado para crear una lista para el Group 2
g2 = players[2:4]

# Usar el rebanado para crear una lista para el Group 3
g3 = players[4:6]

print("Group 1:")
# Mostrar el primer grupo
print(g1)
print("")


print("Group 2:")
# Mostrar el segundo grupo
print(g2)
print("")


print("Group 3:")
# Mostrar el tercer grupo
print(g3)
