
from aafuncionimprimir import espacio

age = 75
if age < 18: 
  print("Junior discount")
elif age >= 75: 
  print("Senior discount")
else:
  print("No discount")
print("Proceed to payment")


espacio()


# El nivel de glucosa es una entrada para este software
glucose_level = int(input("cuanta glucosa en sangre tenes ? -->"))

# Mostrar mensaje si el nivel de glucosa es menor a 70
if glucose_level < 70:
  print("Low glucose level")


# Mostrar mensaje si el nivel de glucosa es mayor a 140
elif glucose_level > 140:
  print("High glucose level")

# Mostrar mensaje si no se cumplen ninguna de las condiciones anteriores
else:
  print("Normal range")