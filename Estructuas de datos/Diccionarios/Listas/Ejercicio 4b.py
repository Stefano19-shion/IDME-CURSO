"""Un programa que lea por teclado una frase y nos devuelva un diccionario
 con la cantidad de apariciones de cada carácter en la cadena."""

# Importación de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:

letras = {} # Diccionario que contendrá las letras (clave) y el nº de veces que aparecen (valor).
letra = "" # Una letra individual de la frase.
frase = "" # Frase que pedimos por teclado y escaneamos

# Programa principal:

system("cls") # Borra la pantalla.
frase = input("Teclea la frase: ")

for letra in frase: # Recorro toda la frase, como una lista.
    if letra != " ":
        if letra in letras: # Miro si la letra está dentro de las claves del diccionario.
            letras[letra] += 1 # Incremento en 1 el nº de apariciones de la letra.
        else:
            letras[letra] = 1 # Añado la letra por primera vez.

for letra in letras:
    print(f"La letra {letra} aparece {letras[letra]}.")
