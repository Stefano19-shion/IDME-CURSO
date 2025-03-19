from os import system  

import gestion_musica
import almacenamiento

# Cargar la colección al iniciar
coleccion = almacenamiento.cargarDatos()

def mostrarMenu():
    while True:
        print("\n🎵 GESTOR DE COLECCIÓN DE MÚSICA 🎵")
        print("1. Agregar canción")
        print("2. Mostrar colección")
        print("3. Guardar y salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            gestion_musica.agregarCancion(coleccion)
        elif opcion == "2":
            gestion_musica.mostrarColeccion(coleccion)
        elif opcion == "3":
            almacenamiento.guardarDatos(coleccion)
            print("Colección guardada. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    mostrarMenu()
