

age = int(input("edad para ver descuento -->"))

if age < 18: 
  print("Junior discount")
elif age >= 75: 
  print("Senior discount")
else:
  print("No discount")


  #Al igual que con cualquier otra declaración 
  # condicional, elif requiere el símbolo de dos puntos : 
  # y que el código que se ejecuta debajo esté indentado.


print("----------------------")

#Puedes anidar declaraciones if-else dentro de otras.


age = 16
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


print("----------------------")

age = int(input("coloque su edad aqui --- > "))
is_student = eval(input("coloque True or False --->"))
if age < 18:
 if is_student:
     print("20% discount")
 else:
     print("10% discount")
else:
  print ("regular price")      


  # Python en el caso de is_student = bool(input("coloque True or False --->")) recibira True con cualquier cadena de texto 
  # ingresada y false si no se completa el campo... por eso usamos "eval"  is_student = eval(input("coloque True or False --->"))



#🌟 omitir la declaración else cuando no es necesaria

#🌟 verificar más condiciones con la declaración elif

#🌟 anidar declaraciones if-else dentro de otras