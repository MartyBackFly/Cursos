from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


# Contador temporizador
# Hacer un script contador de 0 hasta 10, que
# vaya mostrando los números segundo a
# segundo.


import time
import random

print(time.asctime())
print(time.sleep(1))
print(time.asctime())


print(random.randint(1,10))
num = (random.randint(0,100))

print(num)

timer = int(input("segundos -->"))
for i in range(0,timer+1):
    print(i)
    time.sleep(1)



aa()


i = 0
while i < 10:
 print(i)
 time.sleep(1)
 i = i + 1