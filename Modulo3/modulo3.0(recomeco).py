#####################
def cls():
    ##limpando terminal
    from os import system, name
    if name == 'posix':
        return system('clear')
    return system('cls')

# Classe
# Por convenção, utilizamos PascalCase para denominar classes.
# classes são moldes para criar novos objetos. 
# Esses novos objetos são chamados de instâncias. Ex:
nome = str('Luciano')

#objetos também podem ser chamados de instâncias. Você pode chamar qualquer coisa que foi gerada por 
# uma classe de instância ou objeto

#nome é o objeto
# str é a classe
#Luciano é o atributo (atributos são dados que estão dentro da classe)

#mas, e o método? (métodos são funções que estão dentro da classe)
print(nome.upper()) #upper é o método

#para criar uma classe própria, chamamos a indicativa class e depois inserimos o nome da classe
class Pessoa:
    #por enquanto, vamos deixar vazio.
    ...

#agora, vamos criar uma instância
p1 = Pessoa() #-> isso aqui é uma instância/objeto e é através dela que vou nomear atributos
p1.nome = 'Maria' #atribui um atributo,denominado nome
p1.idade = 19 #atribui um outro atributo,denominado idade

#se eu printar assim, vai mostrar apenas o espaço na memória, pois os atributos estão
#contidos/protegidos na classe
print(p1)
#logo, para chamar do jeito correto, basta:
print(p1.nome) #para acessar o nome
print(p1.idade) #para acessar a idade

####Eu também posso criar uma outra instância/objeto, sendo para p2
p2 = Pessoa()
p2.nome = 'Clara' 
p2.idade = 22

#printando nome e idade, que nesse caso, como houve uma nova instância/objeto, serão diferentes 
# dos primeiros.
print(p2.nome, p2.idade)

####----
# No entanto, fazer dessa forma seria bem chato. Ter que definir tudo isso na mão parece ser bem tediante.
# É por isso que foi criado o self, que nada mais é que uma instância temporária.
#Imagine a seguinte definição: self = class() -> logo, self.nome = 'João'
#Dito isso, deixa eu mostrar na prática

class Alunos:
    #para isso funcionar, vamos precisar de um inicializador/construtor, que é o parâmetro init.
    #ele é responsável por iniciar a nossa instância e atributos de classe.
    def __init__(self, nome, turma): #e aqui, passamos o self (lembre-se do exemplo anterior).
        #acima, vou definir os parâmetros que eu quero (já que se trata de uma função)
        #abaixo, vou definir os atributos, como no exemplo:
        self.nome = nome #e aqui eu passo o parâmetro
        self.turma = turma

#agora, vamos inicializar a classe através de um objeto
aluno1 = Alunos('Carlos', '2° Ano')#e no parênteses, eu passo os argumentos (como uma função mesmo).

#e por fim, vamos exibir na tela:
print(aluno1.nome)
print(aluno1.turma)#como pode ver, bem mais simples e mais fácil!!!


#############################################################################
#Aula 200 e 201
# Um método é uma função que se encontra dentro da classe, normalmente tendo um 'self' como primeiro
# argumento, com o intuito de referenciar instâncias. Ex:

class Carro(): #aqui é a classe
    def __init__(self, nome_do_carro): #aqui é o construtor e o nome do veículo
        self.nome = nome_do_carro #quando eu denominar um objeto e chamar essa classe, o argumento que ele passar virá para cá.
    
    #bom, sabemos que um carro acelera e freia, né? para fazer com que isso ocorra, vamos precisar de um método.
    # Pois, um método ocasiona em uma ação e não consiste em exibir strings pré-definidas nos argumentos da classe, como um atributo

    #isso aqui é um método (uma função dentro da classe) e se realmente houvesse um carro correndo, bastaria mexer na variável que guarda sua velocidade em determinada situação.
    def acelerar(self):
        print(f'O {self.nome} acelerou e está a 100km/h')

fusca = Carro('Fusquinha')
print(fusca.nome) #aqui chamamos o atributo nome, que definimos na chamda da classe
fusca.acelerar() #e aqui o método, que fez com que o carro andasse mais rápido.

'''
Em resumo, o self é utilizado como referência para a instância. É de fato como se fosse uma variável que será 
substituída pelo nome do objeto que você declarar fora da classe.

Método é uma função dentro da classe, que ocasiona em ações. Ex: Upper ou lower da class str

atributo são valores pré-definidos que são inseridos na criação de um objeto.

curiosidade: o parâmetro self foi definido assim por conveção entre os programadores. Ou seja,
se você quisesse colocar qualquer outro nome no lugar de self como primeiro parâmetro e não usasse ele,
funcionaria.
'''

#um exemplo prático do self seria chamar a classe diretamente de seu molde.
try:
    #como a classe é um molde, ela necessitaria da instância. 
    Carro.acelerar()
except TypeError as e:
    print(e) #e como ela necessita da instância, vai dar pau se chamamos ela dessa forma.

#no entanto, poderiamos passar esse argumento que ela necessita.
Carro.acelerar(fusca) # e assim, ela não dará pau, pois agora ela tem a instância como argumento.
# Segundo o Luiz Otávio, esse não é um jeito comum de uso, mas é bom para entendimento e demonstração de seu funcionamento

###########################################################################################
# Aula 202, 203, 204 e 205
# Diferença entre atributo de classe e atributo de instância
class Animal:
    #abaixo, defini um atributo de classe, que não precisa necessariamente de uma instância para funcionar
    # Além disso, o atributo de classe pode ser utilizado em qualquer lugar da classe, ou seja, método.
    area = 'Terrestre' #Aqui será utilizado apenas para animais terrestres.

    def __init__(self, nome):
        #aqui, definiremos um atributo de instância, ou seja, que é protegido pelo namespace (escopo da função)
        #o atributo de isntância poderá ser utilizado apenas quando a função que o guarda ser acessada. 
        self.nome = nome

        #para acessar um atributo de classe, precisamos primeiro acessar o namespace da classe.
        #para isso, podemos fazer de duas formas: Através do próprio self ou do nome da classe em si. Ex:
        print(self.area) #acessando pelo self
        print(Animal.area) #acessando diretamente pela classe.
        #segundo o luiz otávio, é mais recomendado que você faça o acesso diretamente pela classe para evitar transtornos no futuro.
        #e realmente é melhor fazer uso através do escopo da classe, pois se houver um atributo de instância e um atributo de classe com os mesmos nomes, um iria sobreescrever o outro.
        

    #Agora, vamos decidir um método, ou seja, uma ação.     
    def comer(self, alimento):
        #realizando ação e ainda assim, utilizando atributo de classe e de instância
        return f'O {self.nome} , animal {Animal.area}, está comendo {alimento}'

#agora, vamos inicializar a classe com um objeto
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comer('Maçã')) 

#e para pura demonstação e diferentemente de um atributo de instância, eu consigo acessar tranquilamente um atributo de classe estando fora da classe e sem necessitar de objeto algum.
print(Animal.area)

#e como previsível, eu consigo alterar o valor do meu atributo de classe daqui
Animal.area = 'aéreo'
print(Animal.area) #como viu, houve alteração.

