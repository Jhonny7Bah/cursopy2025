def caceta(): #def irá criar uma função com uma variável
    print('cacetinha') #aqui é o conteúdo de def
    print('cacetinha')

caceta() #quando eu chamar a função cacetinha, oq estiver dentro dela na hora em que foi criada, será executado.

#None = não valor, semelhante a um false
#funções python retornam None. 

def totozinha_sacana(a,b,c):
    #funções podem receber valores para parâmetros
    #no caso acima, meus parâmetros são: a, b e c, que futuramente receberão valores.
    #como eu definir 3 parâmetros, quando eu atribuir valores a um, terei que atribuir aos três, caso 
    #contrário, ocorrerá um erro
    print(a)
    print(b)
    print(c)

totozinha_sacana(10, 70, 90) #aqui há uma atribuição de valores, chamada também de argumentos
#posso fazer isso quantas vezes eu quiser 
totozinha_sacana('kaka', 'baba', 40)

def saudacao (nome='Marcas'): #para não haver erro, vamos adicionar um nome para se caso a pessoa não passar nenhum argumento
    print('olá, {}'.format(nome))

saudacao('Xablau')
saudacao() #se uma pessoa digitar assim, por padrão daria um erro

def divisao(n1, n2):
    print(n1 / n2)

print(divisao(n2=10,n1=20)) #aqui é um argumento nomeado
#a partir do  momento que eu nomear um argumento, precisarei nomear todos que virão após ele.
#(o que foi dito acima serve tbm para parametros)

print(divisao(10, 20)) #aqui é um argumento não nomeado/ também chamados de argumentos posicionais

#refatorar -> editar o código
#como dito antes, se numa função tiver três argumentos e o usuário chamar a função, digitando dois parâmetros
# o código buga. No entanto, se para cada parâmetro for dado um valor inicial, ou seja, um argumento padrão, isso não acontece.

def soma(x, y, z=0): #demos um valor padrão para o z, pois não sabemos se o user vai precisar dele.
    if z:
        print(f'{x=}{y=}{z=}') #o z só vai aparecer se o user passar o terceiro argumento
    else: 
        print(f'{x=}{y=}')
    print(x + y + z)

print(soma(10, 20, 14))
##############
def notas(a1, a2): #essa linha do def é denominada de assisnatura da função, já que nela tem o nome da função e os parâmetros, tendo algumas vezes argumentos pré-definidos.
    return a1, a2
#escopo -> local onde o codigo pode atingir = pense em variaveis locais e globais
# o def seria um escopo local, já o restante do código, um global. Logo, se eu declaro uma variavel
#dentro do escopo local e tentar acessar de fora sem entrar nesse antes, vai dar pau. 
#ex:
def caceta():
    try:
        marcas_bandida = 10 #var declarada dentro do escopo só vai poder ser acessada na chamada da função
        print(marcas_bandida)
        print(blablabla) #blablabla é uma variável que ainda não foi declarada 
    except NameError:
        print('Deu pau aqui')
caceta()

marcas_bandida = 20 #fora do código, posso criar uma variável com o msm nome que não vai da nada.
print(marcas_bandida)

#mas, se eu definir a função antes de chamar a função, eu consegurei acessar uma variavel globald entro do escopo local.
blablabla = 101010 
caceta() #agora, blablabla irá aparecer com sua atribuição 
#escopo primario

terramota = 5
def escopo(): #escopo secundário
    global terramota #com o global, eu consigo acessar a variável terramota fora do escopo
    #mas aparentemente, isso é uma má prática de programação
    
    terramota = 11 #posso definir uma def dentro da outra, mas a lógica é a mesma (não posso acessar elementos da def1 em def2)
    def escopo2(): #escopo terciário
        global terramota #posso fazer isso aqui tamém, claramente

        print(terramota)
escopo()
print(terramota) #percebe-se que terramota fora do escopo é 11

#call stack = pilha de chamadas
# o interpretador, por padrão, faz a leitura ocidental. No entanto,quando há uma função, o interpretador simplemente o ignora e somente vai o ler na chamada dessa função.
# Com isso, o interpretador vai ter que ler debaixo para cima, nesse momento. Logo, para não bagunçar as informações (principalmente no debbuger), ele cria um sub módulo e um call stack, onde todas as informações referente aquela função acabam sendo armazenadas individualmente.
 

# escopo do módulo é esse que estamos, é o principal
casa = 14
terremoto = 10 
def caceta():
    def teste():
        print(terremoto) #eu não consigo acessar o escopo módulo sem global, mas consigo acessar o escopo de uma função dentro de uma outra função
    global casa #agora, eu consigo acessar a variavel fora desse escopo. 
    #quando eu uso global, o python vai buscar a variavel solicitada mais próxima.
    casa = 16 #nova função, novo escopo
    terremoto = 15
    teste() #terremoto foi definida dentro do desse escopo, mas no sub escopo, eu fiz um print com ele e deu certo  
caceta()
print(casa)

def soma(x, y):
    ... #como dito anteriormente, uma função, por padrão retorna none
        #None significa um não valor, ou seja, um valor sem conteúdo
        #Se o código dentro da função após executado retornar none, por causa da função, consequentemente le enão poderá ser reaproveitado numa variavel
try:
    soma1 = soma(10, 14) #por exemplo, aqui eu estou chamando a função soma e ofertando argumentos
    soma2 = soma(14, 17) #aqui também
    result = soma1 + soma2 #no entanto, quando vou realizar a soma, dá um problema de type error, pois o valor retornado foi None.
    print(result)
except TypeError:
    print('Como pode ver, deu pau', type(soma1)) #se oberservar o tipo retornado, fora Nonetype
#         result = soma1 + soma2
#              ~~~~~~^~~~~~~
# # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

