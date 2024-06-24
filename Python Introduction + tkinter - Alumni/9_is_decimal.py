from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


# Ejercicio 9

# Crea una función que reciba un dato ingresado
# por teclado (str), que verifique que sea un
# número entero posible de convertir (a int),
# y si no lo es vuelva a pedir ese dato, hasta
# que sea posible de convertirlo. Luego, que
# retorne el entero convertido.


numero = input("Ingrese un numero entero: ")

while numero.isdecimal() == False:
    print("Error")
    numero = input("Ingrese un numero entero nuevamente: ")

numero = int(numero)

print(type(numero),numero)




while True:
    entrada = input("Ingrese un número: ")
    try:
        numero = int(entrada)
        
        print(f"Ha ingresado el número {numero}  correctamente. tipo {type(numero)}")
        break
    except ValueError:
        print("Error: La entrada no es un número válido. Por favor, inténtelo de nuevo.")
    
    


# chat 

while True:
    entrada = input("Ingrese un número: ")
    if entrada.isdigit():  # Verifica si la entrada contiene solo dígitos
        numero = int(entrada)
        print(f"Ha ingresado el número {numero} correctamente.")
        break
    else:
        print("Error: La entrada no es un número válido. Por favor, inténtelo de nuevo.")