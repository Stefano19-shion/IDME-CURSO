"""Pida por teclado números, hasta que introduzca el 0. Posteriormente debe mostrar su suma y su producto.
"""

from os import system #importo el comando system de la libreria os

numero = 1 # Para pedir por teclado el valor con el que voy a operar.
suma = 0 # Para acumular los valores sumados del numero pedido por teclado.
producto = 1 # Para acumular la multiplicacion de los numeros.


system("cls")
# Programa principal:
while numero != 0:
    numero= float(input("introduce el numero a multiplicar y sumar:"))
    suma = suma + numero
    if numero != 0:
     producto  = producto * numero

print(f"el numero de valores sumados es {suma}")
print(f"la multiplicacion total es {producto}")


