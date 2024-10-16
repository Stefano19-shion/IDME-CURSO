"""Programa que muestra en pantalla los primeros 
50 números pares."""

# Declaración de variables:

numero = 0 # Para contar el número de valores
contador = 0 # Va a contar el número de valores

# Programa principal:

for numero in range(0,100,2):
    print(numero)
    contador = contador + 1 # También puede ser "contador +=1"

print(f"El número de valores contados es: {contador}.")

