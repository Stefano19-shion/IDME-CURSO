'''Programa que pedira por teclado asignaturas con su calificacion.Luego debe mostrar
solo las aprobadas (>5)y la media aritmetica de todas las calificaciones.
'''
# Importanción de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:

asignaturas = {}  #Diccionario que contendra los datos(nombre y nota)
nombreAsignatura = ' '
calificacion = 0 # Contendra la nota entre 0 y 10(con decimales)
sumaCalificaciones = 0 # Para calcular la media aritmetica

system("cls")
while nombreAsignatura != '': # Bucle para pedir las asignaturas.
      nombreAsignatura = input('Teclea el nombre de la asignatura(ENTER para finalizar): ')
      if nombreAsignatura != "":
        calificacion = float(input('introduce la calificacion de la asignatura'))
        asignaturas[nombreAsignatura] = calificacion

for nombreAsignatura in asignaturas:
    if asignaturas[nombreAsignatura] >= 5:
        print(f"La asignatura{nombreAsignatura} esta aprobada con un {asignaturas[nombreAsignatura]}")
    sumaCalificaciones = sumaCalificaciones + asignaturas[nombreAsignatura]

print(f"La media aritmetica es {sumaCalificaciones/len(asignaturas)}")
