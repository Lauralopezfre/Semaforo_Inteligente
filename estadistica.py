from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd

# Creación de la ventana
window = Tk() 
window.title("Resultados semaforo inteligente")

# Propiedades de la ventana
window.geometry('750x650')

titulo = Label(window, text="Estadisticas semaforo inteligente", font=("Arial Bold", 15))
titulo.grid(column=0, row=0)

pruebaBoton = Label(window, text="")
pruebaBoton.grid(column=1, row=2)

btnBorrar = Button(window, text="Borrar datos")
btnBorrar.grid(column=0, row=1)
btnTerminar = Button(window, text="Terminar")
btnTerminar.grid(column=1, row=1)

# Grafico
fig, axs = plt.subplots(1,3, dpi=80, figsize=(13, 4), sharey=True, facecolor='#0FA49F')


# Acciones botones
def borrar():
    pruebaBoton.configure(text="Se clickeo el boton de borrar")

def terminar():
    # Mensaje para mostrar el resultado final al terminar
    messagebox.showinfo('Resultado final', 'Tantos accidentes')

# Configuración botones
btnBorrar.configure(command=borrar)
btnTerminar.configure(command=terminar)



# Mostrar al usuario
window.mainloop()