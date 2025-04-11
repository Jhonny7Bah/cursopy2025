# Dada a lista de dicionários abaixo, ordene-a de três maneiras diferentes:

# Pelo nome em ordem alfabética.
# Pela idade do menor para o maior.
# Pelo sobrenome em ordem decrescente (Z → A).
pessoas = [
    {'nome': 'Carlos', 'sobrenome': 'Almeida', 'idade': 25},
    {'nome': 'Eduarda', 'sobrenome': 'Santos', 'idade': 28},
    {'nome': 'Bruno', 'sobrenome': 'Ferreira', 'idade': 35},
    {'nome': 'Ana', 'sobrenome': 'Silva', 'idade': 30},
    {'nome': 'Fernanda', 'sobrenome': 'Rodrigues', 'idade': 22},
]

def filtro(filtragem):
    pessoas.sort(key= lambda x:x[filtragem])
    if filtragem == 'sobrenome': pessoas.reverse()
    for __ in pessoas: print(__)

filtro('sobrenome')
filtro('nome')

