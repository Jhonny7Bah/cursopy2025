#aula 1
numero = 10
ha = '\n'

#isso e comentário
print("minha caceta eh da boa, veja: {}, tá?".format(numero))
print("hello world!")

"""
o nome disso aqui é docstring
"""

#abaixo tem outro modo de usar o docstring
print(""" {}
    minha caceta
      eh bem da boa slk

""".format(ha))

#aula 2
print(123, 456, "fds") #uma forma de escrever variaveis ou misturar tipos primitivos num print só
print("{} {} {}".format(123,456,"caceta")) #mesma coisa, po´rem de outra forma 
#o que é colocado na função print são argumentos. No caso acima, chamamos de argumentos não nomeados. 

print(123, 456, 789, sep="-") #sep no caso é um separador, ou seja, a cada virgula colocada, será inserido um traço para separar(nesse caso)
#argumento nomeado é o que já tem por padrão ou que foi declarado como variável, como o sep e end.

#aula4
teste = 10
#classe é entreparenteses e começa com letras  maiusculas
#função tem parenteses e comeca com letras minusculas
teste = 45

print(type('fds')) # a função type diz o tipo trimitivo do argumento
print(type(teste)) #int

caramba = float(input('isso aqui é um flutuante, ou seja, numero quebrado'))

#conversão detipos primitivos

import os #biblioteca de sistema
terra = '4' #isso é um int
me_mama = 10

print(type(terra)) #veja por si só

print(int(terra) + 4) #agora eu converti o terra em str

print(str(10) + 'ha') #isso irá resultar numa concatenacao


#aula 26
n1 = 10

