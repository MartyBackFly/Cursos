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
#choice = int(input("Elije tu juego --->")) # Comenté esta línea ya que se sobrescribía en la siguiente línea
choice = int(input("Elije tu juego (ingresa el numero correspondiente) --->"))
#choice = input("Elije tu juego --->") # Esta línea no es necesaria
# Mostrar el juego correspondiente

# Asegúrate de que el índice esté en el rango válido
if 0 <= choice < len(games):
    print("Has elegido:", games[choice])
else:
    print("La opción ingresada no es válida. Por favor, elige un número entre 0 y", len(games) - 1)
