
import tkinter as tk
from tkinter import messagebox
import ast

# Funciones
def agregar_a_entrada(valor):
    entrada.insert(tk.END, valor)

def calcular():
    try:
        resultado = str(eval_expr(entrada.get()))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, resultado)
    except Exception as e:
        messagebox.showerror("Error", "Entrada no válida")

def eval_expr(expr):
    try:
        tree = ast.parse(expr, mode='eval')
        return eval(compile(tree, filename="", mode="eval"), {"__builtins__": {}}, {})
    except:
        raise ValueError("Invalid expression")

def limpiar():
    entrada.delete(0, tk.END)

# Configuración de la ventana principal
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


"""Explicación Paso a Paso
Importaciones
python
Copiar código
import tkinter as tk
from tkinter import messagebox
import ast
tkinter: Se importa la biblioteca tkinter para crear interfaces gráficas de usuario (GUIs).
messagebox: Se importa el módulo messagebox de tkinter para mostrar mensajes emergentes.
ast: Se importa el módulo ast para analizar y evaluar expresiones de manera segura.
Funciones
agregar_a_entrada
python
Copiar código
def agregar_a_entrada(valor):
    entrada.insert(tk.END, valor)
Esta función toma un valor (como un número o un operador) y lo agrega al final del contenido actual de la entrada de texto.
calcular
python
Copiar código
def calcular():
    try:
        resultado = str(eval_expr(entrada.get()))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, resultado)
    except Exception as e:
        messagebox.showerror("Error", "Entrada no válida")
Esta función se encarga de evaluar la expresión matemática ingresada.
entrada.get() obtiene el contenido de la entrada de texto.
eval_expr evalúa la expresión de manera segura.
Si la evaluación es exitosa, se borra el contenido de la entrada y se muestra el resultado.
Si ocurre un error (como una expresión no válida), se muestra un mensaje de error.
eval_expr
python
Copiar código
def eval_expr(expr):
    try:
        tree = ast.parse(expr, mode='eval')
        return eval(compile(tree, filename="", mode="eval"), {"__builtins__": {}}, {})
    except:
        raise ValueError("Invalid expression")
Esta función evalúa una expresión matemática de manera segura.
ast.parse analiza la expresión y la convierte en un árbol de sintaxis abstracta (AST).
compile compila el AST en código ejecutable.
eval evalúa el código compilado en un entorno restringido, sin acceso a funciones no seguras.
Si la expresión no es válida, se lanza un ValueError.
limpiar
python
Copiar código
def limpiar():
    entrada.delete(0, tk.END)
Esta función borra todo el contenido de la entrada de texto.
Configuración de la Ventana Principal
python
Copiar código
ventana = tk.Tk()
ventana.config(width=400, height=400)
ventana.title("Calculadora")
Se crea la ventana principal de la aplicación y se configura su tamaño y título.
Entrada de Texto
python
Copiar código
entrada = tk.Entry(ventana, font=("Arial", 18), justify="right")
entrada.place(x=20, y=20, width=360, height=50)
Se crea una entrada de texto (Entry) donde se mostrarán las expresiones matemáticas y resultados.
justify="right" alinea el texto a la derecha.
Botones de Números
python
Copiar código
numeros = [
    ('7', 20, 100), ('8', 120, 100), ('9', 220, 100),
    ('4', 20, 160), ('5', 120, 160), ('6', 220, 160),
    ('1', 20, 220), ('2', 120, 220), ('3', 220, 220),
    ('0', 20, 280)
]

for (texto, x, y) in numeros:
    boton = tk.Button(ventana, text=texto, command=lambda t=texto: agregar_a_entrada(t), font=("Arial", 18))
    boton.place(x=x, y=y, width=80, height=60)
Se crea una lista de tuplas que contienen el texto del botón y su posición (x, y).
Se crean los botones de números usando un bucle for.
command=lambda t=texto: agregar_a_entrada(t) asegura que cada botón agregue el texto correspondiente a la entrada.
Botones de Operaciones
python
Copiar código
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
Se crea una lista de tuplas que contienen el texto del botón y su posición (x, y).
Se crean los botones de operaciones usando un bucle for.
Dependiendo del texto del botón, se asigna la función correspondiente (calcular, limpiar o agregar_a_entrada).
Bucle Principal de la Ventana
python
Copiar código
ventana.mainloop()
Este comando inicia el bucle principal de la ventana, lo que permite que la aplicación responda a eventos (como clics de botones) y se mantenga abierta hasta que el usuario la cierre.
Este es un desglose detallado del código, paso a paso, para ayudarte a entender cómo funciona cada parte de la calculadora.


"""