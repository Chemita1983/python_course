# bucle while

import math

numero = int(input("Introduce un numero: "))

while numero < 0:
    print("Error ⛔️-> Introduce un numero positivo.")
    numero = int(input("Introduce un numero: "))

print(f"La raiz cuadrada de {numero} es {math.sqrt(numero):.2f}")
