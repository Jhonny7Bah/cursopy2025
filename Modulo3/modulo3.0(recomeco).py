#####################
def cls() -> None:
    # importando os módulos necessários
    from os import system
    import platform

    # realiza a busca do nome do sistema
    sistema_usuario = platform.system().lower()

    if sistema_usuario == 'windows': 
        system('cls')
        
    elif sistema_usuario == 'linux':
       # busca a distro do usuário
        try:
            dados_linux = platform.freedesktop_os_release()
            distro_id = dados_linux.get('ID', '') # Retorna 'arch', 'ubuntu'
            nome_bonito = dados_linux.get('PRETTY_NAME', 'Linux')
            
            print(f"Limpando terminal do: {nome_bonito}")
            
            # Verifica usando a ID
            if distro_id == 'arch': 
                system('reset')
            else: 
                system('clear')
                
        except AttributeError:
            # apenas gatantia
            system('clear')
            
    else:
        print('Não consegui limpar seu terminal')

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
# Nesse sentido, reduzimos a complexidade mostrando apenas o que é essencial 
# para o uso. Toda a implementação detalhada fica oculta.
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
        raise NotImplementedError(
        'Você não deve usar essa classe diretamente. Use a classe filha.'
        )
'''

# O exemplo acima é uma forma válida de criar uma classe abstrata devido a 
# chamada de um erro (raise) com a justificativa "NotImplementedError"
# (como foi falado antes).
# No entanto, há abordagens mais claras, coesas e padronizadas para isso.
# Uma delas é utilizando o módulo "abc" (Abstract Base Classes), que faz uso
# de uma metaclasse, que é um tipo especial de classe responsável por controlar
# a criação de outras classes (metaclasses serão abordadas mais adiante).

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
   print('deu erro.')  # Can't instantiate abstract class LogAprimorado with
                       # abstract method exibir_na_tela
# Para utilizar essa classe, é preciso criar uma classe filha que reescreva
# o método abstrato. Ex:

class LogDemonstrar(LogAprimorado):
    # e aqui, eu refaço o método.
    def exibir_na_tela(self, msg):
        print(f'msg: {msg}')

# agora eu conseguirei chamar a classe abstrata através de sua classe filha.
LogDemonstrar().exibir_na_tela('hello world')

# @___
# método abstrato -> método sem corpo, utilizado somente por classes filhas. 
# método concreto -> métodos com corpo, podendo ser utilizado em classes mães
# e filhas.

# Abstractmethod + Getter(property) e setter.
class Banco(ABC):
    def __init__(self, nome, saldo):
        # o atributo saldo estará protegido.
        self.nome = nome
        self._saldo = saldo

    # Para atribuir ou visualizar o valor de saldo quando está encapsulado 
    # fora da classe foi definido que será necessário utilizar um getter.
    # Ou seja, um método que acessa o atributo em questão. Em python, temos 
    # um meio mais simples para a criação de um getter, que é uma property
    # (método que se comporta como atributo).
    #
    # Relembrado isso, a property nada mais é que um decorator. Assim como o
    # abstractmethod. Para utilizar uma propery em paralelo com abstractmethod
    # é muito simples, basta colocar um acima do outro na criação do método,
    # de forma hierárquica, ou seja, do mais relevante ao menos relevante de
    # baixo para cima. Nesse caso, como queremos tornar um método  abstrato,
    # o mais relevante seria o abstractmethod. Logo, faremos da seguinte forma:
    
    @property
    @abstractmethod
    def saldo(self): ...

    # Como o método acima vai ser sobreposto quando eu chamar uma classe filha,
    # não precisarei do setter.

    #####
    # No caso do classmethod também. O mais relevante seria o abstractmethod.
    @classmethod
    @abstractmethod
    def tratamento_nome(cls, nome_completo, saldo): ...


class BancoDoBrasil(Banco):
    # Aqui será necessário chamar a classe abstrata da superclass e definir
    # seu corpo.
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

# override = sobreposição de métodos

###############################################################################
# Polimorfismo, type hints e princípios
#
# Polimorfismo, é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade de 
# parâmetros (retorno não faz parte da assinatura academicamente) + princípios
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
# por objetos de uma subclasse sem quebrar a aplicação. (Onde você usar uma
# superclasse, uma subclasse deve conseguir substituir sem quebrar a aplicação).

from abc import ABC, abstractmethod

# Notificação é algo aobstrato, pois pode ser notificação de sms, wpp,
# e-mail, etc. 
class Notificacao(ABC):
    # Em python, há algo que chamamos de type hints, que seria determinar
    # o tipo ou retorno de um método. Logo, podemos utilizar esse princípio
    # para indicar o retorno de um método ou o tipo de dado que algum parâmetro
    # irá receber. Por padrão, o init retorna None, mas para demonstração,
    # iremos fazer isso manualmente.  
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem
        # Obs: Isso não siginifica que se essa função retornar algo diferente
        # de None o código vai quebrar. Em python, funcionaria normalmente até
        # que um código que precise dela e trate ela como 
        # None (pois era o esperado) para talvez quebrar. 

    # enviar será um método abstrato, mas vamos definir que seu retorno será bool.
    @abstractmethod
    def enviar(self) -> bool: ...

# subclasse de notificação 1
class NotificacaoEmail(Notificacao):
    # Outra vantagem do Type Hints é que quando definimos o tipo de um 
    # parâmetro ou retorno em uma função ou método, o interpretador e as
    # ferramentas de desenvolvimento conseguem mostrar automaticamente como
    # essa função deve ser usada. Ou seja, ao chamar o método em outra parte
    # do código, o editor exibe a assinatura da função, com os tipos esperados
    # e o que ela retorna, facilitando o entendimento e reduzindo erros no uso.
    
    def enviar(self) -> bool:
        print(f'E-mail: enviando - {self.mensagem}')
        return True

# subclasse de notificação 2
class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print(f'SMS: enviando - {self.mensagem}')
        return False

# No caso acima, notificação é a superclass, enquanto notificaçãoEmail e
# NotificacaoSMS são subclass. Se você analisar bem, é perceptível que a
# assinatura do método e o retorno são iguais para as subclass, divergendo
# apenas o conteúdo no corpo (leve polimofirsmo). Nesse caso,
# o Liskov Substitution Principle está sendo cumprido, pois se eu chamar a 
# classe filha um, passando os alguns argumentos no init e depois chamar a 
# filha dois e passar o mesmo argumento, o código não vai quebrar. Exemplo:

NotificacaoEmail('Opaaa').enviar() # E-mail: enviando - Opaaa
NotificacaoSMS('Opaaa').enviar() #SMS: enviando - Opaaa

# Por mais que o conteúdo retornado (polimofirmo) tenha sido diferente, 
# os filhos de uma superclasse não quebrou quando eu passei os mesmos
# argumentos. 
# Ademais, o retorno também cumpriu seu objeto, retornando true||false.

# E no caso do Polimorfismo, as classes acimas são derivadas de uma superclass,
# considerando que manteram as mesmas 
# assinaturas (principalmente por conta do princípio), os métodos e por fim,
# tiveram objetivos diferentes em seu corpo, que nesse caso, foi no escopo
# do método enviar. 

###
# Para deixar o conceito de polimorfismo mais claro,
# vamos criar uma função que recebe qualquer objeto do tipo 
# Notificacao (ou suas subclasses).

# Usando type hints, indicamos que o parâmetro 'msg' deve ser uma instância de
# 'Notificacao'.
# Isso permite que o editor reconheça automaticamente os métodos e atributos
# disponíveis dentro do escopo da função.
def notificacao(msg: Notificacao) -> None:
    # Como 'msg' é do tipo Notificacao (ou uma subclasse dela),
    # podemos chamar o método 'enviar' normalmente.
    notificacao_enviada = msg.enviar()

    # Aqui validamos o retorno booleano do método 'enviar'.
    if notificacao_enviada:
        print('notificação enviada')
    else:
        print('notificação não enviada')
# Ao chamar a função 'notificacao' passando subclasses 
# diferentes (Email ou SMS),o código continua funcionando sem erros.
# Isso demonstra claramente:
# - Polimorfismo → as subclasses têm o mesmo método, mas comportamentos
#   diferentes.
# - Liskov Substitution Principle (LSP) → as subclasses podem substituir a
#   superclasse sem quebrar o funcionamento da aplicação.

notificacao(NotificacaoEmail('teste email')) # notificação enviada
notificacao(NotificacaoSMS('teste sms')) # notificação não enviada

###########################################################################
# Criando excessões em python orientado a objetos
# https://docs.python.org/3/library/exceptions.html
# Para criar uma excessão, basta você criar uma classe e herdar alguma
# excessão da linguagem. Em python, é recomendado que você herde de 
# Exception, pois esse é específico para erros e por convenção, quando
# você herda de exception, a classe deverá ter "Error" no segundo nome. Ex:
class DivisaoPorDoisError(Exception):
    # A partir de agora você já tem uma excessão criada, sendo apenas
    # necessário chamar esse erro quando vir o caso.
    ...

# Vou fazer outro erro para usar depois.
class ComplementoDivisaoError(Exception):...

# Vou criar uma função que realizará uma divisão.
def divisao(numero: int):
    if numero is 2: # 'is' faz a mesma comparação que '=='. Por algum motivo,
                    # '==' tá bugado.
        raise DivisaoPorDoisError('Você não deve dividir por dois')
    return 10 / numero

# vou chamar a função e pôr um número qualquer diferente de dois
print(divisao(divisao(5)))
# mas se eu coloco 2, vai lançar uma exessão e por isso, irei tratar.
try:
    print(divisao(2))
# para demonstrar com mais clareza, a excessão vai tratar dois erros, sendo o
#  meu (DivisaoPorDoisError) e ZeroDivisionError. 
except (ZeroDivisionError, DivisaoPorDoisError) as error:
    # Se quisermos descobrir qual foi a exceção capturada,
    # basta acessar a classe associada ao erro e, em seguida, seu nome:
    print(error.__class__.__name__)  # DivisaoPorDoisError

    # Podemos também ver a mensagem descritiva da exceção:
    print(error)  # Você não deve dividir por dois

    # Agora imagine que o objetivo deste bloco 'except' seja apenas
    # registrar informações do erro (ex: logar, exibir detalhes, etc.)
    # antes de deixá-lo continuar a se propagar, ou seja, permitir
    # que o programa quebre normalmente após o registro.
    #
    # Nesse caso, usamos 'raise' novamente para relançar a exceção.
    # Isso faz com que o erro original suba para o próximo nível da pilha.
    #
    # Exemplo:
    # raise  # Relança a exceção capturada
    #
    # (resultado: DivisaoPorDoisError: Você não deve dividir por dois)

    # Mas, se quisermos evitar que o programa seja interrompido,
    # podemos capturar novamente o erro dentro de outro try/except:
    try:
        raise  # Relança a exceção
    except DivisaoPorDoisError as error2:
        print(error2)
    
    # Também é possível complementar uma exceção com outra,
    # mostrando que um erro foi causado por outro erro anterior.
    #
    # Para isso, usamos o formato:  raise ErroPrincipal from ErroCausa
    erro1_divisao = DivisaoPorDoisError('Você não pode dividir por dois!')
    outro_error = ComplementoDivisaoError('Você realmente não pode dividir por dois.')

    # chamadando o erro (basta tirar o comentário que irá funcionar)
    
    # raise erro1_divisao from outro_error

    # Caso você tire o comentário e depois execute o código, o seguinte erro
    #  vai aparecer:

    '''
    __main__.ComplementoDivisaoError: Você realmente não pode dividir por dois.

    The above exception was the direct cause of the following exception:
    (tradução: A excessão acima foi uma causa direta da excessão abaixo:)

    Traceback (most recent call last):
    File "/home/umcex/Documentos/Cursos/cursopy/Modulo3/modulo3.0(recomeco).py", line 1625, in <module>
        raise erro1_divisao from outro_error
    __main__.DivisaoPorDoisError: Você não pode dividir por dois!

    '''

    # Portanto, você agora acaba complementar (encadear) um erro com outro.
    
# Além disso, para criação de erros, temos também as notas, que podem ser
# utilizadas para passar algumas dicas para os desenvolvedores que utilizam
# da sua classe, ou coisa do tipo. 

meu_erro_novamente = DivisaoPorDoisError('você não pode dividir por dois amigo')

# E para adicionar uma nota, basta chamar o método add_note, após instanciar sua 
# classe de erro. Considerando que esse método não aceita argumentos nomeados. 
meu_erro_novamente.add_note('Pare de tentar dividir por dois, tente por três')
meu_erro_novamente.add_note('Cara, sabia que você pode tentar dividir por quatro?' \
' seria mais interessante')

# caso você queira ver as notas somente, basta chamar o atributo __notes__ 

print(meu_erro_novamente.__notes__) # ['Pare de tentar dividir por dois, tente por três', 'Cara, sabia que você pode tentar dividir por quatro? seria mais interessante']

cls()
# E para ver isso no traceback:
try:
    # raise meu_erro_novamente # para ver na pratica, basta tirar isso como um
    # comentário.
    ...
except ComplementoDivisaoError as error:
    print(error)
    '''
    Traceback (most recent call last):
    File "/home/umcex/Documentos/Cursos/cursopy/Modulo3/modulo3.0(recomeco).py", line 1665, in <module>
        raise meu_erro_novamente
    DivisaoPorDoisError: você não pode dividir por dois amigo
    Pare de tentar dividir por dois, tente por três
    Cara, sabia que você pode tentar dividir por quatro? seria mais interessante

    '''

    # E após o raise, vemos as notas.

###########################################################

# Quando criamos uma classe e instanciamos um objeto, ao imprimir esse objeto
# o Python mostra uma representação padrão, herdada de `object`, que inclui o
# módulo, a classe
# e o endereço de memória. Ex:

class Ponto:
    def __init__(self, x, y, z='string'):
        self.x = x
        self.y = y
        self.z = z
p1 = Ponto(10,20)

print(p1) # <__main__.Ponto object at 0x749bfda72660>

# Como eu disse, será possível ver apenas a posição da memória.
# E se quiséssemos trocar essa informação por algo mais amigável? temos alguns
# dunder methods/Magic methods que podemos utilizar para isso.

# __repr__ -> representation - # Representação oficial do objeto. Deve ser o 
# mais precisa possível e mostrar informações relevantes do estado da 
# instância. É a melhor opção para debugging.

# __str__ -> string - apenas um simples texto de mudança para diferenciar o 
# texto padrão, que é a informação do edereço de memória. 

# Detalhe -> str tem mais prioridade que o repr, ou seja, se ambos existirem
# na classe e forem chamadas por uma print, quem vai aparecer é o str.

# forma de uso:

class Ponto:
    def __init__(self, x, y, z='string'):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        nome_classe = type(self) 
        # nome_classe = __class__.__name__ # assim você também pega o nome da
                                           # classe, mas em caso de herança ou 
                                           # mixin, pode ser falho.
        # esse método deverá retornar uma string, sendo que ela deve ser o 
        # mais completa possível
        return f'{nome_classe}(x={self.x}, y={self.y}, z={self.z})'

    # caso queira ver o repr, comente a linha abaixo.
    # (str tem mais prioridade que repr)
    
    # def __str__(self):
    #     return 'opaaaa'

p2 = Ponto(10,20)

print(p2) # <class '__main__.Ponto'>(x=50, y=60, z='string') || 'opaaaa'

# Mas, percebe que no caso rep, a string fica parecendo um objeto? isso pode
# causar confusão e para resolver isso, poderíamos colocar o parâmetro "z"
# entre parênteses. No entanto, há um jeito muito mais fácil de resolver isso, 
# sendo através da formatação rep. Vou demonstrar abaixo.

class Ponto:
    def __init__(self, x, y, z='string'):
        self.x = x
        self.y = y
        self.z = z

    # para indicar a formatação rep, utilizamos (!r). Assim, o python saberá
    # lidar com strings e não criará uma confusão na hora de demonstrar o rep.
    def __repr__(self):
        nome_classe = type(self) 
        return f'{nome_classe}(x={self.x!r}, y={self.y!r}, z={self.z!r})' # retorno: <class '__main__.Ponto'>(x=50, y=60, z='string')
        return f'{nome_classe}(x={self.x}, y={self.y}, z={self.z})' # retorno: <class '__main__.Ponto'>(x=50, y=60, z=string)
        # utilizei dois retornos distintos para demonstrar como iria retornar
        # com e sem formatação. no primeiro retorno, string retorna em aspas,
        #  como se realmente fosse uma string.
        #
        # No segundo retorno também é uma string, mas seria fácil de confundir
        # com qualquer tipo de dado, pois não tem aspas especificando que é
        # uma string.

    # para formatar a string, podemos utilizar
    def __str__(self):
        return f'{self.z!s}'
################

p3 = Ponto(50,60)
print(p3)  # <class '__main__.Ponto'>(x=50, y=60, z='string') || 'string'

# caso você tenha definido string e rep em uma classe, saberá que str tem mais
# preferência que rep. Mas, e se fosse necessário ver o rep de alguma forma?
# temos as seguintes formas:

#através da função rep.
print(repr(p3)) # <class '__main__.Ponto'>(x=50, y=60, z='string')

# através da formatação rep.
print(f'{p3!r}') # <class '__main__.Ponto'>(x=50, y=60, z='string')

###############################################################################
# Exemplo de uso de dunder methods (métodos mágicos)
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

# métodos magicos são funções especiais definidas dentro de classes que
# permitem que objetos interajam com operações built-in do Python. Por exemplo,
# __add__ é um método mágico que é habilitado quando é utilizado o operador de 
# soma (+) em alguma parte do codigo, como 2 + 2. Quando os valores são inicializados
# através de uma classe, o desenvolvedor pode alterar o comportamento desses métodos.

# No exemplo abaixo, vou criar uma classe e alterar o comportamento do add.
class Teste:
    # Aqui irei inicializar os atributos por questão de organizacao
    def __init__(self, n1):
        self.num = n1
    
    # Dentro da classe, chamo o add
    # Atente-se que nesse caso, serão passados 2 valores, onde o primeiro parâmetro será self e 
    # o segundo será other (é o padrão chamar o segundo parâmetro assim em python),
    def __add__(self, other):
        # agora, vou apresentar os dois valores
        print(self.num) # esse apresentará o primeiro valor, aproveitando o atributo no init.
        print(other.num) # esse será o segundo.

        # como percebeu, o other se comporta como um segundo self para o segundo valor.

        # agora, vou retornar um texto qualquer somente para demonstrar.
        return "eu sou um mágico!"

# para funcioanar corretamente, precisamos instanciar dois valores na classe anterior.
# Se os operadores não tiverem o método mágico correspondente, o Python não cai em uma
# soma built-in genérica
valor1 = Teste(10)
valor2 = Teste(2)

# agora, irei realizar uma soma com os dois valores.
print(valor1 + valor2) # imprime:
# 10
# 2
# eu sou um mágico!


# Como pode ver, o comportamento da soma alterou completamente. 
# Esse é o poder de um método mágico!

# é importante deixar claro que quando é feita uma alteração como a anterior, 
# a depender do que tenha sido feito, algumas operações podem não funcioanar 
# corretamente como esperado. No caso acima, foi incremetado ações extras 
# como imprimir na tela e retornar uma string. Portanto, certamente o código
# irá quebrar na chamada de uma operação qualquer. 
try:
    print(valor1 > valor2)
except TypeError as e:
    print(e) # '>' not supported between instances of 'Teste' and 'Teste'

# Uma informação muito importante que tem que ficar clara é que quando 
# uma método mágico for definido, em sua assinatura, deverá haver somente 
# dois parâmetros: self e other. Self sempre irá ficar do lado esquerdo e 
# portanto, será o primeiro valor. Other sempre ficará do lado direito e será
# sempre o segundo valor. Logo, se é feito: a + b, então a será correspondente
# a self enquanto b será correspondente a other. 

####################################

# Resumo da aula
# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe

# init apenas executa inicialmente na classe porque new o chama. Ou seja,
# o new executa antes do init.

class DemonsInitENew:
    # como parâmetro para o new não seria self e sim cls.
    def __new__(cls):
        print("eu sou o new")

    def __init__(self):
        print("eu sou o init")

demons_init = DemonsInitENew() # console: eu sou o new 
# o new executou primeiro e o init nem chegou a executar, correto?
# como foi dito antes, o new é o primeiro a executar e por padrão,
# após sua execução, ele chama o init. Porém, no caso acima não fora feito isso.
#
# Mas irei refatorar o new para chamar o init. 
# No caso abaixo, mostrarei uma das formas do new chamar o init.
print(object.__new__(DemonsInitENew).__init__()) # console: eu sou o init

# detalhe: se new não tivesse valor algum, então por padrão, irá retornar None.

# Ademais, somente em casos muito espeficos que irá necessitar fazer o uso do New.
# Pois, basicamente, você somente irá precisar do new se quiser executar algo antes
# do init no código... caso contrário, não fará tanto sentido você fazer isso. Vou 
# deixar um exemplo de caso para querer executar o new antes:

class DemonsInitENew:
    def __new__(cls):
        print("chamando alguma importacao muito necessaria antes do init")
        print("finalizando logica da importacao ou sabe-se la oq antes do init")
        # o retorno deverá ser a chamada do init. Nesse caso, irei armazenar em uma variavel
        # como tudo isso se trata de uma hierarquia de classes, posso muito bem chamar o super
        # para chamar o init. No entanto, também posso chamar o init de outras formas, como por
        # exemplo, chamar diretamente pelo nome da classe object.__new__(DemonsInitENew). 
        # mas por que é chamado uma classe acima da atual? porque, como foi dito na aula de mro,
        # object é uma classe padrão do python que é está presente em todas as classes desde o momento
        # de criação. Portanto, quando eu chamo object diretamente, eu to chamando uma classe acima e através dela,
        # posso chamar o init. Logo, como apenas precisamos chamar uma classe acima, faz mais sentido usar super.
        chamada_init = super().__new__(cls)
        print()
        return chamada_init

        # detalhe: como aqui tem uma variavel para o init, é possível também criar atributos para o init aqui no new.
        # porém, iria necessitar colocar os parametros de init semelhante ao de new. ex:
        # def __new__(cls, algo)
        # def __init__(self, algo)
        #
        # ou pode usar argumentos nomeados e nao nomeados para executar.


    def __init__(self):
        print("eu sou o init")

demons_init = DemonsInitENew() # retorno:
# chamando alguma importacao muito necessaria antes do init
# finalizando logica da importacao ou sabe-se la oq antes do init
# 
# eu sou o init

#############################################
# 
# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Explicação do professor
# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
#
# Ou seja, para que o context manager funcine, será necessário haver dois métodos
# na classe, sendo o __enter__ para entrada (caminha como um pato) e o __exit__ (
# nada como um pato), tornand-o assim válido para tal uso, transformando-o completamente
# em um pato, no sentido figurado. Vejamos na prática:
#
#
with open('revisao.py', 'r'):
    ...
# vamos tentar recriar posteriormente uma classe que se assemelhe ao papel do open. 
# lembrando que o with funciona sempre com objetos que precisam abrir e fechar.

class MeuExemploParaWith:
    def __enter__(self):
        print("entrando")

    # para o exit será necessário definir parametros de saida para caso ocorra algum transtorno 
    # durante a execucao, o usuario ter a opcao de tratar através da propria classe.
    def __exit__(self, class_exception, exception, traceback):
        print("saindo")

# a classe acima está realmente completa para ser utilizada através do context maneger.
with MeuExemploParaWith():
    # assim que essa linha for executada, o conteudo contido em enter e exit será executado 
    # respectivamente.
    # retorno:

    # entrando
    # saindo
    ...

# assim, consigo fazer o meu proprio gerenciador de contexto. Seja ele para conexão, abertura de arquivos, etc.
# no caso abaixo, vou demonstrar a criação de contexto para abertura de arquivos:

class AbrirArquivo:
    # na classe, por mais que não seja chamada diretamente, o init é sempre um dos primeiros
    # a executar, principalmente quando comparado ao método enter
    def __init__(self, caminho, metodo_abertura):
        # o open tem dois parâmetros padrão, sendo um o caminho e o segundo o método de abertura.
        self.caminho = caminho
        self.metodo_abertura = metodo_abertura
        self.arquivo = None # esse atributo será útil e necessário para salvar o estado do arquivo desejado.
    
    def __enter__(self):
        # o open é não faz parte do gerenciador de contexto. Ele apenas um método
        # para controle e gerenciamento de arquivos, servindo para leitura, criação
        # e escrita.
        self.arquivo = open(self.caminho, self.metodo_abertura) # aqui eu salvo o estado do gerenciador, passando os
        #parametros necessarios.
        #
        # O valor retornado por __enter__ é atribuído à variável após o 'as'
        # no bloco with. Ao retornar o arquivo, exponho o recurso para que
        # o usuário possa manipulá-lo livremente dentro do contexto.
        return self.arquivo
        
    def __exit__(self, class_exception, exception, traceback):
        self.arquivo.close()

cls()
with AbrirArquivo('revisao.py', 'r') as arquivo:
    # gracas ao retorno do __enter__ retornando o objeto self.arquivo apos ser
    # inicializando com os argumentos para gerenciamento, é possível manipular
    # o arquivo em questão aqui. Por exemplo:
    # print(arquivo.read()) # conteudo do resumo.
    ...

#################################
# Este é um exemplo de gerenciador de contexto implementado via classe.
# A classe base (AbrirArquivo) é responsável por abrir e fechar o arquivo,
# enquanto esta classe herda seu comportamento para demonstrar o uso do
# método __exit__ no tratamento de exceções.
#
# no método exit da funcao acima, há três parametros extras. Por padrão, se nada ocorrer no código,
# os três parâmetros recebidos (class_exception, exception e traceback) serão None
class AbrirArquivo2(AbrirArquivo):
    def __exit__(self, class_exception, exception, traceback):

        # vou receber um erro para demonstração 
        print(class_exception, "\n") # retorna a classe do erro (TypeError) 
        print(exception, "\n") # retorna o conteudo do erro ('erro teste')
        print(traceback, "\n") # retorna o traceback associado ao erro

        # garante o fechamento do recurso reutilizando a lógica da classe pai
        super().__exit__(class_exception, exception, traceback)
        
        # retornar True suprime a exceção ocorrida dentro do bloco with. Portanto,
        # se algum erro lá dentro ocorrer, o método __exit__ será chamado e, como
        #  retorna True, o erro não interrompe a execução do programa.
        return True

# isso vai gerar um transtorno no codigo, pois esse ola não existe.
with AbrirArquivo2('revisao.py', 'r') as d:
    raise TypeError('erro teste') # o codigo continua funcionando normalmente.

print('oi') # oi

cls()
##########################################
# Há outra forma de criar um gerenciador de contexto, que é através de um decorator oriundo da 
# biblioteca padrão contextlib, importando o context manager. Exemplo:
from contextlib import contextmanager

# vou criar um exemplo novamente para arquivo.
# portanto, será necessário separar uma função para abrir e fechar o arquivo,
# que deverá iniciar com o decorator @contextmanager.

@contextmanager
def abrir_outro_arquivo(caminho, modo):
    ''' nessa lógica, o tratamento de exceção precisa ser feito manualmente
    com recursos do python, como o try/except/finally.
    como é possível fazer uso do finallly, é possível garantir o fechamento do arquivo
    mesmo que ocorra um erro. Portanto, para esse caso não será necessário o uso do
    bloco except. Porém, mesmo assim, irei utilizar o except para demonstração.
    '''
    
    try:
        print('abrindo o arquivo')
        # aqui, abro o arquivo e salvo o estado.
        arquivo = open(caminho, modo)
        # agora, para disponibilizar o recurso para o usuário,
        # uso o yield, que funciona como um return, porém,
        # diferente, pois após o yield, o código continua
        # executando normalmente. Logo, essa função se tornará
        # um generator e o decotaror lidará com isso como se o yield
        # fosse um return dentro de um __enter__.
        yield arquivo

    # não é obrigatório tratar o erro aqui, mas irei colocar um para demonstração.        
    except Exception as e:
        print(f'Ocorreu erro: {e}')

    # obrigatoriamente, para garantir o fechamento do arquivo
    finally:
        print('fechando o arquivo')
        arquivo.close()

# agora, para usar o gerenciador de contexto, basta fazer da seguinte forma:
with abrir_outro_arquivo('revisao.py', 'r') as a:
    # aqui, posso manipular o arquivo normalmente e 
    # quando o bloco with finalizar, o arquivo será fechado
    print(a.read())

#############################################
# Funções decoradoras e decoradores com classes
#
'''
Considere que você tem duas classes que tem um método em comum, com a mesma assinatura,
mesmo comportamento, etc. Para não repetir código, você herdou esse método de uma superclasse
mixin, ex:
'''

# exemplo de mixin
class AlgoMixin:
    def __str__(self):
        # retornando uma string qualquer
        return 'eu sou um método comum'

# classes que herdam o mixin
class ClasseA(AlgoMixin):
    ...
class ClasseB(AlgoMixin):
    ...

# agora, tanto a classe A quanto a B possuem o método_comum herdado do mixin.
a = ClasseA()
b = ClasseB()

print(a) # eu sou um método comum
print(b) # eu sou um método comum

# porém, é sempre recomendado o uso de composições ao invés de heranças sempre que possível.
# Logo, uma forma de evitar a herança, seria através de uma função. Ex:

def metodo_comum(cls):
    # aqui, eu defino o método comum
    cls.__str__ = 'eu sou um método comum'
    return cls

# agora, para usar esse método comum em outras classes, basta chamar a função na classe. ex:

class ClasseC:
    ...

# como a função retorna atualmente
print(ClasseC.__str__) # <slot wrapper '__str__' of 'object' objects>

# para usar o método comum, basta fazer o seguinte:
ClasseC = metodo_comum(ClasseC)
print(ClasseC.__str__) # eu sou um método comum

# porém, há uma forma mais elegante de fazer isso, que é através de um decorador. Ex:
def metodo_comum_decorador(cls):
    cls.__str__ = 'eu sou um método comum'
    return cls

@metodo_comum_decorador
class ClasseD:
    ...

# agora, para usar o método comum, basta fazer o seguinte:
print(ClasseD.__str__) # eu sou um método comum

cls()
############## 
# também é possível criar decoradores seguindo a mesma lógica para métodos 
# de uma classe. 

# para isso, vamos aplicar o closure, que é uma função que não executa de imediato,
# havendo uma função externa (para controle) e uma interna (para execução de uma lógica)
# extra.

# no método, quando utilizarmos o decorator no método, o método em si entra como argumento
# para o parametro "metodo" da funcao "meu_planeta" abaixo.
def meu_planeta(metodo):
    # toda os argumentos que o método recebeu dentro da classe
    # serão preservados pelos argumentos nomeados e não nomeados.
    def interna (self, *args, **kwargs):
        # o resultado é a execução do método em seu estado original.
        # portanto, se eu retornasse "resultado" de uma vez, nada mudaria.
        resultado = metodo(self, *args, **kwargs)

        # porém, o que estamos fazendo é decorar um método de uma forma muito semelhante
        # a decorar uma funcao em python. Portanto, posso retornar o resultado depois
        # que fizer a minha modificacao, ou então, posso escolher não retornar.

        # como aquele método é responsável apenas por informar o nome do planeta que fora
        # passado pelo usuário, consigo fazer uma lógica com seu resultado e retornar algo
        # oompletamente diferente do esperado.

        # por exemplo, será verificado se é planeta terra. Se sim, então será avisado que 
        # o usuário está em seu planeta natal, caso contrário, lhe será informado que ele
        # está em um planeta estrangeiro.

        # verifica se é o planeta natal do usuario.
        if str(resultado).strip().lower() == 'terra':
            return 'voce está em seu planeta natal!'
        return f'voce não está em seu planeta natal. voce está em: {resultado}'
    
    # chama a funcao interna
    return interna

# criacao convencional de uma classe.
class Planeta:
    def __init__(self, nome):
        self._nome = nome
    
    # chamando decotador
    @meu_planeta # se voce quiser, comente essa linha e vai perceber que o metodo vai funcionar como de costume.    
    def exibir_planeta(self):
        # retorando apenas o nome do planeta.
        return self._nome

terra = Planeta('terra')
marte = Planeta('marte')

print(terra.exibir_planeta()) # 'voce está em seu planeta natal!'
print(marte.exibir_planeta()) # 'voce não está em seu planeta natal. voce está em: marte'

###########

# método especial callable.
# callable é algo que pode ser executado através de parenteses, podendo ser um
# método, funcao, classe, dentre outras coisas.
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
# isso quer dizer que se voce instanciar uma classe e por algum motivo chamar ela
# com parenteses, ela não irá quebrar, contanto que seja passado os parametros solicitados.

# para demonstrar isso, vou criar uma instancia para uma das classes anteriores e 
# tentar executar.

urano = Planeta('urano')

# como sei que vai quebrar, vou chamar isso dentro de um try.
try:
    urano()
except Exception as e:
    print('ocorreu o erro: ',e) # ocorreu o erro:  'Planeta' object is not callable

# como viu, o tentei executar a instancia, mas pelo fato dela não ser callable, 
# o código quebrou. Porém, se eu realmente quisesse que essa classe permitisse
# executar algo da instancia, como foi demonstrado anteriormente, seria necessário
# implementar o método __call__ na classe, como no exemplo abaixo: 

class CallMe:
    def __init__(self, numero):
        self.numero = numero
    
    # se for do desejo do programador, pode deixar os parametros de forma indefinida 
    # através de empacotamento.
    def __call__(self, *args, **kwargs):
        print(f'o número {self.numero} tentou me chamar?')

n1 = CallMe('7444')
# agora, irei tentar executar n1.
n1() # o número 7444 tentou me chamar?

cls()
#######################
# Decoradores com classes
# Decoradores são uma forma elegante de modificar o comportamento de funções ou métodos
# sem alterar seu código-fonte. Eles são amplamente utilizados para adicionar funcionalidades
# de forma reutilizável. Em Python, os decoradores podem ser implementados usando funções
# ou classes. Quando usamos uma classe como decorador, ela deve implementar o método __call__,
# tornando a instância da classe "callable". Isso permite que a classe seja usada como um decorador
# para funções ou métodos, modificando seu comportamento de maneira flexível e poderosa.

class DecoratorSum:
    # o init recebe a função que será decorada como argumento e a armazena em um atributo da
    #  classe.
    def __init__(self, func):
        self.func = func

    # o método __call__ é responsável por executar a função decorada, permitindo que a classe
    # seja usada como um decorador. Ele recebe os mesmos argumentos que a função decorada
    # e pode modificar seu comportamento antes ou depois de chamar a função original.
    def __call__(self, *args, **kwargs):
        print('hahah')
        return self.func(*args, **kwargs)

# agora, para usar o decorador, basta chamar a classe com o decorator na função desejada. Ex:
@DecoratorSum
def soma(x, y):
    print(f'a soma entre {x} e {y} é: {x+y}')

soma(10, 20) # hahah
# execução da função original: a soma entre 10 e 20 é: 30


#########
# o exemplo acima é um decorador simples, onde a classe recebe a função como argumento e
# a executa dentro do método __call__, adicionando uma funcionalidade extra (imprimir 'hahah')
# antes de chamar a função original. Agora, vamos criar um exemplo de decorador com classe
# que recebe um argumento extra no init, além da função a ser decorada. Ex:

class DecoratorSub:
    # value é o argumento extra que será passado no init, além da função a ser decorada.
    # nesse caso, value será utilizado para realizar uma subtração, ou seja, o resultado
    # da função decorada será subtraído por esse valor.
    def __init__(self, value):
        print('vamos decorarrr')
        self.value = value

    def __call__(self, func):
        def interna(*args, **kwargs):
            # aqui, o resultado da função decorada é subtraído pelo valor passado no init.
            result = func(*args, **kwargs)
            return result - self.value 
        return interna

# agora, para usar o decorador, basta chamar a classe com o decorator na função desejada,
# passando o argumento necessário. Ex:
@DecoratorSub(2)
def subtracao(x,y):
    # aqui, a função decorada realiza uma subtração entre x e y, mas o resultado final será
    # subtraído por 2, que é o valor passado no init do decorador.
    print(f'{x} - {y} = {x - y}')
    return x - y

# agora, para executar a função decorada, basta chamar a função normalmente. Ex:
print(subtracao(10,6)) # vamos decorarrr
# execução da função original: 10 - 6 = 4
# resultado final após a decoração: 2 (4 - 2)

cls()
#####################################################
# metaclasses
# Em python, tudo é um objeto, incluindo as classes. As classes são instâncias de metaclasses.
# A metaclasse é a classe das classes, ou seja, é a classe que define o comportamento das classes.
# Por padrão, a metaclasse é a type, mas é possível criar metaclasses personalizadas para controlar
# a criação e o comportamento das classes.
 
class ClasseExemplo:
    ...

ex = ClasseExemplo()
print(type(ex)) # <class '__main__.ClasseExemplo'> -> a classe do objeto
print(type(ClasseExemplo)) # <class 'type'> -> a classe da classe

# logo, sabemos que ex é uma instância da classe ClasseExemplo, e a classe ClasseExemplo
# é uma instância da metaclasse type.

''' resenha professor

# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução

'''
# lembrando que o método __new__ é responsável por criar a classe, enquanto o método __call__
# é responsável por criar a instância da classe. Portanto, quando uma classe é chamada,
# o método __call__ da metaclasse é executado, que por sua vez chama o método __new__ da
# classe para criar a instância, e depois chama o método __init__ para inicializar a instância.

# para criar uma classe através da metaclasse type, basta chamar da seguinte forma:

# type('Name', (Bases,), __dict__), onde 
# Name é o nome da classe
# Bases é uma tupla de classes base (herança, lembrando que recebe object por padrão)
# __dict__ é um dicionário de atributos e métodos da classe (pode ser vazio).

# sendo: 
MinhaClasse = type('MinhaClasse', (), {}) # o primeiro argumento é o nome da classe

print(MinhaClasse) # <class '__main__.MinhaClasse'> -> a classe criada através da metaclasse type

# agora, para criar uma instância da classe criada, basta chamar a classe normalmente:
minha_instancia = MinhaClasse()

print(minha_instancia) # <__main__.MinhaClasse object at 0x749bfda72660> -> a instância da classe criada

# o que foi feito acima foi criar uma classe de forma dinâmica utilizando a metaclasse type,
# que seria algo semelhante a criar uma classe através de uma instancia de uma classe.

# no entanto, também é possível criar uma metaclasse personalizada, herdando da metaclasse type,
# e sobrescrevendo os métodos __new__ e __call__ para controlar a criação e o comportamento
# das classes.

# por padrão, quando criamos uma classe, sua assinatura é a seguinte:
'''
class NomeDaClasse(Bases, metaclass=type):
    corpo da classe

