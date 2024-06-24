from aafuncionimprimir import espacio


animals =["cat", "dog", "bird", "cow"]


print(animals[-1]) # Último elemento
print(animals[-2]) # Penúltimo elemento
print(animals[-3:]) # Últimos 3 elementos
print(animals[-3:-1])



espacio()


vehicle = 'motorbike'
print(vehicle[-4:]) 
print(vehicle[-9:-4]) 

print(vehicle[-4:-9]) #nada


espacio()


c = ['$', '£', '€', '¥']
print(c[1:-1])


espacio()

c = ['$', '£', '€', '¥']
c[1] = '₣'
print(c)



espacio()

c = ['$', '£', '€', '¥']
c[:2] = ['₣', '฿']
print(c)


espacio()

brands = ["Honda", "Toyota", "BMW", "Mercedes"]


print(brands[-3:-1])


espacio()


nums = (55, 44, 33, 22)
print(nums[:2][-1])