#como fazer a função retornar valor != None:
def soma_verdadeira(x, y):
    print('Foda-seeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
    return x + y #return vai retornar tipo que vier após ele ser chamado dentro da função 
    #todo código digitado após o return ser chamado, torna-se um código inalcançável, ou seja, que não irá executar. 

soma_1 = soma_verdadeira(10, 10)
soma_2 = soma_verdadeira(10, 10)
print(soma_1 + soma_2, type(soma_1)) #como pode ver, a soma foi um sucesso e o tipo retornado fora int

#Alt + Shift + Down -> atalho para duplicar linha de código no VS code

#Ctrl + Shift + K -> atalho para apagar uma linha de código no VS code 
def condicaooo(num):
    if num > 14:
        return print('caceco') #funciona parecido com o break em um laço, pois se isso for verdadeiro, o que será retornado será caneco.
    return print('bunda') #é só imaginar que return é um break, problema resolvido!
condicaooo(1) #menor que 14
condicaooo(45) #maior que 14

def somando(*args): #quando eu precisar declarar uma quantidade grande de parametros não nomeados, args, que é uma forma de empacotamento.
#com *args, na chamada da função, poderei dar uma quantidade enorme de argumentos e o código vai funcionar normalmente.
    print(sum(args)) #Quando o player chamar a função e fornecer os argumentos, sum irá somar todos os valores!
    #outra forma de realizar a soma
    soma = 0
    for __ in range(len(args)):
        soma += args[__]
    #fim do cálculo    
    return (soma) #retorna a soma duas vezes
    # return(print(soma)) se eu retornar com uma print, como a print é uma função que retorna None por padrão, esse return que eu fiz será inútil, pois o nome será retornado pra todo efeito.
    # logo, não utilize um print após um return.
print(somando(45, 75, 45, 10, 75)) #posso colocar quantos argumentos eu quiser!

#lembre-se da aula 112 (algo interessante sobre desempacotamento)
listinha = 45, 78, 45, 78
print(sum((45, 78, 45))) #sum é uma função que funciona com iteráveis, ou seja, se eu passar argumentos literais crus, vai dar pau.
#para resolver isso, preciso passar esses argumentos como uma tupla, ou seja, em parenteses

#preciso te relembrar de uma coisa do desempacotamento: Listinha é uma tupla declarada acima
#quando eu declaro uma tupla, array ou dicionário, os argumentos que estou passando automaticamente estão sendo empacotados.

print(listinha) #quando eu imprimo listinha dessa forma, vemos listinha espacotada. 
print(*listinha) #quando eu utilizo o * antes da tupla listinha, o valor é desempacotado

#Higher Order Functions -> funções de ordem superior: função que recebe outra função como argumento ou retornam o valor para outra função
# Higher Order Functions - Funções que podem receber e/ou retornar outras funções
# First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...) - uma das principais características é passar uma função numa variável
#Exemplificações abaixo:

def fds(msg): #é possível fazer a chamada de uma função a partir de uma variavel
    return msg

carai = fds #a variavel carai ta recebendo a função fds
print(carai(10)) #como pode ver, estou colocando argumentos em carai, já que ele tem como elemento a função fds. (não vejo utilidade, mas é bom saber)
print(fds(10)) #mas como pode ver, posso chamar a função diretamente também.  

def imprimindo(msg): #essa função vai imprimir o valor de msg se verdadeiro.
    #além disso, eu posso executar uma função através de outra função (não sei o porquê de querer fazer isso)
    if msg: #aqui, ele faz a comparação para saber se msg is True
        return msg
    #se não, vai tacar o fds.
    return 'foda-se'
#essa função abaixo tem o papel de executar a função acima.
def executado(funcao):#declaro um parâmetro chamado função, que tem que ser correspondente ao nome da função que quero executar
    return funcao #e aqui, ela vai retornar a função

chamada = executado(imprimindo) #nessa variável, eu guardo a chamada da função executar, e logo após, ela realiza a chamada da função imprimindo.
#no caso acima, a função imprimindo, quando chamada, recebe um argumento, que no caso, é 'carai'
print(chamada('carai')) #logo, carai será printado!
#fim das exemplificações


#relembrando:
# argumentos nomeados são aqueles que recebem uma "variavel" ou um nome na chamada da função/método. numa função e ignoram a ordem pré-determinada, por exemplo:
bandido = 14
autista = 15
#caso variável
print('primeiro: {two} segundo: {one}'.format(one=bandido, two=autista))
#no caso acima, two foi primeiro no campo de substituição {}, no entanto, na chamada da variável, quem aparece primeiro é o one
# Se fossem não nomeadas, seguiria a ordem na chamada da variável.
print(bandido, autista)
#no exemplo acima, são agora argumentos não nomeados, seguindo a ordem pré determinada

# caso função
def demonstracao(nome, idade):
    print(f'Nome: {nome}, idade: {idade}')

demonstracao('joão', 16) #nesse caso, o print vai aparecer seguindo a ordem: argumentos posicionais
demonstracao(idade=14, nome='Brasil') #já aqui, eu não segui a ordem, pois idade foi primeiro e nome foi depois
#mas mesmo assim, quando printado, sai certinho, pois foram nomeados. Ou seja, esse argumento agora é nomeado.

#caso método veremos mais tarde!


#falando melhor sobre função de primeira classe e primeira ordem:


#Função de Ordem Superior
#é possível armazenar a função numa var, passar como parametro para outra função, retornar outra função, etc.
# Definição: Uma função de ordem superior é uma função que recebe uma função como argumento ou retorna uma função.


# Funções de Primeira Classe (First-Class Functions)
# Definição: Uma função de primeira classe é uma função que pode ser tratada como um valor. Isso significa que ela pode ser armazenada em variáveis, passada como argumento para outras funções e retornada de funções.

def saudacionar(msg):
    return msg

armazenar_saudacionar = saudacionar #estou acessando a função saudacionar e armazenando ela na variável
print(armazenar_saudacionar('fds')) #como eu tenho a função saudacionar armazenada, eu posso utiliza ela para incrementar um argumento.

#outro caso
#fazer uma função retornar outra função
def saudar():
    print('va pra peste') #função a ser retornada

def executa(func): #função que irá retornar.
    return(func) #func no caso é o nome da função a ser retornada

executa(saudar()) #a função a ser retornada é saudar, logo, saudar será executada.

#um ponto interessante a destacar é que a função imprime o valor na tela quando há ()
#caso não haja (), ela não executa a função. Se houver um print após a chamada da função, ela vai retornar o alocamento na memória em que a função se encontra
print(executa(saudar)) #como pode ver, retornou: <function saudar at 0x00000203F611DB20>, que é a alocação
print(executa(saudar())) #agora, com () após saudar, a função vai executar totalmente e exibir algo até o seu retorno, seja ele retornável ou None

#voltando para função de primeira classe
#outro caso
#aqui estamos fazendo algo parecido, no entanto, a diferença está presente no executador, pois há dois parâmetros.
def givegodnight(msg):
    return msg #se você prestou atenção, agora temos um parâmetro que será retornado aqui
def executagodnight(func_execution, msgg): #aqui, há dois parâmetros, sendo um o retorno de uma outra função e o outro a mensagem
    #no outro msg também existe e é retornado, então o segundo argumento a ser passado aqui servirá para essa função, e logo, para a posterior.
    return func_execution(msgg) #acesso func_execution e também passo msgg, que será retornado como argumento posicional

send_gog_night_in_var = executagodnight(givegodnight, 'boa noite mano') #declaramos uma variável passando o argumento
print(send_gog_night_in_var) #e aqui, ele é exibido.

#outro caso:
#e se em givegodnight eu tiver a necessidade de passar mais de um parâmetro na definição da função?

def goodafternoon(msg, nome): #definindo uma função com dois parametros
    return f'{msg}, {nome}' #exibindo em f strings os dois parametros
    # return msg, nome             se eu fizesse desse jeito, o valor retornado retornaria empacotado.

def execucao_god_after(funcao, *args): #como precisamos dar valores a dois parâmetros, vamos precisar do args, para armazenar qualquer valor a mais que o cara digitar e empacotar
    return funcao(*args) #aqui, ele irá retornar a função e posteriormente, desempactotar args, devido a presença do *
    # return funcao(args)           #se eu fizesse desse jeito, iria retornar um erro de argumento posicional.
    #no caso da linha acima, se o python não considerasse como erro, retornaria o valor empacotado 

print( execucao_god_after(goodafternoon, 'Boa tarde', 'Xablau')) #aqui eu passo os argumentos e tudo funfa de boa

#no geral, eu utilizei ordem superior e primeira classe no código acima. 
#lembrando que primeira classe dá pra fazer analogia com variáveis, pois armazena um valor sem fazer algo com outra def
#ordem superior mexe diretamente com outras funções. 

#limpeza --------------------------- ignore
from os import system
def cls():
    return system('cls')
#-----------------------------------

cls()
#   CLOSURE E FUNÇÕES QUE RETORNAM OUTRAS FUNÇÕES AULA 116
def gerar_gentileza(nome, gentileza ): 
    return f'{nome}, {gentileza}'

print(gerar_gentileza('Danilo', 'Tudo bem?'))
print(gerar_gentileza('Juliano', 'Tudo bem?')) #percebeu que há repetição em relação ao 'tudo bem?'
######################
# segunda parte

#lembre-se da questão dos (), pois se há ele na função, a função executa quando chamada, se não, ela mostra sua alocação na memória
def controle_de_saida(questionamento, nome):
    def verificacao():
        return f'{questionamento}, {nome}?'
    return verificacao #s eu remover os () quando retornar, o valor alocado ele passará a retornar

print('\n\n')
questionamento_saindo = controle_de_saida('saindo', 'João') #<function controle_de_saida.<locals>.verificacao at 0x000001E5A3C6E200>
questionamento_entrada = controle_de_saida('Entrando', 'Maria') #aqui haverá valor, pois o closure foi utilizado

#Definição: Funções que "lembram" os valores de variáveis do seu escopo de criação, mesmo depois de saírem do escopo em que foram criadas.
#  Geralmente, é usado para manter estado dentro de uma função.


#Closure seria parênteses após a chamada da função. Caso ela já tenha em sua definição, não será necessário.
#no caso acima, o closure é necessário, pois a presença do () na respectiva função é ausente
print(questionamento_entrada) #como não usei (), vai retornar a alocação da função na memória
print(questionamento_saindo()) #como usei o (), vai retornar normalmente 'Saindo João'

#terceira parte e finalização
#como irei utilizar o closure, não precisarei de nome na função primária, como é o caso dos exemplos anteriores.
def eletronicos(condicao):
    def verificar(nome): #nome agora vem para verificar
        return f'{condicao}, {nome}'
    return verificar #lembrando que aqui vai sem (), ou seja, na chamada vai precisar de Closure

cond_1 = eletronicos('novo') #tem apenas um argumento padrão
cond_2 = eletronicos('usado')

print(cond_1('pc')) #e aqui, na chamada, eu coloco o eletrônico. Logo, não precisarei esquecer a condição repetidas vezes!
print(cond_2('televisao\n\n'))

#veja o quanto isso é prático:
eletro = ('radio','celular', 'caixa de som', 'impressora', 'arduino', 'teclado',
'Notebook', 'Ventilador', 'torradeira', 'tablet'
)
for verificarr in eletro: #tudo isso de uma vez
    print(cond_1(verificarr))
# e aparentemente, oq eu fiz acima tem algo a ver com programação funcional

#############
#destrinchandoo melhor o closure:
# no caso acima, eu apenas falei que o closure executa uma uma função através dos parênteses, não? mas não é apenas isso!
# Quando você quiser pausar ou adiar a execução de uma função através do closure, você vai precisar de uma função interna, onde será nela a execução que você faria na principal. Ex:
def vou_somar(x, y):
    return x + y
#no caso acima, a função será executada instantâneamente, mas e se eu quisesse definir um valor padrão para somar? para isso, podemos utilizar o closure!
# de início, precisamos entender que o closure terá a função principal e uma secundária, onde será nessa secundária que a mágica vai ocorrer. ex:
def SomandoNumeros(x): #diferentemente da outra, vou passar apenas o parâmetro x nessa função.
    def interno(y): #aqui eu crio a função secundária, onde adiciono o parâmetro y 
        #no caso da criação de uma função dentro da outra, também é chamada de High Order Function, sendo mais específico, Closure.
        return x + y
        #como pode ver, será nessa função interna que a soma será realizada.
    return interno # e no escopo da função SomandoNumeros, retorno a função interna.
    #não sei se lembra, mas para executar uma função, é necessário incrementar parêntreses. No return acima o parênteses não foi incrementado, logo, a função interna não será executada.


# lembrando que uam função executa n vezes e depois volta ao seu estado original, ou seja, precisarei salvar o seu progresso após adquirir o valor de x. Para armazenar, precisarei de uma variável
mais_cinco = executa(SomandoNumeros(5)) #aqui definimos o valor somado mais 5 e armazenamos na variável, onde está pausada sua execução em return interna.
print(mais_cinco) #aqui você observa a execução armazenada na memória.
#como armazenamos uma função dentro de uma variável, estamos praticando o conceito de firt class function, fechando assim o closure, faltando apenas realizar sua execução informando o valor de y
# e para executar, basta utilizar os parênteses na variável para executar a função, informando também o valor de y, ficando:
print(mais_cinco(10)) #retornará 15.


# ###############################
#tipo dict - dicionário
#o dicionário é um tipo mutável, sendo estruturas de dados do tipo par de chave e valor

#para criar um dicionário, basta utilizar a chaves na declaração da variável, ex:
dicionario = {} #isto é um dicionário vazio.
print(dicionario, type(dicionario)) #vazio, dict
dicionario['fds'] = 'vai te lascar' #chave nesse caso seria o fds, tendo como valor o 'vai te lascar
#acima, eu incrementei uma chave denominada fds e atribui um valor para essa chave.
print(dicionario) #ao chamar o dicionário agora, vemos que elenão está mais vazio


#no caso abaixo, vou colocar manualmente as chaves e os valores.
pessoa_01 = {
    'nome': 'Mário',
    'Sexo': 'masculino',
    'Idade': 17 , 
    'profissao': 'estudante'
}
# pessoa_01 = nome do dicionário
# nome, sexo,idade, profissao = chave
# mario, masculino, 17, estudante = valores


print(pessoa_01) #aqui, eu acesso todo o dicionário

print(pessoa_01['Sexo']) #já aqui, eu faço uma busca filtrada no dicionário com base na palavra chave, que é 'sexo'

arrombar = dict(xablau=10, idade=20) #outra forma de declarar um dicionário
#nome do dict   chave  valor\\\\\\\\\\

pessoa_02 = {
    'nome': 'João', #tipo str
    'idade': 19, #tipo int
    'Sexo': 'Masculino', 
    'altura': 1.70, #tipo float
    'endereco': [ #tipo lista
        {'rua': 'Rua da matança', 'número': 39}, #tipo dicionario / casa principal
        {'rua': 'Rua 320', 'numero': 35} #casa secundária
    ]
}
#como visto acima, posso colocar diferentes tipos de dados num dicionário, assim como em listas e tuplas
print(pessoa_02['endereco'][0]['rua']) #esse arrudeio tem como intuito acessar a casa principal do cidadão
#pessoa_02 é o nome do dicionário
# ['endereco'] é para filtrar apenas o endereço no dicionário
# [0] serve para pegar o índice 0 da lista, acessando a casa principal (lembre-se que ali dentro tem uma lista)
# ['rua'] serve para filtrar apenas a rua no sub dicionário

print(pessoa_02, '\n') #exibindo de uma vez, mal organizado

#se eu quiser acessar o dicionário de uma vez de forma um pouco mais organizada, posso utilizar um for
for chave in pessoa_02:
    print(chave,': ', end=' ') #assim vai exibir apenas a chave
    print(pessoa_02[chave]) #aqui vai exibir o conteúdo da chave, que no caso, é o valor.

#crud do dicionário:
#criar, apagar, editar e acessar
#create, read, update, delete
pessoa_03 = {

} 
terracota = 'peste'#input('digite uma chave: ') #também consigo perguntar ao user uma chave para o dict e colocar
pessoa_03[terracota] = 'Xablau' #criei
print(pessoa_03) #acessei #a chave terracota foi implementada como 'peste'

pessoa_03[terracota] = 'caramba' #editei
print(pessoa_03) 

del pessoa_03[terracota] #deletei #vai apagar a chave terracota(peste)
print(pessoa_03)#percebe-se que está vazia

#por mais que tu tnha deletado terracota, ele continuará aparecendo no vscode

if pessoa_03.get(terracota) is None: #get vai fazer uma busca pela chave no dicionário
    print('senão existir, o if vai retornar none e virá para essa linha, tratando o erro')
else: #se existir, vai retornar o nome da chave e virá para o else.

    print(pessoa_03[terracota]) #como pode ver, acessou normalmente, porém, lembre-se que apagamos
    #em outras palavras, vai gerar um erro de keyerror, que é o mesmo erro que acontece quando uma chave não é encontrada

#métodos úteis dos dicionários
pessoa_04 = {
    'nome':'Carlos',
    'idade':24
}
#dunder methods - métodos que iniciam com dois __ e termina com dois __
print(pessoa_04)
print(pessoa_04.__len__()) #vai retornar o número de chaves presentes no dicionário
print(len(pessoa_04)) #outra forma mais fácil e mais usual de saber quantas chaves têm no discionário

print(pessoa_04.keys()) #informa todas as chaves presentes na variável, até as que já foram apagadas
#um detalhe curioso é que quando tilizamos o key em um print, ele claramente retorna as chaves do dicionário, no entanto, aparecem como se estivessem em list
#logo, se quisermos pegar uma informação em específico, como seria? podemos tentar fazer como lista
#  mesmo, mas...

try:
    print(pessoa_04.keys()[0]) #o vscode até aceita, porém quando executado, dá erro.
    #isso ocorre porque dict_key não é uma lista, mas podemos fazer isso de outra forma:]
except TypeError:
    print('deu pau')
keys_lista = (list(pessoa_04.keys())) #agora, que eu converti para list, consigo acessar como tal.
print(keys_lista[0]) #retorna apenas o índice 1, ou seja, 'nome'

print(pessoa_04.values()) #vai retornar os valores das chaves. 
valores = tuple(pessoa_04.values()) #posso converter para tupla tbm
print(valores[0]) #retornará apenas o valor da chave nome

print(pessoa_04.items()) #retorna as chaves os valores, veja o exemplo num for a seguir:
print('')
for pessoas4_tudo in pessoa_04.items():
    print(pessoas4_tudo)    #o resultado saiu empacotado
#como será retornada uma tupla com dois índices [0,1] empacotados, posso utilizar um for com uma lógica parecida com o enumerate, veja:
for chaves, valores in pessoa_04.items():
    print(f'{chaves}: {valores}') #como pode ver, os valores sairam desempacotados.

#uso do setdefault:
# o setdefault vai fazer uma busca na chave que você digitar, no entanto, se ele não encontrar essa chave, ele cria uma
pessoa_04.setdefault('sexo', 'M')#como pode ver, no dicionário pessoa_4 não há a chave sexo, setdefault a criou, juntamente com o valor 'M'.
print(pessoa_04)
pessoa_04.setdefault('nome', 'Terra') #a chave nome já existe, logo, ele não vai substituir o valor 'nome', nem criar outra, pois já existe.
print(pessoa_04)
# ctrl + D -> seleciona a próxima ocorrencia da palavra selecionada

cls()   
#Shallow Copy (cópia rasa) vs deepcopy (cópia profunda)
#ainda continuação de métodos em dicionário 

d1 = {
    'c1':1,
    'c2':2,
    'c3':3,
}
print(d1)
d2 = d1 #é imaginável que quando alguém faz isso, o intito dessa pessoa seria realizar uma cópia do outro dicionário, né?
#no entanto, temos que lembrar que dicionário é um tipo mutável, assim como uma lista.
#e por esse motivo, d2 = d1 desse modo faz com que d2 aponte para o mesmo lugar na memória que d1, logo, se eu fizer uma alteração em d2 ou em d1, ambas variáveis estarão sendo alteradas.
#Logo, infere-se que o que fizemos acima não passa de atribuições simples, onde um dicionário recebe o outro e aponta pra o mesmo local na memória. 
 
d1['c1'] = 3  #alterando o valor de apenas uma em cada
d2['c2'] = 6
print(f'\n{d1}, \n\n {d2}') #percebe que por mais que em tese, tenhamos alterado apenas uma, mas as duas foram alteradas? logo, a cópia que você queria não foi realizada.

#como fazer a cópia da forma correta?
#Utilizando Shallow copy, isso é possível. 

d3 = {
    'c1':1,
    'c2':2,
    'c3':3,
    'lista': [10, 20, 30]
}
d4 = d3.copy() #esse copy realiza uma cópia de d3. 
d3['c1'] = 3  #alterando o valor de apenas uma em cada
d4['c2'] = 6
print(f'\n\n\n{d3}, \n\n {d4}') #e como pode ver, alterou apenas um valor em cada dicionário
#no entanto, shallow copy não passa de uma cópia rasa, ou seja, se houvesse um dicionário dentro do dicionário ou até mesmo uma lista, essa lista e/ou 
# dicionário não seria copiado, e a mesma situação do caso acima iria ocorrer, linkando apenas essa lista no dicionário original e copiando o resto. 
#resumo: shallow copy copia apenas dados imutáveis. Dados mutáveis serão direcionados a mesma posição na memória do dicionário original.

d3['lista'][0] = 45
print(f'\n\n\n{d3}, \n\n {d4}') #como pode ver, foi alterada em ambos
#caso você realmente queira fazer uma cópia de dados mutáveis e imutáveis, basta utilizar a biblioteca deepcopy

from copy import deepcopy #de toda biblioteca copy, quero apenas deepcopy (cópia profunda)
d5 = {
    'c1':1,
    'c2':2,
    'c3':3,
    'lista': [10, 20, 30]
}
d6 = deepcopy(d5) #agora, ele fará uma cópia de dados mutáveis e imutáveis.  
d5['lista'][0] = 1000
d5['c1'] = 3  #alterando o valor de apenas uma em cada
d6['c2'] = 6
print(f'\n\n\n{d5}, \n\n {d6}') #como pode ver, apenas um elemento em uma das na lista foi alterado
cls()
#uso do get
#o get vai realizar a busca de uma chave dentro do dicionário. 


# Se essa chave realmente estiver presente no dicionário, ele retornará o nome da chave.
# caso essa chave não esteja no dicionário, ele simplemente vai retornar None
pessoa_05 = {
    'nome': 'carmita',
    'sobrenome': 'brandão',
}
print(pessoa_05.get('nome')) #como a chave nome existe em pessoa_05, será retornado 'nome'
#nome
print(pessoa_05.get('profissão')) #como profissão não existe no dicionário pessoa_05, será retornado None
#None
print(pessoa_05.get('profissão', 'não existe')) #também posso colocar um valor padrão caso a chave não seja encontrada

#posso utilizar para fazer uma verificação da presença de uma chave num dicionário:
if pessoa_05.get('profissão') is None:
    print('essa chave não tem no dicionário') #como não tem, vai executar isso aqui
if pessoa_05.get('nome'): #como tem, vai executar normalmente a condição
    print('essa chave tem no dicionário')

#uso do pop
print(pessoa_05) #aparece as chaves e valores
pessoa_05.pop('sobrenome') #remove a chave 'sobrenome' do dicionário pessoa_05
#se a chave não for encontrada no pop, vai dar erro de keyerror
print(pessoa_05) #aparece apenas o nome e seu valor, pois pop removeu a chave "sobrenome" com seu atributo.
#popitem -> remover a última chave do dicionário
pessoa_05['idade'] = 10 #incremeto mais uma chave
pessoa_05['peso'] = 99.9 #incremeto mais uma chave
print(pessoa_05) 
pessoa_05.popitem() #removo a última chave do docionário, que no caso foi peso. 
#se o dicionário estiver vazio, vai dar pau
#não posso passar uma chave dentro dos (), caso contrário, vai gerar erro de TypeError

print(pessoa_05) #como pode ver, peso, que é a última chave, foi removida

#oq eu posso fazer com popitem tbm é adicionar a última chave com seu atributo numa variável
ultima_chave = pessoa_05.popitem()
print('\n\n',ultima_chave) #como pode ver, a chave e o atributo ficaram armazenados aqui
print(pessoa_05) #mas mesmo assim, a última chave foi removida do dicionário

cls()
#uso do update
pessoa_06 = {
    'nome':'Carlos'
}
print(pessoa_06)#como pode ver, tem apenas a chave nome e seu atributo carlos

pessoa_06.update({ #o update serve para fazer atualizações no código. 
    'nome':'João',  #eu posso fazer uma alteração de valor para uma chave
    'sobrenome': 'Terramota', #também posso criar uma chave e um valor
})
print(pessoa_06) #veja a atualização da chave nome e o incremento da chave sobrenome
#mais uma forma de fazer um update 
pessoa_06.update(nome='Carlão') #outra forma de fazer um update com argumento nomeado
pessoa_06.update(sexo='M') #como esperado, também posso criar uma chave assim.

print(pessoa_06) #veja a alteração no valor da chave nome e a criação da chave sexo

pessoa_06.update(nome='Maria', sexo='F') #posso fazer tudo isso em uma linha tbm
print(pessoa_06)

#mais outra forma de fazer um update
update_variavel = (('nome', 'Juliano'), ('nacionalidade', 'brasileiro')) 
#o método acima cria uma variável denominada update, que recebe uma tupla.
#nessa tupla, é necessário colocar outra tupla dentro, e dentro dessa outra, você cria ou modifica o valor da chave
#após fazer a modificação, é necessário colocar uma vírgula, mesmo que você não faça uma segunda alteração, É NECESSÁRIO!!!!!!!!!!!
#caso quera fazer uma outra alteração depois da vírgula para indicar que é uma tupla aninhada,  basta colocar uma outra tupla () e dentro dela, fazer a modificação.
#No caso de haver dois elementos ou mais modificados, não precisará adicionar a vírgula após a última modificação.
#vou fazer uma demonstração do erro

try:
    update2 = (('nome', 'João'))
    pessoa_06.update(update2) #não irei explicar aqui, pois vai dar erro, devido a ausência da vírgula

except ValueError:
    print('como pode ver, deu pau') #ValueError

pessoa_06.update(update_variavel) #aqui, no caso, eu chamo update e coloco para ele receber update_variável.
print(pessoa_06) #logo, as mudanças serão exibidas aqui

#se eu não precisar de variável, posso fazer direto, veja:
pessoa_06.update((('nome', 'Marin'),)) #é a mesma lógica do exemplo feito com variáveis
print(pessoa_06)

#também posso fazer isso com lista, no entanto, vou fazer direto.
pessoa_06.update([['nome', 'Otávio'], ])
print(pessoa_06) #podo pode ver, funcionou perfeitamente!
cls()




# isdigit() - retorna true para números inteiros e alguns especiais, como expoentes
print("123".isdigit())  # True
print("²".isdigit())  # True (porque é um dígito especial)

#isdecimal - só retorna true para caracteres compostas por inteiros decimais.
print("123".isdecimal())  # True
print("3.14".isdecimal())  # False (tem ponto)
print("½".isdecimal())  # False (é um número, mas não decimal puro)

# isnumeric - aceita mais formatos de números, como fração, número romano, etc
print("123".isnumeric())  # True
print("½".isnumeric())  # True (porque aceita frações)

#relembrando método de verificação de int
number = '10'
if number.isdigit():
    print('esse é inteiro')



cls()
# Estrutura de dados Set - Conjuntos em python mutáveis
conjunto_a = set() #como declarar um set
print(conjunto_a, type(conjunto_a)) #como no set não há nada, no print, aparecerá o próprio set


conjunto_b = set('cacete')

print(conjunto_b) #como pode ver, o set vai agir como iterável, no entanto,
# o caso acima tem apenas um argumento, com isso, ele vai transformar o argumento em uma espécie de lista desordenada. 

#logo, vamos enviar de uma forma mais direta:
listaaa = 10, 20, 30, 50 
conjunto_b = set(listaaa) #agora, ele realiza ações com um iterável definido, que no caso, é a lista
print(conjunto_b)

#outra forma de declarar o set:
conjunto_c = {'terra'} #dessa forma, vou colocar o valor terra no conjunto c e com isso, ele não bagunçar o argumento, o transformando em lista desordenada.
print(conjunto_c) 

#atenção!!!!
conjunto_d = {} #quando eu não coloco aspas dentro das chaves, o que ele faz é a criação de uma lista!!
print(type(conjunto_d)) #viu? é uma lista!!

conjunto_d = {''} #logo, eu tenho que colocar aspas (simples ou duplas)
print(type(conjunto_d)) #agora, esse tipo é um set

#set não permite valores mutáveis, ou seja, não posso usar uma lista ou dicionário dentro do set.
#se eu tentar usar uma lista ou chave, vai exibir um erro de typeError
#a tupla funcionaria, no entanto, precisará de uma vírgula no final, parecido com o update em tupla ou lista mesmo. 
#logo, é possível deduzir que os set não tem índexes  

#se você coloca um valor duplicado num set, por padrão, o set irá eliminar.
conjunto_e = {1,2,3,4,4,4,5,5,6,7,4,4,5,6,4,}
print(conjunto_e) #como pode ver, eliminou por padrão.

#logo, se eu tiver uma lista e queira remover valores duplicados, posso fazer isso:
lista_a = [10, 10, 10, 40]
print(lista_a)
remover_duplicados = set(lista_a) #converto de lista para set, logo, será removido os duplicados.
print(remover_duplicados)
voltar_para_list = list(remover_duplicados) #aqui eu converto de set para list denovo
print(voltar_para_list)#como pode ver, tudo certo até aqui
#NO ENTANTO, LEMBRE-SE QUE O SET PODE DEIXAR A LISTA FORA DE ORDEM.

cls()
#sem o set, teríamos que fazer uma função para remover os valores duplicados, veja abaixo:
valores = [10, 10, 3, 1, 10, 10]
def apagar_duplicados(valor, lista): #valor = valor a ser removido; lista = sequencia a ser iterada
    for ___ in lista: 
        if valor in lista and lista.count(valor) > 1:
            del lista[lista.index(valor)]

print(valores) #antes de apagar
apagar_duplicados(10, valores) #apagando
print(valores) #depois de apagar

cls()
# métodos úteis para set
# add, update, clear, discard
s1 = set()#aqui temos um set vazio, novamente
s1.add ('fds') #como pode ver, add serve para adicionar um valor no set
print(s1)
s1.update('poxa') #como pode ver, o poxa foi descompactado de forma desordenada. Caso não queira que isso ocorra,
#basta colocar ele dentro de uma tupla ou lista.
print(s1)
s1.update(['poxa', 'slk']) #como pode ver, o poxa foi compactado e normal, juntamente com slk
print(s1)
s1.discard('poxao') #vai fazer uma busca direta por um valor e vai apagar.
#se o valor não existir, a ide vai ignorar, apenas. No entanto, é bom evitar.
print(s1)#poxa foi eliminado

s1.clear()#vai limpar o set
print(s1)

#operadores importantes para o tipo set
s1 = {1,2,3}
s2 = {2,3,4}

#união - vai unir dois conjuntos
print(s1.union(s2)) #como pode ver, houve uma união, não havendo duplicação
print(s1 | s2) #outra forma de fazer a união

#intercessão - faz uma busca e retorna itens presentes em ambas os set (conjuntos)
print(s1.intersection(s2))
print(s1 & s2) #outra forma de fazer a intercessão

#diferença - vai retornar os elementos da esquerda que tem apenas no da direita
print(s2 - s1) #retorna apenas o 4
print(s1 - s2) #retorna apenas o 1 
print(s1.difference(s2)) #outra forma de fazer

#diferença simétrica - os itens que não estão presentes em ambos, ignorando a ordem:
print(s1 ^ s2) #retornará o 1 e o 4 (é como se fosse a intercessão)
print(s1.symmetric_difference(s2)) #outra forma de fazer

#exemplificação do uso do set:
#verificação dos digitos do user 
verifi = set()
while True:
    verifi.add('aaa')#(input('digite algo '))
    print(verifi) #ele digitando num ou não, se ele repetir, o set desconsidera. 
    #se eu tivesse usando uma lista ou tupla, todas as repetições seria consideradas, ou seja, estaria cheio de 'a' desnecessário, por exemplo.
    break
#ordenação
lista_desordenada = [4,7, 4,5,6,8,2]
print(lista_desordenada)
lista_desordenada.sort() #o método sorte vai ordenar a lista
print(lista_desordenada)
print(sorted([4,7,1,2,3,8,9])) #outra forma de ordenar a lista
lista_desordenada.sort(reverse=True) # a lista de trás para frente
print(lista_desordenada)

#o sorted também funciona para ordenar letras. 
carro = 'jao', 'ana','Ana', 'João' ,'carla', 'bruna', 'juliana'
#detalhe: o python utiliza a tabela unicode para fazer a oranização. é tanto que quando você colocou uma letra maiúscula no inicio de uma palavra, ela passou para frente.
carro = sorted(carro)
print(carro)

#função lambda
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#organizar uma sequencia de dict em um array de forma alfabética, utilizando o nome como referência:
def ordenacao(chave):
    return chave['nome'] #defino uma função retornando a chave do dict

lista.sort(key=ordenacao) #utilizo o método sort para ordenar, e como parametro, chamo key passando a função ordenacao
print(lista) #aqui já vai esta ordenado.
for fds in lista: print(fds) #para visualizar melhor, utilizo o for.

# O parâmetro key serve para que você passe uma função (seja definida com def ou com lambda) que extrai um valor de cada elemento da sequência. Esse valor extraído é então usado pelo método sort() (ou pela função sorted())
#  para comparar os elementos durante a ordenação. 
# No exemplo citado, a função pega o valor associado à chave 'nome' de cada dicionário e utiliza esse valor para definir a ordem

cls()
#como pode ver, no caso acima,precisamos fazer o uso de uma função, que no caso, foi a função ordenar.
lista2 = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
#como tal função utilizou apenas uma linha, poderá ser substituido do lambda. Veja a seguir:
for lista_sem_ordem in lista2: print(lista_sem_ordem) #veja a lista desordenada

#uso do lambda
lista2.sort(key=lambda chave:chave['nome']) #como pode ver, eu apenas substituir a função def por lambda, que também é uma função
for haha in lista2: print(haha) #aqui é para ter uma visualização melhor

#criacao de lambda 
lambda_soma = lambda a,b:a+b
#a definição da variável acima, armazenando um lambda é uma forma de fazer uso do lambda
#No entanto, segundo a Pep8, é uma má prática de programação
print(lambda_soma(10, 20))
#acima, você vai obter o resultado da soma entre a e b

#Outra forma
def executa(funcao, *args): #parametro funcao irá receber o nome da função a ser executada, enquanto args, receberá os argumentos da respectiva.
    return funcao(*args) 
#no caso acima, definimos uma função denominada de executa. O intuito dela é executar outras funções.

print(executa(lambda a,b:a+b, 10, 20))
#o código acima trás um print da execução do lambda, realizando a soma e seguindo as recomendações da pep8

multiplicador = executa( 

    lambda m: lambda n: n*m, 3
    #n vem de número, enquanto m vem de multiplicador. 
    #no caso acima, temos uma função dentro de outra função.
    #m solicita um argumento para seu paramentro, enquanto cria a subfunção n.
    #m deve receber um argumento de imediato, que no caso, é 3. Enquanto N deve ser definido na chamada da função.

)
print(multiplicador(5)) #5 é o valor de n, logo ele fará n*m, sendo n=5 e m=3
#caso ainda não tenha entendido, vamos fazer manualmente com uma def.]

#seguindo a mesma lógica da anterior
def criar_multiplicador(multiplicador): #aqui eu crio m, junto com um parâmetro 
    def numero(multiplicando): #aqui eu crio a função n dentro de m
        return multiplicador * multiplicando #aqui eu realizo a multiplicação
    return numero #aqui eu retoro m, para acessar n. 
print(executa(criar_multiplicador(5), 3)) #percebe-se que eu também faço uso do executa, e dentro dele faço a chamada da função, por meio de m.
#logo, passo um argumento para n(5), e logo após, passo uma vírgula e passo um argumento para m(3), realizando assim a multiplicação

#também posso utilizar args no lambda, veja:
print(executa(lambda *args:sum(args), 1,2,3,4,5,6))

#Relembrando empacotamento e desempacotamento:
a, b = 1,2 #nesse caso, 1 e 2 faz parte de uma tupla e eu estou o desempacotando e armazenando separadamente em a e b.
print(a, b)
#demonstracao mais visivel:
tupla = (1,2,3)
a,b,c = tupla
print(c) #por debaixo dos panos, é do jeito acima que funciona as coisas. 

##dicionario
dici = {
    'nome':'João',
    'sobrenome':'Costa'
}
print(*dici)#para desempacotar o dicionário, basta colocar o * antes.
#outra forma:
a,b = dici
print(a, b) #agora, eu desempacoto e armazeno na variável a e b o nome das chaves.
#desempacotar valores:
a,b = dici.values()
print(a, b) #como pode ver, foi desempacotado e armazenado apenas os valores.
#desempacotar chaves e valores:
a,b = dici.items()
print(a,b) #como pode ver, temos dois valores armazenados e a e mais dois armazenados em b, formando assim duas tuplas.
#subdividir as tuplas:
(a1, a2), b = dici.items()
print(a1, a2, b) #como pode ver, criei mais duas variáveis (a1 e a2) para desempacotar a tupla que estava presente em 'a'
#posso fazer a subdivisão simultaneamente também:
(a1, a2), (b1,b2) = dici.items()
print(a1, a2, b1, b2) 
#o nome da prática acima é desempacotamento interno, que pode ser utilizado quando há um valor dentro do outro, onde os () são essenciais.
#outro lugar que percebemos o desempacotamento interno e também poderemos usar, é em um for, veja a seguir
cls()
for chave ,valor in dici.items(): print(chave, valor) #se eu tivesse apenas um valor no for, iria retornar uma tupla, veja o exemplo:
for dicionary in dici.items(): print(dicionary) #retornou duas tuplas.

#logo, percemenos o quanto o desempacotamento interno é importante 
dici = {
    'nome':'João',
    'sobrenome':'Costa'
} #vou repetir o dici para deixar mais próximo do código abaixo que irei adicionar agora.

dici2 = {
    'idade':17, 
    'sexo':'M',
}
cls()
#caso você queira unir os dados de um dicionário com os dados de outro dicionário, veja a seguir:
dici3 = {**dici, **dici2} #para extrair os dados de um dicionário, basta utilizar dois * e logo após inserir o nome dele.
print(dici3)

#uso do kwargs
#lembrando que args empacota argumentos não-nomeados
#KWARGS irá empacotar os argumentos noemados



def teste(*args, **kwargs): #quando eu for fazer uso do kwargs, devo colocar dois ** antes do respectivo. 
    print(kwargs) #observe que args não foi utlizado e é diferente de kwargs. 
    if args:
        print('aqui é os args')
    # for chave, valor in kwargs.items():print(chave, valor) se eu quisesse fazer um for com o desempacotamento para dois valores, também daria certo
    
teste() #não fiz a inserção de dados algum e percebe-se que ele mesmo assim printou, e printou um dicionário vazio.
teste(terra='xablau',) #agora, fiz a definição de um argumento nomeado recebendo um valor. Para Kwargs, isso vai ocasionar em um dicionário, onde há chave (key) e valor (value)
teste('akakakak') #esse aqui e para você perceber que os valores armazenados em args são diferentes dos armazenados em kwargs



lista = {
    'name':'Peste',
    'sobrenome':'caramba',
}

teste(**lista) #lembrando que para extrair um dicionário, basta utilizar dois ** antes do dicionário. O mesmo serve para colocar ele dentro de uma função ;)

##########################################
#list comprehension
#como eu faria a adição de números em uma lista?
lista_vazia = []
for __ in range(10):
    lista_vazia.append(__)
print(lista_vazia)
#o método acima é a forma que com o seu conhecimento atual, você provavelmente faria. 

#outra forma:
print(list(range(10)))
#o método acima é mais prático, utiliza de outros meios, porém chegará ao mesmo resultado de forma mais econônima, no quesito memória.

#no entando, e se eu quiser colocar alguma condição ou ação, como multiplicação por dois ou algo assim? o método acima não iria solucionar, então eu teria que utilizar o antecessor dele? poderia, mas tem um jeito mais prático!
lista_vazia2 = [analisando for analisando in range(10)] 
print(lista_vazia2)
#o caso acima também utiliza outros meios para chegar nos resultados anteriores. Mas e a dúvida em questão?
lista_vazia3 = [multi *2 for multi in range(10)]
print(lista_vazia3)
#agora, você percebe que no caso desse método, você pode colocar ações por fora, como multiplicar por 2.
#E esse aí é um list comprehension, composto por:
#variável = [nome_da_lista * ação for nome_da_lista in intervalo]
cls()

# mapeamento é equivalente a percorrrer uma lista, possivelmente fazendo alguma alteração e colocando os respectivos em outra lista, tendo o mesmo tamanho para ambas len(lista1) == len(lista2)
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },#aqui eu tenho uma lista
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [produto for produto in produtos] #aqui eu tenho o mapeamento da lista anterior   
print(*novos_produtos, sep='\n') #lembrando que o for faz uma iteração em cada elemento da lista 

