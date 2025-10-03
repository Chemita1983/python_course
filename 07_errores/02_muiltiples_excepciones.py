# Multiples excepciones

def dividir():
    ok = True
    try:
        dividendo = float(input("Indica el dividendo: "))
        divisor = float(input("Indica el divisor: "))
        resultado = dividendo / divisor
    except ValueError:
        print("Datos introducidos no validos ⛔️, los datos deben de ser numéricos 🔢")
        ok = False
    except ZeroDivisionError:
        print("No se puede dividir por 0 😲")
        ok = False
    else:
        print(f"El resultado es: {resultado:.2f}")
    finally:
        if ok:
            print("Division finalizada con éxito ✅")
        else:
            print("Division fallida ❌")

dividir()