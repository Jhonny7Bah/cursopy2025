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

