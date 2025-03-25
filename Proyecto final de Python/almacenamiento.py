# almacenamiento.py
import json

ARCHIVO_JSON = "coleccion_musica.json"

def guardarDatos(coleccion):
    """Guarda la colección en un archivo JSON."""
    with open(ARCHIVO_JSON, "w") as archivo:
        json.dump(coleccion, archivo, indent=4)
    print("💾 Datos guardados correctamente.")

def cargarDatos():
    """Carga la colección desde el archivo JSON, si existe."""
    try:
        with open(ARCHIVO_JSON, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []  # Si el archivo no existe, devuelve una lista vacía