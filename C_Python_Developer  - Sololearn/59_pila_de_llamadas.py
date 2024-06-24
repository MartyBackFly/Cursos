import traceback

def is_evenpar(x):
    if x == 0:
        return True
    else:
        return is_oddimpar(x - 1)

def is_oddimpar(x):
    if x == 0:
        return False
    else:
        return is_evenpar(x - 1)

print(is_oddimpar(3))
print(is_evenpar(3))

# Usamos try-except para capturar cualquier excepción y luego imprimimos la pila de llamadas
# try:
#     raise Exception("Mostrar pila de llamadas")
# except:
#     traceback.print_exc()
