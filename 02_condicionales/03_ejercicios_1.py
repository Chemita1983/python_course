'''
Ejercicio 1

Programa que nos dice si un número es par o impar
'''

numero1 = int(input("Introduzca un numero1: "))
numero2 = int(input("Introduzca un numero2: "))
if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Los dos numeros son par")
elif numero1 % 2 == 0 and numero2 % 2 != 0:
    print("El numero numero1 es par")
elif numero1 % 2 != 0 and numero2 % 2 == 0:
    print("El numero numero2 es par")
else:
    print("Ambos son impares")