# Importar la biblioteca tkinter bajo el alias tk
import tkinter as tk
#modifique este archivo
# Importar la constante END del módulo tkinter
from tkinter import END
# Importar el módulo math para operaciones matemáticas avanzadas
import math

# Crear la ventana principal de la calculadora
root = tk.Tk()
# Establecer el título de la ventana
root.title("Calculadora")
# Configurar las dimensiones de la ventana
root.config(width=300, height=450)

# Declarar variables globales para almacenar temporales y operadores
aux = 0
signo = ""

# Función para manejar la selección de operadores
def operador(x):
    global signo, aux
    # Almacenar el operador seleccionado y el valor actual
    signo = x
    aux = float(txtDisplay.get())
    # Borrar el contenido del campo de entrada
    txtDisplay.delete(0, END)

# Función para realizar las operaciones matemáticas
def operacion():
    resultado = 0
    global signo, aux
    # Realizar la operación correspondiente según el operador seleccionado
    if signo == "+":
        resultado = aux + float(txtDisplay.get())
    elif signo == "-":
        resultado = aux - float(txtDisplay.get())
    elif signo == "*":
        resultado = aux * float(txtDisplay.get())
    elif signo == "/":
        resultado = aux / float(txtDisplay.get())
    elif signo == "^":
        resultado = aux ** float(txtDisplay.get())
    elif signo == "%":
        resultado = aux * (float(txtDisplay.get()) / 100)  # Cálculo del porcentaje
    elif signo == "sqrt":
        resultado = math.sqrt(aux)
    elif signo == "n!":
        resultado = math.factorial(int(aux))

    # Borrar el contenido del campo de entrada y mostrar el resultado
    txtDisplay.delete(0, END)
    txtDisplay.insert(0, str(resultado))

# Función para agregar números al campo de entrada
def agregar_numero(numero):
    valor_actual = txtDisplay.get()
    txtDisplay.delete(0, END)
    txtDisplay.insert(0, valor_actual + str(numero))

# Crear un campo de entrada para mostrar números y resultados
txtDisplay = tk.Entry(root)
txtDisplay.place(x=10, y=20)

# Crear botones numéricos del 0 al 9
for i in range(10):
    # Asignar el número correspondiente al botón y llamar a la función agregar_numero
    tk.Button(root, text=str(i), command=lambda num=i: agregar_numero(num)).place(x=30 + (i % 3) * 50, y=140 + (i // 3) * 50)

# Crear botones de operación
tk.Button(root, text="+", command=lambda: operador("+")).place(x=230, y=140)
tk.Button(root, text="-", command=lambda: operador("-")).place(x=230, y=190)
tk.Button(root, text="*", command=lambda: operador("*")).place(x=230, y=240)
tk.Button(root, text="/", command=lambda: operador("/")).place(x=180, y=290)
tk.Button(root, text="^", command=lambda: operador("^")).place(x=130, y=290)
tk.Button(root, text="%", command=lambda: operador("%")).place(x=180, y=140)
tk.Button(root, text="sqrt", command=lambda: operador("sqrt")).place(x=180, y=190)
tk.Button(root, text="n!", command=lambda: operador("n!")).place(x=180, y=240)
tk.Button(root, text="=", command=operacion).place(x=80, y=290)

# Etiquetas para mostrar las conversiones de base numérica
tk.Label(root, text="DEC:").place(x=10, y=40)
tk.Label(root, text="OCT:").place(x=10, y=60)
tk.Label(root, text="HEX:").place(x=10, y=80)
tk.Label(root, text="BIN:").place(x=10, y=100)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
