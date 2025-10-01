'''
Ejercicio 4

Hacer un programa para sumar números pares dentro de un rango.

Ejemplo:
 -  Suma de numeros pares del 2 al 30
    Suma = 240
'''


numero1 = int(input("Introduce un numero1: "))
numero2 = int(input("Introduce un numero2: "))

while numero1 > numero2:
    numero1 = int(input("Introduce un numero1: "))
    numero2 = int(input("Introduce un numero2: "))

lista = range(numero1, numero2+1)
suma = 0
for numero in lista:
    if numero % 2 == 0:
        suma += numero

print(f"Suma = {suma}")