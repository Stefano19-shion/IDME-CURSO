suma= 0
numero = 2
contador = 0

from os import system

system("cls") #Ejecuta el comando cls del sistema operativo ms windows.



while suma <= 1000:
    suma = suma + numero
    numero += 2  # Equivale a escribir numero = numero + 2.
    contador += 1

print(f"La suma total {suma}")
print(f"el numero de valores sumados es {contador}")
print(f"el ultimo numero sumado es{numero}")


    