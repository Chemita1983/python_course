'''
Ejercicio 2

Dibujar un rectángulo

Hacer un programa que pida la anchura y altura de un rectángulo y con la ayuda de una función lo
dibuje con *

'''

def dibujar_rectangulo(ancho, alto):
    for i in range(alto):
        for j in range(ancho-1):
            print("*", end=" ")
        print()

ancho = int(input("Ingrese el ancho: "))
altura = int(input("Ingrese altura: "))
print()
dibujar_rectangulo(ancho, altura)