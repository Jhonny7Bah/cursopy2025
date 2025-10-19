#criando a classe que irá derivar todos os personagens
class Personagem:
    #haverá um nome, vida e level (padrão)
    def __init__(self, nome, vida, level):
        #aqui vamos utilizar o encapsulamento para as informações do personagem
        self.__nome = nome
        self.__vida = vida
        self.__level = level

    #e como consequência do private, vamos criar os getters.
    def get_nome(self):
        return self.__nome
    def get_vida(self):
        return self.__vida
    def get_level(self):
        return self.__level
    def exibir_detalhes(self):
        return f'Nome: {self.get_nome()}\nVida: {self.get_vida()}\nLevel: {self.get_level()}'

#agora vamos criar a classe héroi, utilizando da herança para pegar as cacterísticas padrão do personagem.
class Heroi(Personagem):
    #no caso do héroi, ele terá uma característica a mais: Uma habilidade
    def __init__(self, nome, vida, level, habilidade):
        #para chamar as instâncias da classe mãe ativamente, vamos fazer uso do super e passar os nomes das instâncias.
        super().__init__(nome, vida, level)
        #e aqui vamos criar a nossa nova instância
        self.__habilidade = habilidade
    
    #criar o get dela
    def get_habilidade(self):
        return self.__habilidade  
    #e modificar o exibir detalhes, inserindo agora 'habilidade'
    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nHabilidades: {self.get_habilidade()}\n'

#agora, também com herança, vamos criar a classe que irá derivar todos os vilões. 
class Inimigo(Personagem):
    #a lógica é a mesma para a de heróis,com diferença na característica. Sendo que lá era habilidade e aqui ser tipo.
    def __init__(self, nome, vida, level, Tipo):
        super().__init__(nome, vida, level)
        self.__tipo = Tipo
    
    def get_tipo(self):
        return self.__tipo
    #como viu, houve divergências no resultado em relação a heróis, mesmo vindo de uma classe mãe comum.
    # Essa é uma característica clara do polimifismo.
    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n'

#e agora, vamos criar o nosso primeiro heroi, passando suas características
heroi_principal = Heroi(nome='Heron', vida=100, habilidade='Super força', level=5)
print(heroi_principal.exibir_detalhes())

#e por fim, vamos criar o nosso vilão.
vilao_principal = Inimigo('Pedrinho da goiaba', 50, 15, 'Bandido')
print(vilao_principal.exibir_detalhes())