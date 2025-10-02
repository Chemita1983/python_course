'''
Ejercicio 4

Hacer un programa donde se reemplacen todos los espacios de una cadena por asteriscos y además
que cada palabra comience por mayúsculas.
'''

cadena = input("Ingresa un texto: ")
cadena = cadena.replace(" ","*").title()

print(cadena)