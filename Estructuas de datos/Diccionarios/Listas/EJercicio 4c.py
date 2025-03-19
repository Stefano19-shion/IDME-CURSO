
"""Escribir un programa que cree un diccionario simulando una cesta
 de la compra. El programa debe preguntar el artículo y su precio
y añadirlo al diccionario, hasta que el usuario decida terminar.
Después se debe mostrar por pantalla la lista de la compra y el coste
 total."""

# Importación de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:

compra = {} # Diccionario que la lista de la compra.
producto = " " # Nombre del artículo
precio = 0 # Precio del artículo
importeTotal = 0 # Acumula el importe total de la compra.

# Programa principal:

system("cls") # Borra la pantalla.

while producto != "": # Bucle para pedir los productos
    producto = input("Teclea el producto (ENTER para finalizar): ")
    if producto != "":
        precio = float(input("Introduce el precio del producto: "))
        compra[producto] = precio
    print("") # Salto de línea para separar asignaturas.

print("***** Lista de la compra *****")
print("")
for producto in compra:
    print(f"Artículo: {producto}, precio: {compra[producto]}")
    importeTotal = importeTotal + compra[producto]

print("")
print(f"Importe total compra: {importeTotal}")

