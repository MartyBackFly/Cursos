from aafuncionimprimir import espacio

#multiplica 
nums = [i*2 for i in range(10)]
print(nums)

espacio() 

# eleva al cubo 

cubes = [i**3 for i in range(5)]

print(cubes)

espacio() 

evens=[i**2 for i in range(10) ]
print(evens)


# mismo pero con condicion 

evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)

#  if i**2 % 2 == 0:       

#Esta es una condición que verifica si el cuadrado de i es par. 
#Si es par (el residuo de la división por 2 es igual a 0), se incluye en la lista resultante.

espacio() 


#mismo pero con inpares 


evens=[i**2 for i in range(10) if i**2 % 2 != 0]

print(evens)

espacio()


#sin condicion 

a = [ i for i in range(20) ]
print ("sin condicion --> " + str(a))

#con condicion 

a = [ i for i in range(20) if i%3==0 ]
print ("con condicion --> " + str(a))


espacio()




#ejempo de string en print 

a = [ i for i in range(20) if i%3==0 ]
print(f' manera de convertir a string --> {a}')


espacio()

