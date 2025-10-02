# Funciones con retorno de valor

def sumar(numero1, numero2):
    return numero1 + numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    return numero1 / numero2

def resta(numero1, numero2):
    return numero1 - numero2


print(multiplicar(2,3))
print(sumar(2,3))
print(dividir(24,3))
print(resta(29,3))

# Las funciones pueden retornar varios valores
def prueba():
    return "Chema", 42

print(prueba()) # Se almacenan dentro de una tupla

# O bien podemos decirle donde guardarlos como variables
c,n = prueba()
print(c)
print(n)