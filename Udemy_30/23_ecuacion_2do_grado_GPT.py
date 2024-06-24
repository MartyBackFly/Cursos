import sys

def resolver_ecuacion_segundo_grado(a, b, c):
    discriminante = b ** 2 - 4 * a * c

    if a == 0:
        if b == 0:
            if c == 0:
                print("La ecuación tiene infinitas soluciones.")
            else:
                print("La ecuación no tiene solución.")
        else:
            x = -c / b
            print(f"La ecuación es de primer grado, la solución es x = {x:.2f}")
    elif discriminante < 0:
        print("La ecuación no tiene soluciones reales.")
    else:
        x1 = (-b + (discriminante ** 0.5)) / (2 * a)
        x2 = (-b - (discriminante ** 0.5)) / (2 * a)
        print(f"SOLUCIONES: x1 = {x1:.2f} y x2 = {x2:.2f}")

def main():
    print("-" * 55)
    print("      ECUACION DE SEGUNDO GRADO: ax^2 + bx + c = 0      ")
    print("-" * 55)

    try:
        a = float(input(">>> Valor de a: "))
        b = float(input(">>> Valor de b: "))
        c = float(input(">>> Valor de c: "))

        print("-" * 55)
        resolver_ecuacion_segundo_grado(a, b, c)
        print("-" * 55)

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()



# El .2 indica que se mostrarán dos lugares decimales después del punto decimal.
# La f indica que el número será representado como un número de punto flotante.
# Por lo tanto, .2f se utiliza para formatear un número de punto flotante con dos lugares 