#focalizando na aula 203
##Em poo, as classes tem estado, como high ou low em C+. Ou seja, podemos habilitar uma série de ações com base nela. Ex:
class Camera:
    def __init__(self, nome, estado_filmando=False):#como eu liguei a camera agora, é evidente que significa que ela não está filmando
        #vamos inicializar as instâncias
        self.nome = nome
        self.filmando = estado_filmando
    
    #agora, vamos fazer as ações. Primeiro, para filmar
    def filmar(self):
        #mas antes de apertar no botão de filmar, precisamos verificar se ela não está filmando
        if self.filmando:
            return f'a câmera {self.nome} já está filmando!'
        #caso ela não esteja filmando, vamos colocar ela pra filmar
        self.filmando = True
        return f'a câmera {self.nome} agora está filmando!'

    #vamos agora fazer um método que irá encerrar a gravação,
    #verificando antes se a câmera realmente está em uso.
    def parar_gravacao(self):
        #se realmente estiver em uso:
        if self.filmando:
            self.filmando = False
            return f'A câmera {self.nome} parou de filmar! '
            
        #caso ela não esteja filmando:
        return f'a câmera {self.nome} não está em uso!'

#agora, vamos inicializar o nosso objeto com uma camera!
C1 = Camera('Canon')
#vamos colocar ela pra filmar
print(C1.filmar())
#e agora, vamos colocar ela para filmar de novo
print(C1.filmar()) #como pode ver, ela guardou o estado anterior.
#agora, vamos parar de filmar
print(C1.parar_gravacao()) 
#e por fim, vamos colocar pra filmar novamente
print(C1.filmar()) #e agora ela pode filmar novamente!

###################################################################
# Aula 206, 207 e 208
#__dict__ e vars -> fazem a mesma coisa com uma leve diferença, onde um é método e o outro é uma função.
#O objetivo deles é acessar um atributo de instância e retornar um dicionário, contendo como chave o nome da instância e como valor o seu atributo.
# Ex:
#inicializando o objeto
p3 = Pessoa()
#declarando um atributo de instância
p3.nome = 'Marcos'
#mostrando a saída normal
print(p3.nome) 
#agora, vou usar o dict.
print(p3.__dict__) #retorna chave e valor
#agora com vars
print(vars(p3)) #chave e valor também.

#e um detalhe importante é que isso não é apenas leitura. Ou seja, através de um deles
# posso alterar, incrementar ou remover valores, como um dicionário mesmo. ex:

#incrementando um novo
p3.__dict__['idade'] = 14
#agora o atributo de instância existe!
print(p3.idade)

#alterando atributo
p3.__dict__['nome'] = 'João'
print(p3.nome)

#apagando valores
del p3.__dict__['idade']
try:
    print(p3.idade)
except AttributeError:
    print('Como viu, o atributo de instância foi deletado!')

#e para deixar claro, esse tipo de manipulação não é comum. Mas mesmo assim, é bom saber pra saber que existe!


####Aula 209
# Como você viu na aula anterior, usamos certas convenções para nomes de variáveis, funções, classes e assim por diante.
# Essas convenções tem um nome que podemos usar para nos referir ao modo como estamos nomeando determinados objetos em nosso
# programa: PascalCase, camelCase e snake_case.

# PascalCase - significa que todas as palavras iniciam com letra maiúscula e nada é usado para separá-las, como em:
# MinhaClasse, Classe, MeuObjeto, MeuProgramaMuitoLegal. Essa á a convenção utilizada para classes em Python;

# camelCase - a única diferença de camelCase para PascalCase é a primeira letra. Em camelCase a primeira letra sempre será
# minúscula e o restante das palavras deverá iniciar com letra maiúscula. Como em: minhaFuncao, funcaoDeSoma, etc... Essa
# conversão não é usada em Python (apesar de eu confundir as duas e às vezes acabar chamando camelCase de PascalCase ou
# vice-versa, mas agora você sabe a diferença);

# snake_case - este é o padrão usado em Python para definir qualquer coisa que não for uma classe. Todas as letras serão
# minúsculas e separadas por um underline, como em: minha_variavel, funcao_legal, soma.

# Os padrões usados em Python são: snake_case para qualquer coisa e PascalCase para classes.

##########################################################################
# Aula 210 - classmethods + factories methods
class Pessoa2:
    ano_atual = 2025 #-> lembrando que isso aqui é um atributo de classe, ou seja, eu consido acessar fora da classe sem
    #necessitar definir uma instância

    #abaixo, estará o molde do objeto, necessitando de instância e de dois atributos.
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
    
    #ou seja, acessar atributos, temos o dois meios, sendo um através da classe (molde) e outro através de uma instância.

    #Para métodos, temos a mesma lógica. Exemplo, vamos criar um método abaixo:
    def exibir_nome(self):
        return f'seu nome é {self.nome}'
    
    #mas... você pode até perguntar: todo método precisa necessariamente de uma instância? NÃO!
    # Basicamente, temos um decorador denominado de classmethod (método de classe), que é bem semelhante a um 
    # atributo de classe. Ou seja, você poderá executar o método sem necessitar da instância, acessando somente pelo
    #namespace da classe.

    ## Classmethods
    @classmethod
    def exibir_ola(cls): #enquanto self faz referência a instância, cls faz referência a própria classe (molde). 
        #Pra você entender bem, imagine a seguinte atribuição:-> cls = Pessoa2 <- Considernando que o nome da classe é pessoa2
        # importante: O classmethod por si só não consegue acessar atributos de instância self, por isso, pode ser executado diretamente
        # sem necessitar de um objeto em questão.
        return 'ola'
    
    ## Factory Method
    # Usa @classmethod, logo recebe cls (classe).
    # Enquanto classmethod acessa a classe, o factory method cria uma nova instância da classe
    # com parâmetros diferentes dos passados diretamente ao construtor.
    @classmethod
    def criar_sem_nome(cls, idade):
        # cls aqui funciona como um callable, chamando __init__ com os argumentos definidos
        return cls("Anônimo", idade)

print(Pessoa2.ano_atual) #acessando o atributo de classe sem instância
EP1 = Pessoa2('Pedro', 19) #definindno a instância e os atributos necessários para a classe
print(EP1.exibir_nome()) #aqui, conseguimos executar o método em questão devido a existência da instância.
print(Pessoa2.exibir_ola()) #demonstrando o uso do classmethod, sem prcisar necessariamente da instância para execução.

#Aqui inicializamos o factories metods, passando a idade da pessoa diretamente.
EP2 = Pessoa2.criar_sem_nome(15)
print(EP2.idade)
print(EP2.nome)

#### Vamos dar um pouco mais de utilidade a esse Factories Methods: 
import json

class Pessoa3:
    #definindo o construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def from_dict(cls, dados):
        # Factory method que recebe um dicionário e trata para depois inicializar a classe
        return cls(dados['nome'], dados['idade'])

# Imagine que você recebeu isso de uma API:
json_data = '{"nome": "Ana", "idade": 25}'
dados = json.loads(json_data)

# Cria a instância usando o factory method
p = Pessoa3.from_dict(dados)
print(p.nome, p.idade)  # Ana 25
#Ou seja, esse factories methods basicamente fez o tratamento dos dados recebidos antes de entrar diretamente na classe.
#Com isso, não precisamos tratar diretamente no init, que sobrecarregaria um pouco a classe, principalmente em casos de dados
#que não precisem ser tratados. 
#Ademais, posso fazer inúmeros factories methods dentro de uma classe, ou seja, inúmeros tratamentos à parte.

