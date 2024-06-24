
from aafuncionimprimir import espacio


print("happy birthday".upper())
print("happy birthday".lower())
print("happy birthday".capitalize())



espacio()



#cadenas inmutables, hay que almacenar en variable para concervar el valor 


item = "smartwatch"
print(item.upper())
print(item) #cadena original
item2 = item.upper()
print(item2)


espacio()

#La función find() verifica si un carácter (o un patrón de caracteres) está presente en una cadena. 
#La función devuelve el índice (posición) del valor dado. 
#Si el valor dado está presente varias veces, la función devolverá la primera aparición (el índice más bajo).


print("Bee".find("e"))

print("robot".find("o"))

print("robot".find("t"))

espacio()



print('roBot'.upper())
print('roBot'.lower())
print('roBot'.capitalize())
#print('roBot'.find())    # error si no tiene valor (indice ) el find 

espacio()


# si no esta el valor va a devolver -1 

print("robot".find("A"))

espacio()


# ejercise 

text = input("ingresa tu tessssto en minuscula que lo mayusculizamos gratis --- >>>")

#convertir a mayúsculas

textup = text.upper()

#mostrar en la pantalla

print( )

print(textup)


espacio() 










