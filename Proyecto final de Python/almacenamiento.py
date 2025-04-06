import json
import os

archivo_json = "coleccion_musica.json"

def cargar_coleccion():
    if not os.path.exists(archivo_json):
        return []
    with open(archivo_json, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def guardar_cancion(cancion):
    coleccion = cargar_coleccion()
    coleccion.append(cancion)
    with open(archivo_json, "w", encoding="utf-8") as f:
        json.dump(coleccion, f, indent=4, ensure_ascii=False)
