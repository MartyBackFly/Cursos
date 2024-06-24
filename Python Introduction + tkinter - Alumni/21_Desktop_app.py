from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

"""generar un número aleatorio de 1 al 6
simulando arrojar un dado, ahora debemos
pasarlo a una aplicación de escritorio. La vista
de la aplicación debería ser similar a la imagen
que vemos a la derecha.
En la caja deberían de aparecer los resultados
aleatorios cada vez que se presiona el botón.
Antes de mostrar los resultados se limpia la caja,
dejando el mismo resultado hasta que se vuelve
a pulsar.
Introducción a Python
Una ayuda para resolver el ejercicio
Si tenemos una “caja” generada con tk.Entry()
● caja.delete(0,tk.END) llamada desde
cualquier función limpia la “caja”.
● caja.insert(0,variable) llamada desde
cualquier función inserta el valor de variable
en la “caja”.
Introducción a Python
En la sección de Descargas encontrarás los recursos
necesarios para realizar los ejercicios y su resolución
para que verifiques cómo te fue."""

import tkinter as tk
from tkinter import messagebox
ventana = tk.Tk()
ventana.config(width=400, height=300)
ventana.title("Desktop app")
# def boton_preisonado():
#     print("por apretas el boton ? ")
# def boton_presionado():
#  print(caja.get())
def boton_presionado():
    nombre = caja.get()
    if nombre == "FeDe":
        print("lo has conseguido !!!!")
    else:
        print(nombre)

def boton1_presionado():
    messagebox.showinfo("Boton 2","Lo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeeeLo rompiste eeeeeeeeeeee")
def boton2_presionado():
    messagebox.showwarning("El anti virus","La base de datos de virus ha sido actualizada !! ")
    etiqueta.place(x=370, y=390)


caja = tk.Entry()
caja.place(x=20, y=120, width=200, height=25)
boton = tk.Button()
boton = tk.Button(ventana, text= "Boton 1", command=boton_presionado)
boton.place(x=20, y=160, width=200, height=25)
boton1 = tk.Button(ventana, text= "Boton 2", command=boton1_presionado)
boton1.place(x=20, y=190, width=200, height=25)
boton2 = tk.Button(ventana, text= "Boton 3", command=boton2_presionado)
boton2.place(x=20, y=230, width=200, height=25)
etiqueta = tk.Label(text= "ingresa tu nombre ")
etiqueta.place(x=20, y=90)
ventana.mainloop()




