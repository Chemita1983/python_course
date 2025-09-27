'''
Operadores lógicos

Permite construir operaciones lógicas, se obtiene como resultado booleanos

And (Conjunción) and
Or (Disyunción) or
Negación not

And

True and True = True
True and False = False
False and True = False
False and False = False

Or

True or True = True
True or False = True
False or True = True
False or False = False

Not

Not (True) = False
Not (False) = True

Prioridad:
1 - Not
2 - And
3 - Or

Prioridad global:
1 - ()
2 - **
3 - *,/,mod,not
4 - +, -, and
5 - > ,< ,== ,>= ,<= , !=, or
'''

a = 10
b = 15
c = 20

resultado = not((a > b) or (b < c))
print(resultado)




