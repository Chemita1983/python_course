'''
Ejercicio 6

Suma natural, dado un número que te sume los n primeros números naturales

Por ejemplo, si n = 5, la función debe devolver 1 + 2 + 3 + 4 + 5 = 15.

'''


def sumar_numeros_naturales(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return n + sumar_numeros_naturales(n - 1)

numero = int(input("Ingresa un numero: "))
print(sumar_numeros_naturales(numero))