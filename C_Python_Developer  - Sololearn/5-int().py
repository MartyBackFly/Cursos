
from aafuncionimprimir import espacio

x = "55" # x es una cadena de texto
print(type(x))
y = int(x) # y es un entero
print(type(y))

print (x, y)


espacio()



# Convierte el número en un entero
height = int(input("ingresa la data papi ---->")) 
print(type(height))
# La línea anterior es una forma efectiva de combinar 2 instrucciones en una.
# height1 = input()
# height2 = int(height1)

espacio()


# Ejemplos de conversión automática de tipos de datos

x = 5 # entero
y = 2 # entero
z = x/y # flotante (conversión implícita)
print(z)

a = 3 # entero
b = 1.5 # flotante
c = a + b # flotante
print(c)