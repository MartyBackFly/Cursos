
from aafuncionimprimir import espacio



shopping_cart = [
  "laptop", 
  "smartphone", 
  "headphones", 
  "backpack"
]
print(shopping_cart)


espacio()


last_calls = ["Mom", "Dave", "Lawyer"]
print(last_calls[0])
print(last_calls[1])



espacio()

#las listas son mutables 


nums = [8, 6, 19]
nums[0] = 1
nums[1] = 2
nums[2] = 3
print(nums)


espacio()


words = ["rise", "sun", "glasses"]
print(words[1] + words[0])


espacio()


#ejercicio de juegos 

# Juegos instalados

games = [
  'Soccer', 'Tic Tac Toe', 'Snake',
  'Puzzle', 'Rally']

# Tomar la elección del jugador como un número de entrada
choice = int(input("que juego queres elegir novato ? 0,1,2,3 o 4 ---->"))

# Mostrar el juego correspondiente

print (games[choice])


espacio()


#lista con valores de unas variables 

name = "Sarah"
age = 34
country = "Germany"
info = [name, age, country]
print(info[0])
print(info[1])
print(info[2])


espacio()


# indexacion funciona con cadena de texto 

animal = "Dog"
print(animal[0])
print(animal[1])
print(animal[2])


espacio()


x = "arctic"
print(x[2] + x[0] + x[3])

espacio()

















