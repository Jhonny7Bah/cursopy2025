#módulo três iniciado!!
#programação orientada a objetos (POO)

# Livros referências:
# Php programando com orientação a objetos
# python fluente
# padrões de projetos -> será utilizado mais pra frente!
#Patterns of Enterprise Application Architecture


#limpeza
from os import system
def cls():
    return system('cls')

###############################################
##introdução a classe
#incialmente, classes é um molde ou estrutura utilizada para representar ou modificar objetos.
#quando criamos uma variável, no python, não é necessário colocar o tipo de dado, pois o python é uma linguagem de tipagem dinâmica vai identificar o tipo de dado que você escreveu. 
#mas no caso abaixo, vamos fazer com que o tipo de dado apareça.
terracota = str('Marcoles Amigones')
# instancia = classe(atributo)
# terracota -> objeto
# str/float, int -> classe
# ('') -> atributo
#ou seja, os tipos de dados são classes do próprio python!!!!!!!!!

#Ademais, temos também os métodos, que são funções que modificam o atributo. Quando se trata de uma classe, os métodos são denominados de ações/funções.
print(terracota.upper())
#acima temos um uso prático de uma ação/função/método da instância str, no objeto terracota.

#dito tudo isso, vamos criar a nossa própria classe!
#para criar uma classe, você digita class e depois o nome da classe!
#Por convenção, os programadores decidiram utilizar PascalCase para definir nome de classes!
class MinhaClasse:
    ...
#como pode ver, acabei de criar a minha classe!
#agora, precisamos criar uma objeto(variavel) que vai guardar a nossa classe vazia.
bombadao = MinhaClasse() #tudo ok até aqui.


print(bombadao)#se printarmos a nossa classe, vamos ver informações sobre o módulo main, nome da classe, localização do objeto, etc.
#mas o que vai nos interessar agora são as instâncias! para criar uma instância com atributos, basta criar uma variavel com o nome do objeto, adicionar namespace e atribuir um valor!
bombadao.caramba = 20 #acabei de criar uma instância atributiva!
print(bombadao.caramba) #quando printamos, recebemos um valor padrão na tela, como esperado!

#diferença entre instância atributiva e ações/funções/métodos:
# dados dentro da classe = atributos
# ações/funcoes dentro da classe = métodos
cls()

####uso do __init__ e parâmetro self:
#No entanto, fazer uso de uma classe utilizando o método acima ficaria muito chato e repetitivo.
# Por isso, podemos utilizar dois recursos que vai agilizar o processo
# __init__ -> como vimos antes, o init é responsável por inicializar automaticamente alguma coisa. (na última vez, utilizamos para inicializar módulos)
# self -> o self é um parâmetro necessário que vai servir temporariamente como uma instância para criar um método para a classe respectiva.
#ficará assim:

class AutoClasse: #-> Iniciando a classe e nomeando-a
    def __init__(self, nome, sobrenome): #o init tem que ser o nome da nossa função(método), pois é através dele que a função vai iniciar 
        #e como eu falei, o self é o primeiros parâmetro que tem que ser definido, pois servirá temporariamente como uma instância.
        self.nome = nome #-> e aqui, vamos utilizar o self (instância temporária) e definir um método(nesse caso, atributivo)
        self.sobrenome = sobrenome #fazemos o mesmo aqui



NomeGalactico = AutoClasse('carlinhos', 'oliveira') #e aqui, definimos a nossa primeira instância, juntamente com os seus métodos.
'''
NomeGalactico = objeto
AutoClasse = Classe (a nossa)
Carlinhos, Oliveira = métodos atributivos

'''
#e o parâmetro self passará a ser NomeGalactico
print(NomeGalactico.nome) #como pode ver, tudo certinho
print(isinstance(NomeGalactico, AutoClasse)) #e como pode ver, o objeto NomeGalactico é pertecente a classe AutoClasse

#vou criar uma outro objeto da classe AutoClasse.
NomeMarcado = AutoClasse('Brunao', 13)
print(NomeMarcado.sobrenome) #como pode ver, tudo certinho aqui.

#Seria a mesma coisa que usar uma classe já existente:
objeto2 = str('fds') 
print(objeto2.lower)
print(isinstance(objeto2, str))
# são coisas semelhantes

cls()
#####################
# método -> uma função que está dentro da classe
class Carro:
    def __init__ (self):
        self.nome = 'fusca' #-> isso é hard coded (codificado), pois estou inserindo um valor padrão na mão

