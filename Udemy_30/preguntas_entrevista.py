#► Pregunta 1:

#Comprobar si la lista contiene el número entero x.

lista = [3, 3, 4, 5, 2, 111, 5]
print(111 in lista) # True


#► Pregunta 2:

#Encuentra el número duplicado en la lista de enteros.

elements = [1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9, 7, 5, 34]

def find_duplicates(elements):
    duplicates, seen = set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return list(duplicates)

duplicates = find_duplicates(elements)
print("Elementos duplicados:", duplicates)

#► Pregunta 3:

# Comprobar si dos cadenas son anagramas.

def is_anagram(s1, s2):
    return set(s1) == set(s2)
print(is_anagram("elvis", "lives")) # True
print(set("elvis"))
print(set("lives"))


# ► Pregunta 4:

# Eliminar todos los duplicados de la lista.

lista = list(range(10)) + list(range(10))
print(lista)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
lista = list(set(lista))
print(lista)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# ► Pregunta 5:

# Encuentra pares de enteros en la lista para que su suma sea igual al entero x.

def find_pairs(l, x):
    pairs = []
    for (i, el_1) in enumerate(l):
        for (j, el_2) in enumerate(l[i+1:]):
            if el_1 + el_2 == x:
                pairs.append((el_1, el_2))
    return pairs


# ► Pregunta 6:

# Comprobar si una cadena es un palíndromo.

def is_palindrome(phrase):
    return phrase == phrase[::-1]
print(is_palindrome("anna")) # True


# ► Pregunta 7:

# Use una lista como matriz, pila y cola.

# Lista como una matriz.
lista = [3, 4]
print(">>> Matriz Antes  : " + str(lista))
lista += [5, 6] # l = [3, 4, 5, 6]
print(">>> Matriz Despues: " + str(lista))
 
# Lista como una pila:
# El ultimo que entra es el primero que sale.
lista.append(10) # lista = [3, 4, 5, 6, 10]
print(">>> Pila Antes    : " + str(lista))
lista.pop() # lista = [3, 4, 5, 6]
print(">>> Pila Despues  : " + str(lista))
 
# Lista como una cola.
# El ultimo que entra es el ultimo que sale
lista.insert(0, 5) # lista = [5, 3, 4, 5, 6]
print(">>> Cola Antes    : " + str(lista))
lista.pop() # lista = [5, 3, 4, 5]
print(">>> Cola Despues  : " + str(lista))