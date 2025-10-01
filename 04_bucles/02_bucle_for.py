# Bucle For
import math

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lista:
    print(f"Elemento: {i}")


# Recorrer un diccionario
mapa = {"nombre":"Chema", "apellido":"J.V", "edad":42}
for i in mapa:
    print(f"{i}:{mapa[i]}") # Muestra las claves y los valores

# Otra forma
for key, value in mapa.items():
    print(f"{key}: {value}")

# Recorrer cadenas
cadena = "Chema"
for i in cadena:
    print(f"{i}",end=" ") # end evita el salto de línea y lo sustituye por lo que digamos

# For tipo range
print()
for i in range(10):
    print(f"{i}", end=" ")

print()
for i in range(2,21,2): # Empieza en el 2, termina en el 21-1, y va de 2 en 2
    print(f"{i}", end=" ")

print()
for i in range(20,0,-2): # Empieza en el 2, termina en el 1, y va de -2 en -2
    print(f"{i}", end=" ")