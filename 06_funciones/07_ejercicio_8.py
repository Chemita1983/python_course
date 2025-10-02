'''
Ejercicio 8

Contar cuantas veces aparece una letra en una palabra

contar_caracter(cadena, caracter)

'''

def contar_caracter(cadena, caracter):
    if cadena == "":
        return 0
    if cadena[0] == caracter:
        return 1 + contar_caracter(cadena[1:], caracter)

    return contar_caracter(cadena[1:], caracter)


cadena = input("Ingresa una cadena: ").lower()
print(contar_caracter(cadena, "a"))
