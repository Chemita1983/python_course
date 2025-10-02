'''
Ejercicio 1

Cadena más larga.

Hacer un programa donde se deberá imprimir por la consola la palabra con más caracteres de dos palabras
dadas. En el caso de que ambas palabras tengan la misma cantidad de caracteres, deberás mostrar el mensaje
"Son iguales"
'''

cadena1 = input("Ingresa un texto: ")
cadena2 = input("Ingresa otro texto: ")

if len(cadena1) > len(cadena2):
    print(f"La palabra {cadena1} tiene mas caracteres con {len(cadena1)} caracteres.")
elif len(cadena2) > len(cadena1):
    print(f"La palabra {cadena2} tiene mas caracteres con {len(cadena2)} caracteres.")
else:
    print("Son iguales")
