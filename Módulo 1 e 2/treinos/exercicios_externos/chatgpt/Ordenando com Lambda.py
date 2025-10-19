# Objetivo: Utilizar lambda para ordenar uma lista de dicionários.
# Tarefa:

# Dada uma lista de dicionários representando produtos, onde cada dicionário tem as chaves 
# "nome" e "preco", use o método sort com uma função lambda para ordenar os produtos pelo preço em ordem decrescente.
# Em seguida, crie uma nova lista contendo apenas os nomes dos produtos nessa ordem.
# Exemplo:
produtos = [
    {'nome': 'Produto A', 'preco': 50},
    {'nome': 'Produto B', 'preco': 20},
    {'nome': 'Produto C', 'preco': 30},
    {'nome': 'Produto D', 'preco': 60},
]
# Resultado esperado (nomes ordenados por preço decrescente):
# ['Produto A', 'Produto C', 'Produto B']

#uso do def convencional
def forma1():
    def haha(dicionario):
        return dicionario['preco']
    produtos.sort(key=haha, reverse=True) 
    print(*produtos, sep='\n')
    nova_lista = [produtos[n]['nome'] for n in range(len(produtos))]
    print(nova_lista)
# forma1()
#uso do lambda
def forma2():
    produtos.sort(key=lambda x:x['preco'], reverse=True)
    print(*produtos, sep='\n')
    nova_lista = [produtos[n]['nome'] for n in range(len(produtos))]
    print(nova_lista)
forma2()

