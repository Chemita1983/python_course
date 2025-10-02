'''
Ejercicio 3

Palíndromo

Hacer un programa que determine si una palabra o frase es palíndroma.
Una cadena palíndroma se lee igual de izquierda a derecha que de derecha a izquierda.

Ejemplos
    - oso
    - reconocer
    - anita lava la tina
'''

cadena = input("Ingresa un texto: ")
cadena = cadena.replace(" ","")

esPalindromo = True
indexF = len(cadena)

for i in cadena:
    if i != cadena[indexF-1]:
        esPalindromo = False
        break
    else:
        indexF -= 1

if esPalindromo:
    print("Es palíndromo")
else:
    print("No es palíndromo")


