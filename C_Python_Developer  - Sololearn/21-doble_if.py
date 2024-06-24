from aafuncionimprimir import espacio


# doble if anidado con indexacion para doble condicion si < 18 y si es estudiante 

age = int(input("how old are you ? ---> "))
is_student = True

if age < 18:
  #se ejecuta si la edad es menor de 18
  if is_student:
    #se ejecuta si es menor de 18 y también es estudiante
    print("20% discount")
  else:
    #se ejecuta si es menor de 18 y no es estudiante
    print("10% discount")
else:
  #se ejecuta este código si el cliente tiene 18 años o más
  print("Regular price")


espacio()

age = 29
if age < 18:
  if is_student:
    print("20% discount")
else:
  print("Regular price")
print("Proceed to payment")