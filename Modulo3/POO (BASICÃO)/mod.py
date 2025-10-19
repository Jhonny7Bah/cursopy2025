# POO - Programação Orientada a Objetos - é um paradigma da programação que faz a organização do programa através 
# do uso de objetos
# Objetos são instâncias de classes.
# Uma classe, em termos simples, é um molde para o nosso objeto, tendo como componente atributos (valores definidos) e métodos (ações)

# Classe de exemplo:
# Por padrão, o nome de uma classe é definida com PascalCase
# Uma função quando utilizada dentro de uma classe passará a ser denominada de método.
class Pessoa:
    #após criar uma classe, normalmente temos uma função, começando com o construtor (init),
    # onde quando a função for executada, o init será uma das primeiras coisas a ser executada.
    def __init__(self, nome, idade): #-> self é uma referência a própria classe (instância temporária)
        self.nome = nome #aqui eu faço a criação de uma instância recebendo um nome (isso funcionaria como uma função) E aqui também é um atributo
        self.idade = idade #aqui mais uma outra instância 

    #criação de um método (ainda, nesse caso, é necessário fazer uso do self.)
    def saudacao(self):
        return f'Olá, eu sou o {self.nome} e tenho {self.idade} anos! Tudo bem com você?'

#Criação de um objeto
pessoa_um = Pessoa('Vitória', 17) #para isso, eu faço a chamada da classe na atribuição de uma variável e coloco como argumento os dados necessários. Segue a mesma lógica de uma função para parâmetros.

#se eu fizer assim, vai imprimir apenas o lugar na memória que esse objeto se encontra. 
#Como eu falei antes, funciona como uma função e é semelhante a um keyword args, com a diferença que esse é bem mais avançado.
print(pessoa_um)

#logo, para acessar do jeito certo, basta inserir o nome da instância/atributo desejada. Sendo para nome:
print(pessoa_um.nome)
print(pessoa_um.idade) #para idade

#para demonstrar na tela o uso do método saudacao
print(pessoa_um.saudacao())

#CASO EU QUEIRA CRIAR OUTRO OBJETO
pessoa_dois = Pessoa('Pedro', 23) #--> segue a mesma lógica de uma função. Ou seja, basta chamar e passar os argumentos.
#Agora vamos exibir
print(pessoa_dois.nome)

#se eu quiser, posso guardar algum dado em uma variável também.
mensagem = pessoa_dois.saudacao()
print(mensagem) #como viu, deu certo e com os novos dados.

#########################################################################
# Pilares da programação Orientada a Objetos

# Herança: Herança tem a ver com herdar, ou seja, você adquire alguma coisa de outra coisa. 
# No contexto das classes, haverá uma classe mãe e uma classe filha. Como de costume, a filha herda características da mãe, mas atente-se que é apenas algumas.

#Denominando classe mãe: 
class Animal:
    #um animal normalmente tem um nome, quando adotado.
    def __init__(self, nome):
        self.nome = nome
    
    #Animais terrestres tem a capacidade de andar também, quando não nascem com deficiência
    def andar(self):
        return f'O animal {self.nome} andou! '
    
    #E normalmente também, emitem som
    def emitir_som(self):
        ...

#na classe acima eu apenas formei algumas instâncias genéricas para o mundo animal.
#Agora, vamos criar uma classe filha, que vai herdar a classe mãe:

#para fazer herdar, basta colocar o nome da classe mãe nos parênteses
class Cachorro(Animal):
    #e agora, nesse momento, as instâncias da classe Animal estão aqui!
    #No entanto, não faria sentido criar uma outra classe se eu não tivesse necessidade de alterar algo.
    #Na classe animal, o método emitir som não tem uma ação exata, logo, será lá que iremos modificar,
    # que para fazer isso, basta chamar o método ou atributo novamente!
    
    def emitir_som(self):
        return "au au"

cachorro = Cachorro('Juliano')
print(cachorro.nome) #como pode ver, a classe cachorro Herdou o nome da classe animal
print(cachorro.andar()) #herdou o método andar
print(cachorro.emitir_som()) #e modificou o método emitir som

##########Polimorfismo -> O polimorfismo ocorre quando diferentes classes têm métodos com o mesmo nome,
#  mas comportamentos diferentes em subclasses de uma classe mãe (após uma herança.)

#A classe mãe é animal. Da classe mãe, criamos outra classe denominada de cahorro. Agora, vamos criar uma para gatos.
class Gato(Animal):
    #e vamos modificar o seu som.
    def emitir_som(self):
        return 'maiu' #aqui, fazemos a atribuição mais uma vez do método emitir som, que é derivado da classe Animal.
    #nesse exato momento, houve polimorfismo.

gato1 = Gato('Pedrinho')
print(gato1.nome)
print(gato1.andar())
print(gato1.emitir_som()) # e aqui você ver que novamente está diferente.

