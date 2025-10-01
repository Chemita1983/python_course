'''
Ejercicio 11

Agenda telefónica

Hacer un programa que simule una agenda de contactos. Crear un diccionario donde la clave sea el nombre
de usuario y el valor sea el programa, con el siguiente menu de opciones

1 - Nuevo contacto
2 - Borrar contacto
3 - Ver contactos existentes
4 - Salir del programa
'''

contactos = {}
while True:
    print("------------- Contactos  -------------")
    print("1 - Nuevo contacto")
    print("2 - Borrar contacto")
    print("3 - Ver contactos existentes")
    print("4 - Salir del programa")
    option = int(input("Selecciona una opcion: "))

    if option == 1:
        nombre = input("Introduzca el nombre del contacto: ")
        telefono = input("Introduzca el teléfono del contacto: ")
        if nombre not in contactos:
            contactos[nombre] = telefono
        else:
            print(f"El contacto {nombre} ya existe")
    elif option == 2:
        nombre = input("Introduzca el nombre del contacto a eliminar: ")
        if nombre in contactos:
            del contactos[nombre]
        else:
            print(f"El contacto {nombre} no existe")
    elif option == 3:
        for nombre, telefono in contactos.items():
            print(nombre, telefono)
    elif option == 4:
        break
    else :
        print("Opción no valida")