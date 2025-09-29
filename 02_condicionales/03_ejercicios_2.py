'''
Ejercicio 2

Programa que nos dice el mayor de 3 números
'''

a = int(input("Introduce un numero a: "))
b = int(input("Introduce un numero b: "))
c = int(input("Introduce un numero c: "))

if a >= b and a >= c:
    print(f"El numero a es el mayor de 3 numeros")
elif b >= a and b >= c:
    print(f"El numero b es el mayor de 3 numeros")
else:
    print(f"El numero c es el mayor de 3 numeros")