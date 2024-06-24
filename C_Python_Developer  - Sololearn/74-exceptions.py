from aafuncionimprimir import espacio as aa

aa()

# num1 = 7
# num2 = 0
# print(num1/num2)


# si ejecutas larga una "exception"



# ImportError: una importación falla;
# IndexError: una lista está indexada con un número fuera de rango;
# NameError: se utiliza una variable desconocida;
# SyntaxError: el código no puede ser analizado correctamente;
# TypeError: se llama a una función sobre un valor de un tipo inapropiado;
# ValueError: se llama a una función sobre un valor del tipo correcto, pero con un valor inapropiado.


try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")


    aa()




try:
    variable = 10
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
print("Finished")
 

aa()

try:
    variable = 10
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
    print("Finished")


aa()

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred eyeyey")

aa()

try:
    variable = 10
    #print(variable + "hello")
    print(variable / 0)
except ZeroDivisionError:
    print("Divided by zero mtf")
except (ValueError, TypeError):
    print("Error occurred")

aa()

try:
    variable = 10
    #print(variable + "hello")
    print(f"Result:  {variable / 2}")
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred  ")


aa()

try:
    meaning = 42
    print(meaning / 0)
    print("the meaning of life")
except (ValueError, TypeError):
    print("ValueError or TypeError occurred")
except ZeroDivisionError:
    print("Divided by zero")


aa()

# Una declaración except sin ninguna excepción especificada atrapará todos los errores. 
# Deben utilizarse con moderación, ya que pueden atrapar errores inesperados y ocultar errores de programación.




try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")


aa()

try:
  num1 = input(":-->")
  num2 = input(":-->")
  print(float(num1)/float(num2))
except:
  print("Invalid input")



aa()


def withdraw(amount):
   print(str(amount) + " withdrawn!")

#tu código va aquí
try:
   amount =int(input("ingrese su numero de contraseñá bancaria .. zaraaan "))
   withdraw(amount)
except(ValueError, TypeError):
   print("Please enter a number")


aa()


#buscle hasta que se coloque una entrada valida 


def withdraw(amount):
    print(str(amount) + " withdrawn!")

while True:
    try:
        amount = int(input("Ingrese su número de contraseña bancaria: "))
        withdraw(amount)
        break  # Sale del bucle si el retiro se realiza correctamente
    except ValueError:
        print("Por favor, ingrese un número válido.")
