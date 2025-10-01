'''
Ejercicio 8

Cajero automático

Hacer un programa que simule un cajero automático con un saldo inicial de 1000$ y tendrá
el siguiente menu de opciones.

1 - Ingresar dinero en la cuenta.
2 - Retirar dinero de la cuenta.
3 - Mostrar dinero disponible.
4 - Salir
'''

dinero = 1000

while True:
    print("----------------------- CAJERO AUTOMÁTICO -----------------------")
    print("1 - Ingresar dinero en la cuenta.")
    print("2 - Retirar dinero de la cuenta.")
    print("3 - Mostrar dinero disponible.")
    print("4 - Salir")
    opcion = int(input("Ingrese un opción: "))


    if opcion == 1:
        dinero_ingresar = float(input("Indique dinero a ingresar en la cuenta: "))
        if dinero_ingresar > 0:
            dinero += dinero_ingresar
            print(f"El dinero ingresado es: {dinero_ingresar}$, tiene {dinero}$ en total")
        else:
            print("Dinero a ingresar no valido")
    elif opcion == 2:
        dinero_retirado = float(input("Introduce un dinero a retirar de la cuenta: "))
        if dinero_retirado <= dinero:
            dinero -= dinero_retirado
            print(f"El dinero retirado es: {dinero_retirado}$, le queda {dinero}$ en total")
        else:
            print("No tiene suficiente dinero en la cuenta.")
    elif opcion == 3:
        print(f"El dinero que tiene es: {dinero}$ en total\n")
    elif opcion == 4:
        print("Hasta otra")
        break
    else:
        print("Opción no valida")
