
from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


"""Claro, te explico las diferencias y la razón detrás de usar get() para nombre_archivo y contenido, y getattr() para ruta.

1. get() para nombre_archivo y contenido
Contexto: nombre_archivo y contenido se obtienen a partir de widgets de entrada de Tkinter (tk.Entry y tk.Text respectivamente).
Función: get() es un método de estos widgets que se utiliza para recuperar el texto que el usuario ha introducido en los campos de entrada.

nombre_archivo = entrada_nombre.get()
contenido = entrada_contenido.get("1.0", tk.END)
entrada_nombre.get() devuelve el texto del widget Entry.
entrada_contenido.get("1.0", tk.END) devuelve todo el contenido del widget Text desde el primer carácter ("1.0") hasta el final del texto (tk.END).

2. getattr() para ruta

Contexto: ruta es un atributo que se espera que esté en un objeto label_ruta.
Función: getattr() es una función de Python que se utiliza para obtener el valor de un atributo de un objeto de manera segura, permitiendo especificar un valor predeterminado en caso de que el atributo no exista.


python
Copiar código

ruta = getattr(label_ruta, 'ruta', None)
getattr(label_ruta, 'ruta', None) intenta obtener el valor del atributo ruta del objeto label_ruta.
Si label_ruta tiene un atributo llamado ruta, getattr devolverá su valor.
Si label_ruta no tiene un atributo llamado ruta, getattr devolverá None.

Razón de Uso
get(): Se usa porque nombre_archivo y contenido son datos introducidos por el usuario y almacenados en widgets de Tkinter. Estos widgets tienen el método get() para acceder a sus contenidos.
getattr(): Se usa porque ruta no proviene directamente de un widget de Tkinter sino que es un atributo que podría o no estar presente en el objeto label_ruta. getattr() permite acceder a este atributo de forma segura, proporcionando un valor por defecto (None en este caso) si el atributo no está definido.
Ejemplo Completo
Supongamos que label_ruta es un tk.Label al que se le ha agregado dinámicamente un atributo ruta. Podría verse algo así:

"""
import tkinter as tk
from tkinter import messagebox
import os

def boton_press():
    nombre_archivo = entrada_nombre.get()
    contenido = entrada_contenido.get("1.0", tk.END)
    ruta = getattr(label_ruta, 'ruta', None)
    
    if not nombre_archivo:
        nombre_archivo = "Nuevo Archivo"
        messagebox.showwarning("advertencia xD", "Archivo creado sin nombre")
    
    crear_archivo(nombre_archivo, contenido, ruta)

def crear_archivo(nombre_archivo, contenido, ruta):
    if ruta:
        nombre_archivo = os.path.join(ruta, nombre_archivo)
    
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    
    messagebox.showinfo("información", f"Archivo {nombre_archivo} creado!")

ventana = tk.Tk()
ventana.config(width=600, height=550)
ventana.title("Creador de archivos")

tk.Label(ventana, text="Nombre del archivo", font=("Arial", 12)).place(x=20, y=20)
entrada_nombre = tk.Entry(ventana, font=("Arial", 14))
entrada_nombre.place(x=180, y=20)

tk.Label(ventana, text="Contenido del archivo", font=("Arial", 12)).place(x=20, y=60)
entrada_contenido = tk.Text(ventana, font=("Arial", 14), width=35, height=10)
entrada_contenido.place(x=180, y=60)

label_ruta = tk.Label(ventana, text="Ruta", font=("Arial", 12))
label_ruta.place(x=20, y=100)
label_ruta.ruta = "/path/to/directory"  # Añadir dinámicamente el atributo ruta

boton_1 = tk.Button(ventana, text="Crear Archivo", font=("Arial", 16), command=boton_press)
boton_1.place(x=20, y=300)

ventana.mainloop()


# En este ejemplo, label_ruta.ruta se establece manualmente para ilustrar cómo getattr funciona para acceder a ese atributo.






