from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

import tkinter as tk
import random

def boton_presionado():
    resultado = random.randint(1, 6)
    etiqueta_resultado.delete("1.0", tk.END)  # Borra el contenido actual de la etiqueta
    etiqueta_resultado.insert(tk.END, f"Salio: {resultado}", "salio")  # Inserta "Salio: " con estilo "salio"
    etiqueta_resultado.tag_config("salio", font=("Arial", 16, "bold"))  # Define el estilo "salio"

ventana = tk.Tk()
ventana.config(width=500, height=300)
ventana.title("Tirar el dado")

boton = tk.Button(ventana, text="Arrojar dado", command=boton_presionado)
boton.place(x=20, y=120, width=200, height=25)

etiqueta = tk.Label(ventana, text="Presiona el botón para arrojar el dado", font=("Arial", 18))
etiqueta.place(x=20, y=90, anchor="w")

etiqueta_resultado = tk.Text(ventana, wrap="word", font=("Arial", 24))
etiqueta_resultado.place(x=20, y=160, width=200, height=30)

ventana.mainloop()