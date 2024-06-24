from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


# Ejercicio 5
# A la derecha vemos un diagrama de flujo de
# cómo se hace para calcular un año bisiesto. La
# idea es llevar este algoritmo a código Python.


anio = int(input("año aca --> "))

if anio % 400 == 0:
    print("es biciesto")
elif anio % 4 == 0 and anio % 100 != 0 :
    print("es biciesto")
else:
    print("no es biciesto")
print("The end ")

aa()

# solucion : 


a = input("Ingrese año: ")
a = int(a)
if a % 400 == 0:
    print("Es bisiesto")
else:
    if a % 4 == 0 and a % 100 != 0 :
        print("Es bisiesto")
    else:
        print("No es bisiesto")
print("Fin")