#Se fizermos separadamente:
print(cachorro.emitir_som())
print(gato1.emitir_som())
#São subclasses que foram derivadas da mesma classe, porém, teve um de seus métodos alterado. 
# Ou seja, é chamado o mesmo método e ocorrerá ações diferentes (Polimorfismo.)

####################### Encapsulamento
# Este pilar da poo é responsável por proteger dados sensíveis de uma classe. Esteja ela como atributo, instância ou até mesmo método.
#Private -> caracterizado por dois underlines. Quando você ver um método, instância ou sabe-se lá oq com __, significa que 
#aquilo só vai poder ser utilizado dentro da classe. Por padrão, o python faz uma leve proteção a encapsulamentos do tipo 
# private, mas tem como alternar fácil. 

#vou exemplificar
class ContaBancaria:
    def __init__(self, saldo):
        #como pode ver, estou protegendo o saldo.
        self.__saldo = saldo
        #mas e para acessar o saldo? para isso, basta criar funções que façam o tratamento adequado antes de fornecer.

    #aqui eu mostro quanto a pesosoa tem, sem permitir alterações diretamente no valor original.
    def mostrar_saldo(self):
        return self.__saldo
 

 ##########################
#  Abstração: Também há herança envolvida. Ou seja, você cria uma classe e essa classe que você criou será utilizada como um molde.
# Por exemplo, se você cria a classe animal e ela tem como filha a classe cachorro, não concorda que alguns métodos, como emitir som deveriam ser obrigatórios? É para isso que abstraçãos serve.

#Para garantir que isso ocorra, vamos precisar do módulo abc, tanto da classe como do decorador.
from abc import ABC, abstractmethod

#Agora, vamos criar a classe molde
class Veiculo(ABC): #-> vamos utilizar herança tbm
    #Nesse caso, você não precisa necessariamente colocar um init, a não ser que você vá usar diretamente essa classe para algo.
    #Logo, vamos direto para os métodos
    
    #E aqui, vamos inserir o decorator (isso vai obrigar a classe a ser remapeada) 
    @abstractmethod
    def ligar(self):
        ... #-> como será uma classe abstrata, não preciso também colocar parâmetros.

    @abstractmethod
    def desligar(self):
        ...

#para demonstração, vou criar um objeto e tentar executar a classe. No entanto,vou fazer um tratamento (pois sei que o código vai quebrar)
def execution():
# caso queira verificar a veracidade da informação, basta executar essa função.
    carro = Veiculo()
    return carro

#logo, para usar essa classe do jeito certo, vou precisar de uma outra classe que será a filha dela e passará os parâmtros.
class Moto(Veiculo):
    #esse eu posso deixar em branco
    def __init__(self):
        ...
    #sou obrigado a definir oq cada parâmtro deve fazer
    def ligar(self):
        return 'moto ligada'
    def desligar(self):
        return 'moto desligada'
    #se eu colocasse método apenas para ligar e não modificasse desligar, também iria dar pau. Se quiser testar, é só apagar uma das duas.

honda = Moto()
print(honda.ligar())
print(honda.desligar())


####################################
# Herança múltipla -> uma classe pode assumir atributos e métodos que uma classe mãe possui.
# Porém, ela não se limita a apenas uma classe mãe graças a classe múltipla, que é colocar duas ou mais classes como mãe 
# de uma classe em específico.

#Exemplo:
class Animal:
    #aqui eu vou denominar a instância
    def __init__(self, nome):
        self.nome = nome 

#agora, vou criar uma classe de animais para dois casos: Mamíferos e Aves.
class Mamifero(Animal): #-> recebe a classe animal como mãe
    def amamentar(self):
        return f'{self.nome} está amamentando!'

#vamos criar a classe ave agora
class Ave(Animal):
    def voar(self):
        return f'{self.nome} está voando!'

#posso criar normalmente alguns animais com tal classe
class Elefante(Mamifero):
    #não vou colocar nada aqui, pois não é necessário.
    ...

#aqui vou criar um objeto para demonstracao
elef_1 = Elefante('Pedrinho')
print(elef_1.amamentar())

#vou criar mais uma
class BeijaFlor(Ave):
    ...

#agora uma ave
bf_1 = BeijaFlor('Kauã')
print(bf_1.voar())

#Mas e se fosse um morcego, que é considerado uma mistura para ambos??? Simples, para isso, vamos criar uma herança multipla
# da seguinte forma:

class Morcego(Mamifero, Ave): #basta colocar no campo da herança e separar com vírgula
    #coloco mais um método (opcional)
    def emitir_som(self):
        return 'emitir som'

#crio um objeto para testar
morcegao = Morcego('batman')
#e agora, vou chamar todos os métodos disponíveis para a minha classe:

print(morcegao.amamentar()) #amametar, que é de mamímero, funciona;
# print(morcegao.voar()) voar, que é de ave, funciona
print(morcegao.emitir_som()) # e o som que o morcego ecoa também é efetivado

