from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

import tkinter as tk
from tkinter import Grid


import tkinter as tk
from tkinter import messagebox
import os



ventana = tk.Tk()
ventana.config(width=600, height=550)
ventana.title("Creador de archivos")

tk.Label(ventana, text="Nombre del archivo", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
entrada_nombre = tk.Entry(ventana, font=("Arial", 14))
entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Contenido del archivo", font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=10)
entrada_contenido = tk.Text(ventana, font=("Arial", 14), width=35, height=10)
entrada_contenido.grid(row=1, column=1, padx=10, pady=10)

boton_1 = tk.Button(ventana, text="Crear Archivo", font=("Arial", 16) )



ventana.mainloop()