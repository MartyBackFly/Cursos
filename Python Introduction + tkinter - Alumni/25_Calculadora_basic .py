from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

import tkinter as tk
from tkinter import messagebox

def agregar_a_entrada(valor):
    entrada.insert(tk.END, valor)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Error", "Entrada no válida")

def limpiar():
    entrada.delete(0, tk.END)

ventana = tk.Tk()
ventana.config(width=400, height=400)
ventana.title("Calculadora")

# Entrada de texto
entrada = tk.Entry(ventana, font=("Arial", 18), justify="right")
entrada.place(x=20, y=20, width=360, height=50)

# Botones de números
numeros = [
    ('7', 20, 100), ('8', 120, 100), ('9', 220, 100),
    ('4', 20, 160), ('5', 120, 160), ('6', 220, 160),
    ('1', 20, 220), ('2', 120, 220), ('3', 220, 220),
    ('0', 20, 280)
]

for (texto, x, y) in numeros:
    boton = tk.Button(ventana, text=texto, command=lambda t=texto: agregar_a_entrada(t), font=("Arial", 18))
    boton.place(x=x, y=y, width=80, height=60)

# Botones de operaciones
operaciones = [
    ('+', 320, 100), ('-', 320, 160), 
    ('*', 320, 220), ('/', 320, 280),
    ('=', 220, 280), ('C', 120, 280)
]

for (texto, x, y) in operaciones:
    if texto == '=':
        boton = tk.Button(ventana, text=texto, command=calcular, font=("Arial", 18))
    elif texto == 'C':
        boton = tk.Button(ventana, text=texto, command=limpiar, font=("Arial", 18))
    else:
        boton = tk.Button(ventana, text=texto, command=lambda t=texto: agregar_a_entrada(t), font=("Arial", 18))
    boton.place(x=x, y=y, width=80, height=60)

ventana.mainloop()
