"""Programa para convertir un valor de euros en dólares."""

# Declaración de variables:
cantidad = 0 # Va a contener el valor en euros, que pediré por teclado.
cambio = 0 # Contiene el valor del cambio del día (se pide por teclado)


# Programa principal.
cambio = float(input("Dime el cambio del día de euros a dólares: "))
cantidad = int(input("Introduce el valor de euros a convertir a dólares: "))
print("El valor en dólares es", cambio*cantidad)