novos_produtos = [produto['nome'] for produto in produtos]
print(novos_produtos) #considerando o que eu falei que o for vai iterar, quando o for iterou pelo índice 0 da lista produtos,
# perecebeu a presença de um dicionário, logo, o incorporou em produto. Ademais, produto havia uma filtragem, que era ['nome], logo, ele filtrou apenas pelo nome.

novos_produtos = [{'nome': produto['nome'], 'preco':produto['preco']} for produto in produtos]
print(*novos_produtos, sep='\n') #antes do for, há uma criacao de um dicionário novo. Apesar das chaves serem idênticas ao dicionário produtos, não deixe se enganar.
# Mas o dicionário produtos também é acessado, isso ocorre na parte que coloquei produto['nome'], nessa parte, estou acessando o outo dicionário. 
#O que foi feito ai em cima foi criar um dicionário com os mesmos valores e chaves do dicionário produtos.
# é quase a mesma coisa que fazer:


dicidici = [{**produto} for produto in produtos]
print(*dicidici, sep='\n') #antes do for eu faço a extração dos itens do dicionário produtos, armazenando-o em produto. 
##posso fazer modificações também, veja:

novo_preco = [{'nome':produto['nome'], 'preco':produto['preco']*2} for produto in produtos]
print(*novo_preco, sep='\n') #como pode ver, multipliquei o valor por dois

#consigo fazer modificações se uma condição for atendida, através de um if ternário
maior_que_20 = [{'nome':produto['nome'], 'preco':produto['preco'] *2 if produto['preco'] > 20 else produto['preco']} for produto in produtos]
print(*maior_que_20, sep='\n')

#uso do filtro no list comprehension:
#para facilitar a sua compreensão, lembre-se que o que vem na esquerda do for, é mapeamento e a direita, é filtro.
# varivael = [valor * ação if valor operação condição for valor in intervalo if valor operação ação]ex:
cls()
#caso queira consultar, a aula foi 138
listagem = [n * 2 if n == 7 else n for n in range(10) if n <8]
#no caso acima, o que vem depos do for, é um filtro. Diferentemente do if ternário no mapeamento, ele não precisa de else. 
print(listagem)

