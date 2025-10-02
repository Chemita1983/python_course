# Cadenas caracteres

cadena1 = "Hola Mundo" # Pueden estar entre comillas simples o dobles (o combinadas)
cadena2 = "Hola \tMundo"
cadena3 = r"D:\nombre\trabajos" # Con r delante lo escribe en crudo

parrafo = """ 
Hola que tal estas?
Asi imprimimos en varias lineas
esta chulo
"""

cadena4 = "Hola "
cadena5 = "que tal?"

print(cadena1)
print(cadena2)
print(cadena3)
print(parrafo)
print(cadena4 + cadena5)

# Indices y slicing
cadena1 = "Chema"
print(cadena1[2])
print(cadena1[:])
print(cadena1[1:4])
print(cadena1[2:])
print(cadena1[:3])

# Las cadenas de caracteres son inmutables, no se pueden modificar por índice.
# cadena[0] = a
# cadena = 'a' + cadena[1:]

# Longitud de una cadena
print(len(cadena1))