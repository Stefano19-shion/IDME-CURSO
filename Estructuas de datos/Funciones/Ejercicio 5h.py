"""Escribir una función que devuelva el valor de una resistencia de 4 bandas,
 indicando su intervalo. Habrá que pasarle los colores de las 4 bandas. El formato será:
 
 resistencia(color1, color2, color3, color4) -> (valor nominal, limite inferior intevalo
                                                                ,limite superior intervalo).
 """

# Importación de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:

color1, color2, color3, color4 = 0, 0, 0, 0 # Variables para pedir por teclado.
resultado = [] # Lista que contendrá los valores devueltos por la función

# Definición de funciones:

def resistencia(color1, color2, color3, color4):
    coloresValor = {"Negro": 0, "Marrón": 1, "Rojo": 2, "Naranja": 3,
                    "Amarillo": 4, "Verde": 5, "Azul": 6, "Violeta": 7,
                    "Gris": 8, "Blanco": 9}
    coloresTolerancia = {"Rojo": 2, "Dorado": 5, "Plata": 10}

    valorNominal = (coloresValor[color1] * 10 + coloresValor[color2]) * 10**coloresValor[color3]
    limiteInferior = valorNominal - coloresTolerancia[color4] * valorNominal / 100
    limiteSuperior = valorNominal + coloresTolerancia[color4] * valorNominal / 100
    return(valorNominal, limiteInferior, limiteSuperior)

# Programa principal.

system("cls")

color1 = input("Teclea el primer color: ")
color2 = input("Teclea el segundo color: ")
color3 = input("Teclea el tercer color: ")
color4 = input("Teclea el cuarto color (tolerancia): ")

color1 = color1.capitalize()
color2 = color2.capitalize()
color3 = color3.capitalize()
color4 = color4.capitalize()

resultado = resistencia(color1, color2, color3, color4)

print(f"El valor nominal es {resultado[0]}")
print(f"El intervalo es ({resultado[1]}, {resultado[2]})")