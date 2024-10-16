"""Programa que introduce por teclado el valor de la nota de un examen y diga si está
 aprobado o suspenso (>=5).
 Mejora: vamos a repetir el proceso hasta que se introduzca el valor 0.
 """

# Declaración de variables:

calificacion = 1 # Variable que contendrá el valor numérico de la nota del examen.

# Programa principal:

while calificacion != 0:
    calificacion = float(input("Teclea el valor de la nota del examen (0 para finalizar): "))

    if calificacion >= 5:
        print("Enhorabuena, has aprobado el examen!!")
    else:
        print("Lo siento, suerte la próxima (en junio)")

print("* Fin del superprograma de IA que dice si estás aprobado o suspenso *")

