from imprimir import espacio as aa

aa()

DolaresPorHora = 0

Pago_Semanal = 0

Pago_Mensual = 0

Pago_Anual = 0

DolaresPorHora = int(input("how much gain for hour ? mtf "))





linea_1 = "---------------------------------------------------------"

#calculo

Pago_Semanal = (DolaresPorHora * 40)

Pago_Mensual = (DolaresPorHora * 160)

Pago_Anual = (Pago_Mensual * 12)




# salida 

print(linea_1)
print("CALCULADORA FREELANCER (USD)".center(len(linea_1))) 
print(linea_1)
print (f">>> Precio en dolares por Hora: {DolaresPorHora}")
print(linea_1)
print(f">>> PAGO SEMANAL: {Pago_Semanal}")
print(f">>> PAGO MENSUAL: {Pago_Mensual}".center(len(linea_1) ))
print(f">>> PAGO ANUAL: {Pago_Anual}".rjust(len(linea_1) ))
print(linea_1)