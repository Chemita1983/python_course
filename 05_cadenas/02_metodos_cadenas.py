# Métodos para cadenas

cadena = "Hola Mundo".upper() # Transforma a mayúsculas
print(cadena)

cadena = "Hola Mundo".lower() # Transforma a minúsculas
print(cadena)

cadena = "hola mundo".capitalize() # Convierte a mayúscula la primera letra
print(cadena)

cadena = "hola mundo".title() # Convierte a mayúscula las primeras letras de cada palabra
print(cadena)

cadena = "hola mundo".count("mundo") # Cuenta caracteres o palabras
print(cadena)

cadena = "hola mundo".find("mundo") # Devuelve el índice donde está la primera conicidencia de lo que busquemos
print(cadena)

cadena = "hola mundo".rfind("o") # Devuelve el índice donde está la última conicidencia de lo que busquemos
print(cadena)

cadena = "1000".isdigit() # Devuelve true si la cadena solo contiene números
print(cadena)

cadena = "ABCDE0".isalpha() # Devuelve true si la cadena solo contiene caracteres alfabéticos
print(cadena)

cadena = "ABCDE0".isalnum() # Devuelve true si la cadena solo contiene números y caracteres alfabéticos (no símbolos)
print(cadena)

cadena = "hola mundo".islower() # Devuelve true si toda la cadena esta en minúscula
print(cadena)

cadena = "HOLA MUNDO".isupper() # Devuelve true si toda la cadena esta en mayúscula
print(cadena)

cadena = "Hola Mundo".istitle() # Devuelve true si la cadena es un titulo
print(cadena)

cadena = "      ".isspace() # Devuelve true si la cadena solo tiene espacios
print(cadena)

cadena = "Hola Mundo".startswith("H") # Devuelve true si la cadena comienza con lo que le digamos
print(cadena)

cadena = "Hola Mundo".endswith("Mundo") # Devuelve true si la cadena termina con lo que le digamos
print(cadena)

cadena = "Hola Mundo".split() # Retorna una lista con los elementos de dentro de tu cadena
print(cadena)

cadena = ",".join("Chema") # Separa cada elemento de la cadena por el símbolo que le indiquemos
print(cadena)

cadena = "      Hola     ".strip() # Elimina los espacios de una cadena antes y después de la misma
print(cadena)

cadena = "Hola Mundo".replace("o","@") # Remplaza caracteres o palabras
print(cadena)