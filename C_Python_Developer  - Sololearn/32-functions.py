from aafuncionimprimir import espacio 



#definición de la función
def greet(): 
  print("Hello from a function")
  print("Have a great day")

#llamada a la función
greet()


espacio()

# con argumento 
#definición de la función

def personal_greet(name): 
  print("Hello", name)
  print("Have a great day")


#llamadas a la función
personal_greet("Sarah") 
personal_greet("Henry")


espacio()


#definición de la función
def double(number):
 print(number*2)

#llamadas a la función
double(6)


espacio()



""" def bmi(weight, height):
    index = weight / (height * height)
    
    
    print(index)


    bmi(80, 1.70)

    print(index) """

#Definir función
def bmi(weight, height):
  index = weight / (height * height)
  return index  #sends the return value back



#Llamando a una función y usando el valor de retorno
patient_5 = bmi(61, 1.83) #stores return value
print("underweight:", patient_5 < 18.5)

#Otra llamada
patient_7 = bmi(75, 1.74)
print("underweight:", patient_7 < 18.5)





espacio()

def discounted( price, discount):
  
  return price * (1 - discount / 100)


a = discounted(1000, 50)
print (a)

espacio()




