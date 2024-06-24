import random

class VagueList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)]

  def __len__(self):
    return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])


print("----------------------------------------------------------------")
#sin random 

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index]

    def __len__(self):
        return len(self.cont)

# Crear una instancia de VagueList
vague_list = VagueList(["A", "B", "C", "D", "E"])

# Obtener la longitud de la lista (longitud real)
print(len(vague_list))  # Salida: 5

# Acceder a elementos de la lista (sin desplazamiento aleatorio)
print(vague_list[2])    # Salida: "C"
print(vague_list[2])    # Salida: "C"


print("----------------------------------------------------------------")

# sin __len__  hay que hace rel print  asi print(len(vague_list.cont))

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index]

# Crear una instancia de VagueList
vague_list = VagueList(["A", "B", "C", "D", "E"])

# Obtener la longitud de la lista (longitud real)
print(len(vague_list.cont))  # Salida: 5

# Acceder a elementos de la lista (sin desplazamiento aleatorio)
print(vague_list[2])    # Salida: "C"
print(vague_list[2])    # Salida: "C"



print("-------------------------------------------------")


class Registro:
    def __init__(self, registros):
        self.registros = registros

    def __len__(self):
        return len(self.registros)

# Crear una instancia de Registro
registros = Registro(["Registro1", "Registro2", "Registro3", "Registro4", "Registro5", "Registro6"])

# Obtener la cantidad total de registros utilizando len()
cantidad_registros = len(registros)

print("Cantidad total de registros:", cantidad_registros)  # Salida: 3


print("-------------------------------------------------")

class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __getitem__(self, indice):
        return self.elementos[indice]

    def __setitem__(self, indice, valor):
        self.elementos[indice] = valor

# Crear una instancia de MiLista
mi_lista = MiLista([1, 2, 3, 4, 5])

# Mostrar la lista original
print("Lista original:", mi_lista)
print("Lista original:", mi_lista.elementos)

# Asignar un valor nuevo a un elemento de la lista usando x[y] = z
mi_lista[2] = 10

# Mostrar la lista después de la asignación
print("Lista después de la asignación:", mi_lista.elementos)


mi_lista[3] = 22
mi_lista[4] = 99 
mi_lista[0] = 72

print("Lista después de la 2da asignación:", mi_lista.elementos)




print("-------------------------------------------------")


class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __getitem__(self, indice):
        return self.elementos[indice]

    def __setitem__(self, indice, valor):
        self.elementos[indice] = valor

# Crear una instancia de MiLista
mi_lista = MiLista([1, 2, 3, 4, 5])

# Asignar un valor nuevo a un elemento de la lista usando la sintaxis x[y] = z
mi_lista.__setitem__(2, 10)
mi_lista[3] = 99
mi_lista.__setitem__(4, 72)
# Mostrar la lista después de la asignación
print(mi_lista.elementos)

# la llamada al método mágico __setitem__ se realiza mediante x.__setitem__(y, z). 
# Este método se invoca cuando utilizamos la sintaxis x[y] = z para asignar un valor z a la posición y de la lista x.