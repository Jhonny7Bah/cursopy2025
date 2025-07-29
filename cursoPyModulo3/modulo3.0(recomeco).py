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
# Aula 202, 203 e 204 
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