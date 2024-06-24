

#Toma el nombre como entrada
name = input("text here !")

#Utiliza la concatenación para unir 2 cadenas
message = "Nice to meet you, " + name

#Muestra el mensaje al usuario
print (message)


#---------------------- 


city = "Berlin" #stores a string
age = 42 #stores an integer
balance = 830.29 #stores a float
print(type(city)) #outputs <class 'str'>
print(type(age)) #outputs <class 'int'>
print(type(balance)) #outputs <class 'float'>



#------------------------- 


birth_year = input("how old are you ? --->")
print(type(birth_year))

#por mas que pida numero es un string 
# -- imput() -- convierte el dato a string 

x = "55" # x es una cadena de texto
print(type(x))
y = int(x) # y es un entero
print(type(y))
 


# Convierte el número en un entero
height = int(input("altura")) 
print(type(height))
# La línea anterior es una forma efectiva de combinar 2 instrucciones en una.
    
height1 = input("height1")
    
height2 = int(height1)

print(height1, type(height1))
print(height2, type (height2))

# arriba pasamos el str a int 


age = int(input("En la misma linea ya pide el dato edad y lo conviete a INT ---> "))

print("age", age, type(age))




# Ejemplos de conversión automática de tipos de datos

x = 5 # entero
y = 2 # entero
z = x/y # flotante (conversión implícita)
print(z)

a = 3 # entero
b = 1.5 # flotante
c = a + b # flotante
print(c)

# 🌟 puedes cambiar el tipo de dato de un valor con int(), float() y str()

# 🌟 existen conversiones de tipo de dato implícitas y explícitas en Python

# 🌟 las instrucciones str(), int() y float() son conversiones explícitas


print(30 < 25)
print(5 < 9)
print(50 > 100)


print(type(5 < 9))
print(type(50 > 100))
print(type(True))
print(type(False))


# El programa toma la puntuación como entrada
score = int(input("ingrese lvl --->"))

# Agrega la operación de comparación dentro de los paréntesis
print("paso de lvl ", score > 100)


print(True and False)
print(False and True)
print(True or False)
print(False or True)


light_on =True
door_locked = False
print("la luz esta prendida ?", light_on or door_locked)
print("la cerradura o luz estan ON ", light_on and door_locked)


# Tomar los pasos y los minutos como entradas
steps = int(input("pasos"))
active_minutes = int(input("tiempo activo"))

# Almacenar el resultado de las operaciones en la variable
goal_achieved = (steps > 10000 or active_minutes > 30)

# Mostrar el resultado en la pantalla

print (goal_achieved)