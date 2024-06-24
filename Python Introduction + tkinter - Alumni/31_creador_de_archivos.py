from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


import tkinter as tk
from tkinter import messagebox, filedialog
import os

def crear_archivos(ruta, nombre_base, contenido, cantidad):
    for i in range(1, cantidad + 1):
        nombre_archivo = f"{nombre_base}_{i}.txt"
        ruta_completa = os.path.join(ruta, nombre_archivo)
        with open(ruta_completa, 'w') as archivo:
            archivo.write(contenido)
        print(f"Archivo {nombre_archivo} creado con éxito en {ruta_completa}.")
    messagebox.showinfo("Información", f"Se han creado {cantidad} archivos con éxito en {ruta}.")

def seleccionar_ruta():
    ruta_seleccionada = filedialog.askdirectory()
    if ruta_seleccionada:
        label_ruta.config(text=f"Ruta seleccionada: {ruta_seleccionada}")
        label_ruta.ruta = ruta_seleccionada

def boton_presionado():
    nombre_base = entrada_nombre.get()
    contenido = entrada_contenido.get("1.0", tk.END)  # Obtiene todo el contenido del Text widget
    ruta = getattr(label_ruta, 'ruta', None)
    cantidad_str = entrada_cantidad.get()
    
    if not ruta:
        messagebox.showwarning("Advertencia", "Por favor selecciona una ruta.")
        return

    if not nombre_base or not contenido.strip():
        messagebox.showwarning("Advertencia", "Por favor ingresa un nombre de archivo y su contenido.")
        return

    try:
        cantidad = int(cantidad_str)
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Advertencia", "Por favor ingresa una cantidad válida (número entero positivo).")
        return

    crear_archivos(ruta, nombre_base, contenido, cantidad)
    label_result_1.config(text=f"{cantidad} archivos creados con el nombre base '{nombre_base}'")

# Creación de la ventana principal de la interfaz gráfica
ventana = tk.Tk()
ventana.config(width=500, height=600)
ventana.title("Creador de Archivos")

# Creación de etiquetas y campos de entrada para el nombre del archivo y su contenido
tk.Label(ventana, text="Nombre base del archivo:", font=("Arial", 14)).place(x=20, y=20)
entrada_nombre = tk.Entry(ventana, font=("Arial", 14), width=30)
entrada_nombre.place(x=240, y=20)

tk.Label(ventana, text="Contenido del archivo:", font=("Arial", 14)).place(x=20, y=60)
entrada_contenido = tk.Text(ventana, font=("Arial", 14), width=40, height=10)
entrada_contenido.place(x=240, y=60)

# Creación de etiquetas y campos de entrada para la cantidad de archivos
tk.Label(ventana, text="Cantidad de archivos:", font=("Arial", 14)).place(x=20, y=300)
entrada_cantidad = tk.Entry(ventana, font=("Arial", 14), width=10)
entrada_cantidad.place(x=240, y=300)

# Botón para seleccionar la ruta
boton_ruta = tk.Button(ventana, text="Seleccionar ruta", font=("Arial", 14), command=seleccionar_ruta)
boton_ruta.place(x=20, y=350)

# Etiqueta para mostrar la ruta seleccionada
label_ruta = tk.Label(ventana, text="Ruta no seleccionada", font=("Arial", 14))
label_ruta.place(x=240, y=350)

# Creación del botón y asignación de la función que se ejecutará al ser presionado
boton_1 = tk.Button(ventana, text="Crear archivos", font=("Arial", 18), command=boton_presionado)
boton_1.place(x=20, y=450)

# Creación de una etiqueta que se actualizará cuando se presione el botón
label_result_1 = tk.Label(ventana, text="", font=("Arial", 18))
label_result_1.place(x=240, y=450)

# Inicia el bucle principal de la interfaz gráfica
ventana.mainloop()
