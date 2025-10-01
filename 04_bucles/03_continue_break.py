# Continue - Break

for numero in range(10):
    if numero == 5:
        continue # Salta a la siguiente iteración del bucle
    print(numero)

print()
for numero in range(10):
    if numero == 5:
        break # Termina el bucle
    print(numero)

print("Fin del programa")