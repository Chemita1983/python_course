'''
Ejercicio 4

Calculadora aritmética
'''
print("------------------ CALCULADORA -------------------")
print("Operaciones:\n S - Suma\n R - Resta\n M,P - Multiplicación\n D - Division\n T - Resto\n C - Potencia")
operacion = input("Introduce una operacion: ")
numero1 = float(input("Introduce un numero1: "))
numero2 = float(input("Introduce un numero2: "))

if operacion == "S" or operacion == "s":
    print(numero1 + numero2)
elif operacion == "R" or operacion == "r":
    print(numero1 - numero2)
elif operacion == "M" or operacion == "m" or operacion == "P" or operacion == "p":
    print(numero1 * numero2)
elif operacion == "D" or operacion == "d":
    print(numero1 / numero2)
elif operacion == "T" or operacion == "t":
    print(numero1 % numero2)
elif operacion == "C" or operacion == "c":
    print(numero1 ** numero2)
else:
    print("Opción introducida no valida")