#é possível fazer um for dentro do outro em uma list comprehension
#por exemplo:
listagem = []
for x in range(3):#isso é um for aninhado (um for dentro do outro)
    for y in range(3):
        listagem.append((x, y))
print(listagem) #nesse caso aq, coloquei um for dentro do outro, sendo que quando o x executar uma vez, o y executará 3 vezes, sendo 3x3 = 9 execuções, sendo adicionadas na listagem

#para fazer diretamente num list comprehension, basta:
listagem_lista = [(x, y) for x in range(3) for y in range(3)]
print(listagem_lista)#como pode ver, agora há um for dentro do outro sendo executado perfeitamente. 
# sendo listagem_lista o nome da lista
# (x, y) é uma tupla, já que são dois valores. Ex: n1, n2 = 10, 20
# for x in range é o que vai ser armazenado em x, onde range é o intervalo.
# a mesma logica para y

#detalhe, se eu colocasse um z na tupla, ficando (x, y, z) e após o y colocasse outro for, iria funcionar perfeitamente, sem limitações. 

cls()
nomes = ['João', 'Marcos', 'Pedro', 'Luiz']
novos_nomes = [nome.lower() for nome in nomes]
print(novos_nomes)

kk = (nomes[0]).lower()
ultimate = []
for _ in kk: ultimate.append(_)
print(ultimate)
ultimate.pop()

ultimate.append(kk[-1].upper())
print(ultimate)

testefds = 'Terra'
testehaha = [nome.upper() if testefds[-1] == nome else nome.lower() for nome in testefds]
print(testehaha)

cls()

#como deixar todas as letras de um list comprehension com um title invertido:
maisteste = ['Joao', 'Carlos']
vamos_la = [f'{nome[:-1].lower()}{nome[-1].upper()}' for nome in maisteste]
print(vamos_la) #como pode ver, a última letra está maiúscula

#mil linhas de código!!!
#dicionário comprehension:
produtooo = {
    'nome':'Caneta Azul', 
    'preco':2.5,
    'categoria':'escritório'
}

dc = {chave: valor for chave, valor in produtooo.items()} #acabei de realizar uma cópia do dicionário anterior através de um dicionary comprehension
print(dc)
dc = {chave: valor for chave, valor in produtooo.items() if chave == 'nome'} #como o list comprehension, também consigo fazer uso do filter
print(dc)
dc = {chave: valor*10 if isinstance(valor, float) else valor // 10 for chave, valor in produtooo.items() if chave == 'preco'} #como esperado, também consigo fazer uso do if ternário
#além disso, temos o uso do ininstance, que possui dois parâmetros, sendo útil para verificar se uma variável tal pertence ao tipo primitivo respectivo, veja a declaração a seguir:
# isinstance(variavel, tipo_primitivo) #retorna true ou else
#caso você queira verificar se o valor tal é de dois tipos primitivos, basta:
terra = 10
print(isinstance(terra, (float, int))) #agora, se a variável terra for float ou int, ele vai retornar true
print(dc)
#conversão para tipo dict
listaB = [
    ('a', 'peste'),
    ('b', 'caramba'),
]
# posso fazer:
listaC = {chave:valor for chave, valor in listaB}
print(listaC)
# ou
print(dict(listaB))

#set comprehension
s1 = {aleatorio * 2 if aleatorio >= 8 else aleatorio for aleatorio in range(10) if aleatorio > 4}
#como pode ver, também é possível usar if ternário e filter no set comprehension
print(s1)
cls()

#valores thuthy e falsy 
#abaixo estará uma sequencia de tipos de dados
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)
#quando você declara uma variável e define seu tipo de dado, a depender do valor que você informar, este poderá ser Truthy ou Falsy
# No caso, quando o valor que você declara for vazio, automaticamente, ele se tornará um falsy. Por exemplo:
#None é um não valor, ou seja, não tem valor. Logo, também é falsy
print(lista, dicionario, tupla) #todos eles são valores vazios, logo, serão falsy
###
inteiro = 1
flutuante = 1.5
print(inteito, flutuante) #estes tem valores, logo, é considerado truthy
cls()


#verificações de métodos
#uso do dir, hasattr e getattr em python

#corriqueiramente você vai querer fazer uso dos métodos em uma string ou algum tipo de dado correlacionado.
# Para isso, você pode fazer uso do dir. Por exemplo, você primeiramente executa o debugger e após passar pela string desejada, abre o console do debugger e utiliza o seguinte comando:
# dir(string)
#logo, será printado os métodos possíveis para utilização naquela string.

#######outra forma
# hasattr
# hasattr tem dois parametros, onde um você informa a variável respectiva e no seguindo, verifica se o método existe para ele. Por exemplo:
terracota = 'joão grilo'
maiusculo = 'upper'
print(hasattr(terracota, 'upper')) #como pode ver, o método upper pode ser utilizado na variável terracota.
#no caso dp hasattr, ele apenas vai informar True ou false
###
# getattr faz a mesma coisa, no entanto
print(getattr(terracota,maiusculo)) #ele verifica se é possível e logo após vai vai buscar na memória a alocação do método respectivo
#caso o getattr não encontre o método rspectivo, o código quebra. Logo, você tem que usar com cuidado.
#além disso, como o getattr já sabe onde o método respectivo está alocado na memória, se você coloca um parênteses, o getattr faz a execução do método.
print(terracota) #antes
print(getattr(terracota, maiusculo)()) #depois
#mas por que eu deveria fazer uso do getattr para executar? não seria mais fácil eu pegar a variável e colocar diferetamente:
# terracota.maiusculo() --> Não. Do jeito digitado ao lado não iria funcionar. 

#####aula 145, do livro padrões de projeto
#generator expression, iterables e iterators em python

#DUCK TYPING -> TIPAGEM DO PATO - SE NADA COMO UM PATO E FAZ QUA QUA COMO UM PATO, ENTÃO É UM PATO.
#OU SEJA, SE TEM INTER E NEXT, EU NÃO PRECISO DO MÉTODO DUNDER (.__iter__, .__next__) E SIM, UMA FUNÇÃO, TIPO iter() OU next()
#lembrando que dunder methods - métodos que iniciam com dois __ e termina com dois __
#no exemplo de iterator farei uso de um dunder e posteriormente de uma função para iterator.

#qual a difrença entre o iterável e o iterator? 
lista = ['caceta', 'terracota', 'marcos']


#o iterável tem a responsabilidade de percorrer uma lista individualmente, sabendo quem é início, meio e fim e ao chegar no fim, parar. Ex:
for __ in lista: print(__) #pecorreu a lista de início a fim sozinho.
##
#Já o iterator lhe fornece um valor por vez, não sabendo quem é início, meio e fim, apenas o próximo valor. Ademais, para percorrer a lista, tem que fazer manualmente. Ex: 
segunda_lista = lista.__iter__() #denomino uma nova variáel que vai ter como referência a lista principal
#no entando, nessa nova lista não é possível saber o seu tamanho, selecionar por índices ou realizar coisas do tipo
try:
    len(segunda_lista)
except TypeError:
    print('como viu, deu pau.') 

#mas e para iterar nessa lista? simples, basta usar o next.
print(next(segunda_lista)) #temos apenas o primeiro valor. Para obter os demais, precisamos também do next, pois como eu disse, é manualmente 
print(next(segunda_lista)) #segundo valor da lista
#detalhe importante: o valor anterior, presente no primeiro next já não existe mais na lista 'segunda_lista'. é como se ele tivesse utilizado um pop inverso ou um del no índice 0.
print(next(segunda_lista)) #aqui chegamos ao final da lista. 
#como já chegamos ao final, caso eu faça uso do next novamente, o código quebra. Veja:
try:
    print(next(segunda_lista))
except StopIteration:
    print('como viu, a lista "segunda lista se esgotou e deu pau. "')

cls()
# Generetor expression -> funções que sabem pausar
from sys import getsizeof #o módulo sys possui uma função chamada getsizeof para saber o tamanho de um código em bytes.

#o generetor é similar ao iterator no python. Por exemplo:
primeira_lista = [n for n in range(101)] #com esse list comprehension, vou gerar, números de 0 até 100
print(primeira_lista) 
#mas, esses valores foram gerados de uma só vez e inclusive, já estão salvos na memória, ocupando espaço de uma só vez.
# normalmente você não vai utilizar todos esses valores de uma só vez, logo, poderia enconomizar espaço.
#veja quanto isso ocupa:
print(getsizeof(primeira_lista)) #920 bytes, e se houvesse mais valores, pesaria mais.
##
#mas, e como eu faço um generator? simples, vou fazer isso em um list comprehension para você ver a diferença
segunda_lista = (n for n in range(101)) #também vou gerar valores de 0 a 101, no entanto
print(segunda_lista) #<generator object <genexpr> at 0x0000029877A5D0C0> apareceu isso na tela. E os meus valores?
#então, como eu disse, o generator é similar ao iterator, logo vai iterar individualmente e manualmente pela lista, através da função next ou método next, veja:
print(segunda_lista.__next__())  #agora, apareceu o primeiro valor.
print(next(segunda_lista)) #e agora o segundo valor.
#ou seja, sempre que você precisar do próximo valor, basta utilizar a função ou método next. Mas lembre-se, a lista não tem tamanho, índice e nem nada do tipo, como o próprio iterator.
#e o mais importante de tudo: quanto pesa?
print(getsizeof(segunda_lista)) #pesa apenas 192 bytes.
#caso eu queira todos eles de uma vez, basta eu fazer um iterável:
for n in segunda_lista:
    print(n) #agora terei os valores do dois em diante, até o iterável esgotar!
cls()
#uma ganerator function também é possível ser criada através de uma função, que na verdade, é a forma como ela funciona por debaixo dos panos
#crio uma funcão denominada generator
def generator(n=0):
    #sabemos que return é o fim para uma função, correto? ou seja, por mais que haja algum código no escopo da função após o return ser chamado, esse código será pylance, ou seja, inalcançável. 
    #nesse caso, após o return ser executado, a função finaliza sua execução. No entanto, queremos pausar, como o generator.
    #Para isso, utilizamos o yield e apó ele, informamos um valor. 
    yield 1
    print('opa') #a execução do código só vai parar quando encontrar o próximo yield
    #toda função, se houver yield, se torna uma generator function (função geradora)
    yield 2
    #podemos fazer isso quantas vezes quisermos. A partir de agora, essa função se torna uma generator function
    yield 3
    return 'se lascou' #esse return só vai acompanhar o erro StopIteration (se lascou virá depois de StopInteraion para informar que a geradora foi esgotada.) 
    print('olá') #é um pylance

gen = generator(n=0) #com isso, basta denominar uma variável que vai fazer o armazenamento (esse aqui seria tipo a função iter())
print(next(gen)) #e agora, podemos fazer o next
print(next(gen))
#como é uma função presente em um def, eu posso reutilizar novamente em outra chamada, por exemplo:
print(next(generator())) #começou do 0 de novo. E foi por isso que eu precisei de uma variável por fora para continuar.
#também posso fazer com for e no diretação:
for n in generator():print(n) #como viu, funcionou certinho.
#vamos agora fazer um exemplo para uma utilização prática:
#vamos supor que por algum motivo eu queira fazer um range sem utilizar a função range, que no caso é:
for aa in range(10): print(aa)

#vamos fazer algo parecido com oq acabamos de aprender:
def intervalo(inicio=0, maximum=10): #definimos os parâmtros de iniício e fim na função
    while inicio < maximum: #criamos um while para o código sempre executar com base em uma condição
        yield inicio #fazemos uso do yield para pausar 
        inicio +=1 #incremetamos valores para que o início seja crescente.
iterator = intervalo(maximum=1000) #defino uma variável para armazenar uma lista (é tipo a função iter())

for n in iterator: #fazemos o for para executar de uma só fez. 
    #lembrando que as pausas são consideradas, porém é como se o for estivesse fazendo next várias vezes
    print(next(iterator))

### yield from
#aula 148 para mais detalhes
#caso eu tenha duas funções geradoras complementares, para que isso funcione de forma simplificada, basta usar yield from, veja a seguir:

def gen1():
    yield 1
    yield 2
    yield 3
def gen2():
    yield from gen1() # fazendo uso do from, a primeira coisa que faço é apontar a função geradora anterior.
    yield 4
    yield 5
    yield 6

gen_iter = gen2() #na denominação da variável com o intuito de criar um iter, faço isso com a função geradora complementar (a que tem o from)
print(next(gen_iter))
for __ in gen_iter:
    print(__)
#como pode ver, após executar a primeira função geradora, ele executou a segunda. 
####################################
#tipos de case:
# PascalCase - a cada nova palavra, a inicial é maiuscula
TerraMorta = 0 #declarei uma variável fazendo uso de pascalcase
##

#camelCase - digita a primeira letra minuscula e a inciais de outras palavras maiúsculas
terraMorta = 0
##

#snake_case - a cada palavra digitada, coloca underline para separar
terra_mota = 0
# SCREAMING_SNAKE_CASE - a mesma coisa, porém, é em caixa alta
TERRA_MORTA = 0
##

# #kebak-case - a cada palavra digitada, usa o traço para fazer a separação.
# terra-morta = 0
# # SCREAMING-KEBAK-CASE - a mesma coisa, porém, é em caixa alta
# TERRA-MORTA = 0
# ##
##################################

###########################
#estudo do try, except, else e finally
#o try significa tentar, ou seja, quando chamamos o try e colocamos um código no escopo dele, estamos falando para o try tentar executar o código respectivo.
#o except o tratamento caso encontre algum erro. Por exemplo, se em try houver algum erro no código, através de um except genérico, o erro seria tratado e o programa não quebraria. ex:


try:
    #tente executar o código abaixo, Try
    print(10/0) #não vai dar, pois isso aqui vai gerar um erro de ZeroDivisionError
except:
    #deixa comigo, Try! 
    print('não é possível dividir por 0')
    #como pode ver, o código não quebrou e executou o que há no except

#no entanto, como eu citei no módulo 1 das anotações, utilizar o except dessa forma é uma má prática de programação, indo contra principalmente com o Zenofpython, basta dar um import this no terminal.
#isso é ruim porque o except generalizado vai tratar qualquer tipo de erro, logo, você pode acabar se passando em alguma parte do código e não percebendo onde está errado. 
# Ademais, você também estaria ocultando um possível erro e não o tratando da devida forma. 
# Mas e como eu deveria tratar um erro? simples, basta colocar o nome do erro na chamada do except. veja o exemplo a seguir:

try:
    print(10/0)
except ZeroDivisionError: #como no caso acima o erro é ZeroDivisionError, basta colocar o nome.
    print('não é possível dividir por 0') 
#agora, o try e o except está sendo usado da forma que era pra ser!


#mas e se eu quiser tratar uma sequencia de erros? simples, basta digitar mais de um except! ficando:

try:
    print(kaka/4)
    print(10/0)
except ZeroDivisionError:
    print('não é possível dividir por 0')
except NameError: #quando há a tentativa de utilização de uma variável não declarada, o erro que vai apareer será NameError
    print('variável não declarada')
#nesse caso, o erro que vier primeiro, será tratado

#mas se eu realmente quiser tratar uma sequência? simples, basta colocar uma tupla na hora de indicar o erro.
try:
    print(10/0)
    print('linhaa'[10])
except (ZeroDivisionError, IndexError): #qualquer um dos dois erros que forem verdadeiros, fará com que o except a seguir seja executado.
    print('resolvi tudo! haha')

#mas e se eu quiser saber qual das exceções ocorreu? simples, basta utilizar o as.
# as significa alias, onde irá criar uma variável posteriormente e o que vier anterior a ela, será armazenada.
try:
    print(10/0)
    print('linhaa'[10])
    #lembrando que essa parte é apenas especulação. no momento não entendo nada sobre classes.
    #lembrando que essa parte é apenas especulação. no momento não entendo nada sobre classes.
    #lembrando que essa parte é apenas especulação. no momento não entendo nada sobre classes.
    #lembrando que essa parte é apenas especulação. no momento não entendo nada sobre classes.
