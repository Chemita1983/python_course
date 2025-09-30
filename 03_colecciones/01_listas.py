# Listas

lista = ["Lunes","Martes","Miércoles","Jueves","Viernes"]

print(lista)
print(lista[0])
print(lista[-1]) # De fin a principio, mostraría "viernes"
print(lista[0:3]) # Muestra elementos del indice 0 al indice 2
print(lista[:4])
print(lista[1:])

# Se le puede agregar cualquier tipo de dato
otraLista = ["Chema",42, True, [1,2,3],"Madrid"]
print(otraLista)

# Cuantos elementos tiene la lista
print(len(otraLista))

lista = [1, 2, 3, 4, 5, 6]

# Agrega un elemento al final de la lista

# Agrega un elemento en una lista especifica de la lista
lista.insert(2,2.5)

# Agrega varios elementos al final de la lista
lista.extend([7,8,9])

# Se puede sumar dos listas
lista2 = [10,11,12,13,14]
lista3 = lista + lista2
print(lista3)

# Como saber si un determinado elemento existe en la lista
print(3 in lista)
print("Chema" in lista)

# Como saber en qué índice está algún elemento
print(lista.index(5))

# Cuantos valores concretos existen en una lista
print(lista.count(5))

# Eliminar valores de una lista
lista3.pop() # Elimina el último elemento de la lista
lista3.pop(2) # Elimina el valor del índice 3
lista3.remove(13) # Elimina el valor que le pasamos como parámetro
lista3.clear() # Elimina toda la lista
print(lista3)

# Dar la vuelta a la lista
lista.reverse()
print(lista)

# Multiplicar la lista
lista *= 2
print(lista)

# Ordenar una lista
lista.sort() # De menor a mayor
print(lista)
lista.sort(reverse=True)  # De mayor a menor
print(lista)