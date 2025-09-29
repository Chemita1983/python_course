'''
Ejercicio 5

Descuento del 15% en una tienda
'''

gastado = float(input("Total gastado en una tienda: "))
gastado_descuento = gastado * 0.15
gastado_total = gastado - gastado_descuento

print(f"El 15% de {gastado} es: {gastado_descuento}. Tu compra sale a: "
      f"{gastado_total:.2f}")