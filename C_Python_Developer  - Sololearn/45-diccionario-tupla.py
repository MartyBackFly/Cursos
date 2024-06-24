from aafuncionimprimir  import espacio


# Definir un diccionario con tuplas como claves
student_grades = {('Alice', 'Math'): 90, ('Bob', 'History'): 85, ('Alice', 'English'): 92}

# Acceder a un valor usando una tupla como clave
grade_alice_math = student_grades[('Alice', 'Math')]

print(f"La calificación de Alice en Matemáticas es: {grade_alice_math}")

print(student_grades)

print(student_grades[('Alice', 'Math')])





# En este ejemplo, student_grades es un diccionario que almacena calificaciones de estudiantes. 
# Las claves del diccionario son tuplas que representan la combinación de un estudiante y una asignatura. 
# Dado que las tuplas son inmutables, se pueden usar como claves en el diccionario.
# 
# Puedes acceder a las calificaciones utilizando las tuplas como índices. En este caso, estamos accediendo 
# a la calificación de Alice en Matemáticas utilizando la tupla ('Alice', 'Math') como clave.
# 
# Recuerda que la inmutabilidad de las tuplas hace que sean adecuadas para ser utilizadas como claves 
# en un diccionario, ya que no pueden cambiar después de haber sido creadas.