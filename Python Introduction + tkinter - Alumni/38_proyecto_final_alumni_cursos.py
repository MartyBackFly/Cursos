from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

import tkinter as tk

def verificar(dato):
    if dato == "":
        dato = "error"
    return dato

def convertir(valor):
    if valor.isdecimal():
        valor = int(valor)
    else:
        valor = "error"
    return valor

def ver():
    print("Lista de alumnos:")
    for nombre in alumnos:
        cursos = alumnos[nombre]
        print(nombre + " - " + str(cursos) + " cursos")

def agregar():
    nombre_alumno = caja_nombre.get()
    nombre_alumno = verificar(nombre_alumno)
    cursos = caja_cursos.get()
    cursos = convertir(cursos)
    
    if nombre_alumno == "error":
        print("Error. Nombre vacio.")
    elif cursos == "error":
        print("Error. El ingreso de cursos debe ser solo numeros.")
    else:
        alumnos[nombre_alumno] = cursos
        print("Has ingresado un alumno correctamente.")

def ver_alumno():
    nombre = caja_nombre.get()
    nombre = verificar(nombre)
    if nombre == "error":
        print("Error. Nombre vacio.")
    elif nombre in alumnos:
        print(nombre + " tiene " + str(alumnos[nombre]) + " cursos")
    else:
        print("Ese alumno no tiene cursos")

alumnos = {}
ventana = tk.Tk()
ventana.config(width=400, height=300)
ventana.title("Proyecto integrador")
boton_lista = tk.Button(text="Ver lista de alumnos", command=ver)
boton_lista.place(x=10, y=10)
etiqueta_nombre = tk.Label(text="Nombre alumno:")
etiqueta_nombre.place(x=10, y=60)
caja_nombre = tk.Entry()
caja_nombre.place(x=110, y=60, width=150, height=20)
etiqueta_cursos = tk.Label(text="Cursos:")
etiqueta_cursos.place(x=10, y=100)
caja_cursos = tk.Entry()
caja_cursos.place(x=110, y=100, width=50, height=20)
boton_agregar = tk.Button(text="Agregar a la lista", command=agregar)
boton_agregar.place(x=10, y=150)
boton_cursos = tk.Button(text="Ver cantidad de cursos", command=ver_alumno)
boton_cursos.place(x=115, y=150)
ventana.mainloop()
