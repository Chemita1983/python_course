'''

Ejercicio 3-2

Otra forma de hacer el palíndromo

'''

cadena = input("Ingresa un texto: ")
cadena = cadena.replace(" ","").lower()
cadena2 = cadena[::-1] # Copia la cadena invertida

if cadena == cadena2:
    print("Es palíndromo")
else:
    print("No es palíndromo")