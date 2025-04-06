"""Escribir una función que reciba como parámetro una cadena de palabras separadas por espacios (frase)
 y devuelva, como resultado, cuántas palabras de más de 4 letras tiene la cadena dada.
 """

# Importación de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:

frase = ""

# Definición de funciones:

def contarPalabras(frase):
    j = 0 # Índice que cuenta el número de letras por palabra.
    letra = 0 # Cada una de las letras de la cadena de caracteres.
    contadorPalabras = 0 # Cuenta el número de palabras con más de 4 letras.

    for letra in frase: # Recorro toda la cadena.
        if letra == " ": # Si la letra es un espacio o está al final de la frase.
            if j > 4: # Si he contado más de 4 letras antes de llegar al espacio.
                contadorPalabras = contadorPalabras + 1
            j = 0 # Pongo a 0 el contador de letras por palabra.
        j = j + 1 # Cuenta una nueva letra más.
    
    if j > 4: # Después de salir de recorrer la cadena, miro cuántas letras tiene la última palabra.
        contadorPalabras += 1 
    return contadorPalabras

# Programa principal.

system("cls")

frase = input("Introduce la frase a escanear: ")
print(contarPalabras(frase))