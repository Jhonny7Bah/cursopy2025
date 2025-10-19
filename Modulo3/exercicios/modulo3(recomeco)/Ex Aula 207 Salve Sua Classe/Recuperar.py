#importando a classe
from Salvar import Pessoa, json

#recuperando dados
with open('dados.json', 'r') as read:
    dados = json.load(read)

#recriando a instância com os dados recuperados
p1 = Pessoa(**dados[0])

#exibindo os dados
print(p1.nome)
print(p1.idade)

