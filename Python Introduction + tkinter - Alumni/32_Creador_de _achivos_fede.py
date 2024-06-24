from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

import tkinter as tk
from tkinter import messagebox, filedialog
import os


#creado por FedeHotarola@gmail.com

# https://www.youtube.com/@Marty-Back-Fly
# ctrl + click para link rapido


# hecho con auto-py-to-exe



def crear_archivo(nombre_archivo, contenido, ruta, cantidad, extencion):
    
    for i in range (1, cantidad+1):
        nombre_archivo_extencion = f"{nombre_archivo}_{i}{extencion}"
        ruta_completa = os.path.join(ruta, nombre_archivo_extencion)
        with open(ruta_completa, 'w') as archivo:
            archivo.write(contenido)

    messagebox.showinfo("informacion", f"{cantidad} archivo - {nombre_archivo}{extencion} - creado ! ")



def boton_press():
    
    nombre_archivo = entrada_nombre.get()
    contenido = entrada_contenido.get("1.0", tk.END) # el primer carácter ("1.0") hasta el final del texto (tk.END).
    ruta = getattr(label_ruta, 'ruta', None)
    
    try : 
        cantidad = int(cantidad_1.get())
    except:
        cantidad = 1
    
    extencion = entrada_ext.get()
    
    
    if not ruta:
        messagebox.showwarning("Atencion  tenemos un 3312 ", "Seleccione una ruta.....")
        return
    
    if not nombre_archivo:
        
        messagebox.showwarning("  advertencing xD  ", "Archivo creado sin nombre" )
        

    


    crear_archivo(nombre_archivo, contenido, ruta, cantidad, extencion)

def select_path():
    path_selected = filedialog.askdirectory()
    if path_selected:
        
        if len(path_selected) > 50:
            full = len(path_selected) 
            medio = full // 2
            label_ruta.config(text=f"{path_selected[:medio]} \n {path_selected[medio:]}" )
            label_ruta.ruta = path_selected
            ruta = path_selected
            return ruta
        else:
            label_ruta.config(text=f"{path_selected}" )
            label_ruta.ruta = path_selected
            ruta = path_selected
            return ruta

ventana = tk.Tk()
ventana.config(width=650, height=550)
ventana.title("Creador de archivos")




tk.Label(ventana, text="Nombre del archivito", font=("Arial", 12)).place(x=16, y=20)
entrada_nombre = tk.Entry(ventana, font=("Arial", 14), width=18)
entrada_nombre.place(x=190, y=20)

tk.Label(ventana, text="Extension", font=("Arial", 12)).place(x=420, y=20)
entrada_ext = tk.Entry(ventana, font=("Arial", 14), width=5)
entrada_ext.place(x=500, y=20)

tk.Label(ventana, text="Cantidad de archivitos", font=("Arial", 12)).place(x=16, y=60)
cantidad_1 = tk.Entry(ventana, font=("Arial, 14"), width=18)
cantidad_1.place(x=190, y= 60)


tk.Label(ventana, text="Contenido del archivito", font=("Arial", 12)).place(x=16, y=120)
entrada_contenido = tk.Text(ventana, font=("Arial, 14"), width=28, height=10)
entrada_contenido.place(x=190, y= 120)

boton_1 = tk.Button(ventana, text="Crear Archivo", font=("Arial" , 16), command=boton_press)
boton_1.place(x=220 , y=490)

boton_ruta = tk.Button(ventana, text="Selecciona ruta ", font=("Arial", 13 ), command=select_path)
boton_ruta.place(x=20, y=375)

label_ruta = tk.Label(ventana, text="" , font=("Arial" , 12)  )
label_ruta.place(x=182 , y=379)



ventana.mainloop()