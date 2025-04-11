# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

def dezPorcento(n):
    value = (n / 10)
    return round (value,2)

produtos = [
     {'nome': 'Produto 5', 'preco': 10.00},
     {'nome': 'Produto 1', 'preco': 22.32},
     {'nome': 'Produto 3', 'preco': 10.11},
     {'nome': 'Produto 2', 'preco': 105.87},
     {'nome': 'Produto 4', 'preco': 69.90},
]
#deepcopy + 10% do valor
novos_produtos = [
    {'nome':produto['nome'],
    'preco':produto['preco'] + 
    dezPorcento(produto['preco'])
    } 
    for produto in produtos]
##passando os produtos do maior para o menor
novos_produtos.sort(key=lambda x:x['nome'], reverse=True)

##nova variável através do deepcopy
from copy import deepcopy

produtos_ordenados_por_nome = deepcopy(
    sorted(produtos,
           key=lambda x:x['nome'], reverse=True
           )
)
produtos_ordenados_por_preco = deepcopy(
    sorted(produtos,
           key=lambda x:x['preco']
           )
)

def formatacao(valor, variavel):
    print(variavel, *valor, sep='\n')
    print('')

formatacao(produtos, 'p_antigos')
formatacao(novos_produtos, 'p_novos')
formatacao(produtos_ordenados_por_nome, 'p_orden_por_nome')
formatacao(produtos_ordenados_por_preco, 'p_orden_por_preco')