except (ZeroDivisionError, IndexError) as cade: #qualquer um dos dois erros que forem verdadeiros, fará com que o except a seguir seja executado.
    #no caso acima, estou fazendo uso do as para armazenar a instancia do erro através de uma nova variável
    print('resolvi tudo! haha')
    print(f'o erro foi: {cade}') #o primeiro erro que deu foi a divisão. agora sabemos.
    #mas tem muito conteudo e eu quero saber apenas o nome do erro, sem os demais elementos.
    #então, eu ainda não sei direito sobre classes, mas aparentemente, except é uma classe e os erros que podem ocorrer fazem parte de sua instância.
    #pra entender melhor, pense em uma variável. Variável aceita vároios tipos de dados, né? tipo str, float, int, bool, etc. os tipos de dados são a instância da variável.
    #agora ficou mais simples de entender? basta imaginar que except é uma variável e imaginar tbm que os tipos de dados são os erros.
    #então, para resolver essa parada, vamos precisar de dois métodos(parece que dentro de uma classe, métodos são chamados de atributos.)
    #os métodos/atributos são __class__ e __name__, ficando:
    print(f'que b.o, mas toma ai essa bomba: {cade.__class__.__name__}')
    #agora temos apenas a informação do b.o que deu primeiro.
    
###
#except exception trata qualquer tipo de erro, sendo a mesma coisa que não indicar nenhum erro
try:
    print(10/0)
    print('4444'.find('aasasasassa'))[0]
except Exception:
    print('tratarei de qualquer b.o!')

#como eu disse, esse Exception ignora qualquer tipo de erro.
####uso do finally
# o finally sempre será executado, independente se ele for adicionado no try ou não.
#o inuito do finally é realizar uma ação em conjunto com o Try. Em outras palavras, o Try vai tentar executar normalmente, vamos pegar o exemplo de uma automação. Ela rodaria normalmente dentro do Try.
#Em uma automação específica, você abre uma série de arquivos. Com isso, ao final dela, você precisa fechar todos.
#Se você fizer o código de fechamento dentro do Try, há uma possibilidade do código quebrar. Logo, os arquivos ficarão em aberto.
#o finally vai previnir que os arquivos fechem. Tipo, ao invés de colocar o código de fechamento no final do Try, você pode colocar no finally, e caso o Try der pau ou não, o fechamento dos arquivos será realizado.

# ex:
def demonstracao(n=0):
    try: 
        print(10/n)
    finally:
        print('com o código quebrando ou não, o que estiver em mim\nprecisará ser executado, sou importante!')
#coloquei em uma função para não me atrapalhar no futuro.
# demonstracao() como pode ver, o código deu pau, mas ele fez oq era pra fazer. Se try funcionasse, ele executaria de boa também.ex:
demonstracao(10)#como viu, o código deu certo, porém o finally também foi executado.

#posso fazer uso do finally com o except também.
try:
    print('aoba')
except Exception:
    print('nesse caso, não vai dar pau')
finally: 
    print('eu sou importante!!')
#como viu, funcionou normalmente!
######### uso do else
#o else é utilizado em conjunto com o except, para se caso não houver erro com o intuito de ser tratado.
# ex:
def veja_por_si_so(n=0):
    try:
        print(10/n)
    except Exception:
        print('deu erro')
    else:
        print('não deu erro')
    finally:
        print('vou ser executado novamente, pois sou importante!!')

veja_por_si_so()#como a divisão é por zero, deu erro aqui. Logo, o else não aparece.
veja_por_si_so(10)#aqui a divisão é por 10, logo, não dará erro e o else será executado no lugar do except
######### relembrando
# laços tem else também

for a in range(10):
    print(a)
else:
    print('fds') #após o for ser executado, executará o else.
i = 1
while i < 10: #enquanto i for menor que 10, o while será executado
    print(i)
    i += 1
else:
    print('acabei') #o else funciona aqui assim também kkkkkkkkkkkkkk, ou seja, após o laço finalizar, o else é executado.

#detalhe: exception é a exceção máxima
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions - hierarquia de exceções

cls()
##########lançando exceções (erros)
#como funcionam as exceções e como fazer a sua própria
#dentro de Exception, do except que vem do try, há um conjunto de classes que são utilizadas para tratar um determinado erro, correto?
# ValueError, TypeError, NameError, etc. Todas essas classes.
#no caso, através do raise, podemos determinar um erro, por mais que ele não seja. Veja abaixo:
# raise - relançar a excessão!

def demonstração():
    print('eae mano, beleza?') #teoricamente não vai dar nenhum erro nessa linha, pois foi digitada corretamente!
    raise ValueError('tá errado, quero saber de nada não!') #no entanto, quando usamos raise, forçamos um erro. Nesse caso, está alegando que o erro é ValueError e apresentando uma legenda.
    print('a partir de agora (já que deu erro), tudo que estiver abaixo de raise, se tornará um pyance')
# demonstracao() #não vou executar para não atrapalhar as anotações no futuro

#mas qual a importância do erro? o erro é necessário que ocorra para que você, programador, saiba o que fazer quando esse erro em específico acontecer. 
#por exemplo, se ZeroDivisionError (n/0) não existisse, o que o python iria fazer? retornar um valor qualquer? retornar zero? um? por isso, ele é importante!
#estamos trabalhando para usuários e não sabemos exatamente o que eles podem digitar. Tem casos que pedimos para colcoar o email e ele coloca o nome dele ou a data de nascimento em um str. E aí? Ter erros é importante.

#vou demonstrar como criar um erro próprio no python. Isso não passará de um exemplo, pois o python já lida com isso sozinho.
def demonstracao_4(n=0):
    armazenamento_nulo = []#vamos supor que isso é um logger, um json ou o próprio cache.
    armazenamento_funcional = [] #este também é um outro logger ou json, pois o programador quer saber se muita gente tenta dividir por 0
    if n == 0: #verifico se n ainda é 0
        armazenamento_nulo.append(n) #salvo no logger
        raise ZeroDivisionError('você não pode dividir por 0') #quebro o código.
    else:
        armazenamento_funcional.append(n) #salvo no logger
        return 10/n #realizo a divisão.
# print(demonstracao_4()) #como você pode ver, acabaei de criar o meu próprio erro. Pois o código quebrou quando n = 0, antes de chegar no 10/n, ou seja, criei meu póprio erro.
print(demonstracao_4(1)) #já aqui deu certo 

#um adendo: Uma função tem o intuto de resolver apenas um problema. Se você tenta resolver dois problemas em apenas uma função, é recomendável que crie outra.
#ademais, se está dificil de dar um nome para sua função, significa que ela está fazendo muita coisa 

#vou fazer mais uma demosntração. Nesse caso, também é redundante, mas para o aprendizado vale a pena
#o intuito também é realizar uma divisão, mas caso o usuário digite um tipo de dado diferente de int ou float, vou fazer dar pau sem precisar dividir nada. Será apenas a verificação.

def verificar_tipo_de_dado(n):
    if not isinstance(n, (int, float)):
        raise TypeError(
            f'"{n}" deve ser int ou float, pois é uma divisão. '
            f'{type(n).__name__} enviado.'
        )

# verificar_tipo_de_dado('a') #como pode ver, ele acusou que a é um str.

################ modulos import, from, as e *
# https://docs.python.org/3/py-modindex.html #módulos python (bibliotecas)
##uso do import completo.
def demonstracao_5():
    import sys 
    print(sys.platform) #o namespace plataform é utilizado para saber qual sistema eu tô.
    sys.exit()#lembrado que o exit vai finalizar a execução do programa
# demonstracao_5()
#o import completo vai fazer com que você tenha acesso as funções do módulo completa. 
#no entanto, não é interessante você fazer isso caso vá precisar  apenas de uma função(namespace) em específico e os nomes ficarão grandes.

##uso do from
#o from é utilizado quando você quer importar alguma parte em específico do módulo. Ex:
from math import ceil, sqrt #importo apenas ceil e sqrt
print(ceil(9.6666666666), sqrt(16)) #arredondo o 9.6 e descubro a raiz quadrada de 16
#o from é útil quando você quer fazer uso de partes específicas do módulo. No entanto, tem que ter cuidado para não definir uma variável com o mesmo nome.
#por exemplo, se eu teho uma variável denominada de ceil e ao mesmo tempo fazer a importação de ceil através do from, como vai ficar? 
#com isso, utilizando o from, você fica sem o namespace do módulo. namespace é o modulo., por ex: math.   o que vem depois é a função.

#com o from, também posso dar apelidos. veja a seguir: (pule para o uso do as logo, pois voc~e vai precisar saber disso para entender.)
from math import ceil as arredondar
#fazendo uso do from e import, importei uma função apenas do módulo ceil e armazenei em uma variável através do as
#posso importar dois ao mesmo tempo e dar apelidos:
from math import ceil as arredondando, sqrt as raiz_quadrada 
#peguei duas funções do módulo math e armazenei em duas variáveis diferentes. 

####uso do as
#como dito anteriormente, o as tem o intuito de pegar o que está à esquerda dele e armazenar em uma variável que virá depois.
#para importação de módulo, isso também funciona. Veja:
# import pandas as pd

#fiz a importação do módulo pandas e o armazenei na variável pd.
# print(pd)

#um detalhe importante é que se eu tentar usar o módulo pd através de "pandas", vai dar pau. Vai falar que pandas não foi definido, ou seja, NameError
#É IMPORTANTE DESTACAR QUE  A PRINCIPAL DESVANTAGEM DE RENOMEAR NOME DE MÓDULO É QUE ELA PODE SAIR DO PADRÃO E DIFICULTAR O ENTENDIMENTO DE OUTROS PROGRAMADORES.

###uso do *
##inicialmente, o * no python também pode significar all, e nesse caso, significa all.

# from os import *
# system('aoba')  
#o * quando utilizado na importação, faz com que todo o módulo seja importado para o escopo principal. 
#para você netender melhor, quando importamos a biblioteca math e queremos utilizar algo de lá, basta:
#math.ceil() #correto?
#seguindo o exemplo acima, bastaria:
# ceil() isso pode ser bom quando utilizado para chamar apenas uma função do módulo, mas no caso do *, chama literalmente todas! podendo ocasionar em um problemas com variáveis, já que não tem o namespace(math.) como proteção.
# e para deixar claro: É UMA MÁ PRÁTICA DE PROGRAMAÇÃO!!!!!!!!!!!!!!
#vou deixar estes comentados, pois podem comprometer as minhas anotações futuramente!

################# uso da modularização e introdução ao packages(pacotes)
#a modularização no python é semelhante a importação de bibliotecas (módulos). Na verdade, é a mesma coisa, a diferença é que a biblioteca que você está importando foi desenvolvida por outra pessoa, enquanto na modularização, a 'biblioteca'(conjunto de códigos) foi desenvolvido por você.
#a modularização é utilizada quando você que organizar melhor o seu cóidigo. Por exemplo, se você tem um código muito extenso, não seria interessante você digitar ele completo em apenas um arquivo.py só.
#no caso dessas anotações, estamos chegando quase a 1500 linhas de códigos, sendo que eu tivesse usado a moduralização, teria mais arquivos, porém seria mais organizado.
#dito isso, vou criar um novo documento py denominado secao_2_modulo.py
#acabei de criar. Agora, vou criar uma variável denominada teste_veja_ai, recebendo 'olá mundo!'
import secao_2_modulo #agora que eu fiz isso, vou importar como se fosse uma biblioteca.
print(secao_2_modulo.teste_veja_ai) #e aqui eu tenho acesso a variável que lá fora criada, como se realmente fosse uma biblioteca.
#vou criar uma outra variavel denominada valor_101, recebendo 10, porém vou utilizar o from dessa vez.
from secao_2_modulo import valor_101
print(valor_101) #como pode ver, segue a mesma lógica da biblioteca.
#também posso utilizar função que lá foram criadas, por exemplo, vou criar uma função de soma no valor de somando_101
print(secao_2_modulo.somando_101(10, 20)) #retornou 30
#e por fim, o código que lá estiver, a partir do momento que eu fizer a execução, será executado imediatamente.
#por exemplo, vou colocar print('olá mundãoooooo!!!!!')
#como pode ver no prompt, foi a primeira coisa que executou depois que o módulo foi importado.

# (se o formato do arquivo é .py, logo, este será um módulo do python)

#ah, mas e se eu quiser ter controle sobre os códigos presentes no módulo? simples, existe um método denominado de __name__, que retornará o nome do módulo que ele se enocntra.
#um detalhe importante é que um conjunto de códigos python é denominado de módulo.
#por exemplo, vou colocar esse método para exibir o módulo que estamos nesse código:
print(f'o módulo aqui é: {__name__}') #retornou __main__, ou seja, esse é o módulo principal.
#mas e se eu colocar no código da importação, como ficaria? lá eu vou definir uma função para que eu execute na linha de baixo.
secao_2_modulo.exibir_modulo() #retornou secao_2_modulo, onde 'secao_2_modulo' é o nome do arquivo. Mas lembra que aqui foi retornado outra coisa? __main__? então.

#dito isso, tem algo importante que você tem que se atentar... quando você for importar um módulo próprio, o módulo deverá ficar no mesmo lugar que se encontra o módulo principal.
#porque se o módulo principal estiver em documents e o módulo que você quer importar estiver na área de trabalho, você vai ter que trabalhar com a biblioteca sys para indicar o caminho (algo bem mais trabalhoso.)
# Ademais, se o módulo que será importado estiver presente em uma sub basta no módulo principal, bastaria você utilizar o from, ficando:
# from nome_da_subpasta import nome_do_modulo
# 
# caso o módulo esteja presente em uma subpasta de outra subpasta do módulo principal, basta navegar como se fossem métodos, ex:
# from sub_pasta_do_modulo.outra_subpasta import modulo 
#resolvido!
#um detalhe importante é que para fazer essas navegações, é que as regras para declaração de nome de variável se aplicam para a pasta, subpasta e módulo, se não, vai dar pau.
#pastas no python são chamadas de pacotes quando você tem módulos(arquivos python) dentro dessas pastas.
#logo, tome cuidado para não colocar nomes que já existem em variáveis ou módulos padrão do python 

#caso realmente seja necessário você importar um módulo da área de trabalho, considerando que o módulo main está em documens, para utilizar a biblioteca sys, através da função .path para indicar o caminho.
from sys import path
print(*path, sep='\n') #aqui vemos todos os caminhos de navegação do código atual
#o que eu precisaria fazer era adicionar o caminho do arquivo no sys e já que ele é uma lista, bastaria colocar um appned.
try:
    path.append("D:\\Ghost\\Usuário\\Desktop\\Mortal Kombat 11.url")#vamos supor q esse caminho é um python. Agora, o python sabe que eu tenho módulo lá também, ou seja, um pacote.
except ModuleNotFoundError:
    print('deu certo n')
print(*path, sep='\n') #agora, se eu quiser acessar de lá, já posso, pois é um caminho reconhecido pelo python.
cls()

##################recarregamento de módulos (aula156)
#por padrão, quando você impaorta um módulo no python, a execução dele será realizada apenas uma vez. Isso é uma característica de instância no python, denominada de singleton (executa apenas uma vez e tchau, mesmo se chamar de novo.) 
#o python executa apenas uma vez por questões de eficiencia no código, pois já pensou se o módulo continuasse rodando em segundo plano, consumindo memória desnecessariamente? então. 
import secao_2_modulo #como pode ver, eu importei novamente a secao_2_modulo, mas não deu em nada. Isso prova o que eui falei acima.
#para recarregar o módulo, famos fazer uso da biblioteca importlib e posteriormente, da função reload, ficando:
import importlib
importlib.reload(secao_2_modulo) #agora secao_modulo_2 será executada novamente
import secao_2_modulo #olá mundãoooo apareceu!
#tal prática não é comumente utilizada, pois é mais prático fazer uso de uma função def!

cls()
###################### revisão rápida e aprofundamento aos packages(pacotes)
#inicialmente, aqui no vscode, temos a possibilidade de criar um arquivo e de criar uma pasta. Corriqueiramente o formato do arquivo será .py e a pasta será nome_do_modulo_package
#como dito antes, para navegar entre os arquivos basta colocar from nome_do_arquivo(peckage) import modulo, correto?
#tem também como fazer:
# import nome_do_arquivo.modulo
# from nome_do_arquivo.nome_da_sub_pasta import modulo 
#from nome_do_arquivo import * #como isso também é um módulo, o * (all) também consegue importar tudo de uma vez. (lembrando que isso é uma má prática)
#ademais, ainda falando do *, há uma variável denominada all, onde o intuito dela é denominar o que pode ser utilizado quando * for definido. ex:

