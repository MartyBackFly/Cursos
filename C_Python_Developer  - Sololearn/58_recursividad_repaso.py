


def convert(decimal_number):
    if decimal_number == 0:
        return "0"
    elif decimal_number == 1:
        return "1"
    else:
        return convert(decimal_number // 2) + str(decimal_number % 2)
   
# Solicitar entrada al usuario
decimal_input = int(input("pone numerito -->"))

# Llamar a la función convert() e imprimir el resultado
binary_result = convert(decimal_input)
print(binary_result)



# ejempo con numero 77 

# divide // 2 sin residuo  y divide % 2 obteniendo el residual


# decimal_number	77   res 1
# convert
# decimal_number	38   res 0
# convert
# decimal_number	19   res 1
# convert
# decimal_number	9    res 1
# convert
# decimal_number	4    res 0
# convert
# decimal_number	2    res 0 
# convert
# decimal_number	1    res 1
# Return
# value	"1"

# return 1 + concatenar residual de 2, + 4, + 9, + 19, + 38, +  77

# 1 001101

def is_even_par(x):
    if x == 0:
        return True
    else:
        return is_odd_impar(x - 1)

def is_odd_impar(x):
    if x == 0:
        return False
    else:
        return is_even_par(x - 1)

print(is_odd_impar(3))
print(is_even_par(3))



def convert(decimal_number):
    if decimal_number == 0:
        return "0"
    elif decimal_number == 1:
        return "1"
    else:
        return convert(decimal_number // 2) + str(decimal_number % 2)
   
# Solicitar entrada al usuario
decimal_input = 8

# Llamar a la función convert() e imprimir el resultado

print(convert(8))

# convert(8) = convert(4) + str(8 % 2)
#            = (convert(2) + str(4 % 2)) + str(8 % 2)
#            = ((convert(1) + str(2 % 2)) + str(4 % 2)) + str(8 % 2)
#            = ("1" + "0" + "0") + "0"
#            = "1000"


# Primera llamada - convert(11):

# El número 11 no es igual a 0 ni a 1, por lo que se realiza una llamada recursiva con 
#convert(11 // 2), que es convert(5).
# Se concatena el residuo de la división 11 % 2 como una cadena, lo que es "1".
# La primera llamada retorna "convert(5)" + "1", que es equivalente a la cadena "convert(5)1".
# Segunda llamada - convert(5):

# El número 5 no es igual a 0 ni a 1, por lo que se realiza otra llamada recursiva con 
#convert(5 // 2), que es convert(2).
# Se concatena el residuo de la división 5 % 2 como una cadena, lo que es "1".
# La segunda llamada retorna "convert(2)" + "1", que es equivalente a la cadena "convert(2)1".
# Tercera llamada - convert(2):

# El número 2 no es igual a 0 ni a 1, por lo que se realiza otra llamada recursiva con 
#convert(2 // 2), que es convert(1).
# Se concatena el residuo de la división 2 % 2 como una cadena, lo que es "0".
# La tercera llamada retorna "convert(1)" + "0", que es equivalente a la cadena "convert(1)0".
# Cuarta llamada - convert(1):

# Ahora alcanzamos el caso base, ya que 1 es igual a 1, por lo que esta llamada retorna directamente "1".
# Finalmente, combinamos todas las llamadas recursivas:

# "convert(11)" = "convert(5)1" = "convert(2)1" + "1" = "convert(1)0" + "1" + "1" = "1" + "0" + "1" + "1" = "1011"
# Entonces, convert(11) retorna la cadena "1011", que es la representación binaria de 11. 
#En cada paso, la función construye la representación binaria concatenando las llamadas 
#recursivas y los residuos como cadenas de caracteres.


# https://pythontutor.com/render.html#code=def%20convert%28decimal_number%29%3A%0A%20%20%20%20if%20decimal_number%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20%220%22%0A%20%20%20%20elif%20decimal_number%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20return%20%221%22%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20convert%28decimal_number%20//%202%29%20%2B%20str%28decimal_number%20%25%202%29%0A%20%20%20%0A%23%20Solicitar%20entrada%20al%20usuario%0Adecimal_input%20%3D%208%0A%0A%23%20Llamar%20a%20la%20funci%C3%B3n%20convert%28%29%20e%20imprimir%20el%20resultado%0A%0Aprint%28convert%288%29%29%0A%0A%23%20convert%288%29%20%3D%20convert%284%29%20%2B%20str%288%20%25%202%29%0A%23%20%20%20%20%20%20%20%20%20%20%20%20%3D%20%28convert%282%29%20%2B%20str%284%20%25%202%29%29%20%2B%20str%288%20%25%202%29%0A%23%20%20%20%20%20%20%20%20%20%20%20%20%3D%20%28%28convert%281%29%20%2B%20str%282%20%25%202%29%29%20%2B%20str%284%20%25%202%29%29%20%2B%20str%288%20%25%202%29%0A%23%20%20%20%20%20%20%20%20%20%20%20%20%3D%20%28%221%22%20%2B%20%220%22%20%2B%20%220%22%29%20%2B%20%220%22%0A%23%20%20%20%20%20%20%20%20%20%20%20%20%3D%20%221000%22&cumulative=true&curInstr=0&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false