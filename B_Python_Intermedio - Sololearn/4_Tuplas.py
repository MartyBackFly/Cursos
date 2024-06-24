from aafuncionimprimir import espacio as aa


words = ("spam", "eggs", "sausages")


print(words[0])




# querer asignar valor dara error 
#words[1] = "cheese"


# lista
list = ["one", "two"]
# diccionario 
dict = {1:"one", 2:"two"}
# tupla 
tp = ("one", "two")

aa()


# tuplas pueden ser creadas sin parentesis 
my_tuple = "one", "two", "three"
print(my_tuple[0])


aa()


contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
    
print(contacts[0])
print(contacts[1])
print(contacts[2])
print(contacts[3])
print(contacts[4])





aa()


contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

nombre = input("name ... ")

for contact in contacts:
    if contact[0] == nombre:
        print(f"{contact[0]} is {contact[1]}")
        break
else:
    print("Not Found")


    aa()





tuple = (1, (1, 2, 3))
print(tuple[1])