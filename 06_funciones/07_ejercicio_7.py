'''
Ejercicio 7

Invertir cadena

invertir_cadena("hola")  # devuelve "aloh"
invertir_cadena("python")  # devuelve "nohtyp"
'''

def invertir_cadena(cadena):
    if cadena == "" or len(cadena) == 1:
        return cadena
    return invertir_cadena(cadena[1:]) + cadena[0]


cadena = input("Ingresa un cadena: ")
print(invertir_cadena(cadena))