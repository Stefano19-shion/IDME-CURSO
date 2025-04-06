from os import system  

import gestion_musica
import almacenamiento #Importamos los módulos para poder usar sus funciones.
import tkinter as tk
from gestion_musica import agregarCancion, mostrarColeccion

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Música 🎵")
ventana.geometry("500x400")

# Etiqueta de título
lblTitulo = tk.Label(ventana, text="Mi Colección de Música", font=("Arial", 14, "bold"))
lblTitulo.pack(pady=10)

coleccion = []  

# Botón para agregar una canción
btnAgregar = tk.Button(ventana, text="Agregar Canción", command=lambda: agregarCancion(coleccion))
btnAgregar.pack(pady=5)

# Botón para mostrar canciones
btnMostrar = tk.Button(ventana, text="Mostrar Canciones", command=lambda: mostrarColeccion(coleccion))
btnMostrar.pack(pady=5)

# Mantener la ventana abierta
ventana.mainloop()




             
