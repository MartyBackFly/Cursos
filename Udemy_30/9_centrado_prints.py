

a=0
b=0

a=int(input("numerito a sumar -->"))
b=int(input("numerito 2 pa sumar -->"))

Z= (a+b)

# Formateo del resultado centrado en una cadena
resultado_formateado = f"La suma es  {Z} lalala "

# Imprimir el resultado centrado
print(resultado_formateado.center(60))  # Ajusta el ancho según lo necesites


print("---------------------------------")
print("")
print("---------------------------------")
print("")





# Ancho total deseado para la cadena
ANCHO = 70

# Carácter de relleno
RELLENO = "-"

# Calcula cuántos caracteres de relleno necesitas en cada lado
relleno_total = ANCHO - len(resultado_formateado)
relleno_izquierdo = relleno_total // 2
relleno_derecho = relleno_total - relleno_izquierdo

# Agrega el relleno utilizando ljust() y rjust() y luego imprime el resultado
print(resultado_formateado.rjust(len(resultado_formateado) + relleno_derecho, RELLENO).ljust(ANCHO, RELLENO))

print("")
print("")
print("----------espacio publicitario -------------")
print("")

ANCHOS = 30
RELLENOS = "-"


a = 30
b = 40

F = (a + b)

print(f"asdasd  {F} asdasd".center(ANCHOS, RELLENOS))



print("")
print("")
print("----------espacio publicitario -------------")
print("")






print("---------------------------------")
print("")
print("---------------------------------")
print("")

# Obtener los caracteres para el inicio y el final


caracter_inicio = input("Ingrese el carácter para el inicio: ")
caracter_fin = input("Ingrese el carácter para el final: ")
ancho = int(input("Ingrese el ancho de centrado : "))

# Obtener el mensaje del usuario
mensaje = input("Ingrese su mensaje: ")

len_num = len(mensaje)

# Imprimir el inicio, el mensaje y el final
print (len_num)
print(len(caracter_inicio))
print(len(caracter_fin))
print(caracter_inicio * len_num +" ++ "+ mensaje.center(ancho)  + " ++ " + caracter_fin * len_num)



# si ponemos 2 caracteres en inicio o fin como por ejemplo  44 van a salir el doble de caracteres en la respuesta 
# por que van a ser "44" x len.mensaje y en pantalla se vera si len msj es 2 -->  4444


# ejemplo 

# Ingrese el carácter para el inicio: 11
# Ingrese el carácter para el final: 222
# Ingrese su mensaje: 3333
# 4
# 2
# 3
# 11111111 ++ 3333 ++ 222222222222