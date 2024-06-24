from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

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
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (TypeError):
    print("Error occurred")
except (ValueError):
    print("Error occurred putix")


aa()



valor = "abc"
try:
    numero = int(valor)
except ZeroDivisionError:
    print("Divided by zero")
except (TypeError):
    print("Error occurred")
except ValueError:
    print("El valor no se puede convertir a un entero.")
    



aa()



try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")


aa()


def withdraw(amount):
   print(str(amount) + " withdrawn!")

#your code goes here
amount = input("amount here -->")

try:
   int(amount)
   withdraw(amount)
except: 
   print ("Please enter a number")