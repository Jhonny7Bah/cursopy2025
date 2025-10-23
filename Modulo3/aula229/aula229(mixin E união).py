# O Objetivo dessa aula foi fazer uso do logMixin de forma prática, juntamente com herança.
# Devido a isso, preferi fazer algo mais organizado, em uma pasta separada do módulo principal.
# Ademais, haverá um arquivo irmão que armazenará o código do FileMixin pronto para uso.

# Importanto o módulo irmão.
from logMixinModulo import LogFileMixin

# Criando uma classe genérica 
class Eletronico:
    # todo eletrônico liga e desliga, sendo considerado isso um estado.
    def __init__(self, nome):
        self.nome = nome
        self._ligado = False # isso é um atributo protegido
    
    # agora, basta criar o métodos que irão gerenciar o estado citado anteriormente.
    def ligar(self):
        if not self._ligado:
            self._ligado = True
    
    def desligar(self):
        if self._ligado:
            self._ligado = False
    
# Agora, vamos criar uma especialização da classe eletronico
class Smartphone(Eletronico, LogFileMixin): # E logo após, chamamos também o nosso mixin.
    # lembrando que o mixin vai adicionar métodos extras em nossa classe.
    #
    # Agora, vamos modificar o método da primeira classe.
    def ligar(self):
        # para manter a lógica da classe eletronico, chamamos o super (sem o return)
        super().ligar()
        #após o super executar os seus passos, posso chamar os métodos da minha mixin
        if self._ligado:
            msg = f'{self.nome} está ligado'
            self.log_sucess(msg)
    
    # e o mesmo para desligado
    def desligar(self):
        super().desligar()
        if not self._ligado:
            msg = f'{self.nome} está desligado'
            self.log_sucess(msg)

# por fim, basta inicializar os objetos
galax_s = Smartphone('galax S')
# aqui, ele faz a atribuição no estado e ao mesmo tempo, salva o log
galax_s.ligar()
# aqui também ele altera o estado e salva no log.
galax_s.desligar()

# para ver, basta olhar o arquivo aula228LogFileMixin.txt
