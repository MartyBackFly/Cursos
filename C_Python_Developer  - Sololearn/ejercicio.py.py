# El código dado define una función recursiva convert(), 
# que necesita convertir su argumento de decimal a binario. 
# Sin embargo, el código tiene un error. Corrija el código 
# agregando el caso base para la recursividad, luego tome un número de
# la entrada del usuario y llame a la función convert() para generar el resultado. 
# Entrada de muestra: 8 Salida de muestra: 1000 


def convert(num): 
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return (num % 2 + 10 * convert(num // 2))
    
num = int(input("numerito here --> "))

print(convert(num))

print("----------")

def convert(num): 
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return (num % 2 + 10 * convert(num // 2))
    
num = int(input())

print(convert(num))

# supongamos que num es 13
# 13 % 2 nos da 1 (el residuo cuando 13 se divide por 2), entonces num % 2 es 1.
# 13 // 2 nos da 6 (la división entera de 13 por 2), entonces num // 2 es 6.
# La función se llama recursivamente con num = 6.
# Repite el proceso: 6 % 2 nos da 0 y 6 // 2 nos da 3.
# Ahora, la función se llama recursivamente con num = 3.
# 3 % 2 nos da 1 y 3 // 2 nos da 1.
# Ahora, la función se llama recursivamente con num = 1.
# Dado que num == 1, devuelve 1 (el caso base).
# Subiendo en la pila de recursión, ahora tenemos 1 + 10 * (1 + 10 * (0 + 10 * 1)).
# Simplificando eso, obtenemos 1011, que es la representación binaria de 13.

# Por ejemplo, si num es 13:

# 13 dividido por 2 da 6 con un resto de 1.
# La función se llama recursivamente con 6.
# 6 dividido por 2 da 3 con un resto de 0.
# La función se llama recursivamente con 3.
# 3 dividido por 2 da 1 con un resto de 1.
# La función se llama recursivamente con 1.
# Como num es ahora 1, devuelve 1.
# Volviendo a la llamada anterior con num igual a 3, 
# obtenemos 1 (de la llamada recursiva) multiplicado por 10, y se le suma 1 (el resto), dando 11.
# Volviendo a la llamada anterior con num igual a 6, obtenemos 11 (de la llamada recursiva) 
# multiplicado por 10, y se le suma 0 (el resto), dando 110.
# Finalmente, la llamada original con num igual a 13 obtiene 110 (de la llamada recursiva) 
# multiplicado por 10, y se le suma 1 (el resto), dando 1101, que es la representación binaria de 13.


#codigo pegado en python tutor 

# https://pythontutor.com/render.html#code=def%20convert%28decimal_number%29%3A%0A%20%20%20%20if%20decimal_number%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20%220%22%0A%20%20%20%20elif%20decimal_number%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20return%20%221%22%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20convert%28decimal_number%20//%202%29%20%2B%20str%28decimal_number%20%25%202%29%0A%20%20%20%0A%23%20Solicitar%20entrada%20al%20usuario%0Adecimal_input%20%3D%208%0A%0A%23%20Llamar%20a%20la%20funci%C3%B3n%20convert%28%29%20e%20imprimir%20el%20resultado%0A%0Aprint%28convert%288%29%29%0A%0A%23%20convert%288%29%20%3D%20convert%284%29%20%2B%20str%288%20%25%202%29%0A%23%20%20%20%20%20%20%20%20%20%20%20%20%3D%20%28convert%282%29%20%2B%20str%284%20%25%202%29%29%20%2B%20str%288%20%25%202%29%0A%23%20%20%20%20%20%20%20%20%20%20%20%20%3D%20%28%28convert%281%29%20%2B%20str%282%20%25%202%29%29%20%2B%20str%284%20%25%202%29%29%20%2B%20str%288%20%25%202%29%0A%23%20%20%20%20%20%20%20%20%20%20%20%20%3D%20%28%221%22%20%2B%20%220%22%20%2B%20%220%22%29%20%2B%20%220%22%0A%23%20%20%20%20%20%20%20%20%20%20%20%20%3D%20%221000%22&cumulative=true&curInstr=0&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false