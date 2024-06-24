from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

# Ejercicio 3

# Un empleado cobró 300 dólares por mes desde enero a junio, 
# 500 dólares de julio a octubre, 
#  y 700 dólares por mes en noviembre y en diciembre.
# Hace un programa que calcule el sueldo promedio. Y
# que diga si este “empleado” está cobrando un sueldo
# bajo, normal o mejor de lo normal.
# ● Sueldo bajo: por debajo de 300 dólares.
# ● Sueldo normal: entre 300 a 900.
# ● Sueldo mejor de lo normal: más de 900 dólares.

aa()

enero_a_junio = 300 * 6
julio_a_octubre = 500 * 4
noviembre_a_diciembre = 700 * 2 

sueldo_promedio = (enero_a_junio + julio_a_octubre + noviembre_a_diciembre ) / 3 

print(f"Sueldo promedio {sueldo_promedio}")

if sueldo_promedio > 900 :
    print("Sueldo mejor de lo normal ")
elif sueldo_promedio > 300 and sueldo_promedio < 900:
    print("sueldo normal")
else :
    print("Sueldo bajo ")

aa()