import tkinter as tk
from tkinter import messagebox
from almacenamiento import guardar_cancion , cargar_coleccion

def agregarCancion(titulo, artista, anio):
    def guardar():
        cancion = {
            "titulo": entrada_titulo.get(),
            "artista": entrada_artista.get(),
            "genero": entrada_genero.get(),
            "año": entrada_anio.get()
        }

        if all(cancion.values()):
            guardar_cancion(cancion)
            messagebox.showinfo("✅ Canción guardada", "La canción fue guardada correctamente.")
            ventana_agregar.destroy()
        else:
            messagebox.showwarning("❗ Campos incompletos", "Por favor, completa todos los campos.")

    ventana_agregar = tk.Toplevel()
    ventana_agregar.title("Agregar Canción")
    ventana_agregar.geometry("300x250")

    tk.Label(ventana_agregar, text="Título:").pack()
    entrada_titulo = tk.Entry(ventana_agregar)
    entrada_titulo.pack()

    tk.Label(ventana_agregar, text="Artista:").pack()
    entrada_artista = tk.Entry(ventana_agregar)
    entrada_artista.pack()

    tk.Label(ventana_agregar, text="Género:").pack()
    entrada_genero = tk.Entry(ventana_agregar)
    entrada_genero.pack()

    tk.Label(ventana_agregar, text="Año:").pack()
    entrada_anio = tk.Entry(ventana_agregar)
    entrada_anio.pack()

    tk.Button(ventana_agregar, text="Guardar", command=guardar).pack(pady=10)

from almacenamiento import cargar_coleccion

def mostrarColeccion():
    coleccion = cargar_coleccion()

    ventana_mostrar = tk.Toplevel()
    ventana_mostrar.title("Colección de Música")
    ventana_mostrar.geometry("400x300")

    if not coleccion:
        tk.Label(ventana_mostrar, text="⚠️ La colección está vacía.").pack()
    else:
        for cancion in coleccion:
            texto = f"{cancion['titulo']} - {cancion['artista']} ({cancion['año']})"
            tk.Label(ventana_mostrar, text=texto).pack(anchor="w")
import json

def buscar_cancion_por_titulo(titulo_busqueda):
    try:
        with open("coleccion_musica.json", "r") as archivo:
            canciones = json.load(archivo)
            resultados = [c for c in canciones if titulo_busqueda.lower() in c["titulo"].lower()]
            return resultados
    except FileNotFoundError:
        return []
