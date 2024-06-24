from aafuncionimprimir import espacio as aa
from aafuncionimprimir import rayita as zz


first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
zz()
print(first & second)
zz()
print(first - second)
zz()
print(second - first)
zz()
print(first ^ second)


# El operador de unión | combina dos conjuntos para formar uno nuevo que contenga elementos en cualquiera de los dos. 

# El operador de intersección & obtiene elementos solo en ambos. 

# El operador de diferencia - obtiene elementos en el primer conjunto pero no en el segundo. 

# El operador de diferencia simétrica ^ obtiene elementos en cualquiera de los conjuntos, pero no en ambos. 

aa()

skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}


asd = list(skills & job_skills)
print(asd[0])


aa()

a = {1, 2, 3}
b = {0, 3, 4, 5}
print(a & b)