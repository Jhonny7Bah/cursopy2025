def cls():
    ##limpando terminal
    from os import system, name
    if name == 'posix':
        return system('clear')
    return system('cls')


# criando a classe que irá derivar todos os personagens
class Personagem:
    # haverá um nome, vida e level (padrão)
    def __init__(self, nome, vida, level):
        # aqui vamos utilizar o encapsulamento para as informações do personagem
        self.__nome = nome
        self.__vida = vida
        self.__level = level

    # e como consequência do private, vamos criar os property
    # property -> transforma um método em um atributo de classe
    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        return self.__vida

    @property
    def level(self):
        return self.__level
    
    # como esse aqui será alterado e chamado com o super, não vamos utilizar property
    def exibir_detalhes(self):
        return f'Nome: {self.nome}\nVida: {self.vida}\nLevel: {self.level}'
    #colocando a partir da p3
    def atacar(self, alvo):
        #vamos fazer o dano com base no level do persona
        dano = self.__level * 2
        print(f'{self.nome} atacou {alvo.nome}, ocasionando em {dano} de dano!\n')
        return dano

    #para o caso de receber dano
    def receber_dano(self, dano):
        self.__vida -= dano
        

# agora vamos criar a classe herói, utilizando da herança para pegar as características padrão do personagem.
class Heroi(Personagem):
    # no caso do herói, ele terá uma característica a mais: uma habilidade
    def __init__(self, nome, vida, level, habilidade):
        # para chamar as instâncias da classe mãe ativamente, vamos fazer uso do super e passar os nomes das instâncias
        super().__init__(nome, vida, level)
        # e aqui vamos criar a nossa nova instância
        self.__habilidade = habilidade
    
    # criar o property dela
    @property
    def habilidade(self):
        return self.__habilidade  

    # e modificar o exibir detalhes, inserindo agora 'habilidade'
    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nHabilidade: {self.habilidade}\n'

# agora, também com herança, vamos criar a classe que irá derivar todos os vilões
class Inimigo(Personagem):
    # a lógica é a mesma para a de heróis, com diferença na característica. Sendo que lá era habilidade e aqui será tipo.
    def __init__(self, nome, vida, level, tipo):
        super().__init__(nome, vida, level)
        self.__tipo = tipo
    
    # criar o property
    @property
    def tipo(self):
        return self.__tipo

    # como viu, houve divergências no resultado em relação a heróis, mesmo vindo de uma classe mãe comum.
    # essa é uma característica clara do polimorfismo.
    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nTipo: {self.tipo}'


class Jogo:
    '''Essa classe vai controlar o rumo do jogo'''
    def __init__(self):
        #vamos criar o nosso herói aqui
        self.heroi_principal = Heroi(nome='Heron', vida=100, habilidade='Super força', level=5)
        #e agora, o nosso vilão
        self.vilao_principal = Inimigo('Pedrinho da Goiaba', 50, 15, 'Bandido')
    
    def iniciar_batalha(self):
        '''essa classe vai controlar o rumo da batalha'''
        print('Batalha inicializada! \n')

        #agora, vamos controlar a luta. Enquanto o vilão ou o herói estiverem vivos, a luta permanecerá.
        while self.heroi_principal.vida > 0 and self.vilao_principal.vida > 0:
            #agora, vamos exibir as informações do heroi
            print('--- Herói (VOCÊ) ---')
            print(self.heroi_principal.exibir_detalhes())
            #e as informações do vilão
            print('--- VILÃO (OPONENTE) ---')
            print(self.vilao_principal.exibir_detalhes())

            #vamos gerar iteração com o usuário
            input('Pressione ENTER para atacar...')
            #COLETANDO TIPO DE ATAQUE DO PERSONAGEM.
            escolha = input('Escolha (1 - Ataque Normal, 2 - Ataque Especial): ')
            #para limpar o terminal
            cls()            

            if int(escolha) == 1:
                #heroi ataca vilão
                self.vilao_principal.receber_dano(self.heroi_principal.atacar(self.vilao_principal))
        #para quando um dos lutadores vencer a batalha
        else:
            cls()
            if self.heroi_principal.vida <= 0:
                print(f'{self.vilao_principal.nome} Venceu a batalha!')
            else:
                print(f'{self.heroi_principal.nome} Venceu a batalha!')



#vamos inicializar a classe com um objeto
jogo = Jogo()
jogo.iniciar_batalha()
















'''
vamos comentar o código abaixo por enquanto.
'''
# # e agora, vamos criar o nosso primeiro herói, passando suas características
# heroi_principal = Heroi(nome='Heron', vida=100, habilidade='Super força', level=5)
# print(heroi_principal.exibir_detalhes())

# # e por fim, vamos criar o nosso vilão
# vilao_principal = Inimigo('Pedrinho da Goiaba', 50, 15, 'Bandido')
# print(vilao_principal.exibir_detalhes())
