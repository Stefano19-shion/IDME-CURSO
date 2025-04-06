"""Programa que cree una función que al introducir un valor numérico natural
por teclado, nos diga si es  un número primo o no.
 """

# Importación de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:

numero = 0 # Contendrá el valor a comprobar si es primo.

# Definición de funciones:

def esPrimo(numero):
    for i in range(2, numero):
        if numero % i == 0: # si el resto de la división es 0, no es Primo.
            return False # Devuelvo "False" porque no es primo
    return True # Si sale del bucle y llega aquí es porque todos los restos NO son 0.

# Programa principal:

system("cls")

numero = int(input("Introduce un valor para comprobar si es número primo: "))
if esPrimo(numero) == True:
    print("El número introducido SÍ es primo!!")
else:
    print("El número introducido NO es primo!!")