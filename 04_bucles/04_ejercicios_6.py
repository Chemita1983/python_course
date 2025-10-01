'''
Ejercicios 6

Dado un número por teclado, muestra su tabla de multiplicar
'''

numero = int(input("Introduce un numero: "))
while numero < 0:
    print("Error ⛔️ -> El número debe de ser positivo")
    numero = int(input("Introduce un numero: "))

print(f"-------------- Tabla de Multiplicar del {numero} --------------")

for i in range(0,11):
    print(f"{numero} x {i} = {numero*i}")