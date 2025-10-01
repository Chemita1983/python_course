'''
Ejercicio 3

Pide números y mételos en una lista, cuando el usuario meta 0, dejamos de insertar.
Por último muestra los numeros ordenados de menor a mayor
'''

listaNumeros = []
while True:
    numero = int(input("Introduce un numero: "))
    if numero == 0:
        break
    listaNumeros.append(numero)

listaNumeros = list(set(listaNumeros))
listaNumeros.sort()
print(listaNumeros,end=" ")