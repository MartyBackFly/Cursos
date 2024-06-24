nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)

lista_num = (list(nums))

print (list(lista_num) )
print(len(list(lista_num)))

#extras 


#Se crea un conjunto nums que contiene los números del 1 al 6: {1, 2, 3, 4, 5, 6}.
#Se crea otro conjunto con los números del 0 al 3: {0, 1, 2, 3}.
#Luego, se realiza una operación de intersección entre los dos conjuntos usando el operador &. Esto devuelve un conjunto que contiene los elementos que están presentes en ambos conjuntos. En este caso, los elementos que están en ambos conjuntos son 1, 2 y 3.
#El conjunto nums se actualiza para que ahora contenga el resultado de la intersección, que es {1, 2, 3}.

#se imprime la longitud de la lista resultante utilizando len().
#El resultado final impreso es la cantidad de elementos en nums que son mayores que 1. 
#En este caso, dado que nums contiene {1, 2, 3}, y solo 2 y 3 son mayores que 1, la longitud de la lista resultante es 2, que se imprime.