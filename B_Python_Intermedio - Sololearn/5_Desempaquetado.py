from aafuncionimprimir import espacio as aa


numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)


aa()



x, y = [1, 2]
print(x)
print(y)

x, y = y, x

print(x)
print(y)

aa()


#Una variable que está precedida por un asterisco (*) toma todos los valores de la colección que quedan después de las otras variables.

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)


aa()

def calc(x):
    #your code goes here
    a = 0
    p = 0
    p = x * 4
    a = x * x
    return p, a

side = int(input("Lado -->"))
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))



aa()

# GPT version 

def calc(longitud_lado):
    # Calcula el perímetro sumando los cuatro lados
    perimetro = 4 * longitud_lado
    # Calcula el área elevando al cuadrado la longitud del lado
    area = longitud_lado ** 2
    # Devuelve el perímetro y el área como una tupla
    return perimetro, area

# Solicita al usuario la longitud del lado del cuadrado
longitud_lado = float(input("Ingrese la longitud del lado del cuadrado: "))

# Llama a la función calc() con la longitud del lado como argumento
# Utiliza el desempaquetado de tuplas para obtener el perímetro y el área
perimetro, area = calc(longitud_lado)

# Imprime los resultados
print("Perímetro:", perimetro)
print("Área:", area)




aa()


a, b, c, d, *e, f, g = range(20)
print(len(e))