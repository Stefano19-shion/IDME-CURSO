def agregarCancion(coleccion):
    """Agrega una canción a la colección."""
    titulo = input("Título de la canción: ")
    artista = input("Artista: ")
    genero = input("Género: ")
    anio = input("Año de lanzamiento: ")
    
    cancion = {
        "titulo": titulo,
        "artista": artista,
        "genero": genero,
        "anio": anio
    }
    
    coleccion.append(cancion)
    print("✅ Canción agregada con éxito.")

def mostrarColeccion(coleccion):
    """Muestra todas las canciones de la colección."""
    if not coleccion:
        print("⚠️ La colección está vacía.")
        return

    print("\n🎼 Lista de canciones:")
    for idx, cancion in enumerate(coleccion, start=1):
        print(f"{idx}. {cancion['titulo']} - {cancion['artista']} ({cancion['anio']}) [{cancion['genero']}]")