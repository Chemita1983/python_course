'''
Ejercicio 3

Crear un programa que tenga una lista de clientes, cada cliente tenga su Nombre, Apellido, DNI.
El programa tendrá el siguiente menu de opciones

1 - Agregar nuevo cliente
2 - Mostrar todos los clientes
3 - Mostrar cliente por dni
4 - Eliminar cliente
5 - Salir

PD - Cada opción de menú se realizará con una función.
'''

def agregar_cliente(lista, n, a, d):
    cliente = {
        "nombre": n,
        "apellido": a,
        "dni": d
    }
    lista.append(cliente)

def mostrar_clientes(lista):
   for c in lista:
        print(c["nombre"], c["apellido"], c["dni"])

def mostrar_cliente_por_dni(lista, d):
    encontrado = False
    for c in lista:
       if c["dni"] == d:
           print(c["nombre"], c["apellido"])
           encontrado = True
           break
    if not encontrado:
        print(f"Cliente con dni {d} no encontrado")

def eliminar_cliente(lista, d):
    encontrado = False
    for i in lista:
        if i["dni"] == d:
            encontrado = True
            lista.remove(i)
    if not encontrado:
        print(f"Cliente con dni {d} no encontrado")

lista_clientes = []
while True:
    option = int(input(""" - MENU CLIENTES 
1 - Agregar nuevo cliente
2 - Mostrar todos los clientes
3 - Mostrar cliente por dni
4 - Eliminar cliente
5 - Salir
Seleccione una opción: """))
    print()

    if option == 1:
        dni = input("Ingrese DNI: ")
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        agregar_cliente(lista_clientes,nombre, apellido, dni)
        print()
    elif option == 2:
        mostrar_clientes(lista_clientes)
        print()
    elif option == 3:
        dni = input("Ingrese DNI: ")
        mostrar_cliente_por_dni(lista_clientes, dni)
        print()
    elif option == 4:
        dni = input("Ingrese DNI: ")
        eliminar_cliente(lista_clientes, dni)
        print()
    elif option == 5:
        print("Hasta otra...")
        break
    else:
        print("Opción no valida")