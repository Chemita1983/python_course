# Tuplas

# Son listas inmutables, no se pueden modificar, son más rápidas y consumen menos memoria

tupla = (1, 2, 3, 4, 5) # Estos valores los va a tener siempre
print(tupla)
# No se puede modificar un valor, ni eliminar, ni agregar

# Podemos mostrar elementos como en las listas
print(tupla[1])

# Búsqueda de elementos
print(4 in tupla)
# Por indice
print(tupla.index(4))
# Contar elementos
print(tupla.count(4))
# Cuantos elementos tiene
print(len(tupla))

# Podemos transformar listas en tuplas y viceversa
lista = list(tupla)
print(lista)
tupla = tuple(lista)