#######################################################
cls()
#@staticmethod (métodos estáticos ) -> são métodos (funções) que ficam dentro
#da classe e que não tem acesso a self ou cls. Ou saja, uma função normal.
#Em python, aparenta não ter muita utilidade (como mencionado pelo Luiz). ex:

class Util:
    @staticmethod
    def dobro(x):
        return x * 2  # não usa self nem cls
# Chamando direto pela classe
print(Util.dobro(10))  # 20

# Chamando por uma instância (funciona igual, mas não precisa dela)
u = Util()
print(u.dobro(7))  # 14

# Mesmo resultado se fosse uma função solta fora da classe
def dobro(x):
    return x * 2
print(dobro(10))  # 20

##################################################################
# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    #inicializo o construtor com as instâncias necessárias
    #Chamamos isso de Method
    def __init__(self, host='localhost'): #em redes, o padrão para host é localhost
        self.host = host
        self.user = None #Como não sabemos o usuário e a senha, ambos serão None
        self.password = None
    
    #configurando um setter para "usuário"
    def set_user(self, user): #setter vai servir como um meio para alterar de None para outra coisa
        self.user = user

    #configurando um setter para "senha"
    def set_passoword(self, password): 
        self.password = password
    
    ###
    @classmethod #denomino uma classe que vai passar diretamente os argumentos para init
    def create_with_auth(cls, user, password): #informo os parâmetros necessários
        connection = cls() #inicializo o init
        #após inicializar o init, conseguirei ter acesso aos atributos de instância.
        #Com isso, basta apenas realizar as modificações
        connection.user = user 
        connection.password = password
        #após modificar, basta retornar e a classe inicializa de vez.
        return connection
        '''
        #O código acima faz exatamente a mesma coisa que o código abaixo faz
        return cls(host="localhost", user=user, password=password)        
        '''

    ### O staticmethod, como mencionado anteriormente, será utilizado como uma função normal. Pois não acessa cls e nem self.
    @staticmethod
    def soma(x, y):
        return x+y

#Inicializando a classe em um objeto    
c1 = Connection()
#exibindo o atributo de instância salvo por padrão em user
print(c1.user) # None

#fazendo um setter para alterar o atributo
c1.set_user('Alipio')
#solicito um print para verificar o novo nome
print(c1.user)# Alipio

#demonstração para classmethod + factories methods
#Nesse caso, não precisaremos passar os argumentos da classe diretamente pelo objeto
c2 = Connection.create_with_auth('Alipio', 12345)
print(c2.user, c2.password)

#demonstração do staticmethod
print(c2.soma(2, 2)) #4

##################################################################
#getter e property

# getter - um método para obter um atributo, ou seja, você utiliza de um método para que lhe seja retornado um atributo.
# Isso pode ser útil em um caso de código cliente, onde um ou mais desenvolvedores fazem uso de sua classe para sustentação
# de um código. Com isso, é bem provável que haja mudanças em suas classes e isso pode gerar transtornos no código cliente.
# Por exemplo: Se hoje você define o nome de uma instância de uma forma e amanhã quer trocar esse nome? essa ação não iria ocasionar
# em transtornos no código cliente? é a mesma coisa que você declarar uma variável, utilizar essa variável em outro lugar
#  e posteriormente alterar o nome da variável em sua definição. Com isso, surge um problema... como eu poderia resolver essa questão?
#Uma das formas seria utilizar o getter, que protegeria o escopo dentro de uma função. EX:

class Caneta:
    def __init__(self, cor, marca):
        #você poderia instanciar assim e falar que já está pronto para uso.
        #Porém, caso você mudasse o nome do atributo "cor", geraria transtornos.
        self.cor = cor #por isso,podemos instanciar e deixar um método fazer o restante

        ##property 
        self.marca_caneta = marca

    # definiria uma função
    def get_cor(self):
        #e toda fez que precisasse desse atributo fora da classe, chamava essa função. Logo, problema iria se resolver.
        return self.cor
    
    ### @property - um getter no modo Pythônico
    #Isso iria funcionar perfeitamente na maioria das linguagens. No entanto, em python, temos algo que na maioria dos casos,
    #funciona melhor que o jeito anterior. No nosso caso, é o property. O Property basicamente é um decorator que executa uma
    #função como se ela fosse um atributo qualquer, sem necessitar dos "()", é como se a função/método deixasse de ser callable, 
    # entende? Vou exemplificar.

    @property #como eu falei, aqui vai o decorator
    def marca(self): #aqui você coloca o nome que será chamada fora da classe
        return self.marca_caneta #e aqui você aponta para o atributo de instância dentro da classe.
        #logo, quando caneta.marca ser chamada fora da classe, esse método será executado e como consequência,
        #vai retornar o nome da marca da caneta.
    
    @marca.setter
    def marca(self, valor):
        self.marca_caneta = valor
        # print(valor)
        ...

#-------------- daqui para baixo será uma exemplificação de uso de um código cliente.

caneta = Caneta('azul', 'cross')
#no caso do getter, ao invés de fazer isso
print(caneta.cor)
#eu faria isso, através de uma função.
print(caneta.get_cor()) #isso iria garantir uma proteção extra ao código cliente.

##agora, vou demonstrar com property para a marca.
print(caneta.marca) # e como pode ver, a marca sai normalmente.
caneta.marca = 'fds'

cls()

######## Combinação de property + setter + getter
#De início, vou diretamente criar uma classe denominada filme
class Filme:
    def __init__(self, nome, categoria):
        #definindo um atributo de instância que pode ser acessado de qualquer forma
        self.nome = nome

        #nesse aqui, vamos fazer uma property
        self._exibir_categoria = categoria #Em poo, temos algo chamado de "protected", que informa por convenção 
        # que atributos ou métodos que começa com underline não deverá ser acessado fora da classe. Por isso o "_".

    #realizando o getter, como na classe anterior.
    #(o getter vai retornar o conteúdo presente no atributo de instância _exibir_categoria)
    @property
    def categoria(self): 
        return self._exibir_categoria
    
    #agora, vamos realizar um setter.
    #O setter é equivalente a uma mudança no atributo de instância _exibir_categoria
    #ou seja, se o usuário resolver alterar o nome do atributo, é necessário 
    # fazer a configuração a seguir para não ocasionar transtornos.

    #Para isso, vamos precisar utilizar um decorator que apontará para a função property e especificar o setter, veja abaixo:
    @categoria.setter 
    #agora precisaremos repetir a mesma função da pŕoperty. (Não se preocupe, ninguém vai sobrescrever ninguém.)
    def categoria(self, valor): # -> como parâmetro, é necessário especificar o self e posteriormente, o valor que será passado como argumento.
        if 2 == 2: #e a vantagem é que eu consigo fazer verificações aqui também 
            self._exibir_categoria = valor #-> agora, o valor que for passado aqui será inserido no atributo de instância "_exibir_categoria"
        else:
            raise TypeError('Não é possível instanciar esse tipo de coisa aqui')

f1 = Filme('Anabelle 2', 'Terror')
#sem o controle via property, eu consigo basicamente fazer qualquer coisa,
# como acessar o atributo e alterar o atributo. Ex:
print(f1.nome) #Anabelle 2

#vamos exibir a categoria atual
print(f1.categoria)

#vamos alterar agora
f1.nome = 'Psicopata Americano'

