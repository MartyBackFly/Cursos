from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


import tkinter as tk
import random
####################################
def arrojar():
 caja.delete(0,tk.END)
 valor = random.randint(1,6)
 caja.insert(0,valor)
####################################
ventana = tk.Tk()
ventana.config(width=220,height=200)
ventana.title("Dado 2.0")
boton = tk.Button(text="Arrojar el dado",command=arrojar)

boton.place(x=60,y=40,width=100,height=50)
etq = tk.Label(text="Valor: ")
etq.place(x=60,y=110)
caja = tk.Entry()
caja.place(x=60,y=140,width=100)
ventana.mainloop()