'''

# a metaclasse é definida através do argumento metaclass na definição da 
# classe. Se não for especificada, a metaclasse padrão é a type.

# para criar uma metaclasse personalizada, basta herdar da metaclasse type e
# sobrescrever os métodos __new__ e __call__. Ex:

class Meta(type):
    # o método __new__ é responsável por criar a classe, portanto, é onde 
    # podemos controlar, considerando que será necessário informar sua 
    # assinatura, que é (cls, name, bases, dct), onde:
    #
    # mcs é a metaclasse, sendo uma convenção chamar o primeiro parâmetro de cls.
    # name é o nome da classe sendo criada
    # bases são as classes base da classe sendo criada
    # dct é o dicionário de atributos e métodos da classe sendo criada

    def __new__(mcs, name, bases, dct):
        print('eu sou o new')
        # nesse caso, a metaclasse será a primeira a executar, pois é ela que
        # cria a classe. Portanto, podemos controlar a criação da classe aqui,
        # por exemplo, adicionando um atributo, validação ou método à classe.
        
        # criando a classe normalmente utilizando o super para chamar o método
        #  __new__ da metaclasse type:
        cls = super().__new__(mcs, name, bases, dct) 

        # podemos visualizar o dicionário da classe para ver os atributos e 
        # métodos que ela possui, incluindo os que foram adicionados pela
        # metaclasse.
        print(cls.__dict__)

        # podemos adicionar um método à classe criada, por exemplo:
        def metodo_adicionado(self):
            return 'eu sou um método adicionado pela metaclasse'
        
        # adicionamos o método ao dicionário da classe
        cls.metodo_adicionado = metodo_adicionado

        # podemos adicionar um atributo à classe criada, por exemplo:
        cls.atributo_adicionado = 'eu sou um atributo adicionado pela metaclasse'

        # vamos ver o dicionário da classe novamente para verificar os 
        # atributos e métodos adicionados.
        print(cls.__dict__)

        # podemos verificar também se um método específico ou atributo foi
        # adicionado à classe, por exemplo:
        print('metodo_adicionado' in cls.__dict__) # True

        # não se proecupe, pois os métodos e atributos adicionados na classe 
        # pelo usuário estarão presentes no dicionário da classe, portanto, é 
        # possível verificar de fato a existência e criar uma lógica com ele.
        #  Por exemplo:
        if not 'tratamento_nome' in cls.__dict__:
            raise TypeError('a classe deve ter um atributo tratamento_nome')
        # logo, a classe só vai ser criada se tiver um atributo chamado 
        # tratamento_nome, caso contrário, irá levantar um erro.

        # e por fim, retornamos a classe criada.
        return cls

    # o conteúdo em new vai tratar apenas a criação da classe, ou seja,
    # o comportamento da classe em si. No entanto, ele não trata os argumentos
    # passados pela classe. Logo, será necessário do método __call__ para 
    # tratar os argumentos passados pela classe, ou seja, o comportamento da
    #  nstância da classe. Ex:
    def __call__(cls, *args, **kwargs):
        # o método __call__ é chamado quando uma instância da classe é criada.
        # ele recebe a classe (cls), os argumentos posicionais (*args) e os
        # argumentos nomeados (**kwargs).
        print(f'criando instância da classe {cls.__name__} com args={args}, kwargs={kwargs}')
        return super().__call__(*args, **kwargs) # aqui, chamamos o método 
        # __call__ da metaclasse type para criar a instância normalmente,
        # passando os argumentos recebidos.

    # logo, alteramos todo o comportamento da classe, mas no final das contas,
    # devido ao super, a classe e suas instâncias serão criadas normalmente,
    # mas com as funcionalidades extras.

# agora, para usar a metaclasse personalizada, basta definir a classe com o
# argumento metaclass=Meta. Ex:
class DemonstraMetaclass(metaclass=Meta):
    def __init__(self, nome):
        self.nome = nome
        
    # para passar na validação da metaclasse, é necessário ter um atributo
    # chamado tratamento_nome.
    def tratamento_nome(self): ...

# considere que a metaclasse é executada no momento da criação da classe,
# ou seja, quando a classe é definida. Portanto, ao definir a classe
# DemonstraMetaclass, o método __new__ da metaclasse Meta é executado, criando
# a classe e adicionando os métodos e atributos definidos. Depois, quando uma
# instância da classe é criada o método __call__ da metaclasse é executado,
# permitindo controlar a criação da instância e seus argumentos.

# retornos após ter criado a classe: 

'''
eu sou o new
{'__module__': '__main__', '__firstlineno__': 2438, '__init__': <function DemonstraMetaclass.__init__ at 0x7b7675be2610>, 'tratamento_nome': <function DemonstraMetaclass.tratamento_nome at 0x7b7675be26c0>, '__static_attributes__': ('nome',), '__dict__': <attribute '__dict__' of 'DemonstraMetaclass' objects>, '__weakref__': <attribute '__weakref__' of 'DemonstraMetaclass' objects>, '__doc__': None}
{'__module__': '__main__', '__firstlineno__': 2438, '__init__': <function DemonstraMetaclass.__init__ at 0x7b7675be2610>, 'tratamento_nome': <function DemonstraMetaclass.tratamento_nome at 0x7b7675be26c0>, '__static_attributes__': ('nome',), '__dict__': <attribute '__dict__' of 'DemonstraMetaclass' objects>, '__weakref__': <attribute '__weakref__' of 'DemonstraMetaclass' objects>, '__doc__': None, 'metodo_adicionado': <function Meta.__new__.<locals>.metodo_adicionado at 0x7b7675be2770>, 'atributo_adicionado': 'eu sou um atributo adicionado pela metaclasse'}
True
'''

# vamos criar a instância
demonstra = DemonstraMetaclass('demonstração') # criando instância da classe DemonstraMetaclass com args=('demonstração',), kwargs={}
print(demonstra.nome) # demonstração
print(demonstra.atributo_adicionado) # eu sou um atributo adicionado pela metaclasse
print(demonstra.metodo_adicionado()) # eu sou um método adicionado pela metaclasse
######

# citação do Tim Peters, um dos principais desenvolvedores do Python
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)

# ou seja, as metaclasses são um assunto avançado e complexo, e a maioria dos
# desenvolvedores não precisa se preocupar com elas.

########################################################
# Uso do dir, help e DocString de uma linha para visualização de componetes
# Para demonstrar tanto o uso como a visualização de forma organizada, será
# necessário criar uma pasta específica (provavelmente serão várias aulas). 
# Para não fazer como das outras vezes, onde eu criava a pasta manualmente
# e ia comentando como fazia, irei digitar aqui o código de criação 
# passo a passo, através do módulo pathlib, que sei que ainda não coloquei nada
# aqui sobre ele, mas basta visitar o módulo seguinte (módulo 4) e buscar por
# ele em específico que você passará a entender como fiz aqui.

from pathlib import Path

# coleto o módulo atual
RAIZ = Path(__file__).parent

# crio a pasta que vamos utilizar como referência
pasta_ref = RAIZ / 'aula252' 
Path.mkdir(pasta_ref,exist_ok=True)

# crio o arquivo que será analisado
caminho_arquivo_um_linha = pasta_ref / 'uma_linha.py'
Path.touch(caminho_arquivo_um_linha)

# agora que já foi criado algo, vamos importar o módulo que acabou de
# ser criado.
from aula252 import uma_linha

# vamos verificar os componentes desse módulo
print(dir(uma_linha)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

# através do dir é possível verificar tudo que o módulo tem, seja variável,
# função, etc. Por exemplo, vou adicionar uma variável e função nova:
Path(caminho_arquivo_um_linha).write_text(
    'cor = \'azul\'\n'
        'def imprimir(msg:str):\n    print(msg)'
)

# verificando novamente o conteúdo da do módulo:
print(dir(uma_linha)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'cor', 'imprimir']
# é possível identificar a presença da função 'imprimir' e da variável cor no final.
 
# também é possível verificar cada coisa individualmente, considerando que já
# é sabido o nome dos componetes.
print(uma_linha.__name__) # aula252.uma_linha
print(uma_linha.__cached__) # /home/umcex/Documentos/Cursos/cursopy/Modulo3/aula252/__pycache__/uma_linha.cpython-314.pyc
print(uma_linha.__file__) # /home/umcex/Documentos/Cursos/cursopy/Modulo3/aula252/uma_linha.py
print(uma_linha.__doc__) # None

# no entanto, há uma função que é muito útil quando o desejado é saber tudo
# e com detalhes de um determinado módulo em python, de forma organizada:

# help(uma_linha) # para ver isso funcionando, basta descomentar essa linha 

'''
retorno:
Help on module aula252.uma_linha in aula252:

