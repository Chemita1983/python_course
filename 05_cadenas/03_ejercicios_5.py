'''
Ejercicio 5

Contar vocales (cada una) en una cadena
'''

cadena = input("Ingresa un texto: ").lower()
totalA  = cadena.count("a") + cadena.count("á")
totalE = cadena.count("e") + cadena.count("é")
totalI = cadena.count("i") + cadena.count("í")
totalO = cadena.count("o") + cadena.count("ó")
totalU = cadena.count("u") + cadena.count("ú")

print(f"""
    El texto tiene {totalA} vocales a.
    El texto tiene {totalE} vocales e.
    El texto tiene {totalI} vocales i.
    El texto tiene {totalO} vocales o.
    El texto tiene {totalU} vocales u.
    El texto tiene {totalA + totalE + totalI + totalO + totalU} vocales en total.
""")