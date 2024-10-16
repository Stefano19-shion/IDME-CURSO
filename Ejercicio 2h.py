"""Que el usuario introduzca un número por teclado y se asegure que está
 entre 1 y 10 (ambos incluídos). Si no lo es, que vuelva a pedirlo hasta que lo sea.
 Al final, muéstralo en pantalla."""

# Importación de librerías:
from os import system

# Declaración de variables:

numero = 0 # Valor que voy a pedir por teclado.

# Programa principal:

system("cls") # Borra la pantalla, en Windows.

while numero < 1 or numero > 10:
    numero = float(input("Introduce un número entre 1 y 10: "))

print(f"El número introducido es {numero}")

