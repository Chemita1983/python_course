# Excepciones propias

def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad debe der ser positiva")
    elif edad < 18:
        print("Eres muy joven")
    elif edad < 30:
        print("Eres joven")
    elif edad < 50:
        print("Eres maduro")



edad = int(input("Indique su edad: "))
try:
    verificar_edad(edad)
except ValueError as e:
    print(e)

