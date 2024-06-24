from aafuncionimprimir import espacio


#tomar el peso como entrada
weight = int(input("Weight "))

#completar la función
def shipping_cost(weight):
    valor = weight*5
    print (valor)
    return valor
    
   
#llamar a la función

shipping_cost(weight)
#siempre que llame a la función va a imprimir por que print esta dentro de ella 
espacio()


#  OTRO EJEMPLO ----------------------------------------------------------------


# Tomar el peso como entrada
weight = int(input("Weight "))
# Completar la función
def shipping_cost(weight):
    valor = weight * 5
    return valor

# Llamar a la función y almacenar el resultado en una variable
costo_envio = shipping_cost(weight)

# Imprimir el resultado
print(costo_envio)


espacio()

#  OTRO EJEMPLO ----------------------------------------------------------------


# Tomar el peso como entrada
weight = int(input("Weight "))

# Definir la función para calcular el costo de envío
def shipping_cost(weight):
    costo_envio = weight * 5
    return costo_envio

# Llamar a la función y almacenar el resultado en una variable
valor = shipping_cost(weight)

# Imprimir el resultado
print("shippig cost", valor)

    

""" 
    
El return en una función en Python se utiliza para devolver un valor desde la función al lugar desde 
donde fue llamada. Cuando defines una función con return, estás especificando qué valor debe ser enviado 
de vuelta al código que hizo la llamada a la función.

En el caso específico de tu función shipping_cost:

python
Copy code
def shipping_cost(weight):
    costo_envio = weight * 5
    return costo_envio
La línea return costo_envio está indicando que el valor que se encuentra en la variable 
costo_envio (que es el resultado del cálculo del costo de envío) se devolverá a la ubicación
 desde donde se llamó la función.

Cuando llamas a la función aquí:

python
Copy code
valor = shipping_cost(weight)
Estás asignando el valor devuelto por la función a la variable valor. Entonces, valor contendrá 
el resultado del cálculo del costo de envío. Esto te permite utilizar o imprimir ese valor más 
adelante en tu código.

En resumen, return se utiliza para enviar un valor de vuelta a la parte del programa que hizo la 
llamada a la función. Sin return, la función simplemente se ejecutaría y no proporcionaría un 
resultado utilizable desde el exterior.




User
pero no importa que tengan nombre diferentes ? 
ChatGPT
No, no importa que los nombres de las variables dentro de la función y las variables fuera de 
la función sean diferentes. La clave es que el valor que se devuelve (costo_envio en este caso) 
se asigna a una variable en el lugar desde donde se llamó a la función.

En tu código, dentro de la función, calculas el costo de envío y lo asignas a la
 variable costo_envio. Luego, devuelves ese valor con return costo_envio. Cuando llamas a 
 la función y asignas el resultado a la variable valor, estás simplemente eligiendo un 
 nombre diferente para esa variable.

Aquí está el flujo:

Calculas el costo de envío dentro de la función y lo asignas a la variable costo_envio.
Devuelves costo_envio utilizando return costo_envio.
Llamas a la función y asignas el resultado a la variable valor.
Podrías haber utilizado el mismo nombre en ambos lados (dentro de la función y donde haces la llamada),
 pero en términos de legibilidad y claridad del código, está bien usar nombres diferentes
   siempre y cuando entiendas cómo fluye la información. """