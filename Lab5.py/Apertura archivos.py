#odulo interfaz grafica
import tkinter as tk 

#Submodulo carpetas y archivos

from tkinter import filedialog

#Crear ventana grafica
root = tk.Tk()
root.withdraw()

#Abrir cuadro de dialogo 
ruta = filedialog.askopenfilename(title = "Seleccione un archivo", filetypes= [("Archivos de texto", "*.txt")])

print(ruta)

if ruta:
    try:
        with open(ruta,"r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except:
        print("Error al abrir el archivo")
else:
    print("Debe de escoger un archivo")