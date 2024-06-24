from imprimir import espacio as aa

aa() 

def my_func(f, arg):
  return f(arg)

print(my_func(lambda x: 2*x*x, 5))

aa()


# my_func es una función que toma dos argumentos: f (una función) y arg (un argumento para esa función).
# La función my_func devuelve el resultado de llamar a la función f con el argumento arg.
# Uso de my_func con una función lambda:

# python
# Copy code
# print(my_func(lambda x: 2*x*x, 5))
# Aquí, my_func se utiliza con una función lambda como primer argumento (f) y 5 como segundo argumento (arg).
# La función lambda define una función anónima que toma un argumento x y devuelve 2*x*x.
# Entonces, my_func(lambda x: 2*x*x, 5) se traduce en lambda x: 2*x*x(5), que evalúa la función lambda con x igual a 5.
# El resultado es 2 * 5 * 5, que es 50.
# Imprimir el resultado:

# La función print() se utiliza para imprimir el resultado de my_func(lambda x: 2*x*x, 5), que es 50.
# En resumen, el código define una función llamada my_func que toma una función y un argumento, y 
# luego la llama con ese argumento. Luego, se utiliza my_func con una función lambda que 
# calcula el doble del cuadrado del número y el argumento 5. Finalmente, el resultado (50) se 
# imprime en la consola.


#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))


#  valor de x en -4 

#  x**2  x y la cantidad de veces que se multiplica por si misma -4*-4 = 16 
#  x**3    -4*-4*-4 = -64 

# 5*x = -20

# x : 16 + (-20) +4 

