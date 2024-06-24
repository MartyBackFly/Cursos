shopping_cart = [
  "laptop", 
  "smartphone", 
  "headphones", 
  "backpack"
]
print(shopping_cart)

print("----------------")

# acceder a valores de la lista 

last_calls = ["Mom", "Dave", "Lawyer"]
print(last_calls[0])
print(last_calls[1])


print("----------------")


# cambiar valores de la lista 

nums = [8, 6, 19]
print(nums)
nums[0] = 1
nums[1] = 2
nums[2] = 3
print(nums)


print("----------------")


# Juegos instalados
games = [
  'Soccer', 
  'Tic Tac Toe', 
  'Snake',
  'Puzzle', 
  'Rally']

# Tomar la elección del jugador como un número de entrada

print(games)
print("Loading ... ")
choice = int(input("Elije tu juego --->"))

# Mostrar el juego correspondiente

print(games[choice])



print("----------------")




# ejemplo para no elegir una opcion no valida ..... 
# Tomar la elección del jugador como un número de entrada

print(games)
print("Loading ... ")
choice = int(input("Elije tu juego --->"))

# Mostrar el juego correspondiente

# Asegúrate de que el índice esté en el rango válido
if 0 <= choice < len(games):
    print("Has elegido:", games[choice])
else:
    print("La opción ingresada no es válida. Por favor, elige un número entre 0 y", len(games) - 1)