from aafuncionimprimir import espacio

numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)


# Esto también se puede utilizar para intercambiar variables haciendo a, b = b, a , ya
#  que b, a en el lado derecho forma la tupla (b, a) que luego es desempaquetado.

espacio()

# Una variable precedida de un asterisco (*) toma todos los valores de la colección que sobran de las otras variables.

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)


espacio()


#¿Que generará este código?

a, b, c, d, *e, f, g = range(20)


print(len(e))
print(",.,.,.,.,.,.,.")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


espacio()


a, b, c, d, *e, f, g = range(10)
print(len(e))
print(",.,.,.,.,.,.,.")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)








