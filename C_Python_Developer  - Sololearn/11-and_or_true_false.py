from aafuncionimprimir import espacio

print(True and False)
print(False and True)
print(False and False)
print(True and True)


espacio()


print(True or False)
print(False or True)
print(False or False)
print(True or True)

espacio()


heart_rate = 165
peak_rate = heart_rate > 160
print(peak_rate)


espacio()



#almacena un boleano en una variable 


a = True 

b = False

c = a or b 
d = a and b

print(c)
print(d)


espacio()


light_on = True
door_locked = False
print("light_on or door_locked")
print(light_on or door_locked)

espacio()

print("light_on and door_locked")
print(light_on and door_locked)

espacio()

# que se ejecute primero el parentesis 

lala = (3 > 2) or False

print(lala)

espacio()
