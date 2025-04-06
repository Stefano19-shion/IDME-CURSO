from tkinter import *
from gestion_musica import agregarCancion, mostrarColeccion, buscar_cancion_por_titulo
import tkinter as tk
from tkinter import simpledialog, messagebox
# Crear ventana principal
ventana = Tk()
ventana.title("Gestor de Música 🎵")
ventana.geometry("500x400")
ventana.configure(bg="#f5f5f5")

# Etiqueta de título
titulo_label = Label(ventana, text="Mi Colección de Música", font=("Arial", 16, "bold"), bg="#f5f5f5")
titulo_label.pack(pady=10)

# Entradas
Label(ventana, text="Título:", bg="#f5f5f5").pack()
entrada_titulo = Entry(ventana)
entrada_titulo.pack()

Label(ventana, text="Artista:", bg="#f5f5f5").pack()
entrada_artista = Entry(ventana)
entrada_artista.pack()

Label(ventana, text="Año:", bg="#f5f5f5").pack()
entrada_anio = Entry(ventana)
entrada_anio.pack()

# Función al presionar botón
def agregar():
    titulo = entrada_titulo.get()
    artista = entrada_artista.get()
    anio = entrada_anio.get()
    agregarCancion(titulo, artista, anio)
    entrada_titulo.delete(0, END)
    entrada_artista.delete(0, END)
    entrada_anio.delete(0, END)

# Botón agregar
boton_agregar = Button(ventana, text="Agregar Canción", command=agregar)
boton_agregar.pack(pady=10)

# Botón mostrar
boton_mostrar = Button(ventana, text="Mostrar Canciones", command=mostrarColeccion)
boton_mostrar.pack()

ventana.mainloop()
def buscar():
    titulo = simpledialog.askstring("Buscar", "Ingresa el título a buscar:")
    if titulo:
        resultados = buscar_cancion_por_titulo(titulo)
        if resultados:
            mensaje = "\n".join([f"{c['titulo']} - {c['artista']} ({c['año']})" for c in resultados])
        else:
            mensaje = "No se encontraron canciones."
        messagebox.showinfo("Resultados", mensaje)

# Agregar botón en la interfaz
btn_buscar = tk.Button(ventana, text="Buscar Canción", command=buscar)
btn_buscar.pack(pady=5)