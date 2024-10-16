"""Programa que suma los primeros 50 números impares."""

# Declaración de variables:

numeroImpar = 0 # Número impar, incrementado de 2 en 2.
contador = 0 # Valor para contar el total de números (debe ser 50 al final).
sumaNumeros = 0 # Para ir acumulando la suma de los valores.

for numeroImpar in range(1,100,2):
    sumaNumeros = sumaNumeros + numeroImpar # Acumulo en la variable "suma" la sumade los números.
    contador = contador + 1 # También puede ser "contador +=1"

print(f"La suma total es: {sumaNumeros} y se han sumado {contador} valores impares.")
