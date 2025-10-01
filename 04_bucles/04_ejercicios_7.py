'''
Ejercicio 7

Intenta adivinar un número entre 0 y 100 aleatorio introduciendo numeros por teclado con 4 intentos
'''
import random

intentos = 0
numero_secreto = random.randint(0,100)
while True:
    numero = int(input("Introduce un numero: "))
    intentos += 1
    if numero == numero_secreto:
        print("Enhorabuena lo adivinaste 🥳🥳🎉")
        break
    else:
        if numero < numero_secreto:
            print("El numero secreto es mayor")
        else:
            print("El numero secreto es menor")

print(f"El numero de intentos que utilizaste fue {intentos}")