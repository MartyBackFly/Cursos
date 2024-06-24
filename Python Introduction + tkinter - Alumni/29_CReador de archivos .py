from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

import tkinter as tk
from tkinter import messagebox

def crear_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    print(f"Archivo {nombre_archivo} creado con éxito.")
    messagebox.showinfo("Información", f"Archivo {nombre_archivo} creado con éxito.")

def boton_presionado():
    nombre_archivo = entrada_nombre.get()
    contenido = entrada_contenido.get("1.0", tk.END)  # Obtiene todo el contenido del Text widget
    if nombre_archivo and contenido:
        crear_archivo(nombre_archivo, contenido)
        label_result_1.config(text=f"Archivo {nombre_archivo} creado")
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa un nombre de archivo y su contenido.")

# Creación de la ventana principal de la interfaz gráfica
ventana = tk.Tk()
ventana.config(width=500, height=400)
ventana.title("Creador de Archivos")

# Creación de etiquetas y campos de entrada para el nombre del archivo y su contenido
tk.Label(ventana, text="Nombre del archivo:", font=("Arial", 14)).place(x=20, y=20)
entrada_nombre = tk.Entry(ventana, font=("Arial", 14), width=30)
entrada_nombre.place(x=180, y=20)

tk.Label(ventana, text="Contenido del archivo:", font=("Arial", 14)).place(x=20, y=60)
entrada_contenido = tk.Text(ventana, font=("Arial", 14), width=40, height=10)
entrada_contenido.place(x=180, y=60)

# Creación del botón y asignación de la función que se ejecutará al ser presionado
boton_1 = tk.Button(ventana, text="Crear archivo", font=("Arial", 18), command=boton_presionado)
boton_1.place(x=20, y=300)

# Creación de una etiqueta que se actualizará cuando se presione el botón
label_result_1 = tk.Label(ventana, text="", font=("Arial", 18))
label_result_1.place(x=180, y=300)

# Inicia el bucle principal de la interfaz gráfica
ventana.mainloop()