#o código abaixo será incrementado em secao_2_modulo:
# __all__ = [
#     'terra_cota',
#     'bandido'
# ]
# terra_cota = 10
# bandido_caramba = 'safado'
# bomba_do_rato = 20

importlib.reload(secao_2_modulo)
from secao_2_modulo import *

print(terra_cota)
print(bandido_caramba)
# print(bomba_do_rato) #como pode ver, como bomba do rato não estava na lista do all, ele passa a ser desconsiderado, enquanto os outros dois foram executados normalmente!

####################considerações importantes referente a modularização e package
#uma coisa importante para destacar reerente a modularização, é que você pode fazer uma série de importações, resultando em mais de um módulo main.
#como assim? por exemplo, no caso acima fizemos a importação do módulo socao_2_modulo.py, correto? nesse caso, o módulo que estamos agora se tornaria o módulo main em relação a ele.
# No entanto, o secao_2_modulo também pode realizar importações e em relação a importação que ele realizou, ele é o módulo main dela. Lembrando que apenas em relação a ela, pois se for em relação o módulo que estamos escrevendo, esse aqui é o main. 
#Com isso, se o secao_2_modulo também estiver uma importação, nesse código aqui, eu poderia fazer uso de elementos como variáveis, funções, códigos, etc dentro desse módulo que estamos escrevendo. Isso seria tipo uma importação da importação da importação, gerando 3 conexões com 3 módulos distintos, porém na maioria dos casos, na mesma raiz.

#outra coisa a se atentar é que quando fomos realizar uma importação da importação em uma sub  pasta, não podemos colocar diretamente o caminho imaginando que será a mesma coisa. ex:
# modulo_main
# modulo_secundario
# modulo_terciario 

#main importou secundario e secundario importou terciario, interligando todos. Porém, terciario está dentro de uma pasta, logo, caso eu for usar algo de terciário no módulo main, vou precisar navegar certinho, digitando inicialmente from 'nome_da_sub_pasta'.modulo_secundario import modulo_terciario
#como não houve prática, caso tenha ficado alguma dúvida, consultar aula 158

def importar_e_demonstrar():
    ##aula 159
    #mais uma consideração a se fazer, é que quando importamos diretamente uma pasta, não podemos fazer nada com ela, pois ela não passa de uma pasta com o intuito de organizar módulos.
    import pasta_vazia #é tanto que fazendo dessaforma, se torna um pylance, ou seja, algo que não pode ser alcançável
    print(pasta_vazia) 
    #no caso, o package está vazio, no entanto, podemos tornar ele útil para inicialização através do __init__ 
    #dentro da pasta vazia, irei criar um arquivo denominado de __init__.py (tem que ser exatamente dessa forma). Esse init será um arquivo de inicialização, ou seja, assim que eu fizer a importação do package (pasta_vazia), o conteúdo presente no módulo init será executado no mesmo momento.]
    #dentro de init coloquei a função print, imprimindo na tela um olá mundo!
    from importlib import reload
    reload(pasta_vazia) #fiz uso do reload com o intuito de recarregar o package, pois importações são singleton, lembra?

    import pasta_vazia #como pode ver, olá mundo emergiu! 
    #O Otávio chama isso de enganar o python, pois o package normalmente não executa nada, porém através do módulo de iniciação init, é possível fazer com que algo seja realizado após importar o package.

# importar_e_demonstrar()#vou comentar para não haver conflitos

#Ademais, caso eu tenha mais módulos presentes no package pasta_vazia, posso realizar a importação dos respectivos dentro de init, podendo utilizar variáveis, funções e códigos dos outros módulos apenas importando o package. Estamos realmente enganando o python!Haha
#Dentro de pasta_vazia, vou criar um módulo denominado de somando_agora e criar uma função com o intuito de somar a + b
#crio o um arquivo e denomino como: __init__.py
#agora, vou importar o módulo soma para dentro de init, onde init em relação a soma seria o main, ficando: from Scripts.pasta_vazia.somando_agora import RealizandoSoma
# import pasta_vazia
# print(RealizandoSoma)# - impressão = 20

#acima deu 20 pq eu coloquei valores padrão nos parâmetros, sendo cada um 10.

#E nesse caso, o uso do * (all) seria interessante, pois querendo ou não, você importando tudo manualmente através do init iria simplificar o módico.
# onde no módulo realizando a soma ficaria:
# __all__ = [
#     'RealizandoSoma'
# ]
# #isso no topo do código.
# #no init ficaria
# from Scripts.pasta_vazia.somando_agora import *
# #no módulo principal (main) ficaria:
# from pasta_vazia import *
####################################
# uso do round
cara = 1.45765474758965466 #um float gigantesco
print(round(cara, 2)) #round irá arredondar com base no segundo argumento.
# onde: round(referencia, casas) referencia será quem você quer arredondar, e casas será o número de casas que você quer que tenha.
print(round(cara, 1)) #agora tenho até uma casa decimal.
#detalhe: em contas muito específicas, onde há extrema importância de um cálculo exato com todos os decimais, o round não deve ser utilizado, pois o último número decimal é tratado com imprecisão.


#################varivaveis livres e nonlocal
##Variávis livres - fre values
#As variáveis livres normalmente são declaradas em um escopo anterior em relação as próximas funções (função tem escopo diferente)
#Se você consegue acessar uma variável que não foi criada dentro de uma determinada função, e sim em um escopo diferente, significa que essa á uma free value.
#No exemplo abaixo, no escopo fora, foi declarado a variável a, e esta variável foi acessada na subfunção do escopo fora, que no caso, foi dentro. Tendo assim certeza que a é uma free value.
def fora(x=10):
    a = x #definimos a variável a como x neste escopo.
    def dentro():
        print(locals()) #a função local retorna todas as variáveis que são locais presente neste escopo no formato dict
        #caso você queira saber quem são free values presente em uma função, basta digitaro código abaixo:
        print(dentro.__code__.co_freevars)#  print(funcao.__code__co_freevars) 

        return a #no escopo da função dentro, a variável 'a' é considerada uma variável livre.
                #pois apesar de ter sido declarada em outro escopo, ainda foi possível acessar, mesmo que em um escopo diferente de sua atribuição. 
                # free values -> variavel livre
    return dentro
#como isso de trata de um closure, vou precisar de uma variável para executar a função e armazenar seu progresso.
execucao_1 = fora(10) #o valor do parâmetro x agora é 10, porém, a função dentro não será executada.
execucao_2 = fora(20)
print(execucao_1()) #como pode ver, o valor foi imprimido.
print(execucao_2()) 
#ou seja, a variável a realmente é uma free values  

print(globals()) #lista todas as variáveis globais presentes neste código!!

cls()
##uso do NonLocal
#o Nonlocal é um indicador de variável utilizado para informar ao python quando uma variável em específico não pertence aquele escopo, evitando erros. 
#no exemplo abaixo, criarei uma função que realizará uma concatenação e precisará do nonlocal 
def concatenar(string_inicial):
    valor_final = string_inicial #o que o usuário digitar como argumento para a função concatenar, será armazenado em valor_final.
    def interna(valor_a_concatenar): #aqui eu criarei uma subfunção, aplicando os conceitos de high order funcitions e closure.
        ######Se eu continuar dessa forma, dará erro de UnboundLocalError, pois o python buscou a declaração da variável localmente, o que sabemos que não é.
        #para resolver isto, basta informar para ele que a variavel é um nonlocal, sendo:
        nonlocal valor_final
        #agora vou concatenar.
        #como valor_final é uma free value, eu consigo acessar ele estando em um escopo diferente.
        #no entanto, quando vou realizar uma concatenação, o python está definido por padrão que a variável foi definida nesse escopo, fazendo uma busca local por ela, gerando um transtorno.
        #colocarei essa parte em um try para você ver.
        valor_final += valor_a_concatenar
        return valor_final    
    return interna #efetivando assim o closure 
    
c = concatenar('a') #esse será o valor da string inicial, e ao mesmo tempo, do valor final.
print(c('b')) #agora eu executarei a subfunção definindo um argumento para parâmetro valor_a_concatenar
print(c('c')) 

#agora temos o funcionamento correto da função, aprendendo o que é uma free value e nonLocal, sendo
# free value -> variável livre, ou seja, uma variável que pode ser acessada em um subescopo do escopo de sua declaração.
# nonlocal -> não local, ou seja, um indicativo para o python que a variável respectiva não se e encontra no escopo pela qual estão tentando utilizar ela com intuito de modificações.

############################ funções decoradoras (decorations) e decoradores 
## Funções decoradoras -> São funções que decoram outras funções, adicionando elementos, removendo, restringindo ou alterando.
#Funciona a base de closure, pois seu intuito não é executar, é apenas decorar.
#Abaixo, trarei um exemplo real no caso de uma função que inverte strings de trás para frente, mas e se o user digitar números, e aí? vamos utilizar uma função decoradora para verificação e se for, restringir!

def criar_funcao_decoradora(func):
    #vou criar uma função interna para não acabar executando essa função quando eu fizer sua chamada, trabalhando os conceitos de closure.
    def interna(*args):
        print('Vou te decorar agora!!')
        for arg in args:
            is_string(arg)
        resultado = func(*args)
        return resultado
    return interna
#decorator complementar
def is_string(valores):
    if not isinstance(valores, str):
        raise TypeError('Isso não é uma string!!') 

def inverter_string(string):
    return string[::-1]
print(inverter_string('João')) #como pode ver, funciona normalmente.
#Mas e se fossem números? Vamos criar um decorator agora! Mas para isso, a função decoradora tem que ser anterior a esta.

inverte_string_checando = criar_funcao_decoradora(inverter_string)
invertida = inverte_string_checando('casa')
print(invertida)#funciona
# invertida = inverte_string_checando(123)
print(invertida) #o cod quebra pela minha vontade, devido ao raise caso haja algum número
###########
#caso ainda não tenha entendido o conceito de decorator, vou explicar de forma mais simples:
# decorator -> criar uma função que obtem outra função como argumento, por exemplo, uma função soma e retorna uma derivação da função soma.
# ex:
def funcao_decoradora(func): #criei uma função que receberá outra função
    print('iniciando')#mais uma possibildiade de decoração para função soma
    def interna(*args): #aplicaremos o conceito de high order functions e closure para adiar a execução dessa função.
    #ademais, nesse caso vamos trabalhar com argumentos não nomeados, que serão os argumentos informados para a função que vamos derivar.    
        resultado = func(*args) #aqui vamos armazenar a execução a função que iremos receber como argumento na função decoradora e decorar.
        #lembrando que *args como parâmetro vai empacotar argumentos não nomeados, já o *args fora dos parâmetros, vai desempacotar seguindo uma ordem posicional 
        print('finalizando') #aqui eu coloco algo a mais na função soma, decorando-a
        return resultado #agora, executamos a função soma, já que é ela que vamos decorar.
    return interna #aqui, adiamos a execução da função intera para não quebrar o código. Isso é closure, só para deixar claro.

#agora, vamos declarar a função soma
def soma(x, y):
    return x+y #aqui, efetivamos a soma.

#agora, vamos colocar o decorator em prática, através de uma variável:
decorator_somador = funcao_decoradora(soma) #aqui, informo para ele quem ele vai decorar
print(decorator_somador(10,20)) #e aqui vamos finalizar o closure, informando os valores (argumentos) que serão somados.

### essa decoração também é denominada de wrapper, pois modifica a soma apenas naquele momento da execução, possibilitando ainda que você utilize a função soma sozinha, porém, como ela vai tá sozinha, não vai aparecer o iniciando e finalizando. ex:
print(soma(10,20)) #como viu, foi normal.
###mas se eu quiser usar o decorator novamente, basta:
print(decorator_somador(14,15)) #como viu, deu tudo certinho!


cls()
#parece que o python foi escrito em c, famoso cpython.
############syntax sugar -> áçucar sintático(decoradores)
#um decorador é uma função que recebe outra função como argumento e retorna uma nova função, normalmente com novas funcionalidades, com base na função original.
#no entanto, o decorador precisa de uma variável que receberá a função decoradora para que essa função decoradora receba a função que será decorada, o que para algumas pessoas acabam sendo confuso ou demorado, e é aí que surge o syntax sugar!
#vou recriar um decorator abaixo e exemplificar o uso do syntax sugar.
def decorator(func): #criando o decorator
    print('iniciando a decoração')
    def interna(*args):
        resultado = func(*args)
        print(resultado)
        print('finalizando') #adicionando algo no decorator
        return resultado
    return interna

@decorator #esse aqui é o syntax sugar. Nesse caso, eu estou falando para o python executar a função verificacao como argumento para a função decorador, sem necessidade daquela variável
def multiplicacao(x, y): #aqui eu criei uma função que irá multiplicar valores.
    print(multiplicacao.__name__) #por causa do syntax sugar, se eu perguntar ao python o nome dessa função através do __name__, ele vai me dizer que o nome dela é interna, fazendo parecer que na chamada da função multiplicacao, estaria chamando a subfuncao interna, da função decorator
    #se não fosse um syntax sugar, retornaria o próprio nome da função.
    return x*y


# haha = decorator(multiplicacao) #sem o syntax sugar, eu deveria fazer desse jeito para funcionar
print(multiplicacao(10, 20)) #a partir desse momento, através de syntax sugar, posso chamar diretamente a função multiplicação que ela vai retornar um valor.

cls()
####decoradores com parâmetros 
#primeiro, vou mostrar uma forma que poderia ser utilizada para colocar parâmetros incialmente.

def DecorandoDivisao(func):
    print('segunda decoração')
    def aninhada(*args, **kwargs): #você pode ver a função intera como aninhada em tbm, porém em inglês.
        print('terceira decoração')
        resultado = func(*args, **kwargs)
        return resultado
    return aninhada
#acima, está o código da função decoradora, como você já deve saber.
#abaixo, estará a função referência, que poderá ser utilizada com parâmetros.

def DecoradoraParametros(a,b,c):
    print('primeira decoração, tendo {}, {}, e {}'.format(a, b, c)) #faço uso dos parâmetros e agora tá tudo certo.
    return DecorandoDivisao #Essa função vai retornar o decorador

@DecoradoraParametros(1,2,3) #o ponto de referência do Syntax Sugar vai ter que ser a função DecoraParâmetros
#como ela possui parãmetros, é de extrema importância que você informe quem são a,b e c.
def RealizarDivisao(x, y): #uma função simples para realizar a divisão.
    return x/y

print(RealizarDivisao(10,50)) #como pode ver, funciona normalmente!
cls()
##a segunda possibilidade, que é aproveitando os escopos de todas as funções, seria incrementando o decorator no escopo do próprio DecoratorParâmtros, ficando os três escopos acessíveis. Veja:

#como eu falei, irei utilizar o escopo da fábrica e lá estará decorador e a sua aninhada.
def fabrica_de_decoradores(a, b, c):
    print('primeira decoração')
    def decorador(func):
        print('segunda decoração')
        def aninhado(*args, **kwargs):
            print('terceira decoração')
            resultado = func(*args, **kwargs)
            print(f'vou acessar {a}, {b} e {c} da fábrica.')
            return resultado
        return aninhado 
    return decorador #agora eu faço a inicialização do decorator

#após fazer isso, precisamos fazer uso do syntax sugar, apontando para a fabrica de decoradores, e posteriormente, informar os valores de seus argumenmtos.
@fabrica_de_decoradores(1,2,3)
def Realizar_Subtracao(x, y): #quando eu chamar a função realizar subtração, ela vai realizar tudo normalmente.
    return x-y
print(Realizar_Subtracao(10,2))

cls()
###posso utilizar mais de um decorador em uma função. Ex:
def parametro_decorador(a):
    print('iniciando a decoração')
    print('o parâmetro do decorador no momento é: ', a)
    def decorator(func):
        def aninhada(*args, **kwargs):
            resultado = func(*args, **kwargs)
            salvamento = ''
            salvamento += str(a) #como tem mais de um decorador, para demonstrar, primeiro irei catar o primeiro valor do primeiro a e depois do segundo a, concatenando e depois o exibindo na tela.  
            print(a) 
            return 'acabou'
        return aninhada
    return decorator
#acima está o decorador com parâmetros, como já vimos. No entanto, se quisermos fazer uso de mais de um decorador com parâmetros diferentes, podemos fazer. Veja abaixo:
@parametro_decorador(11)
@parametro_decorador(10)
#como viu acima, utilizei dois decoradores utilizando valores diferentes para a. Nesse caso, quando eu chamar a função potenciação, ele vai aparecer aparecer duas vezes com o valor de a diferente.
#a ordem nesse caso importa, sendo que quem estiver mais próximo da função que será decorada executará primeiro. Nesse caso, o a=10 que vai ter sua execução inicialmente e posteriormente, a outra, tendo a=11.
#Se tivesse mais valores, também iria funcionar. Apenas cuidar na ordem, que como vimos, é decrescente em relação a função que será decorada. 
def RealizarPotenciacao(x, y):
    return x ** y

