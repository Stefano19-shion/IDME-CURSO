"""Programa que cree una función que nos devuelva True si un valor parámetro está
 dentro de un rango, que también introduciremos como parámetros. Si no es así,
   devolverá False. """

# Importación de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:

numero = 0 # Contendrá el valor a comprobar si están dentro del rango.
limiteInferior = 0 # Valor del límite inferior del intervalo.
limiteSuperior = 0 # Valor del límite superior del intervalo.

# Definición de funciones:

def intervalo(num, limInferior, limSuperior):
    if num >= limInferior and num <= limSuperior:
        return True
    else:
        return False


# Programa principal:

system("cls")

numero = int(input("Teclea el número a comprobar: "))
limiteInferior = int(input("Introduce el límite inferior del intervalo: "))
limiteSuperior = int(input("Introduce el límite superior del intervalo: "))

if intervalo(numero, limiteInferior, limiteSuperior):
    print("El valor está dentro del intervalo!!")
else:
    print("El valor está fuera del intervalo!!")