fusca = Carro()
Corsa = Carro()
print(fusca.nome)
print(Corsa.nome) #-> agora é perceptível a influência do hard coded, pois eu criei uma instância nova, mas o valor 'fusca' permaneceu.
print(Corsa)

#para resolver isso, seria interessante evitar o hard coded. Vou refazer a classe e explicar o uso de mais uma coisa, que no caso, é sobre método funcional ou ação.
#método funcional ou que realiza uma ação é um método que está dentro de uma função que pode fazer alguma alteração no valor do objeto(variável)

class SmartPhone:
    def __init__(self, ModeloSmartphone='noValue'): #-> também posso colocar um argumento padrão para não dar pau. 
        self.modelo = ModeloSmartphone #-> agora, evitamos o hardcode e colocamos a escolha do usuário!
    
    #abaixo, vou demonstrar um método funcional, ou seja, que vai executar uma ação que pode modificar o valor inserido.
    #no caso do método pontonofinal, ele vai incrementar um pontinho depois da atribuição.
    def pontonofinal(self): #como sempre, temos que usar o self como primeiro parâmetro.
        print(f'{self.modelo}.')

motorola = SmartPhone('MotoE6') #declarei uma variável (objeto) que vai armazenar um valor atributivo.
print(motorola.modelo) #aqui vemos o que foi inserido, mas não passa de método atributivo.
motorola.pontonofinal() #como pode ver, essa aqui é um método funcional e ele executou uma ação, que no caso, foi acrescentar um ponto ao final.
#como viu acima, deu certo.
##
######Lembrando que cada método dentro da classe tem o seu escopo. Ou seja, se eu declarar uma variável no escopo de um método e posterioremente, criar outro método, não irei conseguir acessar aquela variável do método anterior.
#Porém, se eu executar a classe anterior através do self.método(), irei executar e fazer algo com aquele dado.
cls()

#as classes tem a capacidade de guardar informações depois de executadas uma vez, podendo dar prosseguimento caso haja uma ocorrência de uma segunda chamada.
#no exemplo abaixo, vou demonstrar a mudança de dois estados:

class Cameras:
    def __init__(self, nome, filmagem=False):
        self.nome = nome
        self.filmagem = filmagem
        #acima eu crio a função base e defino os métodos da classe com base nos parâmetros da função
    
    def filmar(self):
       #aqui eu crio mais um método
       if self.filmagem:
           print(f'{self.nome} já está filmando. Volte em outro momento!!')
           return
       print(f'{self.nome} está filmando!!!')
       #como eu falei, as classes guardam valor. 
       #como já estudamos sobre função, em tese, já sabiamos disso, pois classe aparenta ser um conjunto de funções. 
       #logo, quando eu rodar o método filmar (associe a executar a função filmar), ele vai iniciar com um valor Falso

       self.filmagem = True# -> porém, aqui vemos uma nova atribuição de valor. Logo, se esse método for chamado novamente (estando no mesmo objeto), a primeira condição será atendida e ele executará uma nova ação.

camera_um = Cameras('Sony') #definição do nosso objeto

camera_um.filmar() #primeira execução do método
camera_um.filmar() #segunda execução do método no mesmo objeto (ação diferente.)

cls()
###vamos fazer uma exemplificação mais completa agora com o mesmo exemplo!

class Cam:
    def __init__(self, NomeDaCamera, CameraOcupada=False):
        self.NomeDaCamera = NomeDaCamera
        self.CameraOcupada = CameraOcupada

    def filmar(self):
        if self.CameraOcupada:
            print(f'A câmera {self.NomeDaCamera} já está filmando!')
            return
        print(f'Gravando... {self.NomeDaCamera} agora está ocupada!')
        self.CameraOcupada = True
    
    def fotografar(self):
        if not self.CameraOcupada:
            print(f'Fotografando várias fotos sem parar!!')
            self.CameraOcupada = True
            return
        print(f'A câmera {self.NomeDaCamera} está ocupada!!')
    
    def PararCamera(self):
        if not self.CameraOcupada:
            print(f'A câmera {self.NomeDaCamera} não está ocupada, ou seja, está livre para filmar ou gravar!!')
            return
        print(f'Finalizando execução da câmera {self.NomeDaCamera}... Ok, câmera desocupada!!')
        self.CameraOcupada = False
        
c1 = Cam('Sony')
c1.filmar()
c1.PararCamera()
c1.filmar()
c1.PararCamera()
c1.fotografar()
c1.PararCamera()
c1.filmar()

