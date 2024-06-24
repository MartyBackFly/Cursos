from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az
import tkinter as tk
import random



def boton_presionado():
    resultado = random.randint(1, 6)
    etiqueta_resultado1.config(text=f"-- >>", font=("Arial", 18, "bold"))
    etiqueta_resultado2.config(text=f" {resultado}", font=("Arial", 28, "bold"))

ventana = tk.Tk()
ventana.config(width=500, height=300)
ventana.title("Tirar el dado")

boton = tk.Button(ventana, text="Arrojar dado", command=boton_presionado)
boton.place(x=20, y=120, width=200, height=25)

etiqueta = tk.Label(ventana, text="Presiona el botón para arrojar el dado", font=("Arial", 18))
etiqueta.place(x=20, y=90, anchor="w")

etiqueta_resultado1 = tk.Label(ventana, text="", font=("Arial", 18))
etiqueta_resultado1.place(x=20, y=170)

etiqueta_resultado2 = tk.Label(ventana, text="", font=("Arial", 18))
etiqueta_resultado2.place(x=80, y=160)

ventana.mainloop()