#exibir o novo atributo
print(f1.nome) # Psicopata Americano

#No caso da property
f1.categoria = 'Aventura' #você nem percebe que isso aqui é uma propery e que tem uma estrutura complexa rodando por trás dos panos...
print(f1.categoria) # Aventura

##----------Exemplo sem tantos comentários:
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self._preco = preco       # só leitura
        self._estoque = estoque   # leitura/escrita

    # Getter somente leitura
    @property
    def preco(self):
        return self._preco

    # Getter + setter para estoque
    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            raise ValueError("Estoque não pode ser negativo!")
        self._estoque = valor


# Teste rápido
p = Produto("Caneta", 2.5, 100)

print(p.nome)      # Caneta
print(p.preco)     # 2.5
print(p.estoque)   # 100

p.estoque = 50     # altera normalmente
print(p.estoque)   # 50

# p.preco = 3.0    # gera erro, pois preço é somente leitura


############################################################
cls()

#Revisão de setter + property e executando getter (property) no init
#Aula 214
class Cara:
    def __init__(self, nome):
        #executando o getter diretamente no init
        self.nome = nome
    
    #getter
    @property
    def nome(self):
        print('estou no getter')
        return self._nome
    
    #setter
    @nome.setter
    def nome(self, valor):
        print('estou no setter') #Chamo inicializar a classe, no mesmo momento, isso será imprimido.
        self._nome = valor

cla = Cara(nome='Joao')

# print(cla.nome)
# cla.nome = 'Pedropa'
# print(cla.nome)

################################################################
# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções:

#--------
#(sem underline) = public
#       pode ser usado em qualquer lugar

#--------
# _ (um underline) = protected
#       DEVE ser usado apenas dentro da classe ou suas subclasses.

#--------
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python. Após sofrer isso, o objeto fica com o aspecto semelhante
#       a _NomeClasse__nome_attr_ou_method. Sendo que só DEVE ser usado na classe em que foi declarado.
    
class Persona:
    def __init__(self, nome, idade, genero):
        #atributo de instância public
        self.nome = nome
        #atributo de instância protected
        self._idade = idade
        #atributo de instância private
        self.__genero = genero

    #método public
    def exibir_nome(self):
        #acesando public
        return self.nome
    #método protected
    def _exibir_idade(self):
        #acessando protected corretamente (dentro da classe que fora definido, também podendo ser acessado em uma herança)
        return self._idade
    #método private
    def __exibir_genero(self):
        #acessando private corretamente (dentro da classe que fora definido)
        return self.__genero

#inicializando objeto
p4 = Persona('joão', 17, 'masculino')

## acessando os métodos públicos
print(p4.nome)
print(p4.exibir_nome())

## acessando os métodos privados (da forma errada)
print(p4._idade)
print(p4._exibir_idade())
# aviso: vai funcionar perfeitamente. Mas, saiba que estará indo contra a conversão.


## Demonstrando o acesso a modificadores de acesso private (apenas para demonstração)
try:
    #vai dar erro devido ao name mangling (desfiguração de nome)
    print(p4.__genero)
except AttributeError as e:
    print(e) #'Persona' object has no attribute '__genero'
    #e agora, a forma para acessar esse atributo seria:
    print(p4._Persona__genero)
    #acessando o método da mesma forma
    print(p4._Persona__exibir_genero())

    #detalhe -> isso foi apenas para demonstração. Em hipótese alguma vocẽ deverá acessar um atributo ou método
    #privado fora da classe ou em uma subclasse. Isso só deverá ser acessado dentro da classe. Se fizer o contrário,
    #vai funcionar, mas estará indo contra a convensão.

##################################################################################
cls()
#Relações entre classes: Associação, Agregação, e composição.

# Associação é uma relação fraca entre duas classes, que liga uma a outra no mesmo sistema.
# Relação fraca -> Não há dependência. Ou seja, você pode utilizar as classes em conjunto ou individualmente. 
# Na natureza, associação seria algo semelhante a uma protocooperação entre objetos. Ou seja, eles não precisam um do outro
# para realizar suas tarefas, mas junto com o outro, pode funcionar melhor.
# Além disso, quando realizamos uma protocooperação entre objetos, podemos utilizar seus atributos ou métodos estando em
# outra classe. (é por isso que o método escrever funciona sem problemas na classe escritor.)

#definindo a primeira classe
class Escritor:
    def __init__(self, nome):
        self.nome = nome
        #aqui vai ficar a outra classe ou atributo mesmo. Como não há nada ainda, será None.
        self._ferramenta = None #fazendo isso de forma protegida
    
    # realizando o getter para manusear o atributo protegido 'ferramenta'
    @property
    def ferramenta(self):
        return self._ferramenta
    
    #agora o setter para atribuir o valor para ferramenta, podendo ser uma classe ou valor qualquer.
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

#definindo a segunda classe
class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome
    
    #criando o método para retornar o conteúdo do atributo de forma decorada
    def escrever(self):
        return f'{self.nome} está escrevendo!'

#inicializando o primeiro objeto com um atributo de instância
escritor = Escritor('Luiz')
#agora, vamos inicializar o segundo objeto com um outro atributo de instância.
caneta = FerramentaDeEscrever('Caneta Bic')

#para provar que eles não são dependentes, vou inicializar eles sozinhos:
print(escritor.nome) #Luiz
print(escritor.ferramenta) #None

print(caneta.nome)# Caneta Bic
print(caneta.escrever())# Caneta Bic está escrevendo!

#agora, vamos iniciar uma protocooperação
#lembra do atributo de instância ferramenta, que tem setter? é lá que vamos colocar o objeto 
escritor.ferramenta = caneta #agora, os métodos e atributos que estão em canetas poderão ser acessados através do objeto escritor
#método escrever
print(escritor.ferramenta.escrever())
#atributo de instância nome
print(escritor.ferramenta.nome)

#Com isso, foi provado que na associação a protocooperação de fato é efetiva. 


###################
# Agregação é quando dois objetos podem existir sozinhos,
# mas geralmente trabalham melhor juntos.
# Em relações entre classes, é uma forma mais específica da associação:
# levemente mais forte, mas ainda considerada fraca,
# pois cada objeto pode viver de forma independente.
#
# Exemplo: um carro e um pneu. O pneu não precisa do carro
# para existir, e o carro existe como objeto mesmo sem pneus.
# Porém, um carro sem pneus não é muito útil, criando uma
# leve dependência.
# Obs.: as definições podem variar um pouco em outros materiais.
#
# No exemplo abaixo, vamos utilizar o objeto carrinho de compras e produtos, no contexto de um mercado.
# Para um melhor contexto, é sabido que você pode fazer uso de um carrinho sem colocar produtos lá
# dentro, correto? Assim como também é possível pegar um produto sem necessariamente precisar 
# de um carrinho. No entanto, quando se trata de vários produtos, para maior agilidade de coleta e
# somatória, é melhor pegar o carrinho... assim, será muito mais rápido tanto para você como para o caixa.


class Carrinho:
    def __init__(self):
        #aqui será armazenado a quantidade de produtos dentro do carrinho
        self._produtos = []

    #método para inserir produto
    def inserir_produtos(self, *produtos):
        self._produtos += produtos

    # método útil para listar os produtos
    def listar_produtos(self):
        for numero, produto in enumerate(self._produtos, start=1):
            print(f'{numero}° produto é: {produto.nome} e o preço é {produto.preco} reais')
    
    #uma funcionalidade extra e útil para o carrinho seria também a somatória dos produtos (o que não é necessário, mas é útil)
    def somar_tudo(self):
         print(sum(
            produto.preco
            for produto in self._produtos
        ))

