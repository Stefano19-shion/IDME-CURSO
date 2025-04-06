""" Pedirá por teclado una palabra y hemos de decir si es un palíndromo o no.
"""

# Importación de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:
palabra = "" # Contendrá la palabra a comparar
i = 1 # Índice para recorrer la palabra, como una lista.
numVeces = 0 # Número de veces a iterar en las comparaciones de las letras.

# Programa principal:

system("cls")

palabra = input("Introduce la palabra a comprobar: ")

palabra = palabra.lower() # Convierto la palabra a minúsculas.
if len(palabra) % 2 == 1: # Longitud de palabra impar
    numVeces = len(palabra) / 2 - 1
else:
   numVeces = len(palabra) / 2

while i <= numVeces and palabra[i-1] == palabra[-i]:
    i = i + 1

if i > numVeces and palabra[i-1] == palabra[-i]: # Ha salido del bucle con todas las comparaciones buenas.
    print(f"La palabra {palabra} SI es un palíndromo.")
else:
    print(f"La palabra {palabra} NO es un palíndromo.")