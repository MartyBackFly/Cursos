# Tomar el peso como entrada
weight = int(input("Weight--->"))

# Completar la función
def shipping_cost(weight):
    valor = weight * 5
    return valor

# Llamar a la función
envio = shipping_cost(weight)

# con + concatenamos antes de imprimir .... el string + entero no se puede... asi que pasamos el entero a string
print("el envio le costara --> " + str(envio))

# con coma imprimimos string y entero .... 
print("el envio le costara --> ", envio)



