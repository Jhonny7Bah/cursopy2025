from  os import system
def apagar():
    return system('cls')


from itertools import combinations, permutations, product
listafds = [
    ['azul','verde'],
    ['m', 'g', 'gg'],
    ['poliester', 'algodão']
]

# produto = product(*listafds)
# print(*produto, sep='\n')
from copy import deepcopy


lista = ['joao', 'maria', 'ana', 'clara', 'pedro', [1,2,3]]
lista2 = deepcopy(lista)

lista[5][0] = 45
del lista[0]
print(lista)
print(lista2)

apagar()

from functools import reduce
produtos = [
    {'nome':'Produto 1', 'preco':10},
    {'nome':'Produto 2', 'preco':9},
    {'nome':'Produto 3', 'preco':4},
    {'nome':'Produto 4', 'preco':7},
]

def reduceFuncao(acumulador, produto):
    print(acumulador)
    print(produto)
    return produto['preco'] + acumulador

vamoos = reduce(
    reduceFuncao,
    produtos,
    0
)
print(vamoos)