# Acima, eu fiz várias execuções para demonstrar o poder da classe mantendo vários estados que a câmera poderia se encontrar.
# Logo, através desses estados, posso fazer ações específicas e sem me preocupar com muita coisa, o que acaba sendo ótimo!
#E como eu disse antes, esses estados ficam salvos apenas para um objeto/variavel em especifico, como um método convencional do próprio python.
# Ou seja, se eu quiser manipular outro objeto ao mesmo tempo, não haverá problema, pois é como se fosse um escopo à parte. 
# Lembra que o último estado foi para filmar? sendo c1.filmar() ? se eu chamasse c1.filmar de novo, ele não iria filmar novamente porque a câmera ká estaria em uso, correto? Então, vamos testar com um novo objeto.
print('')
c2 = Cam('Canon')
c2.filmar() #como pode ver, não executou o código informando o uso da câmera.
# Logo, agora está provado que um objeto não interfere no outro!

cls()
###############atributos de classe
# São variáveis(objetos) criadas no escopo da classe para todas as instâncias 

class Pessoa:
    ano_atual = 2025 #aqui se situa o meu atributo de classe, e um detalhe importante é que ele é declarado antes das funções. 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def descobrir_ano_nascimento(self):
        #tenho duas formas de acessar um atributo de classe, sendo:
        # Pessoa.ano_atual -> é o jeito mais simples e que tem menos probabilidade de dar pau
        # self.ano_atual -> caso você defina algum método com o nome ano_atual e chamar a atribuição de classe dessa forma, o que você estará fazendo é reatribuindo um novo valor  a atribuição de classe.
        #por isso, a primeira forma demosntrada é a mais usual, pois há menos chance de ocorrer um erro. 
        ano_nascimento = Pessoa.ano_atual - self.idade
        return ano_nascimento


p1 = Pessoa('Carlos', 18)  
print(p1.idade)
print(p1.descobrir_ano_nascimento()) 


#se eu quiser alterar o atributo de classe fora da classe por algum motivo, basta colocar o nome da classe, namespace, o atributo e por fim redeclarar. ficando:
print('\nAgora vou reatribuir o valor do atributo de classe')
Pessoa.ano_atual = 2020 #-> fiz a redecalração e consequentemente, mudei o cálculo de toda a classe.
print(p1.descobrir_ano_nascimento()) #-> quando ano_atual = 2025, aqui retornou 2007
# e isso é o que pode acontecer quando você faz uso do self para o atributo dentro da classe.

cls()
#########################
#uso do __dict__ e do vars.
#Uma classe cria faz alterações em função do objeto, ou seja, quando eu tenho um objeto, basta eu colocar namespace e posteriormente, um método e ele realizará uma ação. Ex:
objeto = Pessoa('Márcio', 20) #->definimos o nosso objeto e atribuimos um valor para ele
print(objeto.descobrir_ano_nascimento()) #aqui, pegamos a atribuição do valor e realizamos uma ação.

#esse valores ficam armazenados dentro de um dicionário, ou seja, de um dict. Para você visualizar, basta:
print(objeto.__dict__) #-> aqui vemos tanto a instância como a sua atribuição.
#outra forma de ver é através da função var, que retornará também um dict.
print(vars(objeto))

#isso é muito útil quando eu quero armazenar uma classe em algum lugar externo ou algo assim, pois assim eu consigo pegar key e value do dicionário, tornando possível o replicar. ex:
armazenar = objeto.__dict__
p4 = Pessoa(**armazenar)
print(p4.descobrir_ano_nascimento()) #como pode ver, consegui replicar o ano de nascimento da pessoa.

#fora que eu consigo fazer alterações diretas também. ex:
p4.idade = 10 #aqui eu faço uma alteração da idade 
print(p4.__dict__) #como pode ver, a idade da pessoa foi alterada.

cls()

