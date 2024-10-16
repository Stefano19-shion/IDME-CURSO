"""Programa que resuelve una ecuación de 2º grado,
 ax2+bx+c = 0, introduciendo los coeficientes a, b y c."""

# Importación de librerías:
from math import sqrt

# Declaración de variables:
a = 0 # Coeficiente del término de segundo grado.
b = 0 # Coeficiente del término de primer grado.
c = 0 # Término independiente.
x1 = 0 # Solución con el "+".
x2 = 0 # Solución con el "-".

# Programa principal:

print("Ecuación de segundo grado: ax^2+bx+c = 0")
a = float(input("Teclea el coeficiente del término de 2º grado (a): "))
b = float(input("Teclea el coeficiente del término de 1º grado (b): "))
c = float(input("Teclea el término independiente (c): "))

print(f"Ecuación de segundo grado: {a}x^2+{b}x+{c} = 0")

x1 = (-b+sqrt(b**2-4*a*c)) / (2*a)
x2 = (-b-sqrt(b**2-4*a*c)) / (2*a)

print(f"Las soluciones son: x1 = {x1} y x2 = {x2}.")