NAME
    aula252.uma_linha

FUNCTIONS
    imprimir(msg: str)

DATA
    cor = 'azul'

FILE
    /home/umcex/Documentos/Cursos/cursopy/Modulo3/aula252/uma_linha.py

'''

# @----
# Podemos também utilizar docstrings para organizar ainda mais o arquivo,
# fazendo com que o help consiga ser mais visual e explicativo. 
# Para demonstrar isso, irei colocar no topo do arquivo um docstring explicando
# o que o módulo faz:

# busco o que já estava escrito no arquivo (lembrando que o doc será no topo)
dados_anteriores = Path(caminho_arquivo_um_linha).read_text() 
# adiciono a doc no topo e depois o conteúdo antigo do arquivo
Path(caminho_arquivo_um_linha).write_text(
    '"""Este módulo faz uma demonstração prática do poder pythônico"""\n'
    'cor = \'azul\'\n'
    'def imprimir(msg:str):\n    print(msg)'
)

# fazendo um help (para verificar o help, descomente a linha abaixo):
# help(uma_linha)
'''
retorno:
Help on module aula252.uma_linha in aula252:

NAME
    aula252.uma_linha - Este módulo faz uma demonstração prática do poder pythônico

FUNCTIONS
    imprimir(msg: str)

DATA
    cor = 'azul'

