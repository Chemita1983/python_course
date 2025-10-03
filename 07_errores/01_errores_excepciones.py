# Errores y excepciones

# Existen 2 tipos de errores, del programador o del usuario

while True:
    try:
        numero = int(input("Ingresa un numero: "))
        print("El valor ingresado es:", numero)
    except : # Se ejecuta cuando hay alguna excepción
        print("El valor ingresado no es un numero")
    else: # Se ejecuta cuando no hay excepciones
        print("No ha habido excepción")
        break
    finally: # Se va a ejecutar siempre
        print("Iteración finalizada")

