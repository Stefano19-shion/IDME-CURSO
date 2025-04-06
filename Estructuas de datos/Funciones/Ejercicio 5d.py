"""Programa que cree reutilizando la función del apartado anterior, debemos indicar
 si son primos o no los valores numéricos de un rango introducido por teclado.
 """

# Importación de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:


numero = 0 # Contendrá el valor a comprobar si es primo.
limiteInferior = 0 # Límite inferior del intervalo de búsqueda.
limiteSuperior = 0 # Límite superior del intervalo de búsqueda.

# Definición de funciones:

def esPrimo(numero):
    for i in range(2, numero):
        if numero % i == 0: # si el resto de la división es 0, no es Primo.
            return False # Devuelvo "False" porque no es primo
    return True # Si sale del bucle y llega aquí es porque todos los restos NO son 0.

# Programa principal.

system("cls")

limiteInferior = int(input("Introduce el valor inferior del intervalo de números a comprobar si es primo: "))
limiteSuperior = int(input("Introduce el valor superior del intervalo de números a comprobar si es primo: "))

for numero in range(limiteInferior, limiteSuperior + 1):
    if esPrimo(numero) == True:
        print(f"El número {numero} SÍ es primo!!")
    else:
        print(f"El número {numero} NO es primo!!")