FILE
    /home/umcex/Documentos/Cursos/cursopy/Modulo3/aula252/uma_linha.py

'''

# @______
# Outro detalhe importante é que também é possível adicionar uma descrição 
# de várias linhas através da docstring, que vai aparecer bonitinho quando for
# utilizado o help. No entanto, é importante destacar que para isso, é 
# necessário que você siga as recomendações de boas práticas da pep8, sendo uma
# delas: uma linha deve ter no máximo até 79 caracteres. Caso passe disso,
# então será necessário quebrar a linha. Abaixo, irei criar um outro arquivo,
# escrever um doc de várias linhas e mostrar como vai ficar.

Path(pasta_ref / 'varias_linhas.py').write_text(
    '''"""Snake_case ipsum pep8 sit amet, indent_four_spaces adipiscing elit.
Try_except do eiusmod tempor variable_name ut labore et strings_triplas magna
aliqua. Ut enim ad backend veniam, quis nostrud list_comprehension ullamco
laboris nisi ut aliquip ex ea lambda consequat. Duis aute irure docstring
in reprehenderit in code_review velit esse cillum dolore eu syntax_error 
pariatur.

Deploy_production ipsum merge_conflict sit amet, code_refactor debugging elit.
Docker_container do eiusmod tempor pipeline_automation ut Jenkins et
Kubernetes magna aliqua. Ut enim ad microservices veniam, quis nostrud
pull_request ullamco cloud_computing nisi ut aliquip ex ea database_schema
consequat. Duis aute irure dark_mode in backend_development in production_ready
velit esse API_endpoint dolore eu logic_error pariatur."""

