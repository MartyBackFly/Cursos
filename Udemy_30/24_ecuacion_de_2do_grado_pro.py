import math

def ecuacion_segundo_grado(a, b, c):
    discriminante = b**2 - 4*a*c

    if a != 0:
        if discriminante >= 0:
            x1 = (-b + math.sqrt(discriminante)) / (2*a)
            x2 = (-b - math.sqrt(discriminante)) / (2*a)
            return x1, x2
        else:
            return None  # No hay soluciones reales
    elif b != 0:
        return None  # La ecuación no tiene solución
    else:
        return "Infinitas soluciones"  # La ecuación tiene infinitas soluciones

# Datos de prueba
datos_prueba = [
    {'a': 2, 'b': 7, 'c': 2},
    {'a': 1, 'b': 2, 'c': 3},
    {'a': 0, 'b': 2, 'c': 3},
    {'a': 0, 'b': 0, 'c': 3}
]

# Imprimir resultados
for idx, prueba in enumerate(datos_prueba):
    a = prueba['a']
    b = prueba['b']
    c = prueba['c']
    solucion = ecuacion_segundo_grado(a, b, c)

    print(f"-------------------------------------------------------")
    print(f"      ECUACION DE SEGUNDO GRADO: {a}x^2 + {b}x + {c} = 0      ")
    print(f"-------------------------------------------------------")
    print(f">>> Valor de a: {a}")
    print(f">>> Valor de b: {b}")
    print(f">>> Valor de c: {c}")
    print(f"-------------------------------------------------------")
    
    
    if isinstance(solucion, tuple):
        x1, x2 = solucion
        print(f">>> SOLUCIONES: x1 = {x1:.2f} y x2 = {x2:.2f}")
        print(f"#######################################################")
    elif solucion is None:
        print(">>> La ecuación no tiene soluciones reales.")
        print(f"#######################################################")
    else:
        print(f">>>>> {solucion}")  # Para el caso de infinitas soluciones
        print(f"#######################################################")
    
    print(f"-------------------------------------------------------")
