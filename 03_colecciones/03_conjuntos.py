# Conjuntos

# Tipo de colección donde los elementos se agregan de forma desordenada, no puede haber duplicados

conjunto = set() #Siempre y cuando sea vacío
conjunto = {1, 2, 3, 5, 4, "Chema", True, False} # En los conjuntos no podemos agregar otro tipo de colecciones
print(conjunto) # No se muestra True porque True lo transforma a 1 y los conjuntos eliminan duplicados

# Agregar elementos
conjunto.add(6)
conjunto.add("Marta")
conjunto.add("A")
print(conjunto)

# Eliminar elementos de un conjunto
conjunto.discard("A")
conjunto.discard("Marta")
conjunto.discard("Chema")
print(conjunto)

# Búsqueda de elementos
print(5 in conjunto)
print(5 not in conjunto)

# Eliminar el conjunto entero
conjunto.clear()
print(conjunto)

# Conjuntos 2

# Si vas a inicializar el conjunto directamente se puede poner asi:
print("\nCONJUNTOS 2")
a = {1,2,3}
b = {3,4,5}

# Igualdad
print(a == b)

# Número de elementos
print(len(a))

# Union de conjuntos (Muestra los elementos que hay en ambos conjuntos)
c = a | b
print(c)

# Intersección (Elementos que están en los dos conjuntos)
c = a & b
print(c)

# Diferencia (Elementos de a que no están en b)
c = a - b
print(c)

# Diferencia simétrica (Elementos que están en a y en b pero no en ambos)
c = a ^ b
print(c)

# Saber si un conjunto pertenece a otro
c = {1,2,3,4,5,6}
print(a.issubset(c))
print(b.issubset(c))

# Superconjunto, si los elementos de c están en a
print(c.issuperset(a))

# Conjuntos disconexos (No comparten ningún elemento)
print(a.isdisjoint(b))

# Conjuntos inmutables
a = frozenset({1,2,3,4,5}) # No podríamos modificar ya ningún valor