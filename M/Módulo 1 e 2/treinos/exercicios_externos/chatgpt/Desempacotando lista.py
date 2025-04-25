# Objetivo: Praticar desempacotamento de tuplas dentro de uma list comprehension.
# Tarefa:

# Dada uma lista de tuplas onde cada tupla contém um nome e uma idade, use list comprehension com desempacotamento
# para criar uma nova lista de strings formatadas no estilo "Nome: {nome}, Idade: {idade}".

# Exemplo:
pessoas = [("João", 25), ("Maria", 30), ("Pedro", 22)]

# Resultado esperado:
# ["Nome: João, Idade: 25", "Nome: Maria, Idade: 30", "Nome: Pedro, Idade: 22"]


formato = [f'Nome: {n[0]}, Idade: {n[1]}' for n in pessoas]
print(formato)



