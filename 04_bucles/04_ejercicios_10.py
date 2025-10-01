'''
Ejercicio 10

Hacer un programa que pida una cadena por teclado, luego meta los caracteres en una lista sin
repetir caracteres
'''

frase = input("Ingresa una cadena por teclado: ")
lista = []
for caracter in frase:
    if caracter not in lista:
        lista.append(caracter)

print(lista)