print('hello world!')
'''
)

# importando o novo módulo
from aula252 import varias_linhas

# agora, vamos olhar o help (para verificar o help, descomente a linha abaixo):
# help(varias_linhas)

'''
retorno:
Help on module aula252.varias_linhas in aula252:

NAME
    aula252.varias_linhas

DESCRIPTION
    Snake_case ipsum pep8 sit amet, indent_four_spaces adipiscing elit.
    Try_except do eiusmod tempor variable_name ut labore et strings_triplas magna
    aliqua. Ut enim ad backend veniam, quis nostrud list_comprehension ullamco
    laboris nisi ut aliquip ex ea lambda consequat. Duis aute irure docstring
    in reprehenderit in code_review velit esse cillum dolore eu syntax_error
    pariatur.

    Deploy_production ipsum merge_conflict sit amet, code_refactor debugging elit.
    Docker_container do eiusmod tempor pipeline_automation ut Jenkins et
    Kubernetes magna aliqua. Ut enim ad microservices veniam, quis nostrud
    pull_request ullamco cloud_computing nisi ut aliquip ex ea database_schema
    consequat. Duis aute irure dark_mode in backend_development in production_ready
    velit esse API_endpoint dolore eu logic_error pariatur.

FILE
    /home/umcex/Documentos/Cursos/cursopy/Modulo3/aula252/varias_linhas.py
