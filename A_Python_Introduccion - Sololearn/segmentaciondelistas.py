

#seleccionar del primer elemento en adelante 


cart = ['lamp', 'candles', 'chair', 'carpet']


print(cart[:3])

print("")
print("----------")
print("")


# lo mismo en cadena de texto ... 

vehicle = 'motorbike'
print(vehicle[:5])

print("")
print("----------")
print("")


#segmentar del X numero hasta el final 

cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[1:])


print("")
print("----------")
print("")

vehicle = 'motorbike'
print(vehicle[5:])

print("")
print("----------")
print("")

platform = ['iOS', 'Android', 'Web']
print(platform[:])



print("")
print("----------")
print("")

#Python admite "indexación desde el final", llamada indexación negativa. 
#Esto significa que el último valor de una secuencia tiene un índice de -1.


animals =["cat", "dog", "bird", "cow"]

print(animals[-1]) # Último elemento
print(animals[-2]) # Penúltimo elemento
print(animals[-3:]) # Últimos 3 elementos
print(animals[-3:-1])

print("")
print("----------")
print("")


# se puede convinar la segmentacion positiva con la negativa 
#Lo lograste! Aprendiste que:

 

#🌟 Python admite "indexación desde el final" (indexación negativa)

#🌟 El último valor de una secuencia tiene un índice de -1



c = ['$', '£', '€', '¥']
print(c[1:-1])


print("")
print("----------")
print("")



animals =["turtle", "dog", "bird", "shark"]

print(animals[-1:]) 
print(animals[-2:]) 
print(animals[-3:]) 
print(animals[:-1]) 
print(animals[:-2])
print(animals[:-3])



print("")
print("----------")
print("")



#cambiar valor en la lista ... 

c = ['$', '£', '€', '¥']
c[:2] = ['₣', '฿']
print(c)