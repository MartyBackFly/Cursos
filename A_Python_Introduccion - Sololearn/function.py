#definición de la función
def greet(): 
  print("Hello from a function")
  print("Have a great day")

#llamada a la función
greet()

print("")
print("-------------------------------")
print("")


#definición de la función
def personal_greet(name): 
  print("Hello", name)
  print("Have a great day")


#llamadas a la función
personal_greet("Sarah") 
print("........")
personal_greet("Henry")


print("")
print("-------------------------------")
print("")


#definición de la función
def double(number):
  print(number*2)

#llamadas a la función
double(6)

print("")
print("-------------------------------")
print("")




def bmi(weight, height):
    index = weight / (height * height)
    print(index)

bmi(79, 1.70)   #peso - altura 

print("")
print("-------------------------------")
print("")
