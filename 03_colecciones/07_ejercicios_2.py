'''
Ejercicio 2

Escriba un programa que tenga dos listas y que a continuación cree las siguientes listas:

- Lista de palabras que aparecen en las dos listas
- Listas de palabras que aparecen en la primera lista, pero no en la segunda
- Listas de palabras que aparecen en la segunda lista, pero no en la primera
- Lista de palabras que aparecen en ambas listas
'''

lista1 = ["Chema","Pedro","Marta","Maria","Juan","Juan","David","Delia","Carmen"]
lista2 = ["Chema","Marta","Pablo","Marcos","Mateo","Luisa","Fátima","Conchi"]

a = set(lista1)
b = set(lista2)

# Palabras que aparecen en las dos listas
c =  a | b
print("Palabras que aparecen en las dos listas")
print(list(c))

# Palabras que aparecen en la lista 1 pero no en la lista 2
c =  a - b
print("Palabras que aparecen en la lista 1 pero no en la lista 2")
print(list(c))

# Palabras que aparecen en la lista 2 pero no en la lista 1
c =  a - b
print("Palabras que aparecen en la lista 2 pero no en la lista 1")
print(list(c))

# Palabras que aparecen en ambas listas
c =  a & b
print("Palabras que aparecen en ambas listas")
print(list(c))