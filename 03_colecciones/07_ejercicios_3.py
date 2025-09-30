'''
Ejercicio 3

Escribe un programa que cree una lista con los siguientes personajes de El Señor de los Anillos
Nombre: Aragorn
Clase: Guerrero
Raza: Dunadan del norte

Nombre: Gandalf
Clase: Mago
Raza: Istar

Nombre: Legolas
Clase: Arquero
Raza: Elfo Sindar
'''

personajes = []

aragorn = {"Nombre": "Aragorn", "Clase": "Guerrero", "Raza": "Dunadan del norte"}
gandalf = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"}
legolas = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}

personajes.append(aragorn)
personajes.append(gandalf)
personajes.append(legolas)

print(personajes)
print(personajes[2]["Nombre"])