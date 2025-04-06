"""Programa que utilice una función que aplique un descuento a un precio dado. Tomará dos parámetros,
 el precio y el porcentaje de descuento. Devolverá el importe del precio con el descuento aplicado. 
 También utilizará un parámetro opcional, que es el porcentaje de impuestos.
 Debe controlar que el porcentaje esté en 0 y 100, y si no es así devolver un error y un valor -1.
 """

# Importación de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:


precio = 0
porcentajeDescuento = 0
porcentajeImpuesto = 0

# Definición de funciones:

def calculoImporte(precio, descuento, impuesto = 0):
    if descuento < 0 or descuento > 100:
        print("Error: el descuento debe estar entre 0 y 100 %")
        return -1
    return precio * (1 - descuento / 100) * (1 + impuesto / 100)

# Programa principal.

system("cls")
precio = float(input("Introduce el precio del artículo: "))
porcentajeDescuento = float(input("Teclea el porcentaje de descuento: "))
porcentajeImpuesto = input("Introduce el porcentaje de Impuesto (ENTER -> No descuento): ")

if porcentajeImpuesto == "":
    print(f"El importe final es: {calculoImporte(precio, porcentajeDescuento)}")
else:
    print(f"El importe final es: {calculoImporte(precio, porcentajeDescuento, float(porcentajeImpuesto))}")
    
