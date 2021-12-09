import sys
print(sys.version)

from tkinter import * 
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np

# Creación de la ventana
window = Tk() 
window.title("Resultados semaforo inteligente")

# Propiedades de la ventana
window.geometry('750x650')

titulo = Label(window, text="Estadisticas semaforo inteligente", font=("Arial Bold", 15))
titulo.grid(column=0, row=0)

btnBorrar = Button(window, text="Borrar datos")
btnBorrar.grid(column=0, row=2)
btnTerminar = Button(window, text="Terminar")
btnTerminar.grid(column=1, row=2)

# Grafico
menu = ['Autos', 'Peatones']
colores = ['red', 'blue']
tamaño = [45, 55]
explotar = [0.05, 0.05]

fig, ax1 = plt.subplots(dpi=100, facecolor= '#0FA49F', figsize=(5,5))

plt.title("Accidentes automovilisticos", color='white', size=18, family='arial')
ax1.pie(tamaño, explode=explotar, labels=menu, colors=colores, autopct='%1.0f%%', pctdistance=0.6, shadow=True, startangle=90, radius=0.7, labeldistance=0.3)

ax1.axis('equal')

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().grid(column=0, row=1)

# Acciones botones
def borrar():
    messagebox.showinfo('Resultado final', 'Se borro')

def terminar():
    # Mensaje para mostrar el resultado final al terminar
    messagebox.showinfo('Resultado final', 'Tantos accidentes')

# Configuración botones
btnBorrar.configure(command=borrar)
btnTerminar.configure(command=terminar)

# Mostrar al usuario
# window.mainloop()

# Contectar con arduino 
import serial
from datetime import date, datetime, time
from BD.cruze import Cruze
from BD.cruzesBD import CruzesBD
from BD.persistenciaBD import PersistenciaBD
from BD.persistenciaException import PersistenciaException

persistencia = PersistenciaBD()
a = serial.Serial("COM13", 9600, timeout = 5) 

estado = ''
data = str(a.readline())
estado = data

valor = True
while True:
    data = str(a.readline())
    if(data == estado and data != "b''"):
        while valor:
            try:
                data = data[2:][:-5]
                cruze = Cruze(data, datetime.now(), True)
                persistencia.agregarCruze(cruze)
                valor=False
            except PersistenciaException as pe:
                print(pe.msj)
                print(pe.cause)
    elif data != "b''":
        valor=True
        estado = data