'''

# @___
# Agora que já mostrei como fazer, irei fazer uma demonstração de uso real
# da dogstring, inicialmente com funções. Como mostrei, todas as funções 
# aparcerem no help, correto? e para cada uma delas, é possível incrementar uma
#  docstring explicando para que ela serve e também utilizar type hints para 
# informar os tipos que cada parâmetro deverá receber, juntamente com o 
# retorno(considere que essa é somente uma das formas de documentar função ou 
# qualquer outra coisa). Portanto, irei criar abaixo mais um arquivo para
# demonstrar como seria isso.

# inserindo o código
codigo_funcao = '''\
"""Este módulo apenas vai exemplificar o uso de uma função com docstring

No geral, haverá somente duas funções.
"""

def multiplica(
    x: int | float,
    y: int | float,
    z: int | float | None = None
) -> int | float:
    """Multiplica x, y e/ou z

    Multiplica x e y. Se z for enviado, multiplica x, y, z.
    """
    if z is None:
        return x * y
    return x * y * z

# eu não ia mostrar outra forma de usar doc numa função, mas farei abaixo:
def subtracao(x, y):
    """ Essa função realizará uma
        subtração entre x e y.
    
    :param x: primeiro número    
    :type x: int ou float
    :param y: segundo número    
    :type y: int ou float
    
    :return y: subtração de x - y
    :return_type: int ou float
    """

    return x-y
'''
# Antes de continuar, perceba que eu também adicionei um comentário no código
# acima com o intuito de mostrar que no help, comentários não aparecem.

# criando o arquivo e inserindo o codigo
Path(pasta_ref / 'documentando_funcoes.py').write_text(codigo_funcao)

# importando o módulo
from aula252 import documentando_funcoes

# chamando o help para o novo módulo
# help(documentando_funcoes)

'''
retorno:
Help on module aula252.documentando_funcoes in aula252:

NAME
    aula252.documentando_funcoes - Este módulo apenas vai exemplificar o uso de uma função com docstring

DESCRIPTION
    No geral, haverá somente duas funções.

FUNCTIONS
    multiplica(x: int | float, y: int | float, z: int | float | None = None) -> int | float
        Multiplica x, y e/ou z

        Multiplica x e y. Se z for enviado, multiplica x, y, z.

    subtracao(x, y)
        Essa função realizará uma
            subtração entre x e y.

        :param x: primeiro número
        :type x: int ou float
        :param y: segundo número
        :type y: int ou float

        :return y: subtração de x - y
        :return_type: int ou float

FILE
    /home/umcex/Documentos/Cursos/cursopy/Modulo3/aula252/documentando_funcoes.py
'''

# @____
# Eu realmente não queria trazer outros estilos de organização de função para
# docstring, mas irei trazer 3, sendo um o estilo que mostrei 
# anteriormente (reST) e como extra, trarei um exemplo de como escrever isso
# caso a função haja um exception. Segue para o arquivo:

# Definindo o conteúdo do arquivo com tratamento de erro
codigo_exceptions = '''\
"""Este módulo demonstra como documentar EXCEÇÕES (Raises).
"""

# -------------------------------------------------------------------------
# 1. Google Style
# -------------------------------------------------------------------------
def funcao_google(x: int, y: int) -> int:
    """Realiza uma operação, mas falha se y for 2.

    Args:
        x (int): O primeiro número.
        y (int): O segundo número.

    Returns:
        int: O resultado da operação.

    Raises:
        ValueError: Se y for igual a 2.
    """
    if y == 2:
        raise ValueError("y não pode ser 2 neste sistema")
    return x + y


# -------------------------------------------------------------------------
# 2. NumPy Style 
# -------------------------------------------------------------------------
def funcao_numpy(x: int, y: int) -> int:
    """
    Realiza uma operação, mas falha se y for 2.

    Parameters
    ----------
    x : int
        O primeiro número.
    y : int
        O segundo número.

    Returns
    -------
    int
        O resultado da operação.

    Raises
    ------
    ValueError
        Se o valor de y for estritamente igual a 2.
    """
    if y == 2:
        raise ValueError("y não pode ser 2 neste sistema")
    return x + y


