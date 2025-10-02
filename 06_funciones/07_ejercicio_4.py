'''
Ejercicio 4

Factorial con recursividad
'''

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1) # Ternario

numero = int(input("Ingresa un numero: "))
print(f"El factorial de {numero} es {factorial(numero)}")