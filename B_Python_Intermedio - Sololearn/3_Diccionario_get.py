from aafuncionimprimir import espacio as aa

pairs = {
   1: "apple",
   "orange": [2, 3, 4], 
   True: False, 
   12: "True",
   3: "buacamole"
}
print(pairs.get("1", "not found"))
print(pairs.get(1, "not found"))
print(pairs.get(7, 42))
print()
print(pairs.get(12345, "nota eso"))
print(pairs.get("orange"))

print()
print(pairs.get(12 , "not found"))
print(pairs.get(5 , "not found"))
print()
print(pairs.get(12))
print(pairs.get("apple"))
print()
print(pairs.get(True))
print(pairs.get(False))
print()
print(pairs.get(3))
print(pairs.get(32, "no le hay"))
print()
print(len(pairs))


#en Python, True es considerado como 1 y False como 0. 
# Entonces, cuando utilizas True como clave, estás sobrescribiendo la clave 1 que definiste anteriormente en el diccionario.

data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

a = input("pais --> ")

print(data.get((a), "Not found"))


aa()

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))

aa()