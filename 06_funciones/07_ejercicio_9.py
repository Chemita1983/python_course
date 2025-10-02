'''
Ejercicio 9

Crea una función recursiva llamada maximo(lista) que devuelva el valor máximo dentro de una lista
de números enteros.

Ejemplo:
maximo([3, 7, 2, 9, 5])  # devuelve 9
maximo([10])             # devuelve 10
maximo([-1, -5, -3])     # devuelve -1
'''

def maximo(lista):
    if len(lista) == 0:
        return None
    if len(lista) == 1:
        return lista[0]
    else:
        return max(lista[0], maximo(lista[1:]))


# Función para probar maximo con varios casos
def probar_maximo():
    casos = [
        ([3, 7, 2, 9, 5], 9),
        ([10], 10),
        ([-1, -5, -3], -1),
        ([], None),
        ([100, 50, 200, 150], 200)
    ]
    for i, (entrada, esperado) in enumerate(casos):
        resultado = maximo(entrada)
        print(f"Test {i+1}: maximo({entrada}) = {resultado} | Esperado: {esperado} | {'✅' if resultado == esperado else '❌'}")

probar_maximo()