#agora a classe produto, contendo nome e preço
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

#### demonstração

#vou desempacotar dois produtos (dois objetos) através da classe Produto.
p1, p2 = Produto('farinha', 5), Produto('caneta', 1.20)
print(p1.nome) # farinha
print(p1.preco) # 5

#Com isso, foi provado que o objeto p1 (o mesmo vale para p2) não precisa do carrinho.

## criando o carrinho
c = Carrinho() #inicializamos o carrinho em um objeto
c.listar_produtos() #lista o que tem dentro do carrinho (nada)
c.somar_tudo() #soma o que tem dentro do carrinho (nada)

# Com isso, também foi provado que o carrinho não precisa do produto para funcionar.
# Ou seja, ambas funcionam (o que prova a relação fraca), mas na maioria dos casos,
# usar dessa forma não vai ser muito eficiente... por exemplo, e se for mais de um
# produto e ambos fossem maiores? haverá problemas...

# Por isso, podemos combinar da seguinte forma:
c.inserir_produtos(p1, p2) #colocamos os objetos que guardam os produtos no método inserir_produtos, da classe Carrinho.
#agora, eu consigo ver quais produtos tem no meu carrinho
c.listar_produtos()
# e também conseguimos somar tudo
c.somar_tudo() 

# Com isso, aprendemos um pouco do funcionamento da agregação, que é um tipo específico de associação entre classes.

#########
# Composição é uma forma mais forte de agregação:
# o objeto "pai" é responsável pelo ciclo de vida do "filho".
# Quando o pai deixa de existir, o filho também é destruído.
#
# Em Python, o gerenciamento de memória é automático.
# O garbage collector (GC) identifica objetos sem referências
# e libera sua memória. Em CPython isso normalmente acontece
# assim que o contador de referências chega a zero,
# mas a ordem e o momento exatos não são garantidos.
#
# Exemplo: um Livro é composto por várias Páginas.
# Se o Livro é destruído, as Páginas deixam de existir como parte desse livro.

#pai
class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        # Ao criar o livro, criamos também as páginas
        #Perceba também que a classe página foi inicializada dentro da classe livro, 
        #criando assim uma relação entre classes.
        self.paginas = [Pagina(numero) for numero in range(1, total_paginas + 1)]

    def listar_paginas(self):
        for pagina in self.paginas:
            print(f'Página {pagina.numero} do livro "{self.titulo}"')
    
    # Em Python, __del__ (destrutor) é executado quando o garbage collector decide
    # liberar um objeto que não tem mais referências. O comando del apenas remove
    # uma referência, o que pode levar o GC a destruir o objeto e disparar __del__.
    def __del__(self):
        print('o livro {} se perdeu!!!!'.format(self.titulo))

#filho
class Pagina:
    def __init__(self, numero):
        self.numero = numero
    
    # Quando o objeto que inicializa a classe livro for apagada, a classe página será apagada
    # Também, já que a vida da classe Página será gerenciada pela classe Livro quando Livro for 
    # inicializada em um objeto.
    def __del__(self):
        print('a página {} está se perdendo...'.format(self.numero))

### Demonstração
livro = Livro("Python Essencial", 3)

# O livro gerencia as páginas
livro.listar_paginas()
# Saída:
# Página 1 do livro "Python Essencial"
# Página 2 do livro "Python Essencial"
# Página 3 do livro "Python Essencial"

# Se removermos a referência ao livro, suas páginas também serão apagadas
# pelo Garbage Collector quando não houver mais uso.
del livro
# Agora não temos mais acesso às páginas
print('###################aqui termina o codigo')

######################################################################################
#### Herança simples - Relações entre classes
# Associação - um objeto usa outro objeto
# Agregação - um objeto tem outro objeto
# Composição - um objeto É dono de outro objeto e gerencia seu tempo de vida
# Herança - um objeto É outro objeto (relação "é um")
#
# Herança vs Composição
# Herança não faz parte da composição, pois não se trata de uma relação de "ter", e sim de "ser".
# - Na herança: Usuario É uma Pessoa
# - Na composição: Livro TEM Páginas
#
# Nomenclaturas
# Classe principal:
#   -> super class, base class, parent class
# Classes filhas:
#   -> sub class, child class, derived class

# Super classe
class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def mostrar_classe(self):
        # retorna a classe real da instância
        return self.__class__.__name__

# Classe filha herdando Pessoa
class Usuario(Pessoa):
    ...

p1 = Pessoa('Pedro', 17, 'Feminino')
print(p1.idade)
print(p1.mostrar_classe())  # Pessoa

# Na declaração do objeto, o construtor de Pessoa será o mesmo de Usuario.
u1 = Usuario('Caua', 14, 'Feminino')
print(u1.idade)
print(u1.mostrar_classe())  # Usuario

# MRO -> Method Resolution Order:
# Refere-se à ordem de busca de métodos e atributos em uma hierarquia de classes.
# No exemplo, Usuario herda de Pessoa, e ambas herdam de object (implícito em Python 3).
print(Usuario.mro())  # forma prática de visualizar a ordem de resolução

# Pra você ter noção, antigamente, no Python 2, uma classe era declarada assim:
class Ex(object):
    ...
# Hoje em dia, em Python 3, não precisa mais. Mas de toda forma,
# object continua sendo a raiz da hierarquia de classes do Python.

# Informação importante:
# Ao usar herança, você herda atributos e métodos da classe mãe. Isso significa que
# parte do comportamento já vem pronto e, em muitos casos, não é necessário reescrevê-lo.
#
# O problema é que, quanto mais níveis de herança você cria, mais difícil fica entender
# de onde vem cada método ou atributo. Esse acoplamento pode deixar o código complexo
# e difícil de manter.
#
# Por isso, uma boa prática para iniciantes é limitar a hierarquia a, no máximo, 3 níveis.
# Passou disso, geralmente é mais indicado usar composição (relação entre classes) em vez
# de herança profunda.

#######################################################################################################3
cls()

### Eu também posso herdar classes que já existem e fazer alguma mudança. Por exemplo:
class MinhaClasse(str): # -> herdei elementos da classe str
    def lower(self): # -> vamos alterar apenas o método lower
        return 'Tudo bem'

# vamos inicalizar a classe com um objeto
string1 = MinhaClasse('Olá, amigo!')

# Os demais métodos que não foram modificados da classe str, vão funcionar normalmente
print(string1.upper()) # OLÁ AMIGO

# mas o lower (que foi modificado), vai retornar o que definimos
print(string1.lower()) # Tudo bem 

