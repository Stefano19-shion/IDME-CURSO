"""Programa de Login que compruebe el usuario y contraseña en el
diccionario a continuación. El usuario tendrá un máximo de
3 intentos, y al acceder correctamente se mostrará un mensaje
de bienvenida, con el nombre y apellidos del usuario."""

# Importación de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:

usuarios = {
	"aexposito":
	    {"nombre": "Antonio",
		    "apellidos": {"primerApellido": "Expósito", "segundoApellido": "Núñez"},
	    "password": "123456"},
	"fgonzalez":
	    {"nombre": "Francisco",
		    "apellidos": {"primerApellido": "González", "segundoApellido": "Martínez"},
	    "password": "jejejaja"},
	"lcastillo":
	    {"nombre": "Lourdes",
		    "apellidos": {"primerApellido": "Prieto", "segundoApellido": "Valverde"},
	    "password": "6789"}
	    }

usuario = "" # Se pedirá por teclado para buscarlo en el diccionario.
contraseña = "" # Se pedirá por teclado para buscarlo en el diccionario.
numIntentos = 0 # Cuenta el número de intentos (3 para bloquear).
valido = False # Indicará si la combinación de usuario y contraseña es válida

# Programa principal:



while numIntentos < 3 and valido == False:
    system("cls") # Borra la pantalla.
    usuario = input("Introduce el usuario: ")
    contraseña = input("Contraseña: ")
    numIntentos += 1
    if usuario in usuarios and contraseña == usuarios[usuario]["password"]:
        valido = True
        print(f"Bienvenid@:  {usuarios[usuario] ['nombre']} {usuarios[usuario] ['apellidos'] ['primerApellido']} {usuarios[usuario] ['apellidos'] ['segundoApellido']}")
    else:
        print(f"La combinación de usuario y contraseña no es válida!!. Te quedan {3 - numIntentos} intentos.")
        valido = False
        input("Pulsa ENTER para continuar")

	




 

