# Condicionales combinados

edad = int(input("Ingrese la edad: "))

if 0 < edad <= 100:
    if edad >= 18:
        print("Es mayor de edad.")
    else:
        print("No es mayor de edad.")
else:
    print("La edad introducida no es valida.")