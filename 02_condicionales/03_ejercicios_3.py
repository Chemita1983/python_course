'''
Ejercicio 3

Comprobar vocales, hacer un programa que pida un caracter e indique si es una vocal o no

'''

char = input("Introduce un caracter: ")
if len(char) != 1:
    print("Debe indicar solo un caracter")
else:
    if (
            (char == "a" or char == "A") or
            (char == "e" or char=="E") or
            (char == "i" or char == "I") or
            (char == "o" or char=="O") or
            (char == "u"or char == "U")
    ):
        print("El caracter introducido es una vocal")
    else:
        print("El caracter introducido no es una vocal")