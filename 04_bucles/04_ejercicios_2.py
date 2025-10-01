'''
Ejercicio 2

Llenar una lista con los números del 1 al 10 y luego modificar los
elementos de la lista multiplicándolos por un valor que el usuario diga
'''

numeros = list(range(1, 11))

numero = int(input("Introduce un numero: "))

print(f"Lista final con los elementos multiplicados por {numero}")
for index, i in enumerate(numeros): # enumerate para crear el index
    numeros[index] *= numero

for i in numeros:
    print(i)