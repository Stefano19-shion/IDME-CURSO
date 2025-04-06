""" Pedirá por teclado la lista de los números de la lotería de los
 últimos 7 días. Posteriormente los mostrará ordenados de menor a
  mayor y de mayor a menor."""

# Importanción de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:
listaLoteria = [] # La lista que contendrá todos los elementos.
numero = 0 # Contiene el valor del número de la lotería

# Programa principal:

system("cls")

for indice in range(0,7):
    numero = int(input(f"Introduce el {indice + 1}º número de la lotería: "))
    listaLoteria.append(numero)

print("Lista desordenada...")
print(listaLoteria)

listaLoteria.sort()
print("Lista ordenada de menor a mayor...")
print(listaLoteria)

listaLoteria.sort(reverse = True)
print("Lista ordenada de mayor a menor...")
print(listaLoteria)