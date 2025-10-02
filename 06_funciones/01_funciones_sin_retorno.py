# Funciones sin retorno de valor

def saludar():
    print("Hola")

def saludando(nombre):
    print(f"Hola {nombre}")

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {i*numero}")

numero = int(input("ingrese un numero: "))
tabla_multiplicar(numero)