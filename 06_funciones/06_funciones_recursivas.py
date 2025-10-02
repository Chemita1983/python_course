# Funciones recursivas
# Aquellas que se llaman asi mismas


def cuenta_atras(numero):
    if numero > 0: # Caso base -> aquí se corta la recursividad
        print(numero)
        cuenta_atras(numero - 1)
    else:
        print("BOOOOOM!!!! 💥💥💥💥💥")

cuenta_atras(5)