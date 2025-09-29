'''
Ejercicio 3

Hacer un programa para intercambiar el valor de dos variables:

a = 10 => a = 5
b = 5 => b = 10
'''

a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))
a,b = b,a
print(f"El resultado de a es: {a}")
print(f"El resultado de b es: {b}")