print(RealizarPotenciacao(2,4)) #aqui você vai ver o cod sendo executado duas vezes.

cls()
################################
##### count é um iterador infinito!
#o count é semelhante ao range, pois tem início e intervalo, que no caso é o step. A diferença é que o range tem início, fim e step, já o count só tem início e step.
demonstracao_range = range(0, 11, 2) #start=0, end=11, step=2 Ou seja, começa no zero e vai até o 11 pulando de 2 em 2
print(demonstracao_range)
#no caso do count,precisamo chamar o módulo itertools para fazer seu uso.
from itertools import count
#agora, veja:
uso_count = count(start=0, step=2) 
for __ in uso_count: 
    if __ >= 11:    #logo explicarei a razão de ter usado um for
        break
    print(__)
#como viu, seguiu uma lógica similar a lógica do range. Mas, e por que usou um for? O count do itertools funciona a base de iterator.
print(hasattr(uso_count, '__iter__')) #como pode ver, ele tem iter
print(hasattr(uso_count, '__next__')) #como pode ver, ele tem next também.
print(hasattr(demonstracao_range, '__iter__')) #o range é um iterator também
print(hasattr(demonstracao_range, '__next__')) #mas não tem next.
#logo, foi necessário fazer uso do for para o count. Ademais, o count é um contador sem fim, ou seja, se eu fizer um for, tenho que colocar um limite para ele parar, se não, executará infinitamente!
for __ in uso_count: 
    if __ >= 30:    #como pode ver, coloquei um limite!
        break       # e como ele é um iterator, o next se torna o __ e executará a função n vezes.
    print(__)

##############################################
# uso do combinations, permutations e product do módulo itertools
#lembrando que todas as funções aqui explicadas funcionam a base de interator, logo, o next, list ou iterable como o for seriam necessários para visualizar.
#listas exemplos
pessoas = [
    'Joana', 'Carlos', 'Maria', 'Josefa'
]
camisetas = [
    ['preta', 'lilás'],
    ['p', 'm', 'g']
]
def funcao_separadora(iteravel):
    print(*list(iteravel), sep='\n')
    print()
    #o intuito da função acima é converter o interator para list, esgotando o seu valor e posteriormente, garantir maior visualização do código.
##combinations
from itertools import combinations
#combinations fará um determinado número de combinações, onde vai considerar apenas a ocorrência dela uma vez. Ex:
#  Apareceu: "joao, branco", logo, não irá aparecer o seu oposto, que seria: "branco, joao"
# Ademais, ela édeterminada pela seguinte lei:
# combinations(intervalo, numero_de_combinações), onde intervalo guardará o que irei combinar dentro de um tipo de dado, como list e o número de combinações será quantas vezes ele irá combinar. 
funcao_separadora(combinations(pessoas, 2)) #nesse caso, o intervalo será pessoas e a ocorrência de combinações será de 2
funcao_separadora(combinations(pessoas, 3)) #nesse caso, o intervalo será pessoas e a ocorrência de combinações será de 3
cls()

##permutations
from itertools import permutations
#permutations também faz parte do módulo itertools, sendo bem similar com combinations.
#a diferença é que ele vai considerar as duas ocorrências da formação de uma combinação. Ex:
# Apareceu "terra, cota" como combinação. Será considerado também: "cota, terra" como outra combinação, sendo essa combinação um pouco mais extensa. 
# tendo a mesma lei de formação que a anterior. (combinations)
funcao_separadora(permutations(pessoas, 2)) #duas combinações 
funcao_separadora(permutations(pessoas, 3)) #três combinações
cls()

##product
from itertools import product
#já essa é bem diferente da anterior. Pois, através dela, é possível determinar combinações de mais de um ponto de referência.
#o que eu quero dizer é que você pode ter um tipo de dados dentro do outro e ele será considerado. Um exmplo é o próprio camisetas, sendo um list dentro de um list.
funcao_separadora(product(camisetas)) #como é uma lista dentro da outra, vai precisar desempacotar para visualizar melhor.
funcao_separadora(product(*camisetas)) #como pode ver, ele fez várias combinações diferentes.
camisetas.append(['masculino', 'feminino']) #incrementei mais duas possibilidades para combinações com o intuito de demonstrar o poder da coisa.
funcao_separadora(product(*camisetas)) #como pode ver, deu tudo certo até aqui!!
cls()
########################################### uso do 
#groupby - siginificado=agrupar por
# função do itertools utilizada para filtrar com base em uma referência. No caso abaixo, vamos filtrar com base na key nota.
#lembrando que groupby também funciona a base de interator
from itertools import groupby
alunos = [
     {'nome': 'Luiz', 'nota': 'A'},
     {'nome': 'Letícia', 'nota': 'B'},
     {'nome': 'Fabrício', 'nota': 'A'},
     {'nome': 'Rosemary', 'nota': 'C'},
     {'nome': 'Joana', 'nota': 'D'},
     {'nome': 'João', 'nota': 'A'},
     {'nome': 'Eduardo', 'nota': 'B'},
     {'nome': 'André', 'nota': 'A'},
     {'nome': 'Anderson', 'nota': 'C'},
 ]


alunos_organizados = sorted(alunos, key=lambda x:x['nota'])
#faz a organização da lista, para não ficar bagunçado através do sorted
#ademais, isso é muito interessante, pois caso o dado seja digitado posteriormente, ele criaria uma sub divisão "A" do que já tem.
#Por exemplo, se você coloca pra filtrar pela nota e abaixo da nota, alguma pessoa tira mais uma pontuação. Vai ficar: A, B, C, D, A (repetiu.)
#para n repetir, o sorted passa a ser importante 
grupos = groupby(alunos_organizados, key=lambda x:x['nota'])
#esse key lambda vai informar a função groupby a como fazer a filtragem 
# partir de agora, ele vai começar a filtrar pela letra de pontuação!

for chave, grupo in grupos:
    print(chave)
    #aqui podemos ver como ele filtra 
    #no entanto, precisaremos de mais um for para executar os values das chaves 
    for aluno in grupo:
        print(aluno)
        #agora podemos ver quem eram os values e a filtragem fora concluida. 

cls()
########################################
# uso do map, partial e GeneratorType 

produtos = [
     {'nome': 'Produto 5', 'preco': 10.00},
     {'nome': 'Produto 1', 'preco': 22.32},
     {'nome': 'Produto 3', 'preco': 10.11},
     {'nome': 'Produto 2', 'preco': 105.87},
     {'nome': 'Produto 4', 'preco': 69.90},
 ]
# método convencional de aumentar o preço de lista
def aumentar_dez_por_cento(x):
    return x/10 #dez por cento

produtos_comprehension = [
    {'nome':produto['nome'], 'preco':produto['preco']+aumentar_dez_por_cento(produto['preco'])}
    for produto in produtos
]
print(*produtos_comprehension, sep='\n')
#acima, utilizamos o list comprehension para aumentar 10% do valor original

#uso do map
#map é um mapeador, ou seja, ele vai iterar por cada item da lista.
#vamos resolver essa parada com o map agora. Aumentar 10%, no caso
#função map participa de programação funcional

mapeamento = list(map(lambda x:x['preco']+(x['preco']/10), produtos))
print(mapeamento)
#como pode ver, ele iterou por toda a lista e tirou 10%
#o map é um iterator, logo, para exibir o seu valor, ele vai precisar de uma iteração com next ou esgotamento. No caso acima, foi preferível o esgotamento para exibir logo o valor.

#uso do partial 
# partial é uma função do módulo functools, onde funciona exatamente como uma closure.
from functools import partial
new_products = {'product_name':'Bread', 'price':10}
#vamos aumentar o valor em 10%
def to_up_10(valor, porcentagem):
    return round(valor * porcentagem, 2)
    #lembrando que aquele dois ali representa o número de casas que o round vai fazer.

value_10_now = partial(
    to_up_10,
    porcentagem=1.1 #esse 1.1 vai amentar em 10%
)
aumentando = {**new_products, 'price':value_10_now(new_products['price'], porcentagem=1.1)}
#com o ** eu fiz a extração dos itemns da new_products e depois fiz a mesma lógica do closure usando a partial.
print(aumentando)

#uso do generatorType
#é um módulo do módulo type que tem o intuito de verificar se o dado é um generator.
#pode ser utilizado para distinguir generator de iterator.
from types import GeneratorType
bandi = (n for n in range(10)) #esse cara é um generator expression

#agora, basta utilizar o isinstance para verificar se é verdade
print(isinstance(bandi, GeneratorType)) #como pode ver, é um generator.
#vamos agora declarar um iterator
iterrr = iter(list(range(11)))
print(iterrr.__next__()) #sabemos que isso é um iterator, mas vamos verificar
print(isinstance(iterrr, GeneratorType)) #como pode ver, o teste para verificar se é um generator deu negativo.

###uso do filter
#já fizemos uso do filter no list comprehension

lista_de_valores = list(range(11)) #valores gerados até 11
filtragem = [ #variável do tipo list
    num *2 #mapeamento
    for num in lista_de_valores #iteração
    if num >= 5 #filter (só vai entrar na filtagrem quem for >= 10)  
]
print(filtragem) #como pode ver, filtragem feita.

#filter funciona e realiza ações com base em uma lista já criada, assim como o map. Casos do filter:
# if filter > listaReferencia# - nada será armazenado   
# if filter < listaReferencia# - todo o map será armazenado   

#outra manifestação do filter é através de sua própria função. 
# filter também é baseado nos conceitos de iterator.

filtragemList = filter(#denominação da variável e seu tipo filter.
    lambda x:x > 4, #aqui fica a função, seja lambda ou def. Ademais, após a função, virá o filter.
    lista_de_valores #aqui é a lista de referência.
)

print(list(filtragemList)) #agora, vamos esgortar a filtragem e receber o seu valor.

#ademais, filter também pode ser utilizado para tratar falsy
tratamento_nao_valor = list(filter(None, ['', 'Aoba', 1, [], [1,2,3], (), ('a'), {}, {'aoba':'gato'}]))
print(tratamento_nao_valor) #como pode ver, utilizamos None como Func e da lista analisada passa a ser removido os falsy
cls()

###########uso do reduce
#o reduce tem o intuito de reduzir uma sequências de índices a apenas um.
#ele não é diretamente embutido no python, por isso, precisaremos importar o módulo functools, trazendo a função reduce
from functools import reduce
#abaixo há uma sequ~encia de produtos com valores. O nosso objetivo final será somar tudo!
produtos = [
    {'nome':'Produto 1', 'preco':10},
    {'nome':'Produto 2', 'preco':9},
    {'nome':'Produto 3', 'preco':4},
    {'nome':'Produto 4', 'preco':7},
]
#o reduce precisa de uma função à parte. Nela, haverá os seguintes parâmetros: acumulador e produto, onde:
# acumulador -> ponto de início
# produto -> variável referência

def func_do_reduce(acumulador, produto):
    #essa função acumulador vai executar n vezes com base na quantidade de elementos presentes em produto.
    print(acumulador)
    print(produto)
    # return 1 #o valor retornado dessa função será retornado pelo acumulador. Ou seja, se aqui tem return 1, o acumulador será sempre 1
    #sabendo disso, podemos fazer com que ele retorne o valor da key preco e somar com ele mesmo, ficando:
    return produto['preco'] + acumulador #lembre-se que o valor inicial do acumulador é 0
    #acima, pegamos a variável referência e filtramos pela key preço. Logo, ele irá retornar sempre esse valor.
    #Com isso, seria apenas somar com o acumulador, que antes possuia a key 'preco' do índice anterior, realizando uma soma a cada execução e assim, concluindo o nosso objetivo final.
    

totalizando = reduce( #aqui criamos uma variável recebendo reduce.
    func_do_reduce, #trás à tona a função necessária para reduce que aparentar funcionar com closure (pois não executou)
    produtos, #argumento para produto
    0 #argumento para acumulador
    #é importante colocar o valor inicial do argumento acumulador, pois apesar de funcionar quando não colocado, pode gerar transtorno na lógica.
    #se eu não colocar o 0, ele vai iniciar do índice da [0] da variável referência, o que eventualmente pode complicar.
)   
print(totalizando)
#agora, vamos fazer todo esse process, só que usando uma lambda.
#como sabemos, o reduce precisa de uma função e o lambda é uma função e nesse caso, faria mais sentido fazer uso dela.

reduceLambda = reduce(
    lambda acumulador, produto: produto['preco'] + acumulador,
    produtos, 
    0
)
print(f'O total é: {reduceLambda}') #como pode ver, mais simples e mais fácil!

######################################
#########Funções Recursivas e Recursividade
#funções recursivas são funções que podem se chamar de volta
vezes = 0
try: 
    def recursiva():
        global vezes
        print('vou me retornar!!')
        vezes +=1
        print(vezes)
        return recursiva()
    recursiva()
except RecursionError:
    print('chegou ao limite da recursão!')

#como eu disse, uma função recursiva é uma função que retorna ela mesma várias vezes. É como se ela fosse um laço.
#No entanto, uma função recursiva tem um limite máximo de execução, sendo até 1000, sendo executado 1000 vezes (um for recursao in range(1000)), como visto no prompt. Por isso que ela se encontra dentro de um try, para não quebrar o código.
#O limite é mil porque se deixar, essa função pode travar o computador, trazendo malefícios e por isso, ela deve ser controlada. 
# o intuito da função recursiva é pegar um problema maior e resolver em pequenas partes. 
#No exemplo abaixo, vou exemplificar um caso simplório, sendo uma situação onde o obejetivo é contar até 10.
#aparentemente, as funções recursivas no python são irrelevantes por causa da existência dos loops. No entanto, como ele faz parte de progamação funcional, pode ser que você queira o utilizar.

def recursandoNow(inicio=0, fim=10): #nosso problema maior é fazer a contagem
    #controle
    if inicio > fim:    
        return fim #quando fazemos uso de um return, sabemos que a função quebra e retorna o valor a direita no mesmo momento.
    #Resolução
    #Para dividir o problema em partes menores, nesse caso, precisamos somar um por um, ficando:
    #caso recursivo
    print(f'Continha: {inicio}')
    inicio +=1
    return recursandoNow(inicio, fim) #e aqui estamos efetivando a função recursiva
    #é importante colocar os parâmetros da função anterior.
recursandoNow()

#caso você queira aumentar o limite da função recursiva, você pode chamar o módulo sys e fazer uso da função setrecursionlimit(n)
from sys import setrecursionlimit
setrecursionlimit(1011)
vezes = 0
try:
    recursiva()
except RecursionError:
    print('já foi o máx')
#como pode ver acima, aumentou o limite até 1011 


####################introdução ao venv
# venv é um ambiente virtual que fica armazenado em formato de pasta do próprio python que você pode criar no seu computador.
#ademais, tudo que voc~e instalar em um ambiente virtual, ficará somente nele com o intuito de prevenir possíveis conflitos de versões ou algo assim.
# o venv é utilizado corriqueiramente quando você precisa trabalhar em sistemas legados, ou seja, sistemas que foram desenvolvidos há tempos atrás, com versões antigas.
#  dentro do venv tem inúmeras versões do python, e por causa dela, você não iria precisar mexer no seu python global ou algo do tipo para mexer nesse projeto, o que torna o venv muito útil.
# você pode ver o venv normalmente com o seguintes nomes:
# venv, env, .venv(sistemas linux), .env (sl)

# criando um ambiente virtual pelo power shell:
# python -m venv venv
# ou
# py -m venv venv
# onde:
# -m -> executa uma lib de script
# venv -> é o script de criação do ambiente virtual
# venv ->o segundo venv é o nome que eu escolhi para essa pasta.

# sobre as pastas:
# lib -> são instalações de terceiros que você fará
# bin/scripts -> pasta de scripts que trás os executáveis 

#ainda comandos no Power Shell
#comandos para verificação de local:
# gcm python -> para ver onde me encontro no momento, tendo o python como referência final.
#gcm python -Syntax -> vejo de forma resumida o local que me encontro no momento.
 
#se for algum motivo eu precisar saber dessas paradas em um macos, o comando é:
# which python -> vejo de forma resumida o local que me encontro

