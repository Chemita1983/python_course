'''
Ejercicio 5

Desarrollar un programa que permita sumar los dígitos 12de un número con la ayuda de una
función recursiva

Entrada 123
Salida 6
'''


def sumar_digitos(n):
    return 0 if n == 0 else sumar_digitos(n//10) + (n%10)

numero = int(input("Ingresa un numero: "))
print(sumar_digitos(numero))