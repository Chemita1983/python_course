# Operadores ariméticos

'''
Prioridades aritméticas
1 - Parentesis ()
2 - Exponenciación **
3 - Multiplicación, División y Módulo *, /, %
4 - Sumas y restas +, -

'''

num1 = 10
num2 = 5

resultado = num1 + num2
print(resultado)

resultado = num1 - num2
print(resultado)

resultado = num1 * num2
print(resultado)

# La division siempre devuelve decimales
resultado = num1 / num2
print(resultado)

num2 = 3
resultado = num1 / num2
print(resultado)

# Operador de división entera, siempre redondea a la baja
resultado = num1 // num2
print(resultado)

# Operador modulo, devuelve el resto de la division
resultado = num1 % num2
print(resultado)

# Operador de exponente
resultado = num1 ** num2
print(resultado)


resultado = 3**3 * (13/5 - (2*4))
print("resultado:", resultado)