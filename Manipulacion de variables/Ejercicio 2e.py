"""Programa que lee por teclado 2 números y diga cuál es mayor
 (supondremos que son diferentes).
"""
# Importación de librerías:
from os import system

# Declaración de variables.
numero1 = 0 # Contiene el primer número.
numero2 = 0 # Contendrá el segundo número.

system("cls") # Ejecuta el comando "cls" en Windows para borrar el terminal.

numero1 = int(input("Teclea el primer número: "))
numero2 = int(input("Teclea el segundo número: "))

if numero1 > numero2:
    print("El primer número es MAYOR que el segundo.")
else:
    print("El primer número es MENOR que el segundo.")

