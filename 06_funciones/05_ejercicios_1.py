'''
Ejercicio 1

Desarrollar un programa que pueda calcular el valor del tipo de cambio de moneda (de tu moneda hacia
dólar y viceversa)

'''

EUROS_TO_DOLLAR = 1.17
DOLLAR_TO_EUROS = 0.8509

def euros_to_dollars(euro):
    return euro * EUROS_TO_DOLLAR
def dollars_to_euros(dollar):
    return dollar * DOLLAR_TO_EUROS

while True:
    option = input("""
CAMBIO DE MONEDA
1 - € -> $
2 - $ -> €
3 - Salir
Seleccione una opción: """)

    if option == '1':
        euros = float(input("Ingrese un valor en €: "))
        print(f"Son {euros_to_dollars(euros):.2f} $")
    elif option == '2':
        dollars = float(input("Ingrese un valor en $: "))
        print(f"Son {dollars_to_euros(dollars):.2f} €")
    elif option == '3':
        print("Hasta otra...")
        break
    else:
        print("Opción no valida")