# -------------------------------------------------------------------------
# 3. Padrão reST - reStructuredText
# -------------------------------------------------------------------------
def funcao_padrao(x: int, y: int) -> int:
    """Realiza uma operação, mas falha se y for 2.

    :param x: O primeiro número.
    :type x: int
    :param y: O segundo número.
    :type y: int
    :return: O resultado da operação.
    :rtype: int
    :raises: ValueError: Se y for igual a 2.
    """
    if y == 2:
        raise ValueError("y não pode ser 2 neste sistema")
    return x + y
'''

# Criando o arquivo
Path(pasta_ref / 'documentando_funcoes_exception.py').write_text(
    codigo_exceptions
    )
cls()
# Importando para testar
from aula252 import documentando_funcoes_exception

# chamando help (descomente a linha abaixo para visualizar):
# help(documentando_funcoes_exception) 

'''
retorno:
Help on module aula252.documentando_funcoes_exception in aula252:

NAME
    aula252.documentando_funcoes_exception - Este módulo demonstra como documentar EXCEÇÕES (Raises).

FUNCTIONS
    funcao_google(x: int, y: int) -> int
        Realiza uma operação, mas falha se y for 2.

        Args:
            x (int): O primeiro número.
            y (int): O segundo número.

        Returns:
            int: O resultado da operação.

        Raises:
            ValueError: Se y for igual a 2.

    funcao_numpy(x: int, y: int) -> int
        Realiza uma operação, mas falha se y for 2.

        Parameters
        ----------
        x : int
            O primeiro número.
        y : int
            O segundo número.

        Returns
        -------
        int
            O resultado da operação.

        Raises
        ------
        ValueError
            Se o valor de y for estritamente igual a 2.

    funcao_padrao(x: int, y: int) -> int
        Realiza uma operação, mas falha se y for 2.

        :param x: O primeiro número.
        :type x: int
        :param y: O segundo número.
        :type y: int
        :return: O resultado da operação.
        :rtype: int
        :raises: ValueError: Se y for igual a 2.

FILE
    /home/umcex/Documents/Cursos/cursopy/Modulo3/aula252/documentando_funcoes_exception.py
'''

##########
# @___
# E como pode imaginar, também funciona para classes. Com reST, irei
# demontrar um exemplo. Portanto, irei criar um outro arquivo para isso.

classe_documentacao = '''\
"""
Esse módulo é apenas uma exemplificacão de documentacao para classes.
"""

class divisao_doc:
    """
    Essa classe é responsável por gerenciar divisões de valores
    de forma responsável, tratando apenas números inteiros.
    """
    def __init__(self, a:int, b:int) -> float:
        """
        Inicializa o construtor com os argumentos passados.
        
        :param a: primeiro valor
        :type a: int
        :param b: segundo valor
        :type b: int
        """
    
        self.valor_a = a
        self.valor_b = b
    
    def calculo(self):
        """
        Verifica o tipo dos argumentos passados e se forem inteiros, então
        realiza uma divisão.
        
        :return: divisão entre o primeiro valor e o segundo
        :rtype: float
        :raises TypeError: Se algum dos argumentos não for inteiro.
        """

        # verifica o tipo dos dados informados
        if not type(all(x,int) for x in (self.valor_a, self.valor_b)):
            raise TypeError('será aceito somente valores inteiros')

        return self.valor_a / self.valor_b
'''
# criando o arquivo
Path(pasta_ref / 'documentando_classes.py').write_text(
    classe_documentacao
)

# importando o arquivo
from aula252 import documentando_classes

# chamando o help (descomente a linha abaixo para visualizar)
# help(documentando_classes)

'''
Help on module aula252.documentando_classes in aula252:

NAME
    aula252.documentando_classes - Esse módulo é apenas uma exemplificacão de documentacao para classes.

CLASSES
    builtins.object
        divisao_doc

    class divisao_doc(builtins.object)
     |  divisao_doc(a: int, b: int) -> float
     |
     |  Essa classe é responsável por gerenciar divisões de valores
     |  de forma responsável, tratando apenas números inteiros.
     |
     |  Methods defined here:
     |
     |  __init__(self, a: int, b: int) -> float
     |      Inicializa o construtor com os argumentos passados.
     |
     |      :param a: primeiro valor
     |      :type a: int
     |      :param b: segundo valor
     |      :type b: int
     |
     |  calculo(self)
     |      Verifica o tipo dos argumentos passados e se forem inteiros, então
     |      realiza uma divisão.
     |
     |      :return: divisão entre o primeiro valor e o segundo
     |      :rtype: float
     |      :raises TypeError: Se algum dos argumentos não for inteiro.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

FILE
    /home/umcex/Documents/Cursos/cursopy/Modulo3/aula252/documentando_classes.py\
'''

##########################################################
# Doc: https://docs.python.org/pt-br/3/howto/enum.html
# Explicacao do professor:

# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
# -----------------------------------

# um exemplo para o uso do enum:
# Vamos supor que há um joguinho simples onde o persongem principal tem que 
# se movimentar pelo mapa. Considerando que as a movimentacão é composta por:
#
# Esquerda;
# Direita;
# Cima;
# Baixo;
#
# Logo, podemos utilizar uma variável qualquer e para verificar se a 
# movimentacão para tal lugar é permitida, podemos utilizar um for in simplemente
# um in com uma lista. No entanto, conforme isso cresce, pode acabar ficando 
# baguncado. Logo, podemos utilizar o enum para tal objetivo, sendo chamado da 
# seguinte forma:

# O enum é um módulo que já vem com o python
import enum

# agora, basta declarar uma classe que vai herdar da classe Enum, sendo
# possível adiantar os argumentos.
Direcoes = enum.Enum(
    # Perceba que como os dados na lista não irão mudar, irei inicializar
    # como constante (Letras em caixa alta).
    'Direcoes',[
        'ESQUERDA', 'DIREITA', 'CIMA', 'BAIXO',
    ]
)

# para acessar o conteúdo dentro da instancia, há algumas formas.
# Dentre elas há:

# Busca com base no número (por ordem)
print(Direcoes(1)) # Direcoes.ESQUERDA

# busca com base no nome
print(Direcoes['ESQUERDA']) # Direcoes.ESQUERDA

# busca com base no namespace # Direcoes.ESQUERDA
print(Direcoes.ESQUERDA) 

# é possível também acessar diretamente tanto o nome como o valor:
print(
    Direcoes.DIREITA.name, Direcoes.DIREITA.value # DIREITA 2
) 

# Para fazer a movedura do personagem, será criada uma funcao.
def mover(direcao: Direcoes): 
    # para verificar se dado enviado em direcao é válido, é possível verificar
    # a instancia do tipo de dado que foi enviado:
    if not isinstance(direcao, Direcoes):
        raise TypeError('Dado inválido!')
    
    print(f'movendo para: {direcao}')

mover(Direcoes.BAIXO) # movendo para: Direcoes.BAIXO
mover(Direcoes.CIMA) # movendo para: Direcoes.CIMA
mover(Direcoes.ESQUERDA) # movendo para: Direcoes.ESQUERDA
mover(Direcoes.DIREITA) # movendo para: Direcoes.DIREITA

# uma informacao importante: Até onde é sabido, a metaclasse que constrói 
# enum.Enum possui uma metaclasse própria.

# Assim, é utilizado um enum. No entanto, para algumas config o meio acima pode
# não funcionar a tipagem como esperado. Devido a isso, algumas pessoas 
# preferem fazer de outra forma, sendo:

class NovaDirecao(enum.Enum):
    # no caso de uma criacao manual, será necessário adicionar value e name de
    # forma manual, sendo:

    ESQUERDA = 1
    DIREITA = 2
    
    # caso deseje que value seja definido de forma automatica, pode utilizar 
    # enum.auto da seguinte forma:
    CIMA = enum.auto
    BAIXO = enum.auto

# e por fim, a tipagem passa a aparecer.
# print(NovaDirecao...)

##########################################



