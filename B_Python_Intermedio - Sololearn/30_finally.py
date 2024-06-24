from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Error --> Divided by zero")
finally:
    print("This code will run no matter what")


aa()

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)


aa()


try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)


aa()

# ejercicio 

menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']
#your code goes here

try:
    num = int(input())
    print(menu[num])
    
except:
    print("Item not found")

else: 
    print("Thanks for your order")