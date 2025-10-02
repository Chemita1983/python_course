# Argumentos por valor o referencia

def doblar_por_valor(numero):
     numero *= 2
     print(numero)

def doblar_por_referencia(numero):
    return numero * 2 # Por referencia, se está actualizando el valor original

n = 5
doblar_por_valor(n) # Por valor, pasa una copia de n
n = doblar_por_referencia(n)
print(n)


# Todas las colecciones en Python se pasan por referencia
def doblar_valores(numeros):
    for i,v in enumerate(numeros):
        numeros[i] = v * 2

nums = [5,10,15,20]
doblar_valores(nums)
print(nums)

# Sí queremos enviar por valor los elementos de una lista
nums = [5,10,15,20]
doblar_valores(nums[:]) # nums[:] crea una copia y el original se mantiene
print(nums)