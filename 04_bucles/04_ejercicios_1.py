'''
Ejercicio 1

Llenar una lista con los números del 1 al 50, luego mostrar la lista con un bucle for
los elementos deben de mostrarse asi:

1-2-3-4...-50
'''

lista = list(range(1, 51)) # Crea una "colección ficticia"

for i in lista:
    if i == len(lista):
        print(f"{i}",end="")
        continue
    print(f"{i}",end="-")