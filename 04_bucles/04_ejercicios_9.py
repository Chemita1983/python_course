'''
Ejercicio 9

Muestra una frase sin espacios y contar las letras
'''

frase = list(input("Introduce un frase: "))
fraseFinal = ""
for c in frase:
    if c != " ":
        fraseFinal += c

print(fraseFinal)
print(f"La frase tiene: {len(fraseFinal)} letras")