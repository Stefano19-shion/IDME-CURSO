"""Programa que suma los primeros N números pares."""

# Declaración de variables:

numeroPar = 0 # Número par, incrementado de 2 en 2.
contador = 0 # Valor para contar el total de números (debe ser 50 al final).
sumaNumeros = 0 # Para ir acumulando la suma de los valores.
valorFinal = 0 # Contendrá el número de valores a sumar.

# Programa principal:

valorFinal = int(input("Introduce el número de valores pares a sumar: "))

for numeroPar in range(0,2*valorFinal,2):
    sumaNumeros = sumaNumeros + numeroPar # Acumulo en la variable "suma" la sumade los números.
    contador = contador + 1 # También puede ser "contador +=1"

print(f"La suma total es: {sumaNumeros} y se han sumado {contador} valores pares.")
