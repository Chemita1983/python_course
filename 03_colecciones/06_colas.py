# Colas (con listas)

# FIFO -> First input, first output. Primero en entrar, primero en salir.

cola =  ["Chema", "Marta", "Maria"]

# Agregando elementos al final de la cola
cola.append("Juan")
cola.append("Carmen")
print(cola)

# Sacando elementos por el principio
elemento = cola.pop(0)
print(f"Sacando el elemento {elemento}")
print(cola)