# Diccionarios

# Poseen clave y valor, se guardan desordenadamente, puedes meter cualquier tipo de dato dentro de
# un diccionario

diccionario = {}
diccionario = {
    "azul": "blue",
    "rojo": "red",
    "verde": "green",
    "amarillo": "yellow",
    "naranja": "orange"
}
print(diccionario)
print(diccionario["azul"]) # Muestra el valor de la key introducida

# Agregar elementos al diccionario
diccionario["marron"] = "brown"
print(diccionario)

# Modificar elementos
diccionario["verde"] = "GREEN"
print(diccionario)

# Eliminar elementos de un diccionario
del(diccionario["marron"])
del(diccionario["naranja"])
print(diccionario)

agenda = {
        "Chema": {"edad": 42, "estatura": 1.91, "poblacion":"Madrid"},
        "Marta": [46,1.80, "Madrid"],
        "Carmen": [68, 1.77, "Barcelona"]
        }
print(agenda["Chema"])

print("\nDICCIONARIOS 2")

juventus = {
    10: "Paulo Dybala",
    11: "Douglas Costa",
    7: "Cristiano Ronaldo",
    17: "Mario Mandzukic"
}

# print(juventus[70]) -> Esto da una excepción de tipo keyError
print(juventus.get(70, "No existe jugador con ese dorsal"))

# Comprobar un valor
print(10 in juventus)
print(70 in juventus)

# Mostrar las claves
print(juventus.keys())

# Mostrar lo values
print(juventus.values())

# Mostrar todos los elementos (los mete en una tupla)
print(juventus.items())

#Cuantos elementos hay en el diccionario
print(len(juventus))

# Eliminar todos los elementos de un mapa
diccionario.clear()
print(diccionario)