#parei na aula 9. 
# Pesquisar sobre o tal super.
#--------------------------------------------------------------------------
# Apenas para limpeza do terminal (ignore)
def cls():
    from os import system
    return system('cls')
#---------------------------------------------------------------------------

cls()
###################################################################
# Um decorador em Python é uma função especial que permite modificar ou estender o comportamento de outra função ou método sem alterar diretamente seu código.
# Ele é amplamente utilizado para adicionar funcionalidades de forma elegante e reutilizável, como validações, logs, autenticação, entre outros.
# Os decoradores são aplicados usando o símbolo @ antes da definição da função que será decorada. Veja:

#Primeiro, vou criar uma função qualquer
def meu_decorador(func):
    #como aqui eu vou executar uma outra função, vou precisar denominar uma aninhada para aplicar o closure.
    def wrapper():#Envoltório, invólucro ou embalagem (normalmente a aninhada para esse resultado tem esse nome)
        print('antes da função') #primeira coisa que vai executar, decorando a função.
        func() #depois a função passada como parâmetro da func principal executa
        print('depois da função') # e por fim, uma outra decoração é acionada.
    return wrapper

#para aplicar o conceito, vou precisar colocar o decorador na função que será decorada. 
#para isso, utiliza-se o @ e posteriormente, coloca-se o nome da função que vai decorar.
@meu_decorador
def minha_funcao():
    #vou colocar algo qualquer aqui
    print('olá, eu sou a função!')

#agora, na execução da função que vai ser decorada, ela se passa como argumento em no parâmetro func da função: "meu_decorador"
# e meu_decorador executa, exibindo elementos, podendo adicionar, remover ou incrementar elementos que minha_funcao não tinha.
# Tudo isso sem alterar o conteúdo principal da minha_funcao
minha_funcao()

###########também posso fazer com classes:
#denomino a classe normalmente
class MeuDecoradorDeClasse:
    def __init__(self, func):#aqui eu devo passar um argumeto que vai se remeter a função.
        self.func = func
    
    #__call__ denomina uma função dentro da classe, ou seja, quando eu chamar essa classe, o conteúdo presente no escopo de call
    # será como uma função e imediatamente será executado. E o restante, agirá como uma classe.
    def __call__(self):
        #mesma lógica anterior.
        print('antes da classe ser decorada')
        self.func()
        print('depois da classe ser decorada')

#aqui eu chamo o decorador
@MeuDecoradorDeClasse
#denomino a uma outra função
def segunda_funcao_decora():
    print('oláaaaaa')

#e faço a execução da função acima, para assim, efetivar a lógica e a decoração,
segunda_funcao_decora()
##########################################################################################

# decoradores comuns:
    #classmethod
    # staticmethod

class MinhaClasse:
    valor = 20 #isso aqui chama-se atributo de classe e pode ser acessado de qualquer lugar, desde que esteja dentro da classe.
    def __init__(self):
        pass

    # para acessar, basta colocar self e o namespace para o nome do atributo
    def value(self):
        return self.valor
obj = MinhaClasse()
print(obj.valor)

# posso fazer diretamente pela classe tbm
print(MinhaClasse.valor)

#no entanto, é apenas nesses casos. Pois normalmente, precisariamos de uma instância para acessar determinado valor de uma classe.

#################### static metod -> método estático
#é um método de classe utilizado como decorador para indicar que um método de classe ou um conjunto não haverá parâmetros como cls ou self. Ou seja, é literal um método parado.
# Segundo o professor, não é um bom sinal quando há uam quantidade meio grandinha de métodos estáticos.

# vou criar um exemplo qualquer
class Matematica:
    @staticmethod
    def somar(x, y):
        return x+y
# agora, basta criar um objeto
realizar_soma = Matematica.somar(10, 20)
print(realizar_soma)

#já o classmethod, é normalmente utilizado quando queremos criar instância para a nossa própria classe, trocando o self por cls. EX:
#o classmethod não depende necessariamente de um objeto ou de uma instância (self) para existir.
# class Pessoaa:
# def__init__(self, nome, idade, sexo):
    # self.nome = nome
    # self.idade = idade
    # self.sexo = sexo

# @classmethod
# def criar_com_idade(cls, idade, sexo, altura_padrao=1.70):
    # nome = f"Pessoa{idade}{sexo.upper()}"  # Nome genérico só pra exemplo
    # pessoa = cls(nome, idade, sexo)
    # pessoa.altura = altura_padrao  # adiciona atributo extra
    # return pessoa
# 

# Criando uma pessoa com classmethod
# p = Pessoa.criar_com_idade(25, 'f')

# print(f"Nome: {p.nome}")
# print(f"Idade: {p.idade}")
# print(f"Sexo: {p.sexo}")

##############################