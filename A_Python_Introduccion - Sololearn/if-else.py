

age = int(input("how old are you ? --->"))

if (age >= 18):
  print("Regular price")
else:
  print("Discount")



print("---------------------")


age = 30
if age >= 18:
  print("Regular price")
else:
  print("Discount")
print("Proceed to payment")


print("---------------------")

age = 32
is_student = False
if age < 18 or is_student:
  print("Discount")
else: 
  print("Regular price for false student and 32 years old ")


print("---------------------")


  # Tomar el número de espacios disponibles como entrada
spaces = int(input("pone cuantos espacios queda en el estacionamiento como entrada "))

# Mostrar mensaje si hay espacios disponibles
if spaces > 0 :
  print("Available spaces")
else:

# Mostrar un mensaje diferente si no hay espacios disponibles

  print("Sorry, the parking lot is full")

print("---------------------")

# if sin else 

age = 16
if age < 18:
  print("Apply Discount")
print("Proceed to payment")


print("---------------------")

# if todo en la misma linea 
age = 16
if age < 18: print("Apply Discount")
print("Proceed to Payment")