
#ejemplo sin return 

def saludar(nombre):
    print("Hola, " + nombre)

resultado_saludo = saludar("Juan")
print("Resultado del saludo:", resultado_saludo)


print("")
print("-------------------")
print("")

# Definir una función que suma dos números y devuelve el resultado
def sumar(a, b):
    
    resultado = a + b
    

    return resultado  # Devuelve la suma de a y b

# Llamada a la función
resultado_suma = sumar(5, 4)

# Imprimir el resultado
print("La suma es:", resultado_suma)


print("")
print("-------------------")
print("")

#Definir función
def bmi(weight, height):
  index = weight / (height * height)
  return index  #sends the return value back

#Llamando a una función y usando el valor de retorno
patient_5 = bmi(61, 1.83) #stores return value
print(patient_5)
print("underweight:", patient_5 < 18.5)


print("")
print("-------------------")
print("")

#Otra llamada
patient_7 = bmi(75, 1.74)
print(patient_7)

print("underweight:", patient_7 < 18.5)


