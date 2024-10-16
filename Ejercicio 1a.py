"""Programa que pide por teclado dos números y muestra por pantalla
su suma y su resta"""

# Declaración de variables.
numero1 = 0 # Contiene el primer valor que pido por teclado.
numero2 = 0 # Contienen el segundo valor que voy a pedir por teclado.

# Programa principal.
numero1 = int(input("Introduce el primer número: ")) # Pido por teclado el primer número y lo convierto a entero.
numero2 = int(input("Introduce el segundo número: ")) # Pido por teclado el segundo número y lo convierto a entero.

print("La suma es ", numero1+numero2) # Sumo las dos variables y lo muestro en pantalla 
print("La resta es ", numero1-numero2) # Restos las dos variables.