print(n1 / 3)#divisão real (float)
print(n1 // 3 ) #divisão inteira

print(2 ** 3) #dois elevado a 3

print(10 % 2) #resto da divisão de 10 por 2.
    
#aula27

print('Jao' + ' ' + 'baitora') #pecularidade da soma (concatenar)
print('fds ' * 10) #ira multiplicar o fds 10 vezes.
print(3 * 'caceta ') #também

print(...) #esses tres pontinhos sechama elipse e pode ser usado em uma linha de codigo que nao pensei ainda 

#aula28 ordem de precedencia
# () [] {}
# ** 
# * / // %
# +-

##aula31 
#meios de usar varivaies no print:
teste = 'pomba'
#os meios abaixo chegarão ao mesmo resultado 
print('eu tenho uma', teste)
print(f'eu tenho uma {teste}') #formatracao f-strings
print('eu tenho uma {}'.format(teste))

#quando não tem nome, eu chamo de argumento, como abaixo:
print('eu tenho uma {0} e maiis outra {0}, so q n tenho mais {0}'.format(teste)) #um jeito de utilizar apenas uma variável através de uma ordem numérica
#agora tem nome e eu chamo de parametro nomeado, veja:
print('minha {eita} se encontra mole'.format(eita = teste)) #ao lado está um parametro nomeado local, ou seja, a variavel eita so pode ser usada aq 
#caso eu começar a utlizar o format como parametro nomeado, terei que terminar, ou seja, utilizar apenas parametros nomeados no format completo.

#quando uma função está dentro de um objeto, ela é chamada de método. 

num = 10000.00

print(f'ataaa {num:,.2f}') #caso queira separar com virgulas 


print('vamos ver isso {fds}'.format(fds = num))

print(f'qual é o número: {num=}') #eu uso o = para ver o nome da variavel no print e posteriormente, sua atribuicao

 #aula 34 condicionais
if 1+1 == 2:
    print('deu bom')
elif 1+1 == 3:
    print("tem coisa errada ai pow")
else:
    print('vai te lascar ')


#aula37 operadores logicos
#maior >
#maior ou igual >=
#igual ==
#diferente != 
# and = duas condições tem que ser verdadeiras
# or = uma das duas condições no if tem que ser verdadeiras
#not = é como se fosse um diferente

#0, 0.0, '' são os verdadeiros valores considerados false

 
carro = None #uma variável sem atribuição 
print(carro)

#verificacao = input('Você quer entrar nessa peste?\n[S]im [N]ão ')
verificacao = 'N'

if(verificacao == 'S' or verificacao == 's'): #para "or", uma das cond tem que ser True

    verificacao2 = input('certeza mesmo, garai? \n[S]im [N]ão ')
    
    if(verificacao2 == 'S' or verificacao == verificacao2 == 's') and (verificacao == 'S' or verificacao == 's'):
        #o caso acima utiliza or e and(para se caso duas condições forem true, a condição dara verdadeira)
        #o if é parecido com uma expressão no sentido de expressão, então para não gerar bugs, colocaremos o parenteses 
        print('va queimar rosquinha va')
    
    
    else: print('va da caneco ')

else:
    
    print('entao va da o caneco ')
teste = 'jao'

print('caceta 'or 'my caceta') #quem for verdadeiro no operador or, aparece primeiro

print('teste drive' and 'hahahaha') #ele vai parar no último que foi verdadeiro

print('j' in teste) #verifica se a letra está no valor da variável (true)
print('jao' not in teste) #verifica se a letra está no valor da variável e retorna o oposto(false)

nome = 'xablau'
preco = 1000.0045

variavel = '%s, o preço foi ' % nome #o nome disso é interpolação
#no caso acima, apenas uma variavel foi colocada, então não precisa de ()
print(variavel)
variavel = '%s, o preço foi %d' % (nome, preco) #aqui precisará de ()
#essa interpolação é utilizada para converter tipos primitivos. ex: float --> int, como no ex acima.
print(variavel)
#ou
variavel = '%s, o preco foi %.2f' % (nome, preco) #dois num decimais após a virgula 

print(variavel)

#padds
variavel = 'caceta'
print(f'{variavel: >10}') #o valor da variável será printado após 10 espaços
print(f'{variavel: <10}.') # preenche 10 espaços para frente
print(f'{variavel: ^10}')# dentre dez espaços, ele faz o possível para centralizar o conteúdo da variável
print(f'{variavel:a^10}') #esse a é apenas uma demonstração, pois ele preenche os espaços com qualquer letra
print(f'{100.00000:.2f}') #formatação para duas casas float

print(f'{15420.0545:0>+1.1f}') #pra saber se o numero é positivo ou negativo 

print(f'{74:08x}') #hexaadecimal (não sei a utilidade)

#aula 46
#fatiamento de strings

caceta = 'ola mundo'
         #012345678   indices positivos
        #-987654321   indices negativos
print(caceta[4]) #escolho uma parte da string com base no índice

print(caceta[0:-6], len(caceta)) #vai do 0 ate o indice 5 (6-1)
#a funcao len serve para ver o comprimento do conteudo da variavel 

print(caceta[0:-6:2]) #vai do 0 ao 5 pulando de 2 em 2

print('ata' in caceta) #nao tem 'ata' na variavel caceta

print(caceta[::-2]) #inverte de trás para frente

try:
    kaskkhsa        #try vai verificar verificar o código e se houver algum erro,
                    #jogara para except. oq eu digitei daria erro, então ele ignorará o erro e vai para except
except:
    print('deixe de canecagem')


CONST = 10
print(CONST)

CONST = 20 #errado!!!!!
print(CONST)
#o coidigo acima é mutável, mas como a variavel está completamente em maiúsculo, os dev considera conts
#pois não existe constante no python

velocidade_do_carro = 61
km_do_carro = 100 #posição do carro na estrada

RADAR_1 = 60
POSICAO_RADAR = 100
RADAR_RANGER_MULTAGEM = 1


#essa barra é um indicativo para continuar na outra linha
# \
 
if km_do_carro < (POSICAO_RADAR + RADAR_RANGER_MULTAGEM) and \
   km_do_carro > (POSICAO_RADAR - RADAR_RANGER_MULTAGEM) \
   and velocidade_do_carro > RADAR_1:
        print('tomou no papero ')
#para não ficar com muitas ifs, vamos fazer assim:

velocidade_do_carro = 60
km_do_carro = 100 #posição do carro na estrada

RADAR_1 = 60
POSICAO_RADAR = 100
RADAR_RANGER_MULTAGEM = 1

RANGER_PRA_MAIS = km_do_carro < (POSICAO_RADAR + RADAR_RANGER_MULTAGEM)
RANGER_PRA_MENOS = km_do_carro > (POSICAO_RADAR - RADAR_RANGER_MULTAGEM)
RESULTADO_RANGE = RANGER_PRA_MAIS is True and RANGER_PRA_MENOS is True

if RESULTADO_RANGE is True and velocidade_do_carro > RADAR_1:
    print('Tu realmente é um lascado e ta devendo ao governo slk')
else:
    print('parabéns, você não foi roubado! No entanto, o governo irá te roubar de outra forma >)')

#id e a identidade do valor guardada na memoria
#por exemplo, quando uma variavel é declarada, ela gera um id, que é armazenado na memoria
# e é possível acessar, e é assim que o python busca esse elemento na memoria
carambolas = 10
print(id(carambolas))

carambolas = None


print(carambolas is None)# o is tem o mesmo sentido do == e o nome é um valor não declarado
# tem também o not none e o is none para inversão. 
 
 #tipod built-in -> são os tipos que já vem com o python, como str, int
 #além disso, str, int, etc são tipos imutáveis, ou seja, que não podem ser mudados ao decorrer do código
 
whilee = True
while whilee: #laço while -> enquanto essa condição for verdadeira, execute o conteúdo abaixo dentro da identação
    print('ha')

    whilee = False #quebra o while de cara
    break #busca o while mais próximo para interromper a sua repetição 

contador = 0
while contador < 10:
    print(contador)
    contador = contador + 1 #uma forma de controlar o while
    #contador +=1 é mais prático
    #operadores de atribuição simplificado:
    # = += -= *= /= //= **= %=

contar = 0
while contar <= 10:
    print(contar)
    contar +=1

    if contar == 6:
        print('não vou mostrar o 6')
        continue #esse tal de continue é utilizado para caso seja necessário retornar para o início do laço
        # continue também é utilizado para o while mais próximo

contar = 0
while contar <= 100:
    contar +=1
    if contar >= 30 and contar <= 60:
        print(f'não vou mostrar o {contar} hahahah')
        continue #de uma forma mais compreensível, ficaria desse jeito ai 
     
    print(contar)

caceta = 'caramba'
caceta = caceta.startswith('c') #pergunta se começa com c, é um método (true) 
print(caceta)

broca = 'Haha'
broca.lower().endswith('a') #método que verifica se termina com a (true )

caramba = 'te lascar meu mano'
i = 0
while i < len(caramba):
    print(caramba[i])
    i+=1 
else:
    print('O while tem else') #o else só não é válido quando o while é quebrado (break)

#para trocar o nome de todas as variáveis de uma vez, basta selecionar uma variável, marcar e apertar f2


linhas = 2
colunas = 2
 
linha = 1
while linha <= linhas:
    coluna = 1
    while coluna <= colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1

texto = 'hahaha' #quando o valor da variável é previsível, basta utilizar o for no lugar do While
for teste in texto:
    print('caceta')

novo_texto = ''
for letra in texto:
    novo_texto += '*{}'.format(letra)
    print(novo_texto)
print(novo_texto)

#range -> início, fim, intervalos(pula de quantos em quantos)
for ha in range(10): ... #vai de 0 até 10
for kk in range(0,4): ... #vai de 0 até 4
for kaka in range(0, 4, 2): print('caceta') #vai de 0 até quatro pulando de 2 em 2
    
for paridade in range(0, 100, 2): print(paridade) #pego todos os pares de 0 até 98

# iterável -> que entrega uma coisa por vez (str, range, etc) (__iter__)
#iterador -> busca quem é o próximo valor
#iter -> busca o interador 
#método uma ação que vou chamar para o meu objeto, ex:
peste = 'aaa'
peste.upper() #isso é um método

#demonstração de como o for funciona por debaixo dos panos aula 74:
testando_slk = 'caceta'

iterador = iter(testando_slk)

print(iterador) #aqui informa o iterador por causa da funcção iter
print(next(iterador)) #Quando a função next é chamada, ele faz uma busca no valor 
#armazenado na variável testando_slk e retorna um iterável, ou seja, um único valor.
#no entando, ele precisa fazer isso várias vezes para retornar os próximos valores, por exemplo:
print(next(iterador)) #aqui ele já buscou o segundo valor testando_slk[1] e o retornou.
print(next(iterador)) #[2]
print(next(iterador)) #[3]
print(next(iterador)) #[4]
print(next(iterador)) #[5]
#print(next(iterador)) #[6] No 6, como não há mais nada, ele vai alegar um b.o de StopIteration
#daí no for é tratado com um try e except, onde o valor de except é fechado com um break.
#veja no exemplo abaixo com um while :

while True:
    try:
        print(next(iterador)) #a repetição vai rolar normalmente
    except StopIteration: #quando o problema StopIteration ocorrer:
        break #o for acaba 

#fim da explicação de um for 

for i in range(10):
    if i == 2:
        print('vamos pular o 2')
        continue

    if i == 8: 
        print('nada mais vai executar')
        break
    for j in range(0, 1):
        print(i, j)
os.system('cls')
#uma lista é mutável, diferente de uma str
#duas formas de criar uma lista:
#Além disso, posso colocar diferentes tipos primitivos numa lista. Por ex:
caceta = list()
caceta = ["carai", 1015, True, 4.5, ['slk', 10]] #forma convencional
#e como visto no exemplo acima, posso usar uma lista dentro de outra lista
print(caceta)
print(caceta[4]) #acessando o conteúdo na lista dentro de outra lista. 
print(caceta[0].upper()) #utilizando métodos na list

del caceta[0] #del irá detetar um elemento da lista com base no índice. Nesse caso, irá deletar o "carai"
print(caceta) #o indice 0 agora é o 1015

caceta.append('mais um') #adiciono mais um elemento no final da lista 
print(caceta)

caceta.pop() #remove o último elemento da lista
print(caceta) #não existe o 'mais um'

caceta.pop(0) #quando eu coloco um índice nos parenteses, ele remove da lista com base nesse índice
print(caceta) #removeu o 1015

teste = caceta.pop() #uma forma de encontrar e salvar o último valor da lista
print(teste[-1]) #outra forma de encontrar o último item da lista
print(teste)

caceta.insert(0, "carai") #adiciono um item com base no índice sem apagar o anterior(o valor armazenado anterior anda um índice para frente)
print(caceta) #o "carai" agora está no índice 0

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b #os elementos de ambas as listas se misturam, formando apenas uma lista.
lista_a.extend(lista_b) #ele incrementa os valores de lista b na lista a

print(lista_c) #concatenado 
print(lista_a) #juntado

caceta.clear() #utilizado para limpar a lista completamente
print(caceta) # a lista agora está vazia

#dados mutáveis tem que tomar cuidado, pois por mais que o código de reatribuição venha depois,
#ele vai acabar alterando em ambas variáveis, como no exemplo abaixo:
mais_lista_a = [10, 20 ,30]
mais_lista_b = mais_lista_a

mais_lista_a[0] = 40 #no caso de uma imutável, o índice 0 para b ainda seria o 10, mas como lista é 
#mutável, acabou mudando juntamente com a variável a
print(mais_lista_b)

mais_lista_b = mais_lista_a.copy() #mas, fazendo desse jeito, esse problema é resolvido, mantendo o valor
#inicial daqui pra cima da lista a.
mais_lista_a[1] = 'caceta'

print(mais_lista_a) #como pode ver, mudou apenas na lista a.
print(mais_lista_b)

#o list também é um iterável, por ex:
for __ in mais_lista_b:
    print('carai') #lista a tinha 3 elementos, então vai se repetir 3 vezes.
#testes
for __ in 'teste':
    print('hahaha')

for aa in __:
    print('putz')
#fechamento dos testes

os.system('cls')
#ex rapido
nomes = ['joao', 'Maria', 'Carmelita']
nomes.append('carai')
nomes.append(456)

indices = 0
for __ in nomes:
    print(f'{indices}, {nomes[indices]}, {type(nomes[indices])}')
    indices+=1

#ex rapido fechamento
#desempacotamento

#no caso abaixo eu crio uma lista com três elementos 
peste = ['carai', 'mermao', 'marcos_gay']
#abaixo, novamente, eu crio três variáveis seguidas e coloco para se atribuirem com base no valor acima
telasca1, telasca2, telasca3 = peste

#quando eu imprimir uma dessas variaveis, ela virá sozinha. Isso é o desempacotamento
print(telasca3)

#um jeito mais fácil:
carambaa, bandido = ['porra', 'marcas']
#também é um desempacotamento e tem q ter a mesma quantidade de valores e variáveis, se n dá pau
print(caramba, bandido) 

#se eu quiser apenas um valor:
bunda_de_loki, *_ = ['Juliano', 'Carro', 'Bilau']
print(bunda_de_loki,'\n', _) #no caso, bunda de loki tem apenas Juliano e _ tem carro + bilau, entando ambos empacotados numa lista ainda. 
os.system('cls')


#tuplas - lista imutável 
tinta = 'carro', 'casa' #tupla declarada
tinta = ('carro', 'casa') #uma forma mais bonita de criar uma tupla
peste = [10, 20 ,30] #lista criada

#a tupla é um pouco mais rápida que a lista, então, se eu precisar trabalhar com algo do tipo e não
#precisar alterar elementos na lista, é melhor utilizar a tupla.

print(tinta[0]) #mesmo jeito que usa a lista 
peste = tuple(peste) #conversão de list para tupla
print(type(peste)) #agora é tupla
peste = list(peste)
print(type(peste)) #agora é list

#uma forma mais fácil de resolver aquele exercício rápido:
#aula 89
bundao = ('treta', 'xablau', 'carai')

te_lascar = enumerate(bundao)
print(te_lascar, '\n') #será apresentado um código doidão, mas tipo, é só usar o next que fica tudo de boa

for __ in bundao:
    print(next(te_lascar)) #resolvido

print('teste\t teste \n') #assim como o \n é para quebra de linha, o \t é para um tab

num_1, num_2 = 0.1, 0.2
num_3 = num_1 + num_2
print(num_3) #como pode ver, essa soma retornou um número float gigante na tela, e isso é comum no python e em outras linvuagens
#para tratar isso, seria interessante utilizar o :.1f,ex:
print('{:.1f}'.format(num_3)) #retornará apenas 0.3
#outra forma:
print(round(num_3, 2))#coloco a variavel e o numero de decimal (arredonda)
#outra forma quando precisa de todos os números da float:
import decimal
num_1, num_2 = decimal.Decimal('0.1'), decimal.Decimal('0.2') #tem que colocar como string
num_3 = num_1 + num_2
print(num_3) #retorna a conta certinha

frase = ' minha caceta, é da boa'
quebrartudo = frase.split() #caso não haja nenhum argumento, a minha string acabará se tornando uma lista a cada espaço
print(quebrartudo)

comecacaceta = frase.split(',') #vai dividir a minha string para lista a partir da vírgula
print(comecacaceta)

print(frase.strip())#corta os espaços no início e fim da minha string
#rstrip corta o espaço da esquerda e rstrip o da direita

#lembre-se que quebrar tudo é uma lista agora.
print(quebrartudo) #veja
#se eu quiser unir todo mundo novamente, basta usar o join
print( ' '.join(quebrartudo)) #dentro das aspas simples eu coloco o separador, se não tivesse nada, iria ser convertido para str, mas tudo ficaria agarradinho

salas = [ #lista dentro de lista
    #0          #1
    ['Carlos', 'André'], #0
    #0          #1
    ['juliano', 'Carlão'], #1
    #0
    ['Coroi', (10, 20, 30)] #2 também consigo incrementar uma tupla dentro da lista

]
print(salas[1][1]) #irá ser printado carlão
print(salas[2][1][2]) #imprimindo o 30 presente na tupla


for sala in salas: #para cada itens na variável salas
    for aluno in sala: #percorra todos os elementos e armazene em "sala"
        print(aluno) #exiba os elementos um a um

os.system('cls')
#caso a mais do desempacortameto
a, b, c , *_ = 'caceta', 'xablau', 10, 20, 40 #no caso, estou desempacotando os três primeiros e o resto eu guardo no _
print(a,b,c)
print(_) #esses valores ainda estão empacotados

#mas e se eu quisesse pegar o último valor e empacotar o resto?
a, b, *_, c = 'caceta', 'jão', 10, 30
print(a, b, _, c) #basta colocar o *_ antes e depois continuar escrevendo

a,*_, b, c = 'caceta', 'jão', 10, 30#posso pegar qualquer valor e gaurdar como resto, basta eu adicionar o *_ no lugar
print(a, b, _, c)

#outras formas de desempacotar
lista = ['caceta', 'jão', 10, 30]
print(lista) #aqui vai sair uma lista
print(*lista) #aqui vai sair um "str"

for __ in lista:
    print(__, end=' ') #desempacotamento sem quebra de linha

print('\n\n')
#lembrnado que o sep é o separador, e que em alguns casos, para facilitar, posso utilizar um \n como separador.
#ex:

terracota = [
    ['caceta', 'terra'],
    ['bora canecadaa', 'que bandidagem'],
    ['bora canecadaa', 'que bandidagem', ['caceta', 'terra']],
]
print(terracota) #meio bagunçado de entender

print( *terracota, sep='\n') #mais fácil 

#operação ternária = if e else em uma linha
terra = 10
print('Marcos deu' if terra > 8 else 'Marcos não deu. (ainda)' )

terraslk = terra = 40 if True else print('teve como não') #terra será 40. Se não fosse, o print demonstrado seria armazenado na variável
print(terraslk)

print('Marcos é gay' if 10 == 11 else'ainda ta virando. ' if 20 == 20 else 'que ferrado') #uma continuação no if, com if se. mas é confuso em uma linha só.

#uma forma de tratar o cpf
cpf = '568.145.545-00'
cpfint = int(cpf.replace('.', '').replace('-', ''))
print(type(cpfint))

#outra forma de tratar o cpf
import re #expressão regular em inglês
cpf2 = re.sub(r'[^0-9]', '', '582.752.544-45')  
#esse re.sub vai fazer uma coleta. No caso, vai coletar apenas 9 números inicialmente
#qualquer espaço ou letra qualquer, será substituida pelo que estiver dentro das ''. No caso acima, será substituida por nada.


print(cpf2) #aqui temos o cpf tratado, porém, é str

#código prosidural = executa da esquerda para direita, de cima para baixo

#parar execução do código
import sys 

for kakak in range(20):
    print('minha caceta', kakak)
    if kakak == 12:
        sys.exit() #quando kakak for == 12, o código é finalizado
#numeros aleatorios
os.system('cls')

import random
print(random.randint(0, 10)) #vai gerar um número aleatório de 0 a 10

 