### Uso do super
# no caso de você querer fazer uma modificação leve em um método, como um logger:
class MinhaClasse2(MinhaClasse): #-> vou herdar os atributos e métodos da minha classe
    def lower(self):
        print('Vou deixar tudo minúsculo!')
        # o super busca na superclasse o método existente. Com isso, podemos utilizar o super como
        # uma ponte para retornar o próprio método com o estado anterior.
        return super().lower() 

        #O super acima também recebe argumentos, sendo:
        # 't' -> primeiro a classe que ela se encontra no momento
        # 'obj' -> o segundo, que é self (a instância).
        #
        # No caso dessa classe, tais argumentos não foram passados.
        # No entanto, se fosse para passar, seria da seguinte forma:
        # 
        # super(MinhaClasse2, self).lower()
        #
        # Mas, em python, quando você chama o super da forma como eu fiz no return, ele já
        # Vem com os parâmetros declarados iniciamente dessa forma como demontrei acima, evitando
        # Verbosidade.
        #
        # No entanto, sabemos que o super dessa classe é "MinhaClasse". Isso acontece porque,
        # ao chamar super(), o Python entende automaticamente que estamos dentro da classe
        # "MinhaClasse2", que, por sua vez, é uma subclasse de "MinhaClasse".
        #
        # Assim, o interpretador reconhece que "MinhaClasse2" possui uma superclasse
        # e faz a busca nela. É justamente esse processo que permite que o método
        # "lower()" seja executado, mesmo não existindo diretamente no escopo de
        # "MinhaClasse2". O Python então localiza o método correspondente na classe
        # mãe ("MinhaClasse") e o executa.

string2 = MinhaClasse2('Carlito')
print(string2.lower())


### Outro caso de uso do super

class Animal:
    def __init__(self, especie): # o constutor necessitou de um parâmetro, que no caso, foi a espécie
        self.especie = especie

# como as classes abaixo são classes filhas, ao serem inicializadas, irão precisar do argumento "espécie" também para
# inicializar.
class Gato(Animal):
    # no entanto, se aqui fosse necessário um parâmetro a mais, como raça?
    # Se simplemente fizermos:
    # def __init__(self, raca): 
    # Isso iria sobrepor o init original, eliminando o parâmetro espécie.
    #
    # Para evitar isso, usamos o “super()” para acessar o construtor da classe mãe (Animal)
    # e reaproveitar seus parâmetros.

    def __init__(self, especie, raca): # eu sei que o parâmetro que tem lá é especie, logo, adiciono ele no construtor.
        self.raca = raca
        super().__init__(especie) # e para acessar, utilizo o super para fazer o acesso ao parâmetro original
        # Com isso, eu crio um novo parâmetro no construtor e já inicializo com o self, presente na classe original. 

    # Além disso, consigo incrementar um método aqui também, que seja apenas dessa classe e de suas filhas.
    def ronronar(self):
        print('vrum vrum cvrummm')

# Mas, quando os parâmetros de uma superclasse são inúmeros, passar cada parâmetro do init em um super acaba sendo 
# um tanto quanto demorado... é por isso que há uma segunda opção: Utilizar argumentos nomeados e não nomeados com
# empacotamento e desempacotamento. Veja no exemplo abaixo:
class Cachorro(Animal):
    # Inicialmente, chamo o método que precisará ser modificado e passo o parâmetro que quero incrementar.
    # Após passar tal parâmetro, passo *args e **kwargs para empacotar todos os parâmetros recebidos, de forma flexível
    def __init__(self, sexo,*args, **kwargs):
        # agora eu posso instanciar o novo parâmetro
        self.sexo = sexo
        # e no super, chamar o init da superclasse e desempacotar os parâmetros lá existentes.
        super().__init__(*args, **kwargs)

        # Com isso, modifiquei o construtor sem necessitar adicionar os parâmetros manualmente.

        # Desvantagem: Não preserva a tipagem e na chamada do método para instansciar externamente 
        # (criação de um objeto à partir da classe), os parâmetros não aparecem.

# agora, inicio a classe normalmente.
generico = Animal('gaha')
gato1 = Gato('felino','siamês')
cachorro1 = Cachorro('fêmea', 'rottweiler')

# objeto inicializado à partir da classe Animais
print(generico.especie)
print(generico.__dict__) #{'especie': 'gaha'}

# objeto inicializado à partir da classe Gato
print(gato1.raca)
gato1.ronronar()
print(gato1.__dict__) # {'raca': 'siamês', 'especie': 'felino'}

# objeto inicializado à partir da classe Cachorro
print(cachorro1.especie)
print(cachorro1.__dict__)





##################################################################################################################

### Explicando melhor o MRO (Method Resolution Order)
# Inicialmente, vamos criar três classes que receberão os mesmos atributos de classe e métodos.

class A:
    atributo_a = 'valor a'

    def demonstrar(self):
        print('A')
##
class B(A):
    atributo_b = 'valor b'

    def demonstrar(self):
        print('B')

##
class C(B):
    atributo_c = 'valor c'

    def demonstrar(self):
        print('C')

# vamos inicializar apenas a classe C
c = C()

# vamos verificar o mro das classes
print(A.mro()) #[<class '__main__.A'>, <class 'object'>]
print(B.mro()) #[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
print(C.mro()) #[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

# Logo, percebemos que a classe C herdou todas as classes anteriores, pois:
# A não herdou ninguém
# B herdou de A
# C herdou de B

# Logo, C tem todos os atributos e métodos das classes anteriores.

# Porém, no mro, a hierarquia começa da classe que foi chamada. No exemplo acima,
# Se eu busco o mro à partir da classe A, o método "demonstrar" vai imprimir na tela
# a letra 'A'
#
# Isso acontece porque a busca no mro vai começar da classe ou opbjeto que ele foi chamado.
# Com isso, ele busca determinado método ou atributo na classe que eu chamei. Se ele não encontrar,
# Ele busca na classe mãe (se houver). Se ainda assim na classe mãe não houver, ele busca nas outras
# classes que estão ligados a ele através da Herança. E se ele não encontrar em nenhuma das subclasses,
# será retornado erro na tela. No entanto, se ele encontrar, vai parar de buscar e inicializar o método
# em questão. É como se fosse um for buscacando algo com auxilio de um if, que quando encontra, aciona o break.  

#exemplo:
# a busca começa na classe C, mas na classe C não existe atribuito de classe a,b ou c. Logo, ele buscará nas subclasses.
print(c.atributo_a) # inicializa em C, depois busca em B e logo busca em A, encontrado. 
print(c.atributo_b) # inicializa em C, depois em B, encontrado.
print(c.atributo_c) # inicializa em C e encontra em C.

# abaixo, o demonstrar existe em todas. Tanto A, como B e C. Mas como eu disse, o mro começa a da classe que foi chamada e
# como em C existe o método demonstrar, a busca é finalizada. (famosa sobreposição)
c.demonstrar() # inicializa em C e encontra em C.

######
# Como foi visto anteriormente, em um dos casos de uso do super, podemos fazer alguma modificação em uma classe e ainda
# chamar o método da função anterior, correto?

