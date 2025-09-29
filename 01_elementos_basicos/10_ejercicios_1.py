# 1 - Escribir la siguiente expresion de manera algorítmica

# a**3 * (b**2 - 2*a*c) / 2b

a = float(input("Escriba el numero de a: "))
b = float(input("Escriba el numero de b: "))
c = float(input("Escriba el numero de c: "))

resultado = (a**3 * (b**2 - 2*a*c)) / (2*b)
print(f"El resultado es: {resultado}")

# 2
resultado = ((3+5*8)<3 and (-6/3*4)+2<2) or (a>b)
print(f"El resultado es: {resultado}")