##############################
# métodos de classe + @classmethod + factories methods (métodos de fábrica)
class Pessoinha:
    anoatual = 2025 #aqui é um exemplo de atribuição de classe
    #vou conseguir acessar o ano atual de qualquer lugar do escopo dessa classe e até mesmo fora quando a classe for chamada.
    
    def __init__(self, nome, idade): #-> esse é o método convencional
        self.nome = nome
        self.idade = idade
    ######
        staticmethod #-> uma função/método que não utiliza self ou cls como primeiro argumento.
    # ou seja, é uma função convencional, considerada unútil pelo próprio Otávio, que aparentemente a única utilidade é quando você quer por algum motivo proteger o escopo da classe.
   
   
    @staticmethod
    def funcaoEstatica(*args, **kwargs):
        print('oiiii')
    ###que vai ser aq mesma coisa que isso
    def FuncaoEstatica(*args, **kwargs):
        print('oiiii')
    #coloquei args e kwargs para simbolizar os argumentos nomeados e não-nomeados, pois independente do caso ou uso, não fará diferença.
    #No entanto, vale ressaltar que uma utilidade extra para o staticmethod é para anotação.
    #por exemplo, quando uma pessoa for analisar o método, se ver o nome staticmethod lá, já vão identificar quem é estático, quem é método de instância e quem não é com mais facilidade.

    ##############
    #o class méthod é um decorator que não vai precisar de argumentos para sua execução em alguns casos.
    #ou seja, quando eu fizer a chamada da função saudação e não passar nenhum argumento, ele vai executar normalmente.
    #por padrão, é definido cls(que é o nome da classe) para sua execução. Como o class method é utilizado no escopo da própria classe, o parâmetro cls é preenchido com o respectivo. 
    # Ademais, o class method é algo trabalhado juntamente com hard coded e factory methods em alguns casos.
    ######USO:
    @classmethod  #-> aqui já fazemos uso do classmethod
    def saudacao(cls):
        #cls faz referência a própria classe, que nesse caso, é Pessoinha.
        print('seu bandido!!!') #e aqui é o que ele irá executar!

    #vamos tentar deixar esse negócio mais explicativo com um exemplo.
    #supunhamos que temos uma aba de dados para inserir pessoas que possuem 50 anos e precisamos de todas juntas.
    
    ###factory method
    # o factory pode ser utilziado em conjunto com o classe method. O que ele vai fazer é retornar um novo objeto.
    # por exemplo:
    @classmethod
    def criar_com_50_anos(cls, nome): 
        return cls(nome, 50)#retorna a própria classe Pessoinha recebendo dois argumentos: o nome e a idade
    #o que fizemos acima é um factorie method, que é um método que cria um novo objeto com alguma lógica ou algo arbitrário.

#########
class Dados:
    #InstanceMethods
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    #ClassMethods sem Factory
    @classmethod
    def saudacionar(cls):
        return 'tudo bem? '
    
    #ClassMethods com Factory
    # Cria um novo objeto
    @classmethod
    def retornar(cls, nome):
        idade = 50
        return cls(nome , idade) #agora, eu pego um parâmetro que é o nome, que será dito pelo usuário
        #e utilizo hard coded para o parâmtro idade, pois será sempre 50!!
    
    @staticmethod
    #staticmethod
    def saudacaodnv():
        return'opaaa'

pessoa1 = Dados('Carlos', 45) #definindo o objeto
###
print(pessoa1.nome, pessoa1.idade) #instancemethods
print(pessoa1.saudacionar()) #classmethods sem factory

#sobre os classmethod com factory, posso chamar dessas duas formas:
pessoa2 = pessoa1.retornar('Carlos') #chamando classmethods com factory diretamente de pessoa1
pessoa3 = Dados.retornar('Mário') #chamando classmethods com factory diretamente da classe.
print(pessoa2.nome, pessoa2.idade) #Classmethos com Factory
print(pessoa3.nome, pessoa3.idade) #Classmethos com Factory
print(pessoa1.saudacaodnv()) #staticmethod
####
"""
method ou instancemethod ou método de instância -> self
classmethod ou método de classe -> cls(abreviação de classe)
staticmethod ou método estático -> não tem cls e nem self. 
"""
        
#EXECUÇÔES!!!!!!!
# p1 = Pessoinha('Carlos',14) #a criação de um objeto
# print(p1.nome)
# print(p1.idade)
# ######################
# p2 = Pessoinha.criar_com_50_anos('Mário') #a criação de outro objeto, porém aqui eu não preciso digitar a idade, que será sempre 50
# print(p2.nome, p2.idade)
# # o class method é como se fosse uma extensão da própria classe, pois ele não conflita com elementos que nela já estiverem. é tanto que nem self ele tem.terracota
# # Pra entender com facilidade, é como se eu tivesse fazendo: Pessoinha(argumento1, argumento2), porém dentro da própria instâcia da classe.

# Pessoinha.FuncaoEstatica()
# Pessoinha.funcaoEstatica()#como pode ver, não houve diferença.