#mas como o caminho do python está no path, não seria necessário ter essa complicação toda pra saber.
#basta fazer uso do python -V, tanto macOS como windows e linux
# python -V -> BUSCA no path a versão do python e consequentemente o seu caminho.

#####ativação ou desativação de ambiente virtual
# utilizando o cmd ou PowerShell, você pode navegar para venc/scripts e executar activate. Logo, seu ambiente virtual estará ativado.
#para desativar é a mesma lógica, a diferença é que você vai executar a pasta deactivate
# para ativar ou desativar em um linux ou mac, é a mesma coisa também. Porém, tem uma diferença: é necessário colocar um . ou source e depois venv/bin/activate

# onde:
# . -> faz referência a pasta que você está no momento
# source -> faz referencia a uma pasta, nesse caso, a ela própria
# venv -> ao ambiente virtual já criado
# bin -> é como se fosse a pasta Scripts do windows
# activate -> realiza a ativação

########uma coisa importante para falar é que quando o ambiente virtual está ativo, ele muda temporariamente o path.
# veja a seguir os caminhos:
# C:\Python313\python.exe -> path quando o venv está desativado
# D:\Ghost\Usuário\Documents\cursopy2025\venv\Scripts\python.exe -> path quando o venv está ativado
#quando o ambiente estiver ativado, qualquer coisa que você fizer no python, como a instalação de um módulo, ficará ali. Ou seja, se você desativar o venv e voltar para o python global, aquilo que você instalou não poderá ser mais usado.

#####
#quando eu encontrar em um compilador do venv, tudo que eu instalar será posto na pasta lib.
# para instalar um módulo, você pode fazer:
# pip install <nome_do_modulo> - instalará um módulo. Caso você esteja no venv, isso será instalado na pasta lib
# pip uninstall <nome_do_modulo> - vai desinstalar algum modulo que você já tem.

# pip freeze - lista todos os pacotes instalados (tem que ser no terminal)
#pip index versions <nome_do_pacote> -> vai listar todas as versões disponíveis para o pacote em questão.
# ex: pip index versions pyautogui - listagem de versões nesse momento que me encontro:
# Available versions: 0.9.54, 0.9.53, 0.9.52, 0.9.51, 0.9.50, 0.9.48, 0.9.47, 0.9.46, 0.9.45, 0.9.44, 0.9.43, 0.9.42, 0.9.41, 0.9.40, 0.9.39, 0.9.38, 0.9.37, 0.9.36, 0.9.35, 0.9.34, 0.9.33, 0.9.31, 0.9.30, 0.9.26, 0.9.25, 0.9.24, 0.9.23, 0.9.22, 0.9.21, 0.9.20, 0.9.19, 0.9.18, 0.9.17, 0.9.16, 0.9.15, 0.9.14, 0.9.13, 0.9.12, 0.9.11, 0.9.10, 0.9.9, 0.9.8, 0.9.7, 0.9.6, 0.9.5, 0.9.4, 0.9.3, 0.9.2, 0.9.1, 0.9.0
#   INSTALLED: 0.9.54
#   LATEST:    0.9.54

#pip install <nome_do_modulo>==versão - instala uma versão em específico do módulo respectivo.
# pip install pyautogui==0.9.45 -> instala a versão que especifiquei do módulo pyautogui

# pip install <nome_do_modulo> --upgrade -> instala a última versão do módulo
# pip install pyautogui --upgrade -> instala a última versão do pyautogui

################uso do requirements.txt
# o requirements será um arquivo que você irá criar para informar quais módulos serão necessários para um sistema ou projeto.
# Por exemplo, se um projeto precisar essencialmente de uma versão em específico do pyautogui, a instalação do pyautogui estará dentro da pasta requeriments.txt
# Isso é normalmente utilizado em um venv, já que o ambiente virtual (quando criado) vem virgem, ou seja, sem instalação nenhuma. Logo, eu precisarei instalar os módulos necessários e a depender do projeto que eu vá dar continuidade, poderei fazer o donwload de todas as dependências através de requirements

# para criar esse arquivinho, basta voc~e entrar no projeto e digitar pip freeze > requirements.txt
# pip freeze > requirements.txt -> cria o nosso arquivo que vai armazenar as nossas dependências.
# após requirements ter sido criada, você entrará nela e vai informar o nome das dependências e suas versões. Ex:

# dentro de requirements:
# autopep8==2.0.0
# pyautogui==1.2.0
# PyMySQL == 1.0.2

#agora, depois de ter feito isso, seu requirements para aquele projeto já tá pronto. Basta entrar na venv e executar.
# pip install -r requirements.txt
# -r -> referência a requirements
# e posteriormente, informo o nome do arquivo (normalmente é requirements mesmo) 

#########recarregar o vscode
# Ctrl + Shift + P -> vai abrir a janela de execução
# digite: Reload Windows e aperte enter
#  Logo, o vscode será recarregado.
cls()

#########################Criando arquivos com python + Context manager
#############
#Para criar um arquivo no python, é necessário inicialmente entender como vanevamos em um caminho.
#Sabemos que no windows, quando queremos dedifinir um caminho, uma das possibilidades que temos é colocar duas barras, correto? caso contrário, o python entende isso como namespace.
diretorio = 'D:\\Ghost\\Usuário\\Documents\\testaa.txt' #criação do diretório para chegar até aqui.
print(diretorio) #como pode ver, o diretório aqui contou apenas uma barra e ficou tudo certinho.

#para navegação de arquivos, é necessário fazer uso do open, que também é necessário para manipulação.
# para utilização do open, temos que entender suas possibilidades:
# w (escrita)     r (leitura)     x(criação)      a (escrever ao final)
# b (binário)     t (modo de texto)       + (leitura e escrita)


capa = open(diretorio,'w')#executei, agora o arquivo foi criado e aberto.
#no entanto, a aprtir do primeiro momento que abrimos, temos que fechar
capa.close() #agora sim!
# normalmente é utilizado um try e um finally com o close para garantir seu fechamento

#mais um exemplo para fixação 
arquivo = 'jao'
CAMINHO = f"D:\\Ghost\\Usuário\\Documents\\{arquivo}.txt" #denomino todo o diretório

abertura = open(CAMINHO, 'w')#faço um arquivo de fixação.
#caso o arquivo não exista e você colocar uma ação de leitura, tipo o r (read), vai dar pau.
# ex: abertura = open(CAMINHO, 'r') -> isso iria gerar sérios problemas.
abertura.close() #e como sempre, você tem que fechar o arquivo quando abrir.



######context manager - abre e fecha um arquivo.
# Se você quiser fazer algo mais breve e sem uso do close, pode ser que seja útil pra você o with open, que abre e após a execução do arquivo, ele fecha.

#funciona com os mesmos princípios do duck typing (se nada e faz quaqua como pato, então é um pato.)
#sendo que se abre arquivo e tem open, então é um open e precisa ser fechado.

with open(diretorio, 'r+') as arquivando:
    arquivando.write('Olá mundo! ') #digita olá mundo no documento
    arquivando.write('terra') #a quebra de linha é obrigatória, caso contrário, ficará tudo coladinho

######segunda prática + # métodos úteis do open:
# write -> escreve
with open(CAMINHO, 'w') as ARQUIVO: #como dito antes, o with tem o papel de abrir e fechar o arquivo, seguindo o conceito do context meneger, quase que uma derivação do duck typing.
    #os comandos para o arquivo devem permanecer dentro deste escopo.
    ARQUIVO.write('Digito algo no documento.') #este aqui serve para digitar algo no documento.
    #lembrando que quando você utilizar o write novamente, ele vai continuar de onde parou. 
    ARQUIVO.write('bandido \n') #ou seja, ele vai juntar o 'bandido' na mesma linha do texto anterior.
    #LOGO, BASTA COLOCAR UMA QUEBRA DE LINHA, FICANDO:
    ARQUIVO.write('safado') #como viu no documento, está tudo ok!


print('é um arquivo do tipo', type(CAMINHO))
#read
# como o arquivo já foi criado e devidamente fechado, devido ao uso do context manager, posso abrir novamente.
#com isso, vamos criar agora um de leitura, seguindo a mesma lógica
with open(CAMINHO, 'r') as ARQUIVO_LEITURA:
    print(ARQUIVO_LEITURA.read()) #e aqui, aparece para mim o que tem no arquivo.

cls()
#uso do w+ ou r+ com seek
with open(CAMINHO, 'w+') as MISTO:
    MISTO.write('Joao Carlos')
    #agora vamos printar
    print(MISTO.read())
    #como pode ver, na printagem não deu certo, pois quando eu uso o write, ele digita nmo documento e ao finalizar, deixa o cursor do 'mouse' no final do arquivo.
    #como, quando fazemos uso do read, ele só vai mostrar tudo que estiver a frente do cursor, mas como o python jogou o cursor para o final, devido o uso do qrite, não vamos conseguir ver nada.
    #é por isso que o seek existe. Seu intuito é mover o cursor do mouse para alguma posição e nesse caso, podemos colcoar para o topo.
    MISTO.seek(0,0)
    print(MISTO.read()) #como pode ver, agora o 'Joao Carlos foi exibido. '
    
    ####### uso do writelines:
    #serve para você colocar multiplas linhas!
    MISTO.writelines(
        ('\n','linha2\n', 'linha3\n')
    )
    MISTO.seek(0,0)
    print(MISTO.read()) #como pode ver, tres linhas foram inseridas! sendo que uma era pra efetuar a quebra. 

    cls()
    ######uso do readline
    #como você viu, o read ler de uma vez, correto? mas você também poderia colocar ele para ler or partes.
    MISTO.seek(0,0)#coloca no topo da página
    print(MISTO.readline())
    print(MISTO.readline())
    print(MISTO.readline())
    print(MISTO.readline())
    #como pode ver, ele executou um a um. Nesse quesito, ele parecido com o next, a diferença é que se você estrapolar, ele não dará erro de stop iteration.
    #mas um problema que vemos ali é que os arquivos executa também a quebra de linha, o que as vezes pode ser o que não queremos, né? pois colocamos a quebra de linha pensando em utilizar o read, para executar tudo de uma vez.
    #para resolver isso, basta colocar um end='', eliminando as quebras de linha ou
    # .strip, que removerá todos os espaços, incluindo as quebras de linha., ficando:  
    
    print('problema da quebra corrigido')
    MISTO.seek(0,0)#coloca no topo da página
    print(MISTO.readline().strip())
    print(MISTO.readline(), sep='')
    print(MISTO.readline()) #essa aqui é a própria quebra de linha
    print(MISTO.readline(), sep='')

    #ou pra resolver isso podemos iterar
    print('\noutra forma')
    MISTO.seek(0,0)
    for linhaa in MISTO.readlines():
        print(linhaa.strip())
    
#um muito importante é o a+, pois o w apaga tudo que estiver no arquivo para escrever de novo.
# o a já vai para o final, e possibilita a escrita também. Ex:
with open(CAMINHO, 'a+') as add:
    for number in range(0, 21, 2):
        add.write(f'{number} \n') #como pode ver, segue a mesma lógica das demais e não apagou nada.
        #segundo o Otávio, é uma boa forma de gerar loggers.
    add.write('gayzão\n')
    #como pode ver, um acento ou caracter especial vai ocasionar em um transtorno na execução, que é uma palavra incorreta.
    #isso ocorre porque a codificação do linux/mac é diferente do windows, ocasinando em uma decodificação inusitada.

# para resolver isso, basta incremntar um argumento no open, que no caso, é o enconding e logo após, informar o formato de codificação.
with open(CAMINHO, 'a+', encoding='utf8') as adicionado:
    adicionado.write('gayzãooo')
    #dentro do arquivo está certinho e problema resolvido!

############### apagando ou renomeando arquivo
def uso_do_os():
    import os
    os.remove(CAMINHO) 
    os.unlink(CAMINHO)
    # as duas funções da os servem para apagar o arquivo.
    os.rename('D:\\Ghost\\Usuário\\Documents\\cursopy2025\\Scripts\\apagar.py',
            'naoAagueporEnquanto.py'
            )  #renomeia ou move um arquivo. Nesse caso, eu renomeei
#se eu quiser mover, bastava eu apontar um outro caminho como segundo argumento.
#coloquei dentro do def para não dar pau

cls()
#####################introdução ao Json
# Json - > javascript object notation
#json é um banco de dados local
import json
#para fazer uso do json, inicialmente é necesário criá-lo. Uma das formas mais fáceis de criar o json, é através do próprio context maneger
#mas primeiro, precisamos criar uma lista que será salva
pessoas_novas = [
    {'nome':'Carlos', 'idade':15 , 'sexo':'M'},
     {'nome':'Joana', 'idade':10 , 'sexo':'F'},
     {'nome':'Maria', 'idade':35 , 'sexo':'F'},
     {'nome':'João', 'idade':17 , 'sexo':'M'},
    
]

print(*pessoas_novas, sep='\n') #como pode ver, o nosso dict foi criado tudo certinho.
#agora, vamos inseri-lo em um json. E para isso, vamos começar criando um json

with open('arquivojson.json', 'w', encoding='utf8') as arquivojson:
    json.dump(pessoas_novas, arquivojson) 
#nesse momento, as informações do dicionário pessoas_novas se encontra em um arquivo json que também acabamos de criar.

with open('arquivojson.json','r', encoding='utf8') as jsonleitura: #encoding para informar a codificação
    #como pode ver, é uma estrutura similar a criação de um arquivo qualquer através do context maneger  
    leitura = json.load(jsonleitura)
    print(leitura)

#no entanto, quando você coloca alguma pontuação em alguma vogal, consequentemente, vai ocorrer algo semelhante com a questão da codificação.
#porém, como se trata de um banco de dados, é interessante você deixar dessa forma para não gerar algum conflito no futuro.
#mas, se mesmo assim corrigir isso for muito importante para você, basta informar false para argumento para o parâmetro ensure_ascii no dump.
with open('arquivojson.json', 'w', encoding='utf8') as arquivojson:
    json.dump(pessoas_novas, arquivojson, ensure_ascii=False) 
#como pode ver, o joão agora foi corrigidio.
#ademais, temo sum outro problema, que no caso, é a visualização.
#como pode ver ao entrar no json, todos os dados estão em uma linha só e podemos resolver isso com o argumento indent = numero de linhas
with open('arquivojson.json', 'w', encoding='utf8') as arquivojson:
    json.dump(pessoas_novas, arquivojson, ensure_ascii=False, indent=2) 
    #como pode ver, agora ele está bem organizadinho!!

#uma informação útil:
# O Json não suporta métodos complexos como funções, sets, classes, etc (tem como forçar) por padrão, mas objetos que você consegue converter de python para json, podem ser inseridas, como str, int + float (number no json), dict (objeto no js), list (array), bool, etc.

cls()
############################
# Criação de lista qualquer evitando colocar valor imutável como argumento padrão.
#isso é mais um execício que um conceito, mas vou explicar.
def adiciona_clientes(nome, lista=None):
    #se em lista tivesse um valor mutável como list [], quando eu fosse criar uma outra lista, tipo clientes dois, ele iria agregar esse valor juntamente com os que eu já tinha passado.
    if lista is None:
        lista = [] #e se caso o cidadão realmente não digitar nada, posso aproveitar esse none que ele vai retornar para fazeruma função.
        lista.append(nome)
        return lista
    lista.append(nome)
    return lista


cliente1 = ['carlos']
cliente2 = ['joão']
cliente3 = ['danilo']

capa = 0
for add in [cliente1, cliente2, cliente3]:
    capa+=1
    adiciona_clientes(capa, add)
#aqui eu faço a criação de lista s individuais e abaixo, printo elas
#fora que nelas eu faço uso da função que criei para mostrar eficácia.

print(cliente1,'\n',cliente2,'\n',cliente3)
#e como pode ver, deu certo

# Rubber Duck Debugging -> uma técnica utilizada para explicar um problema em específico - normalmente utilizada com patinhos.
# Essa técnica consiste em pegar o patinho e explicar o que você precisa fazer para ele e qual seria a melhor forma de fazer. 
# É importante que você faça isso falando em voz alta, para fazer com que você compreenda com mkais facilidade o que você está dizendo.
# Com isso, quando você explica seu problema e como pode resolver para o patinho ou qualquer outra coisa que você estiver, vai ser mais fácil resolver.

cls()
dicionaryy = {
    'nome':'carlos',
    'idade':14
}
dicionaryy['fds'] = 14

print(dicionaryy)