class D(C):
    atributo_c = 'valor D'

    def demonstrar(self):
        # super().demonstrar()
        # se eu deixar assim, ele vai chamar automaticamente o método da função mãe de D, que no caso, é C.
        # Isso seria o equivalente a super(D, self).demonstrar()
        #
        # Isso significa que eu indico que a classe é D (a atual) e também indico o objeto (self).
        # Mas e se eu falar pra ele que essa classe na verdade é B?
         
        super(B, self).demonstrar() # retorno: A

        # Isso significa que eu disse pra ele que a classe que ele começará a busca para o mro
        # é B e como se trata de superclasse, ele foi procurar a superclasse de B, que no caso é A.
        #
        # É como se eu falasse: Ei, agora você não deve iniciar a busca por D, você deve começar por B.

        # Importante:
        # Se eu não quisesse usar o super() para acessar um método da classe mãe, 
        # eu poderia chamar diretamente a classe base (caso eu saiba qual é) junto 
        # com o método e o argumento de instância (self). Isso executa algo semelhante 
        # ao super(), mas não faz a mesma coisa internamente, ele apenas chama o método 
        # definido naquela classe específica, ignorando a hierarquia de herança.
        #
        # Portanto, embora funcione, o mais recomendável é utilizar super(), pois ele
        # segue a MRO (Method Resolution Order) e garante que a busca do método seja feita
        # de forma correta e dinâmica, especialmente em casos de herança múltipla.
        A.demonstrar(self)
 
d = D()
d.demonstrar()

########################################################################################

# c3 superclass linearization

# Em Python, assim como em algumas outras linguagens de programação, é possível utilizar o conceito
# de Herança Múltipla.
# Nos exemplos anteriores, quando criamos uma classe filha, passamos apenas uma classe entre parênteses,
# isso indica que essa classe é a superclasse (ou classe mãe).
# No entanto, também é possível adicionar duas, três ou mais classes entre parênteses, separadas
# por vírgulas. Quando isso ocorre, dizemos que estamos utilizando Herança Múltipla,
# pois a nova classe passará a herdar atributos de classe, métodos e construtores de
# todas as classes que foram declaradas na herança.
#
# Contudo, isso torna o MRO (Method Resolution Order) um pouco mais complexo, já que o Python
# precisará determinar a ordem exata em que as classes serão pesquisadas quando houver métodos
# ou atributos com o mesmo nome.
# Ainda assim, o MRO é inteligente o suficiente para resolver esses conflitos de forma consistente,
# o verdadeiro desafio está em manter o código compreensível e organizado à medida que a hierarquia cresce.
#
#  Além disso, hás casos que será utilizado mixin, que nada mais é que uma classe usada em herança múltipla
# para adicionar funcionalidades específicas a outras classes, sem fazer parte direta da hierarquia 
# principal dessas classes.
# Ela é pensada para ser combinada (mixada) com outras classes, e não para ser instanciada por conta própria.

# vou mostrar um exemplo de herança múltipla com mixin

# mixin
class logg:
    def log(self, msg): 
        print(f'[LOG]: {msg}')

# classe animal
class Animal:
    def __init__(self, especie):
        self.especie = especie

#Herança múltipla
class Ovelha(logg, Animal): # foram passadas as duas classes anteriores
    def __init__(self, nome, especie):
        self.nome = nome
        # e aqui, vou acessar a classe mãe que possui o parâmetro especie no init
        super(Ovelha, self).__init__(especie)
    
    # o emitir som será utilizado para o mixin
    def emitir_som(self):
        # e como eu herdei logg, o método log poderá ser utilizado aqui
        self.log('beermemee')

    #resultado: Utilizei funcionalidades de duas classes diferentes em apenas uma classe.

# aqui eu passo os argumentos
ovelha1 = Ovelha('Shaun', 'Ovis aries')
# e agora, poderei acessar normalmente cada método da classe Animal.
print(ovelha1.nome) # Shaun
print(ovelha1.especie) # Ovis aries
ovelha1.emitir_som() # [LOG]: beermemee
print(Ovelha.mro()) # [<class '__main__.Ovelha'>, <class '__main__.logg'>, <class '__main__.Animal'>, <class 'object'>]

# Observação:
# No mro acima, percebemos que após ele ter buscado na própria classe, ele buscou em logg, para depois
# buscar em animal e por fim, object builting. No entanto, nem sempre isso acontece... pode haver casos que por mais
# que determinada fosse passada primeiro, ela pode acabar não sendo a próxima a ser chamada no mro.
# 
# Isso acontece porque o python utiliza um algoritmo para saber qual classe deverá procurar depois, que
# é o C3 superclass Linearization. Esse algoritmo é o que o python utiliza atualmente, mas pode mudar.
# Nesse algoritmo, conforme a classe vai ficando complexa (com muitas heranças), mais difícil será prever
# o mro e poderá possibilitar o caso citado acima.
#
# Por isso existem o método .mro() e o atributo __mro__, que ajudam a inspecionar e debugar a
# estrutura de herança. Ainda assim, lembre-se: segundo a PEP 8 e o Zen do Python,
# "A complexidade é inimiga da clareza." 

### Problema Diamante
# Como dito anteriormente, em herança múltipla, uma classe pode herdar elementos de duas ou mais classes, correto?
# Dito isso, há um caso que possui um certo nível de complexidade, que é o caso do diamanate.
# Esse caso ocorre quando duas classes mãe tem uma outra classe mãe em comum na sua definição,
# possibilitando uma sobreposição errônea.
# Se não entendeu, com o exemplo abaixo, vai entender melhor.

# classe mãe
class um:  
    def quem_sou(self):
        print('um')

# classe dois herda de um
class dois(um):
    def quem_sou(self):
        print('dois')

# classe três herda de um.
#Logo, classe dois e classe três tem uma mãe em comum
class tres(um):
    def quem_sou(self):
        print('tres')

#classe quatro herda de classe dois e de classe três
class quatro(dois, tres):
    ...
    # def quem_sou(self):
        # print('quatro')

#logo, o exemplo visual ficaria da seguinte forma:

#           um
#         /    \
#       dois  tres
#         \    /
#         quatro

# percebeu que isso forma um diamante? e no caso de chamar um método que está
# presente em todas as quatro? o mro vai utilizar o seu algoritmo para cálcular isso.
# como ainda se trata uma complexidade relativamente simples, ainda poderemos deduzir.

# sendo: o mro vai buscar em quatro e vai encontrar. Mas, caso não encontrasse, iria buscar em dois
# já que dois está na frente. Se não achasse em dois, iria buscar em tres e se não encontrar em três,
# buscaria em um.

exam = quatro() 
exam.quem_sou() # dois

# e como sabemos, "um" é a mãe de dois e três, que parece que vão aparecer mais de uma vez no mro, né?
# mas não. Quando o mro faz a busca, antes ele faz a mesclagem e assim, evita duplicações. Veja na saída abaixo:
print(quatro.mro()) # [<class '__main__.quatro'>, <class '__main__.dois'>, <class '__main__.tres'>,
# <class '__main__.um'>, <class 'object'>]

# pair programing -> programação guiada
###############################################################################
# POO - Abstração.
## Abstração é o ato de focar no que o objeto faz, e não em como ele faz. 
# Nesse sentido, reduzimos a complexidade mostrando apenas o que é essencial para o uso.
# Toda a implementação detalhada fica oculta.
#
# Exemplo: você não precisa entender de motores para dirigir um carro. Ou seja,
# toda a complexidade foi abstraída, restando apenas o necessário para o uso.
#
# Em Python, isso também acontece com classes, onde podemos criar estruturas que
# definem o comportamento esperado (abstração), mas deixam a implementação para
# as classes filhas. Veja:

# Classe base (abstrata)
class Log:
    def log(self, msg): 
        # Esse método serve apenas como modelo para as subclasses.
        raise NotImplementedError('Você não deve usar essa classe diretamente. Use a classe filha.')
    
    # método de error que vai retornar o método log com o Erro
    def log_error(self, msg):
        return self.log(f'Error: {msg}')
    
    # método de suceso que vai retornar o método log com o sucesso
    def log_sucess(self, msg):
        return self.log(f'Sucess: {msg}')
    
