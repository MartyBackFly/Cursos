from aafuncionimprimir import espacio



seats = 15 # número inicial de asientos
while seats > 0: # ¿hay asientos disponibles?
  
  print( "Sell ticket") # boleto vendido
  print("")
  
  print(seats, "antes de descontar") # número de asientos antes de descontar en el bucle como ejemplo
  print("")
  seats = seats - 1 # número de asientos actualizado y descontado en cada vuelta del bucle como ejemplo
  
  print(seats, "luego de descontar ")
  print("")


# sin el contador de asientos tendriamos un bucle infinito por que la condicion siempre va a ser verdadera 


espacio()


counter = 0
while counter < 4:
  print(counter)
  counter = counter + 1


espacio()



  # Toma el número como entrada
number = int(input("number here ---> "))

# Usa un bucle while para la cuenta regresiva

while number > -1:
    print (number)
    number = number - 1

espacio()



password = "SecretWord"
guess = input()
while guess != password:  
  guess = input() 
print("Access Granted")



espacio()