# Pilas (con listas)

# LIFO -> Last input first output. Último en entrar, primero en salir.

pila = [1,2,3]

# Añadiendo elementos al final
pila.append(4)
pila.append(5)
print(pila)

# Sacando el último elemento
elemento = pila.pop() # pop retorna el último elemento que elimina
print(f"Sacando el elemento {elemento}")
elemento = pila.pop()
print(f"Sacando el elemento {elemento}")
print(pila)