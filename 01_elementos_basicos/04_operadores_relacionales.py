'''
Operadores relacionales.
Se utilizan para establecer una relación entre dos valores.
Compara estos valores entre sí y esta comparación produce un resultado de certeza o falsedad (verdadero o falso).
Los operadores relacionales tienen menor prioridad que los aritméticos.

> Mayor que
< Menor que
>= Mayor o igual que
<= Menor o igual que
!= Diferente
== Igual
'''

resultado = 10 < 20
print("10 < 20,     resultado:", resultado)

resultado = 10 > 20
print("10 > 20,     resultado:", resultado)

resultado = 10 <= 20
print("10 <= 20,     resultado:", resultado)

resultado = 10 >= 20
print("10 >= 20,     resultado:", resultado)

resultado = 10 == 20
print("10 == 20,    resultado:", resultado)

resultado = 10 != 20
print("10 != 20,    resultado:", resultado)

a = 10
b = 20
c = 30
resultado = a + b == c
print("a + b == c, resultado:", resultado)