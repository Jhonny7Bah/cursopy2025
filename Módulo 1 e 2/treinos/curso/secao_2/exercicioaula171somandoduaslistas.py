
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

def zipper(lista1, lista2):
    intervalo = min(len(lista1), len(lista2))
    return [
        lista1[i] + lista2[i]
        for i in range(intervalo)
    ]

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

print(zipper(l1, l2))

#############agora, quero que faça aparecer os valores restante da lista maior:
from itertools import zip_longest

def todos_valores(lista_1, lista_2):
    resultado = [
        x + y for x,y in zip_longest(lista_1, lista_2, fillvalue=0)
    ]
    return resultado
print(todos_valores(l1, l2))