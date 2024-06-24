from aafuncionimprimir import espacio


espacio()

contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

nombre_buscado = input("Ingresa un nombre: ")

for contacto in contacts:
    if contacto[0] == nombre_buscado:
        print(f'{contacto[0]} is {contacto[1]}')
        break
else:
    print("Not Found")






contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

# Obtener el nombre del usuario como entrada
nombre_buscado = input("-->")

# Buscar el nombre en la lista de contactos
encontrado = False
for contacto in contacts:
    if contacto[0] == nombre_buscado:
        print(f'{contacto[0]} is {contacto[1]}')
        encontrado = True
        break

# Mostrar "Not Found" si no se encuentra el contacto
if not encontrado:
    print("Not Found")



   


    espacio()


def get_contact_age(name, contact_list):
    for contact in contact_list:
        if contact[0] == name:
            return contact[1]
    return "Not Found"

contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

# Entrada del usuario
name_to_search = input("-->")

# Obtener la edad del contacto o "Not Found" si no se encuentra
age_result = get_contact_age(name_to_search, contacts)

# Imprimir el resultado
print(f"{name_to_search} is {age_result}")
