'''
Ejercicio 5

Calcular el factorial de un número introducido por teclado
'''

numeroOriginal = int(input("Introduce un numero: "))
while numeroOriginal < 0:
    print("Error ⛔️ -> El número debe de ser positivo")
    numeroOriginal = int(input("Introduce un numero: "))

# Con While
numero = numeroOriginal
factorial = 1
if numero != 0:
    while numero >= 1:
        factorial *= numero
        numero -= 1
print(f"El factorial de {numeroOriginal} es {factorial}")

# Con For
numero = numeroOriginal
factorial = 1
for i in range(2, numeroOriginal + 1):
    factorial *= i
print(f"El factorial de {numeroOriginal} es {factorial}")