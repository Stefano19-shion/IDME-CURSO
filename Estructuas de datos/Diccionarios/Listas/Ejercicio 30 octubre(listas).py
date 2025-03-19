"""Simula una lista de compras. El programa debe permitir al usuario realizar las siguientes operaciones:
1.- Agregar un artículo a la lista de compras.
2.- Eliminar un artículo de la lista de compras.
3.- Mostrar los artículos que están actualmente en la lista.
4.- Salir del programa. """

# Importanción de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:
listaCompra = [] # La lista que contendrá todos los elementos.
opcion = 0 # Contiene el valor de la opción escogida por teclado.
nombre = "" # Contendrá el nombre del elemnto de la lista a añadir o borrar.

# Programa principal:

while opcion != 4:

    system("cls")

    print("") # Salto de línea para dejar una línea en blanco.
    print("***************   MENÚ PRINCIPAL  ****************")
    print("1.- Agregar un artículo a la lista de la compra.")
    print("2.- Eliminar un artículo a la lista de la compra.")
    print("3.- Mostar todos los artículos de la lista de la compra.")
    print("4.- Salir del programa")
    print("")
    opcion = int(input("Elige la opción correspondiente... "))

    if opcion == 1:
        print("") # Hago un salto de línea.
        nombre = input("Introduce el nombre del nuevo artículo: ")
        nombre = nombre.capitalize()
        if nombre in listaCompra:
            print("Error: El artículo ya se encuentra en la lista")
            print("")
            input("Pulsa una tecla para continuar...")
        else:
            listaCompra.append(nombre)
            print(f"El artículo '{nombre}' ha sido añadido a la lista correctamente")
            print("")
            input("Pulsa una tecla para continuar...")

    if opcion == 2:
       print("")
       nombre = nombre.capitalize()
       nombre = input("iIntroduce el nombre del articulo a eliminar :")
       if nombre in listaCompra:
            listaCompra.remove(nombre)
            print(f"El articulo {nombre} ha sido eliminado correctamente de la lista de la compra")
            print("")
            input("Pulsa una tecla para continuar...")
       else:
           print(f"Error: El articulo{nombre} NO se encuentra en la lista")
           print("")
           input("Pulsa una tecla para continuar...")
           
    
    
    if opcion == 3:
        print("")
        if listaCompra == ():
         print("Lista de compra vacia.")
        else:
         for articulo in listaCompra: #Recorro la lista completa.
            print(f"- {articulo} .")
        input("Pulsa una tecla para continuar...")
   