cls()
#################################
# property - um getter no modo pythônico!
# getter é um método para obter ou retornar um atributo.
#modo pythônico - modo de fazer as coisas utilizado funções, métodos, decoradores mais específico do próprio python! 
class Caneta:
    def __init__(self, cor):
        self.cor = cor
    #aqui eu crio um getter que irá receber o valor da cor e posteriormente, retornar.
    def getter(self):
        return self.cor
 
caneta = Caneta('azul')
print(caneta.getter()) #e aqui eu utilizo o método getter, que vai exibir na tela a cor!
#o método getter é útil para casos que você precise trocar o nome do atrinuto na classe.
# Porém, quando o programa é muito grande, o dev vai ter o trabalho de alterar tudo também!
#se houver código cliente, aí que complica mais ainda. 
# código cliente - é o código que usa o seu código
#Por isso, eu poderia criar um método com o nome do atributo e dentro, retornar o valor do atributo(com o nome dele em si já alterado na variável, deixando o código mais legível!!!)

###uso do property
#o getter é um exemplo de modo não-pythônico, pois ele é clássico para outras linguagens de programação.
#já o property faz a mesma coisa do getter, porém é um decorador exclusivo do python.
# Ademais, o property faz um método(função) se comportar como atributo (já executa na hora)
# property é um modo pythônico!

class Lapis:
    def __init__(self, cor):
        self.corTintaSLK = cor #considere que o antigo nome desse atributo era cor
    
    @property #aqui ele já vai executar a função cor quando chamada.
    #como o antigo nome do outro atributo era cor, se eu mudasse ele lá, iria ter que mudar em todo o código.
    #para agilizar, eu simplemente posso criar uma função com o antigo nome e fazer ela retornar a cor com base no novo nome do atributo.
    #com a ajuda do property, ele vai executar o método(função) assim que chamado!
    def cor(self):
        return self.corTintaSLK

l1 = Lapis('branco')
print(l1.cor)
print(l1.cor)
print(l1.cor)
print(l1.cor)
print(l1.cor)

cls()
################################
#####aula 213
# property + setter no modo pythônico!
#como dito anteriormente, o property vai inicializar uma função a partir do momento que é chamada.
#normalmente, o property é utilizado como como um getter, que no caso, é como valor atributivo no uso de um método.
#No entanto, o property acaba sendo um método que se comporta como um atributo durante a prática.
#Já o setter é um decorador que irá fazer a modificação em algum elemento do property, podendo também ser utilizado um controle para a ocorrência de algo. Na minha visão, parece muito com um decorator com syntax sugar.
class Canetaa:
    def __init__(self, cor):
        self._cor = cor
    #aqui acima inicializamos os atributos

    @property
    #já aqui, chamamos o property
    def cor(self):
        print('property')
        return self._cor
    #####
    #abaixo, chamamos o setter. O setter precisa ser chamado com o nome do método presente no property, como ilustrado abaixo.
    @cor.setter
    #com isso, podemos reutilizar o nome da property.
    def cor(self, valor): #-> aqui vemos um tal de valor, que nesse caso, vamos utilizar o setter para fazer uma alteração na cor.
        print('estou no setter, finalmenteeeee,', valor) 
        if valor == 'Amarelo': #aqui ele faz a verificação se o valor é amarelo
            raise TypeError('Não aceito essa cor! ') #se for amarelo, o código quebra
        self._cor = valor #se não for amarelo, o código aceita e atribui a nova cor.

caneta_azul = Canetaa('Azul') #inicialmente eu digo que a cor é azul 
print(caneta_azul.cor) #aqui será imprimido o azul na tela
caneta_azul.cor = 'Rosa' # e aqui eu faço uma reatribuição do valor, através do setter.
print(caneta_azul.cor) #antes era azul e agora é rosa

#######outra forma útil de fazer uso do setter é definir a atribuição de cara
cls()
class TamanhoCamisa:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    @property
    def tamanho(self):
        return self._tamanho
    
    @tamanho.setter
    def tamanho(self, valor):
        print('ESTOU NO SETTERRR')
        self._tamanho = valor
        
#com o método acima, o SETTER é inicializado juntamente do init
camisa_polo = TamanhoCamisa('P')
print(camisa_polo.tamanho)

#lembrando que vou ter que dar uma olhada nesse método depois!!!

# Por convenção, atributos que começam com um ou dois underline(s) não devem ser utilizados fora da classe, ou seja, fora do escopo da classe. ex: lapis._cor ou lapis.__cor
# método que é utilizado para a configuração de um determinado atributo
