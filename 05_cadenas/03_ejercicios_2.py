'''
Ejercicio 2

Frase terminada en punto.

Hacer un programa para dectectar si una frase introducida por el usuario termina con un punto o no.
Deberás imprimir por la consola una de las siguientes opciones "Termina con un punto" o "No termina
con un punto"

'''

cadena = input("Ingresa un texto: ")

if cadena.endswith("."):
    print("Termina con un punto")
else:
    print("No termina con un punto")