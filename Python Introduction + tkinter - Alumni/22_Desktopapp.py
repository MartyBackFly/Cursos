from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

import tkinter as tk
from tkinter import messagebox

def boton_presionado():
    nombre = caja.get()
    if nombre:
        if nombre == "FeDe":
            mensaje = f"¡Hola, {nombre}!"
        else:
            mensaje = f"Hola, {nombre}"
        messagebox.showinfo("Mensaje", mensaje)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un nombre.")

def boton_2_presionado():
    messagebox.showinfo("Botón 2", "Has presionado el botón 2.")

def boton_3_presionado():
    messagebox.showinfo("Botón 3", "Has presionado el botón 3.")

ventana = tk.Tk()
ventana.config(width=400, height=300)
ventana.title("Desktop app")

caja = tk.Entry(ventana)
caja.place(x=20, y=120, width=200, height=25)

boton1 = tk.Button(ventana, text="Enter", command=boton_presionado)
boton1.place(x=20, y=170, width=200, height=25)

boton2 = tk.Button(ventana, text="Botón 2", command=boton_2_presionado)
boton2.place(x=20, y=210, width=200, height=25)

boton3 = tk.Button(ventana, text="Botón 3", command=boton_3_presionado)
boton3.place(x=20, y=250, width=200, height=25)

etiqueta = tk.Label(ventana, text="ingresa tu nombre")
etiqueta.place(x=20, y=90)

ventana.mainloop()