# Classe concreta que implementa a abstração
class LogMixin(Log):
    def log(self, msg):
        print(msg)

# Agora, LogMixin implementa o comportamento definido em Log,
# escondendo a complexidade e exibindo apenas o necessário.
LogMixin().log('Sistema iniciado!')
LogMixin().log_error('Deu pau')
LogMixin().log_sucess('Deu tudo certo')

# mas caso você tente acessar log diretamente, perceba que vai dar erro:
try:
    Log().log('olaa')
except:
    print('Se isso for executado, então deu erro.')

#########
# Agora, vamos utilizar a classe que criamos para realizar o salvamento 
# de arquivos. Para isso, vamos precisar de uma nova classe, que será filha.

from pathlib import Path # importanto path para manipulação caminhos
from datetime import datetime # esse eu vou usar para adicionar o momento do log.
from zoneinfo import ZoneInfo # esse será para passar o timezone

# crio a classe e herdo a classe Log
class LogFileMixin(Log):
    # sobrescrevendo o método log
    def log(self, msg):
        # busca o caminho que o código foi executado e volta para trás uma vez
        caminho_atual = Path(__file__).parent
        # denomina um caminho para o arquivo de log
        arquivo_log = caminho_atual / 'aula228LogFileMixin.txt' 

        # passando o tz de SP
        tz_SP = ZoneInfo('America/Sao_Paulo')
        
        # buscando a hora atual com o tz e formatando
        agora = datetime.now(tz=tz_SP).strftime('%d/%m/%Y %H:%M:%S')

        # utiliza context maneger para escrita de em arquivos
        with open(arquivo_log, 'a') as f:
            f.write(f'{agora} -> {msg}')
            f.write('\n')

# Agora, quando eu indicar um log, ele vai salvar esse log no arquivo.
#
# Para erro:
LogFileMixin().log_error('Não gostei do nome da variável')

# para sucesso:
LogFileMixin().log_sucess('aí sim, nome maneiro!')

##########################
# A próxima aula será a aula 229 e estará dentro de uma pastinha,
# para maior organização.

##################################################
# Classe abstrata - Abstract Base Class (abc)
#
# Para definir uma classe abstrata, podemos usar algo assim:

'''
class Log:
    def log(self, msg): 
        # Esse método serve apenas como modelo para as subclasses.
        raise NotImplementedError('Você não deve usar essa classe diretamente. Use a classe filha.')
'''

# O exemplo acima é uma forma válida de criar uma classe abstrata devido a 
# chamada de um erro (raise) com a justificativa "NotImplementedError" (como foi falado antes).
# No entanto, há abordagens mais claras, coesas e padronizadas para isso.
# Uma delas é utilizando o módulo "abc" (Abstract Base Classes), que faz uso de uma metaclasse —
# um tipo especial de classe responsável por controlar a criação de outras classes.
# (O conceito de metaclasse será abordado mais adiante.)

# para chamar o módulo, basta fazer da seguinte forma:
from abc import ABC, abstractmethod

# Criamos uma classe abstrata herdando de abc
class LogAprimorado(ABC):
    # Herdar de abc apenas não significa que sua classe agora é abstrata.
    # Para tornar sua classe abstrata,é necessário que ela contenha,
    # pelo menos, um método com o decorador @abstractmethod.
    
    
    @abstractmethod #agora, essa classe se comportará como classe abstrata. 
    def exibir_na_tela(): ...

# Se tentarmos instaciar essa classe diretamente, o código quebra.
try:
    LogAprimorado().exibir_na_tela()
except TypeError:
   print('deu erro.')  # Can't instantiate abstract class LogAprimorado with abstract 
   # method exibir_na_tela

# Para utilizar essa classe, , é preciso criar uma classe filha que implemente o método 
# abstrato. Ex:

class LogDemonstrar(LogAprimorado):
    # e aqui, eu refaço o método.
    def exibir_na_tela(self, msg):
        print(f'msg: {msg}')

# agora eu conseguirei chamar a classe abstrata através de sua classe filha.
LogDemonstrar().exibir_na_tela('hello world')

#######################################################################################
# método abstrato -> método sem corpo, utilizado somente por classes filhas. 
# método concreto -> métodos com corpo, podendo ser utilizado em classes mães e filhas.

# Abstractmethod + Getter(property) e setter.
class Banco(ABC):
    def __init__(self, nome, saldo):
        # o atributo saldo estará protegido.
        self.nome = nome
        self._saldo = saldo

    # Para atribuir ou visualizar o valor de saldo quando está encapsulado fora da 
    # classe foi definido que será necessário utilizar um getter. Ou seja, um método
    # que acessa o atributo em questão. Em python, temos um meio mais simples para a
    # criação de um getter, que é uma property (método que se comporta como atributo).
    #
    # Relembrado isso, a property nada mais é que um decorator. Assim como o abstractmethod.
    # Para utilizar uma propery em paralelo com abstractmethod é muito simples, basta colocar
    # um acima do outro na criação do método, de forma hierárquica, ou seja, do mais relevante
    # ao menos relevante de baixo para cima. Nesse caso, como queremos tornar um método
    # abstrato, o mais relevante seria o abstractmethod. Logo, faremos da seguinte forma:
    
    @property
    @abstractmethod
    def saldo(self): ...

    # Como o método acima vai ser sobreposto quando eu chamar uma classe filha, não precisarei
    # do setter.

    #####
    # No caso do classmethod também. O mais relevante seria o abstractmethod.
    @classmethod
    @abstractmethod
    def tratamento_nome(cls, nome_completo, saldo): ...


class BancoDoBrasil(Banco):
    # Aqui será necessário chamar a classe abstrata da superclass e definir seu corpo.
    @property
    def saldo(self):
        return self._saldo
    
    # agora sim, inserir o setter.
    @saldo.setter
    def saldo(self, valor):
        print('o saldo foi alterado')
        self._saldo = valor

    # e alteramos o classmethod
    @classmethod
    def tratamento_nome(cls, nome_completo, saldo):
        init_treatment = nome_completo.split(' ')[0]
        return cls(init_treatment, saldo)

# instanciar os objetos.
p1 = BancoDoBrasil('João', 50)
p2 = BancoDoBrasil.tratamento_nome('Carla Silva Dantas', 25)

# atribuição no objeto p1
print(p1.nome)
print(p1.saldo)
p1.saldo = 60
print(p1.saldo)

# atribuição no objeto p2
print(p2.nome)
print(p2.saldo)
p2.saldo = 60
print(p2.saldo)

#######################################
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura academicamente) + princípios
# que contam. Sendo: Assinatura do método: nome, parâmetros e retorno iguais
#
# Princípios que contam:
#
# S - Single Responsibility Principle (Princípio da Responsabilidade Única)
# O - Open Closed Principle (Princípio Aberto/Fechado)
# L - Liskov Substitution Principle (Princípio da Substituição de Liskov)
# I - Interface Segregation Principle (Princípio da Segregação de Interface)
# D - Dependency Inversion Principle (Princípio da Inversão de Dependência)

# Liskov Substitution Principle (Princípio da Substituição de Liskov): Objetos
# de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.

"""
Depois trazer um exemplo
"""