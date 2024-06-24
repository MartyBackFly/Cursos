from aafuncionimprimir import espacio

num_set = {1, 2, 3, 4, 5}

print(3 in num_set)


espacio()


letters = {"a", "b", "c", "d"}
if "e" not in letters:
    print(1)
else:
    print(2)

   
espacio()


#Los elementos duplicados se eliminarán automáticamente del conjunto.
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)

nums.add(-7)
print(nums)

nums.remove(3)
print(nums)

nums.remove(2)
print(nums)

print(len(nums))

espacio()



#Los conjuntos pueden combinarse mediante operaciones matemáticas.
#El operador unión | combina dos conjuntos para formar uno nuevo que contenga elementos en cualquiera de ellos.
#El operador intersección & obtiene elementos sólo en ambos.
#El operador diferencia - obtiene elementos en el primer conjunto pero no en el segundo.
#El operador diferencia simétrica ^ obtiene elementos en cualquiera de los dos conjuntos, pero no en ambos.


first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

# Unión de conjuntos
print(first | second)

# Intersección de conjuntos
print(first & second)

# Diferencia de conjuntos (elementos en first pero no en second)
print(first - second)

# Diferencia de conjuntos (elementos en second pero no en first)
print(second - first)

# Diferencia simétrica de conjuntos (elementos que están en uno pero no en ambos)
print(first ^ second)

# salida {1, 2, 3, 4, 5, 6, 7, 8, 9}  # Unión
# salida {4, 5, 6}  # Intersección
# salida {1, 2, 3}  # Diferencia de first - second
# salida {8, 9, 7}  # Diferencia de second - first
# salida {1, 2, 3, 7, 8, 9}  # Diferencia simétrica



espacio()



a = {1, 2, 3}
b = {0, 3, 4, 5}
print(a & b)

espacio()



skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

print(skills & job_skills)

asd= list(skills & job_skills)

print(asd[0])