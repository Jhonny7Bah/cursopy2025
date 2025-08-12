#importando depenências
import json

#definindo a classe
class Pessoa:
    #inicializando o construtor
    def __init__(self, nome: str, idade: int):
        #definindo os atributos de instância
        self.nome = nome
        self.idade = idade

#para o caso de eu executar em outro modulo
if __name__ == '__main__':
    #criando objeto e passando os atributos
    p1 = Pessoa('Cláudio', 13)

    #exibindo atributos
    print(p1.nome)
    print(p1.idade)

    compactacao = [p1.__dict__]

    #context manager para salvar em json
    with open('dados.json', 'w') as pd:
        json.dump(compactacao, pd)


