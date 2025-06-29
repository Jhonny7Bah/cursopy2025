from funcao_soma import soma
print(soma(40,20))
##acima eu fiz a importação de um módulo demonstrando o uso do __name__

###############################################################
##módulo datetime, utilizando principalmente para data e hora
##documentação -> https://docs.python.org/3/library/datetime.html
from datetime import datetime
#lembrando que é o segundo módulo datatime, já ambos tem o mesmo nome.
data = datetime(2025, 5, 21, 17, 48) #aqui eu posso inserir na mão a data e a hora.
#Ademais, posso inserir horas, minutos, segundos, etc.
#2025 = ano, 5 = mês (maio), 21 = dia; 17 = hora, 48 = minuto
print(data)

#Outra forma de fazer isso é passando a data e a hora diretamente de uma string. Veja:
data_str_data = "2025-05-21 17:54:00"
#acima eu declaro a data e a hora como devem ficar. 
#No entanto, ela também deve armazenar um formato. Para isso, é relevante consultar a documentação, mas irei fazer um breve resumo.
#Directive (Diretiva) é um símbolo que acompanha uma letra, caracterizando uma ação. Ex:

# %Y -> simboliza o ano, contendo 4 dígitos; %m -> simboliza o mês; -> %d simboliza o dia
# %H -> Simboliza a Hora; %M -> Simboliza o Minuto ; %S -> Simboliza o segundo;
# Um detalhe importante é que o formato da letra diferencia. Ou seja, se está maiusculo na documentação, não coloque minúsculo. Caso contrário, o cod quebra.

#agora, vamos formatar seguindo o padrão.
data_formatada = '%Y-%m-%d %H:%M:%S' #no nosso caso,a formatação tem que ser exatamente dessa forma

#isso foi necessário para utilizar o método strptime e assim que necessita tanto da formatação normal como da diretiva.
data = datetime.strptime(data_str_data, data_formatada)
print(data)
#não sei a utilidade do strptime ainda, mas logo saberei!!

######
#posso utilizar o método now do módulo datetime para obter a data e hora nesse exato momento também.
data_e_hora_agora = datetime.now()
print(data_e_hora_agora) #como pode ver, deu certinho.

#com o método now eu também posso ver a data e a hora em outros países.
# isso é possível devido ao timezone, que é uma divisão geográfica que determina o horário local da região.
#para fazer isso do timezone como argumento, vou precisar importar o módulo pytz, juntamente com o types-pytz, que o types-pytz serve apenas para trazer a sintaxe do pytz para o vscode. sendo:
# pip install pytz types-pytz

#https://en.wikipedia.org/wiki/List_of_tz_database_time_zones 
# no site acima é possível saber o timezone de cada país. 

from pytz import timezone #importo timezone
data_e_hora_em_tokyo = datetime.now(timezone('Asia/Tokyo')) #coloco timezone como argumento para now e dentro de timezone eu faço a indicação do lugar
print(data_e_hora_em_tokyo) #agora eu sei as horas de Tokyo!!

###algo muito interessante é que caso você queira incrementar um horário atual através do datetime e coloca um outro timezone, é possível!

combinacao = datetime(2025, 5, 23, 21, 35, 0, tzinfo=timezone('Asia/Tokyo'))
#ou seja, informo a data, depois a hora e por fim, chamo o parâmetro tzinfo e coloco o datetime respectivo como argumento.
print(combinacao) #fazendo isso ele entende que essa data e hora é correspondente a data e hora lá de Tokyo em si. No entanto, nesse exato momento, eu tinha colocado a data e hora do Brasil.

#################fora isso, também existe o timestamp (marca temporal), tendo início em 1970, onde os segundos começaram a ser contados daquela data e são até hoje.
#é útil para servidores, base de dados, windows, etc.
criado_data = datetime.now()
print(criado_data.timestamp()) #1748047417.558204 #isso é no momento que executei o código
#acima ele vai mostrar o número contados até hoje iniciando do dia 01/01/1970
print(datetime.fromtimestamp(1748047417)) 
#e através do método fromtimestamp, quando eu colocar o número de segundos, irei saber que dia e que horas era aquele. BEM TOP

#####################
def cls():
    from os import system
    system('cls')
    ##limpandno
# aula 276
#é possível comparar com operadores lógicos as datas.
fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/05/2025 10:15:00', fmt)
data_fim = datetime.strptime('23/05/2025 23:05:00', fmt)
print(data_inicio > data_fim) #como viu, posso comparar.
print(data_fim - data_inicio ) #dá pra tirar a diferença entre os dias (3 days, 12:50:00)
#o que ele retornou nada mais foi que um time delta, lembrando que delta significa variação. 
#se eu quiser pegar um valor mais específico da diferença, basta:
diferenca = data_fim - data_inicio
cls()
print(diferenca.days) #pego apenas os dias referenciais
print(diferenca.seconds) #pego apenas os segundos referenciais
print(diferenca.microseconds) #pego apenas os microsegundos referenciais
#digo referencial porque são os valores de acordo com a diferença e não os totais.
#caso eu queira os segundos totais, vou precisar do método total_seconds.
print(diferenca.total_seconds()) #agora ele retorna os segundos totais!

###############
# https://docs.python.org/3/library/datetime.html#timedelta-objects
#documentação do timedelta
# caso eu queira criar um datetime, ou seja, definir uma quantidade de dias ou horas, basta:
from datetime import timedelta #importar o módulo timedelta
d1 = timedelta(days=10) #passar a quantidade de dias, horas e segundos
print(d1) #apenas 10 horas
d2 = timedelta(hours=5) #passei 5 horas para d2
print(d2) #apenas 5 horas
#se eu quiser somar eu posso
print(d1+d2) #ficará 10 dias e 5 horas!

cls()
######Documentação do dateutil
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
#o dateutil permite faz as mesmas coisas que o timedelta, porém ele faz de forma mais rápida e direta.
#para fazer uso dele, também será necessário instalar o módulo, através do comando:
# pip install python-dateutil types-python-dateutil
# e para importar
from dateutil.relativedelta import relativedelta
data_fim = datetime.strptime('23/05/2025 23:05:00', fmt)
print(data_fim + relativedelta(seconds=60))
print(data_fim + relativedelta(hours=20))
print(data_fim + relativedelta(days=20))
print(data_fim + relativedelta(day=1))
print(data_fim + relativedelta(microseconds=2000))
#como pode ver, posso incrementar inúmeros valores e tenho mais possibilidades para argumentos.
#se você for no meio dos () do relativedelta e apertar ctrl + espaco, irá ver mais opções.
diferenca_exata = relativedelta(data_fim,data_inicio) 
print(diferenca_exata) #aqui ele irá descrever com exatidão a diferença de anos, meses, dias, horas, minutos, etc.
print(diferenca_exata.days) #posso filtrar tbm para ver apenas a diferença em dias.

cls()
######uso do strftime
#esse método, da biblioteca datetime, é utilizado quando você quer formatar uma data ou hora. Ou seja, você já tem o time definido e quer fazer uma alteração 
# no formato. Ex:
horario_atual = datetime.now() #essa é uma situação que o horário já vem definido.
print(horario_atual) #como pode ver, veio com microsegundos e seguindo o padrão americano, correto? mas e se eu quisesse alterar o formato para ptbr?
horario_fmt_ptbr = horario_atual.strftime('%d/%m/%Y %H:%M:%S')
#acima eu utilizei o horário atual como referência e chamei o método strftime. Com isso, o argumento que irei passar lá dentro é o formato que eu desejo. Esteja ele em uma variável ou definido com hard coded, como no código acima. 
print(horario_fmt_ptbr) #como pode ver, alterei o formato.
#algo importante a constar é que através do uso do strftime, o objeto deixará de ser um inteiro e passará a ser uma string. Com isso, ficarei impossibilitado de realizar cálculos de tempo.
print(type(horario_atual)) #apontando para o objeto que não sofreu com o strftime, o tipo dele é dado como class.
print(type(horario_fmt_ptbr)) #já o objeto que sofreu com o strftime, ele é dado como str.

print(horario_atual + timedelta(hours=2)) #Logo, aqui eu posso fazer cálculo de tempo.
try:
    print(horario_fmt_ptbr + timedelta(hours=2)) #E como aqui passou a ser str, se eu tentar fazer a soma, o código quebra.
except TypeError:
    ...
#Caso eu queira fazer a remoção de uma diretiva, mantendo seu padrão inteiro, basta:
horario_int_fmt_ptbr = datetime(horario_atual.year, horario_atual.month, horario_atual.day)
#acima eu removi três diretivas em relação ao objeto horario_atual.
print(horario_int_fmt_ptbr) #veja na prática
cls()
caso2 = datetime(2025, 5, 24)
fmt_brl = '%d/%m/%Y %H:%M:%S' 
#acima eu declaro uma variável com o formato brl
print(caso2.strftime(fmt_brl))
#e uso o strftime para alterar o formato
caso3 = datetime.strptime('2025/05/19','%Y/%m/%d') 
print(caso3.strftime(fmt_brl))
#e no caso três eu faço também. 
print(caso3.strftime('%Y'))
#acima eu faço para se caso eu queira apenas o ano no formato str.
print(caso3.year) #caso eu queira o ano no formato int


cls()
###############
# Módulo calendar (calendário) e algumas de suas funcionalidades
## Usando calendar para calendários e datas
# Documentação do calendar: 
# https://docs.python.org/3/library/calendar.html

import calendar #o calendar é um módulo nativo do pyhton, ou seja, para utilizar, basta importar.
print(calendar.calendar(2025)) #o método calendar é utilizado quando eu quero ver no meu terminal o calendário do ano fornecido como argumento, que nesse caso, é o calendário de 2025.
#caso você queira saber apenas os dias de um mês em específico, basta:
print(calendar.month(2025, 5)) #agora irá aparecer no meu terminal o calendário de maio de 2025.
#caso eu queira o último dia do mês
print(calendar.monthrange(2025, 5)) #também informo o ano e o mês desejado.
#por fim, ele irá me retornar na tela o dia da semana onde o mês deu-se início e posteriormente, o dia do mês que mês vai acabar/acabou. 
#caso eu queira saber com exatidão o dia da semana, basta:
primeiro_dia, ultimo_dia = calendar.monthrange(2025, 5)
print(calendar.day_name[calendar.weekday(2025, 5, 31)]) #hard coded
#ou
print(calendar.day_name[calendar.weekday(2025, 5, ultimo_dia)])
#nesse caso, weekday vai pegar o último dia da semana.
#mas e se eu quiser o primeiro dia?
print(calendar.day_name[primeiro_dia]) # e aqui ele mostra o primeiro dia da semana.
#weekday vai retornar o dia da semana de uma determinada data, começando do 0, sendo 0 segunda e finalizando em 6, sendo 6 domingo.
cls()
###por fim, temos também o monthcalendar, que é retornado os dias de um mês especifico
mes_atual = calendar.monthcalendar(year=2025, month=5) #aqui ele vai retornar os dias do mes que escrevo esse codigo. 
print(mes_atual) #como viu, ele retornou uma lista dentro de uma lista, correto? juntamente com uns 0.
#a primeira tupla é equivalente a um mês
#a segunda tupla é equivalente aos dias da semana, é tanto que se você contar, vai perceber que há 7 dígitos.
for mes in mes_atual:
    print(mes) 
#E os zeros são dias do mês passado. Lembre-se que tem meses que não começam do 1 no calendário, pois maio no calendário começa dia 27. E como abril vai até 30, 30-27 = 3. É por isso que há 3 zeros ali no início. E como maio vai até 31 e essas tabelas tem 32 dígitos, ele acabou pegando o primeiro dia de junho e por isso que é 0.
#se eu quiser tratar, basta eu fazer o seguinte:
for mont in mes_atual:
    for dia in mont:
        if dia == 0:
            continue
        print(dia)
        #agora eu tratei. 

######################
#uso da biblioteca locale para tradução
#documentação da biblioteca:
# https://docs.python.org/3/library/locale.html
import locale #locale também é um módulo nativo do python
#vamos fazer um exemplo prático do locale
print(calendar.calendar(2025)) #imprimo o calendario do ano que me encontro, que como pode ver, está em inglês.
locale.setlocale(locale.LC_ALL, '') #agora faço uso do locale, onde:
#setlocale é o método que irá fazer a conversão.
# locale.LC_ALL é o que irei converter, é a Categoria. Nesse caso, será tudo, como monetário, tempo, número, etc.
# '' -> é o locale que ele vai utilizar. Ou seja, como nesse caso está vazio, ele vai fazer uso do locale padrão do sistema.
print()
print(calendar.calendar(2025)) #e como pode ver, agora está 
#caso eu queira saber qual é o locale que estou utilizando no momento, basta:
localee, codificacao_de_caracteres = locale.getlocale()
print(localee)#esse é o locale
print(codificacao_de_caracteres) #e essa é a configuração de caracteres, que sempre é recomendado colocar utf8, que não é o caso desse cara. 
#vamos reestruturar então:
locale.setlocale(locale.LC_ALL,'pt_BR.utf8')
print(locale.getlocale()) #como pode ver, agora está utf8. Porém, ele não pega mais uma locale ou configuração padrão do sistema, pois eu defini na mão.

##não sei no Windows, mas no MAC e Linux, para saber as locales disponíveis no sistema, basta utilizar o seguinte comando:
# locale -a
#esse -a indica para pegar todas. 
#intercionalização -> ver depois
#ainda tem muito a testar desse módulo.

###########################módulo os
# o módulo os é um módulo nativo do python. Ele fornece funções para que o python possa se comunicar com o sistema operacional.
# Documentação: https://docs.python.org/3/library/os.html
import os #é assim que eu faço a importação desse módulo.
os.system('cls') #a função system executa um código escrito em batch script, que é a linguagem utilizada pelo cmd. Caso você esteja no Shell ou no Bash, ele também vai executar, porém, tu vai ter que usa a linguagem nativa do ambiente. 

##uso do os.path
#já o os.path trabalha apenas com caminhos e não faz nenhuma operação de entrada/saida
caminho = os.path.join("D:\\","Ghost", "Usuário", "Pictures", "AnyDesk") #aqui ele reconhece o sistema operacional e junta todo mundo, como um caminho mesmo.
print(caminho) #como pode ver, o meu so é windows e por isso a barra utilizada foi "\"

#caso eu queira dividir novamente, basta utilizar o path.split()
print(os.path.split(caminho)) #nesse caso, será retornado uma tupla, sendo que o primeiro índice simboliza o diretório e o último índice simoliza o arquivo.
#posso fazer assim tbm:
dire, arq = os.path.split(caminho) #aqui eu desempacoto a tupla nas variáveis
print(dire, arq) #com isso, consigo segregar.

print(os.path.splitext(caminho)) #caso houvesse aqui um arquivo de fato, esse comando iria segregar o arquivo e o formato.
#Ou seja, através do código acima, se houvesse um arquivo.txt, este código iria retornar o arquivo junto com o diretório, no índice 0 da tupla e no índice 1 iria retornar apenas o formato (nesse caso seria .txt)

print(os.path.exists(caminho)) #verifica se o caminho existe. Se existir, retorna true. Se não, retorna false.

print(os.path.abspath('.')) #retorna o caminho absoluto de uma pasta. Nesse caso eu coloquei o '.' para fazer referência a pasta que me encontro no momento.

print(os.path.basename(caminho)) #retorna a parte final de um caminho, seja ele um arquivo ou pasta. é como se você fizesse um [-1] no diretório, pra pegar a última parte.

print(os.path.dirname(caminho)) #vai retornar apenas o diretório de um arquivo. Se houver um arquivo no final do diretório, esse arquivo não será retornado. 

print(os.path.isdir(caminho)) #retorna verdadeiro se essa pasta for um diretório

home = os.path.expanduser("~") #mostra a home/raiz no momento em que ele foi executado.
print(home)

print(os.path.dirname(__file__)) #pega o nome completo do arquivo atual.

def prevencao(): #coloquei dentro de uma função para não correr o risco de apagar alguma coisa.
    os.unlink('') #apaga o arquivo que você colocar aqui dentro
cls()

####uso do os.listdir
# é utilizado para navegar em caminhos
caminho_da_pasta = os.path.join('D:\\','Ghost','Usuário','Desktop','cursopy2025','Modulo4','listdirdemonstracao_imagens') #primeiro eu faço o caminho até a pasta que quero modificar
for item in os.listdir(caminho_da_pasta): #aqui eu já posso iterar dentro dela, através do lisdir(caminho)
    print(item) #aqui ele retornou o nome das pastas
    #no entanto, é perceptível que para entrar na outra pasta, vamos precisar fazer um outro for, ou quem sabe, uma função recursiva. Essa questão dele ter acessado apenas a primeira pasta é denominada de primeiro nível.
    #ademais, vou ter que criar um novo caminho com base no nome da pasta também, já que o caminho anterior é com base no caminho inicial da pasta.
    caminho_da_pasta_noutra_pasta = os.path.join(caminho_da_pasta, item)
    #e agora vamos iterar
    for pastas in os.listdir(caminho_da_pasta_noutra_pasta):
        print(pastas) #e agora eu consifo ver o caminho que nelas estão!


cls()
####uso do os.walk
#O walk é uma função que permite uma recursão dentro da pasta. Ou seja, ela consegue percorrer por todos os itens que nela estiver,
# sendo utilizada no lugar do listdir em alguns casos, quando é necessário percorrer por tudo. 
# Quando utilizada, ela gera uma sequência de tuplas, tuplas essas que são compostas por: Diretório Atual (root), uma lista de subdiretórios (dirs)
# e uma lista de arquivos com o diretório atual. (files.)
#no exemplo anterior para o listdir, ela acaba sendo mais útil.
##aula 284
caminho_da_pasta = os.path.join('D:\\','Ghost','Usuário','Desktop','cursopy2025','Modulo4','listdirdemonstracao_imagens') 
for root, dirs, files in os.walk(caminho_da_pasta):
    print('Pasta atual ',root) #mostra o caminho atual
    print('Pastas:  ',dirs) #mostra as pastas
    print('Arquivos: ',files) #mostra os arquivos
    #como viu, através de um for e para iterar por cada uma das pastas e arquivos, o walk foi mais útil

cls()
##########uso do os.path.getsize() e os.stat
##os.start por padrão pode lhe retornar a data da última modificação do arquivo, data de criação, tamanho, dentre outras coisas.
##documentação: https://docs.python.org/3/library/stat.html

#inicialmente, vamos iterar por cada elemento da pasta datravés do os.walk.
for bot, diret, arq in os.walk(caminho_da_pasta):
    for arquivo in arq:
        print(arquivo) #iterando por cada arquivo separadamente.
        caminho_completo = os.path.join(bot, arquivo) #definindo o caminho completo, juntando root atual com o arquivo atual no for.
        #para pegar o tamanho do arquivo
        print(os.path.getsize(caminho_completo)) # e aqui eu passo como argumento o caminho completo. Logo, descubrirei o tamanho do arquivo. 

        #agora, para utilizar o os.stat, basta:
        arquivo_info = os.stat(caminho_completo) # o argumento que você geralmente vai precisar passar aqui é o diretório completo.
        print(arquivo_info.st_size) #st_size vai pegar o tamanho do arquivo. Mas você também pode coletar outras coisas referente ao arquivo.
        # exemplos:
        print(datetime.fromtimestamp(arquivo_info.st_mtime)) #st_mtime mostra o timestamp da última modificação
        print(datetime.fromtimestamp(arquivo_info.st_atime)) #st_atime mostra o timestamp do último acesso
        print(arquivo_info.st_uid) #id do usuário dono do arquivo.


cls()

# ###################os + shutil para copiar aquivos.
# # Abaixo, irei demonstrar um exemplo prático de boa parte dos comandos que aprendemos ultimamente com a combinação de outro módulo - shutil 
#Como o objetivo é copiar os arquivos de uma pasta para outra, primeiro vamos definir o caminho da pasta que vamos copiar os arquivos. 
CAMINHO_ORIGINAL = os.path.join(os.path.abspath('.'), 'listdirdemonstracao_imagens') 

#agora, vamos criar uma outra pasta para mandar os arquivos copiados. Para isso, podemos usar o makedirs do os, no entanto, precisamos passar o caminho da nova pasta com seu nome como argumento.
#Logo, vamos definir o caminho da nova pasta.
NOVA_PASTA = os.path.join(os.path.abspath('.'), 'NOVA_PASTA')
#e por fim, criar a nova pasta.
os.makedirs(NOVA_PASTA, exist_ok=True) #este comando serve para criar uma nova pasta. ele apenas vai precisar do caminho como argumento.
#esse exist_ok vai servir para informar ao python se esta pasta já existe. Pois assim, o código não iria dar pau e nem tentar criar aquela pasta toda vez que o compilador passasse por essa linha. 

#para iterar pelos arquivos de forma fácil, podemos utilizar o walk, juntamente com um for.
def realizar_copia():
    for root, dirs, files in os.walk(CAMINHO_ORIGINAL):
        
        #como as pastas (dirs) estão empacotadas, para cria-las indivualmente, vamos precisar desempacotar.
        for dir_ in dirs:
            #como estamos no mesmo diretório que a pasta que iremos copiar, basta pegar as informações diretamente dela. No sentido que que como as pastas e subpastas serão as mesmas, bastaria utilizar um replace para segregar.
            caminho_novo_diretorio = os.path.join(root.replace(CAMINHO_ORIGINAL, NOVA_PASTA), dir_)
            #após isso, basta utilizar o método do makedirs para criar uma pasta já com o diretório e nome definidos
            os.makedirs(caminho_novo_diretorio, exist_ok=True)
        
        ##como os files vinheram empacotados, vamos precisar desempacotar. Por isso, vamos chamar outro for
        for file in files:
            #agora que os files já foram desempacotados, como o intuito é copiar um arquivo para outro lugar, vamos precisar coletar o caminho.
            caminho_e_arquivo = os.path.join(root, file) #o caminho completo será a concatenação do root com o nome do arquivo atual
            print(caminho_e_arquivo)     
            #para realizar a cópia completa de todos os arquivos, vamos precisar utilizar uma lógica com o replace
            #nesta lógica, pegamos todo o caminho que a antiga pasta tinha e incrementamos na nova, coletando assim os arquivos dos subdiretórios e todo o resto.
            caminho_novo_arquivo = os.path.join(root.replace(CAMINHO_ORIGINAL, NOVA_PASTA), file)
        
            #como o nosso intuito é copiar, vamos agora chamar o módulo shutil, lembrando que também é possível fazer isso com o módulo os.
            import shutil
            #e agora vamos chamar o método de cópia
            shutil.copy(caminho_e_arquivo, caminho_novo_arquivo) #vamos pegar de camiho_e_arquivo para mandar para caminho_novo_arquivo

def apagar_pasta_demontracao():
    #como vimos antes, para você apagar uma pasta, você precisaria do os.unlink. No entanto, se nessa pasta houver subdiretorios, eu teria que fazer isso recursivamente.
    # é por isso que existe uma função shutil que resolve todo esse esquema. o nome dela é rmthree. Fazemos assim:
    from shutil import rmtree
    rmtree(NOVA_PASTA, ignore_errors=True) #E esse ignore erros não vai quebrar o código caso a pasta não exista.
    #a partir de agora, a pasta já foi apagada.
# apagar_pasta_demontracao()

def copiar_pasta_demonstracao():
    #e se eu quisesse copiar uma pasta de um lugar para outro de uma forma muitoooooooo mais fácil, bastaria eu utilizar um método da shutil tbm
    from shutil import copytree
    #e através do copythree, realizo a cópia.
    copytree(CAMINHO_ORIGINAL, NOVA_PASTA)
    #é importante notar que caso a pasta já tenha sido criada, o código vai quebrar.

#para renomear ou mover shutil.move ou shutil.rename
#renomear e mover é a mesma coisa.
def renomear_demonstracao():
    from shutil import move
    #no primeiro argumento eu coloco a pasta anterior e posteriomente o novo nome/caminho que ela vai ficar. 
    move(NOVA_PASTA, NOVA_PASTA + 'CASAA')
# renomear_demonstracao()

#################################
# json.dumps e json.loads com strings + typing.TypedDict
# O módulo json já vimos antes. Porém, agora vamos aprofundar mais um pouco.
# 
# para importar o json:
import json
#  
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         falseAdd commentMore actions
# None          null

#uso do loads
#lembre-se que o load serve para fazer a leitura de um arquivo json. 
# Já o load também irá fazer a mesma coisa, porém, todo arquivo json deve ter sua tipagem como str. Ex:

#Aqui vou utilizar docstrings para facilitar a minha vida. Apesar da variável abaixo não ser um json, ela vai simular um.

#por enquanto, pule a importação abaixo e a classe.
from typing import TypedDict #inicialmente, vamos importar a tipagem
class Movie(TypedDict): #colocamos a tipagem na base da classe
    #e aqui, vamos passar o nome das chaves (key) e a tipagem esperada
    
    title: str #key = title e tipagem = str 
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float #essa barra significa "OU" OR. Ou seja, a tipagem aqui será None ou float

string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''
print(type(string_json)) #aqui ele vai acusar que é um str
try:
    json.load(string_json)
except AttributeError:
    print('Como viu, não podemos fazer com o load normal, pois todo o conteúdo é uma str')
    # perceba que o comando chama-se loads, onde "load" significaria carregar e o "s" significaria string
novo_tipo = json.loads(string_json)
print(type(novo_tipo)) #e agora, ele se torna um dicionário.

print(novo_tipo['title']) #quando fazemos algo do tipo, o vscode não consegue nos mostrar as keys presentes no dicionário
#é por isso que há um meio para conseguir resolver essa questão, através do módulo typing. Vá lá para cima, na declaração da classe.
#viu a lógica da classe? então agora vamos fazer o loads novamente, mas de uma forma diferente.

loads_com_tipagem : Movie = json.loads(string_json) #aqui indicamos a classe que a variável vai seguir
print(loads_com_tipagem['title']) # e agora já aparece, facilitando nossa vida.

#agora vamos para o dumps, que é semelhante ao dump.
#O intuito do dumps é pegar todo o arquivo e converter para o formato json.

json_string_new = json.dumps(loads_com_tipagem, indent=2)
print(json_string_new) #como pode ver, foi tudo convertido.

 
#um breve resumo sobre o dump e os load.
# O dump basicamente converte um arquivo que está em uma variável para json. Posteriormente,
# ele armazena aquela conversão em algum lugar, que no caso, vai ser em um arquivo json. Ou seja,
# ele abre um arquivo em modo de escrita para armazenar

# O load faz a conversão de um arquivo json para um código python, podendo ser dicionário, lista, str, etc.
# Considere que esse arquivo json se encontrará fora do python, abrindo um arquivo json em modo de leitura (famoso with open) 

# ou seja, pra ficar bem fácil: Se não tem um "s" no final, você está trabalhando com arquivo (o json vai ser lido ou escrito em algum arquivo)
# se tiver, você vai trabalhar com o json diretamente no código 

#Eu não fiz exemplo de uso porque já tem no código, tanto nesse módulo como em algum outro.

cls()
############################################################################
##path também é um módulo que trabalha com caminho, sendo semelhante ao submódulo de os.path
# referência: https://www.youtube.com/watch?v=T17BTNKBeJY&ab_channel=Ot%C3%A1vioMiranda

from pathlib import Path
caminho_projeto = Path()
print(caminho_projeto) #mostra o caminho relativo
print(caminho_projeto.absolute()) #mostra o caminho absoluto
print(caminho_projeto.resolve()) #também mostra o caminho absoluto, porém pode dar pau quando de trata de soft link (caminho de atalhos)

CAMINHO_ARQUIVO = Path(__file__) #mostra o caminho absoluto e também o arquivo. Isso ocorre por conta do __file__, pois a classe Path vai apenas dar a possibilidade de manipular o caminho posteriormente.
print(CAMINHO_ARQUIVO)
#IMAGINE PARENT COMO PASTA ACIMA
print(CAMINHO_ARQUIVO.parent) #Navega até a mãe do caminho. Ou seja, inicia a navegação do início e seu ponto de parada será final -1
print(CAMINHO_ARQUIVO.parent.parent) #Esse aqui é a mãe da mãe do arquivo. Ou seja, vai navegar até cursopy2025, que é o equivalente a final -2
print(Path.home()) #aqui eu consigo adquirir a home do usuário.

# _true_div_ -> verificar depois

#como se trata de um path, eu consigo também manipular caminhos
ideia = CAMINHO_ARQUIVO.parent
print(ideia / 'casa') #a barra da divisão pode ser utilizada para mostrar uma nova pasta
#Até aqui eu apenas manupulei o diretorio, sem criar pasta ou arquivo algum.
arquivo = ideia / 'comando.txt' #posso fazer isso para arquivos tbm
print(arquivo) 
#vamos criar esse caminho de acordo com o diretório acima
arquivo.touch() #com o método touch sobre a variável, ele vai criar o arquivo.
def apagar():
    arquivo.unlink() #isso aqui vai apagar o arquivo.
#coloquei dentro de uma função porque eu vou precisar dele 
arquivo.write_text("Olá mundo!!") #aqui eu consigo escrever dentro do arquivo.
print(arquivo.read_text()) #aqui eu consigo ler o que tem dentro do arquivo.

#o método de escrita acima só consegue escrever uma única vez. Ou seja, se você precisar escrever mais de uma
# coisa, ele vai apagar o que tinha antes no arquivo.
#nesse caso, seria mais interessante abrir um arquivo em modo de escrita através de um context manager
with arquivo.open('+a') as pd: #abrindo o arquivo em modo de leitura e escrita
    arquivo.write_text('\nMundo crueeeel!!!')
    print(arquivo.read_text()) # e assim iria seguindo!

#para criar um diretório, primeiramente temos que definir um caminho
CAMINHO_PASTA = ideia / 'demonstracao'
print(CAMINHO_PASTA) #como pode ver, inicialmente eu criei o diretório
# e com o método mkdir, eu consigo criar uma pasta a partir de um caminho.  
CAMINHO_PASTA.mkdir(exist_ok=True) # e mais uma vez, o método exist_ok é um meio para tratar o transtorno que vai ocorrer caso a pasta já exista.
#agora eu também posso criar uma subpasta
subpasta = CAMINHO_PASTA / 'vejafunfar'
print(subpasta) #subpasta criada na memória ram
#e agora vamos criar ela na memória rom
subpasta.mkdir(exist_ok=True) #tudo ok 
#e agora, vou criar um arquivo dentro da subpasta
novo_arquivo = subpasta / 'arquivo.txt'
print('novo_arquivo.txt') #acabo de criar o arquivo na memória 
#e agora vamos materializar
novo_arquivo.touch(exist_ok=True)
#vou colocar um conteúdo dentro dele 
novo_arquivo.write_text('Hey mano, suave na nave? ')
#e vou exibir pra você
print(novo_arquivo.read_text()) #como viu, tudo certinho!!

#tá, mas e se você agora quiser apagar a pasta demosntração, considerando que há subpastas e arquivos dentro dela?
#Utilizaria unlink, ou rmdir, correto? o unlink não iria funcionar por problemas de permissão e o rmdir também não porque a pasta não está vazia.
#ou seja, para apagar uma pasta dessa natureza, é necessário apagar seus subitens de forma recursivas, apagando cada elemento um a um e a última seria a pasta em si. 
#e um detalhe importante é que o unlink é comumente utilizado para apagar um arquivo.

#comentei porque não vai funcionar. 
# CAMINHO_PASTA.unlink()
# CAMINHO_PASTA.rmdir()

def removendo(root: Path, remover_root= True):
    #aqui eu vou iterar dentro do diretório do arquivo
    for file in root.glob('*'): #glob como'*' vai selecionar a todos
        #se na hora que o for estiver passando, file for uma pasta
        if file.is_dir():
            #apago a pasta
            file.rmdir()
        #se não for uma pasta, é um arquivo
        else:
            #aí eu apago o arquivo
            file.unlink()
    #e se você quiser apagar a raiz também, basta deixar como True e ele fará o serviço.
    if remover_root:
        file.rmdir()
#e aqui eu chamo a função.
# removendo(novo_arquivo)

# No entanto, se eu quisesse apagar isso da forma mais fácil do mundo, bastaria eu chamar a função shutil
def outro_meio():    
#um dos meios é através do shutil.
    from shutil import rmtree
    rmtree(CAMINHO_PASTA, ignore_errors=True) #isso aqui vai apagar de uma vez.
outro_meio() # e agora ela foi de arrasta

cls()

####################################
# Introdução ao CSV
# CVS -> Comma Separeted Values - Valores Separados Por Vírgulas
# é uma extensão que separa os dados em forma de tabela. Sendo que cada linha (i) representa uma linha da tabela
# e as colunas são separadas por vírgulas. 
#  Utilizada comumente em programas como excel, calc, sheets, etc. Para exportação ou importação de dados.
#Um arquivo .csv pode ser aberto em uma planilha eletrônica e também em um editor de texto.
#Quando você quer utilizar uma virgula dentro de uma célula, aspas duplas normalmente são inseridas para não gerar transtornos. 
# exemplo:

'''
nome, idade, sexo
Victor, 17, M
Joana, 19, F

'''

#agora com aspas:

'''
nome, idade, localidade, ocupação
João, 22, "Avenida D, 111", policial
Maria, 19, "Rua João da Mata, 110"

'''

#e na presença de aspas duplas, será necessários implementar duas aspas antes da palavra, ficandoa assim:
'''
nome, idade, endereço_completo
Pedro, 45, "Av.452, 18, ""Centro"""
Julieta, 56, Rua.110, 96, ""Interior""" 

'''
##################### Agora vamos praticar
#inicialmente, vamos criar um arquivo csv
from pathlib import Path #importar o path para apontar o caminho
caminho_atual = Path(__file__).parent / 'aula293.csv' #aqui eu pego o caminho absoluto, volto uma casa e aponto um arquivo
print(caminho_atual) #veja
caminho_atual.touch() #aqui eu faço a criação do arquivo.
#para manipular meu csv, vou precisar importar o módulo csv
import csv

######uso em casos de uma lista de dicionários
#essa será a minha lista de dicionários
lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]
#abro o arquivo em modo de escrita 
with open(caminho_atual, 'w') as arq_dict:
    nome_das_colunas = lista_clientes[0].keys() #primeiro eu pego as keys de cada dicionário pelo índice
    escrever_no_csv = csv.DictWriter(arq_dict, 
    fieldnames=nome_das_colunas) # e em fieldnames, eu passo as keys. Esse fieldnames é o parâmetro para o cabeçalho.
    
    escrever_no_csv.writeheader() #e agora incrementamos o cabeçalho.

    #porm fim, vamos incrementar os valores agr
    for clientes in lista_clientes:
        escrever_no_csv.writerow(clientes)
        # e tudo jóia!

#para escrever alguma coisa no meu csv, primeiramente eu vou precisar abrir o csv em modo de escrita.
with open(caminho_atual, 'w', newline='') as arq: #esse newline vazio vai prevenir que haja quebras de linha desnecessárias.
    #após isso, vou precisar informar os nomes das colunas de forma empacotadas, seja de lista, tupla, etc.
    nome_colunas = ['Nome', 'Idade', 'Sexo']
    #depois eu vou ter que apontar o arquivo em aberto, indicando que vou escrever
    escritor = csv.writer(arq, delimiter=',') #utiliza a vírgula como delimitador/separador padrão.
    #e agora utilizo o wirterow para escrever uma nova linha, informando o que quero escrever como argumento.
    escritor.writerow(nome_colunas)
    escritor.writerow(('Erick', 19, 'M'))
    escritor.writerow(('Joana', 18, 'F'))
    # e assim vai, inserindo dados.

####por fim, vamos ler os arquivos!
#para isso, basta abrir o csv em modo de leitura, sendo:
with open(caminho_atual, 'r') as read_csv:
    leitor = csv.reader(read_csv) #utilizo o reader para retornar em lista
    #mas como isso é um iterator, vou precisar utilizar um next ou iterar de uma vez com um for.
    #vamos chamar um next
    print(next(leitor))
    #agora vamos iterar:
    cls()
    for linha in leitor:
        print(linha) #aqui eu vejo os dados que lá dentro tem.
    #no caso acima, o retorno será em um formato de lista.

#no entanto, eu consigo fazer com que o retorno seja um dicionário também, sendo: 
with open(caminho_atual, 'r') as read_csv_dicionario:
    leitor_dict = csv.DictReader(read_csv_dicionario) #dictreader serve para indicar o retorno em dict
    for linha in leitor_dict:
        print(linha) #e como pode ver, ele também retornou os dados, porém no formato dict. 

cls()
##################################################################
# random tem geradores de números pseudoaleaórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
import random #assim importamos o módulo random

# o random funciona a base do random.seed com base nos segundos. Desse modo, ele consegue gerar valores de forma "aleatoria"
#porém, mesmo assim ainda é possível prever a saída, já que funciona com base nos segundos. É por isso que não é interessante utilizar para fins de segurança, como gerador de senhas ou algo do tipo.

#####uso do randrange
# random.randrange(inicio, fim, passo) é tipo o range, tendo início, fim e o pulo. Ou seja, se em pássp tivesse 2, o programa iria sortear os números pulando de dois em dois, que consequentemente haveria apenas números pares.
print(random.randrange(10, 20)) #vai sortear números aleatórios entre 10 e 20
print(random.randrange(10, 20, 2)) #vai sortear números aleatórios entre 10 e 20 pulando de 2 em 2

#caso eu não precise do step(passo), posso utilizar o randint
print(random.randint(10, 20)) #é a mesma lógica do randrange, porém é sem o step (passo.)

#caso eu quera gerar um número de ponto flutuante aleatório, basta:
print(random.uniform(10, 20)) #vai gerar um número aleatório com ponto flutuante entre 10 e 20

#caso você queira mudar a ordem de uma lista de forma aleatória
lista = [x for x in range(10)] #gera valores de 0 à 9 de forma crescente 
print(lista) #veja a ordem como tá agora
random.shuffle(lista) #utilizando o shuffle para embaraçar a lista original 
print(lista) #e como pode ver, a ordem agora é diferente
#Ou seja, pra ficar bem calro: O shuffle pode não ser uma boa as vezes por modificar a lista original.

#uso do sample, para coletar uma certa quantidade de valores aleatórios em uma lista 
lista2 = [x for x in range(10)] #gera valores de 0 à 9 de forma crescente 
novos_nomes = random.sample(lista2, k=2) #o parâmetro k é responsável por coletar o número de itens aleatórios que você quer pegar na lista
print(novos_nomes) #sempre que o código executar, ele vai pegar dois valores diferentes.
#e o retorno sempre será um outro iterável, sem repetição!

#uso do choices 
#o choices faz a mesma coisa que o sample. A única diferença é que o choices vai repetir valores.
#como a lista original não foi modificada no cod anterior, vou usar ela!
print(random.choices(novos_nomes, k=2)) #uma hora ou outra ele vai repetir.

#uso do choice
#o choice vai pegar um iterável de uma lista. 
print(random.choice(novos_nomes)) #pega apenas um valor aleatoraimente

cls()
###############################################################
#o módulo secrets é bem semelhante ao módulo random. No entanto, ele não funciona a base do seed, como o random
import secrets #importanto o secrets, que é nativo do python

print(secrets.randbelow(100)) #sorteia um número aleatório entre 0 e 99
print(secrets.choice([1,2,3])) #escolhe um único valor de uma lista

#para trabalhar diretamente com alguns métodos random, o secrets oferece o seguinte meio:
aleatorio = secrets.SystemRandom() #agora eu posso utilizar os métodos do módulo respectivo
#a partir de agora, posso utilziar qualquer método da função random. Ex:
print(aleatorio.randint(10, 20)) #como viu, deu certinho.
# Pesquisar depois -> time attack

#bom, mas e para gerar uma senha, que é o foco desse módulo?
#para facilitar, vamos importar a biblioteca string e obter todas as letras e pontuações possíveis do alfabeto.
import string
print(string.ascii_letters) #aqui você percebe a presença de todas as letras do alfabeto maiúsculas e minúsculas. 
print(string.punctuation) #aqui eu pego todas as pontuações possíveis
print(string.digits) # e aqui eu pego todos os números a base 10
#eu poderia ter feito tudo isso na mão, mas para agilizar, é melhor importar string que já dá isso pronto.

#agora, vamos juntar todos eles
juncao = string.ascii_letters + string.punctuation + string.digits
print(juncao)
#vamos definir a quantidade de dígitos que queremos
numero_de_digitos = 10 
#vamos colocar para pegar valores aleatórios
senha_list = aleatorio.choices(juncao, k=numero_de_digitos)
print(senha_list) #como viu, isso retornou como uma lista
#agora vamos juntar isso
senha_final = ''.join(senha_list)
print(senha_final) # e agora a senha está sendo gerada de forma aleatória.
#o código abaixo, quando colocada em um terminal, vai gerar uma senha alfanumerica de forma aleatória.
# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"

####################################################################################
# Falando um pouco mais sobre a library string
#string.Template para substituir facilmente varivaveis em texto. É como se fosse uma forma de fazer mala direta em python
# doc: https://docs.python.org/3/library/string.html#template-strings

from string import Template #importamos o submódulo

#criamos os dados que vamos passar no texto
dados = {
    'nome':'Pedro',
    'data_nascimento':'32/02/2000'
}

#depois criamos o texto
# Lembrando que se o texto estivesse dentro de um arquivo, seria possível pegar o contexto de lá,
#  abrindo o arquivo em modo leitura
#para colocar os espaços que serão substituídos, basta colocar cifrão ($) e posteriormente, o nome da key no dicionário
#para deixar mais organizado, posso colocar cifrão e chaves, sendo: ${key}
texto_pronto = '''
Olá, senhor ${nome}, nascido em ${data_nascimento}, 
Tudo bem com sua pessoas?
'''

#agora, basta criar uma variável, chamar a classe e apontar para o texto
template = Template(texto_pronto)

#e por fim, para fazer a substituição, basta chamar o método substitute e apontar o dicioário.
print(template.substitute(dados))

#no entanto, se houver algum campo no texto que não foi preenchido ou o contrário, o código quebrará.
#para garantir que isso não aconteça, temos o método safe_substitute, que vai tratar caso isso aconteça.
print(template.safe_substitute(dados))

#O delimitador padrão é o cifrão (#), mas se houver algum motivo muito esquisito, posso mudar o delimitador.
# Para isso, vou ter que criar uma classe recebendo como base a classe Template
class MyTemplate(Template):
    delimiter = '!'

#agora, vamos fazer um replace para trocar o cifrão pela exclamação
novo_texto = texto_pronto.replace('$','!')
print(novo_texto) #veja o texto trocado

#e vamos criar um novo template com base na nossa classe
Temp = MyTemplate(novo_texto)
#e por fim, vamos realizar o substitute. 
print(Temp.substitute(dados)) #agora, você fez a mala direta com o limitador exclamação ou de negação (!)
#Não é comum a troca do limitador. 

###############################################################
# Variáveis de ambiente são variáveis que se remete ao sistema operacional, como usuário, senha, host, etc.
#Normalmente temos três tipos de ambientes para o código, sendo o local, o de testes/produção (que normalmente é separado para testar algumas coisas) e o de desenvolvimento (quando o de teste dar certo e é enviado para o projeto principal).
#Digo isso, para se conectar a uma api, servidor ou a qualquer outra coisa que precise de credenciais, para não deixar isso exposto no código,
#  podemos fazer uma configuração através de uma variável de ambiente. SE ISSO FICASSE EXPOSTO NO CÓDIGO, QUALQUER PESSOA PODERIA LOGAR NO SERVIDOR OU API 

#-------------------------------------
#COMANDOS SHELL

#No windows, para criar uma variável de ambiente no powershell, basta digitar o seguinte comando:
'env:VARIAVEL="VALUE"'
#Posteriormente, basta colocar:
'dir env:' #e você vai ver todas as variáveis de ambiente, principalmente a sua
#detalhe -> como são variáveis de ambiente salva em memória ram, quando o terminal for fechado, essa variável de ambiente se perderá.
#-------------------------------------

#Para fazer isso em python, vamos precisar da biblioteca os.
import os
#para consultar uma variável de ambiente:
print(os.getenv('NOME_DA_VARIAVEL')) #caso ele não encontrar a variável de ambiente, será retornado None.
#considerando que essa variavel de ambiente está funcionando, para usar em um programa, bastaria aramzenar em uma variável do python. ex:
valor_ficticio = os.getenv('NOME_DA_VARIAVEL')

#para ver todas as variáveis de sistema, basta: 
print(os.environ)

#No entanto, fazer isso toda vez acaba sendo chato. É por isso que o dotenv do python existe!
# Doc: https://pypi.org/project/python-dotenv/
# python-dotenv é uma biblioteca Python que permite que você faça uso de arquivos de configuração para armazenar e acessar 
# as suas variáveis de ambiente de forma mais fácil e segura em seus projetos.

# Para utilizar o python-dotenv, basta instalá-lo com o pip e, em seguida, adicionar um arquivo chamado 
# .env na raiz do seu projeto.

# # Ative seu ambiente virtual
# pip install python-dotenv
# Esse arquivo deve conter as suas variáveis de ambiente e seguir o seguinte formato:

# # .env
# VARIAVEL_DE_AMBIENTE_1=valor
# VARIAVEL_DE_AMBIENTE_2=valor
# VARIAVEL_DE_AMBIENTE_3=valor

#Após instalar o dovenv, basta fazer a chamada do módulo
import dotenv

#acabei de criar na mão um arquivo denominado de .env
#acabei de colocar alguns arquivos no dotenv

#se você for mandar para um repositório no github, coloque esse .env no .gitignore

#agora vamos buscar o .env e carregar as variáveis de ambiente com base no arquivo
dotenv.load_dotenv() 

cls() #limpeza

#por fim, vamos exibir um valor que lá tem na tela:
print(os.getenv("DB_PASSWORD")) # e agora eu pego a minha senha.

#MAIS UMA VEZ, SE VOCÊ FOR COLOCAR ISSO NO GITHUB, O .ENV NÃO DEVE IR JUNTO.
# Nesse caso, você vai criar um .env de exemplo, colocar as mesmas variaveis e valores quaiquer. Vou fazer isso agora.

#Criei o .env-example
#coloquei o dotenv no gitignore
#coloquei valores no .env-example 

os.environ['nome'] = 'jao' #crio uma variavel de ambiente com python

###############################################
# Compactando arquivos com python
#Primeiro, vamos criar um arquivo. Como aqui já há inúmeros package de exemplo, vou reaproveitar o NOVA_PASTA (que nesse momento está vazia.)
#para iterar, vamos importar o módulo pathlib
import pathlib
DIRETORIO_ATUAL = pathlib.Path(__name__)
pasta_reaproveitada = DIRETORIO_ATUAL.absolute().parent / 'NOVA_PASTA' / 'arquivo.txt'

#agora, vamos escrever alguma coisa dentro dela.
with open(pasta_reaproveitada, 'w') as arq:
    arq.write('Olá, meu caro amigo!')

#Agora, vamos importar o módulo zipfile
import zipfile

#vamos criar um lugar para o nosso zip com o formato zip
CAMINHO_COMPACTADO = pasta_reaproveitada.parent / 'arquivo.zip'

#e vamos fazer um context de abertura com o zip
with zipfile.ZipFile(CAMINHO_COMPACTADO, 'w') as zip: #no primeiro argumento para o context, eu coloco o caminho para o meu zip
    def naotranstorno():
        zip.write(pasta_reaproveitada)#aqui eu coloco a pasta que ele vai compactar.
        #no entanto, fazer da forma acima pode gerar um transtorno. Pois, ele vai pegar e criar um caminho completo, desde a raiz até o final,ou seja, o meu zip
        # vai ter a mesma estrutura de arquivos que o meu.
    
    #para resolver isso, bastaria passar o nome do arquivo como segundo argumento.
    zip.write(pasta_reaproveitada, 'arquivo.txt') #agora vai aparecer normal.

#para descompactar, basta abrir em modo leitura
with zipfile.ZipFile(CAMINHO_COMPACTADO, 'r') as zip_read:
    print(zip.namelist()) #se eu quiser ver oq tem dentro do arquivo
    #para desempacotar, primeiro vamos fazer um caminho para ele
    DESEMPACOTAR_CAMINHO = pasta_reaproveitada.parent / 'desempacotar'
    def descompactar():
        #LEMBRE-SE DE OLHAR ISSO AQUI DEPOIS
        zip.extractall(DESEMPACOTAR_CAMINHO)#e agora ele está desempacotado.

#########curiosidade interessante:
# Se você digitar o caminho do ambiente virtual e depois der um pip install, você já automaticamente instala as dependências
# necessárias dentro dele. Ex:
# .venv\Scripts\activate -m pip install pandas



########################usualidade do sys.argv
#o método argv do módulo sys é útil para quando há um script que funciona com base na execução do módulo atual.
#Ou seja, se eu executar esse código em um cmd, eu precisaria navegar até a pasta e colocar moduloexp.py, logo este módulo iria executar.
#é aí que entra o argv, pois se ao invés de eu digitar apenas o nome do módulo, digitasse um argumento em conjunto? ex: moduloexp.py -a
# por padrão, nada iria acontecer. Mas eu posso fazer um código com o argv que fará com que algo aconteça se isso for feito.  

#primeiro, vamos importar diretamente o método
from sys import argv

def argsvdemonstracao():
    #abaixo, vamos printar o conteúdo em argv.
    print(argv) #percebemos que primeiro vem o móduloexp.py

    #vou para o terminal e digitar algo como "aoba"

    #o argv captorou e agora:
    print(argv)

    #como argv é uma lista, posso fazer da seguinte forma:
    if argv[1] == 'aoba':
        print("Vou apagar o seu system32!!")
    #logo, o código executa normalmente e essa condição será atendida! Daí, eu posso fazer n coisas. 
    #e assim vai, passando os argumentos para o script python.

####################################################
# No caso acima, foi explicada uma forma de passar argumentos de forma simples. Baixo, vou mostrar outra forma, forma essa que será mais robusta.
# https://docs.python.org/pt-br/3/howto/argparse.html
#Aula 307

#Importando o módulo, que por sinal, já é nativo.
from argparse import ArgumentParser

#inicializando a variavel que será responsável por armazenar a classe
parseamento = ArgumentParser()

# Denominando os argumentos, passando os parâmtros necessários para a execução do comando 
parseamento.add_argument('-b', #abreviação
                        '--basico', #nome
                        help='Olá mundo na tela!',
                        type=str, #tipo esperado pelo código
                        metavar='STRING', #informação de tipo para o usuário
                        default=None, #passando valor padrão
                        required=False, #Se true, o usuário é forçado a passar esse argumento.
                        #OS DOIS PARÂMTROS E ARGUMENTOS A SEGUIR IRÃO RETORNAR UMA LISTA
                        # nargs='+', #recebe mais de um valor. ex: moduloext -b "a" "b" "c"
                        # action='appned' #recebe o valor mais de uma vez ex: moduloext -b "a" -b "b" -b "c"
                        )

#inicializando os parâmetros, passando a possibilidade de receber argumentos
argumentos = parseamento.parse_args()

#Agora, eu posso manipular oq vai rolar
print(argumentos.basico) #por padrão, se o argumento não for inserido, é retornado none. Esse padrão pode ser alterado na definição do parâmetro.

#com isso, posso fazer um controle.
if argumentos.basico == None:
    print('nada digitado')
else:
    print('O valor que você digitou foi: ',argumentos.basico)

# ESSE é apenas o basicão doq dá pra fazer com esse módulo!


##################################################################################
# Procolo HTTP - HyperText Transfer Protocol (Protocolo de Transferência de Hiper Texto) é um protocolo utilizado
# para enviar e receber mensagens na internet. 
# Web scarping (Raspagem de dados) - busca de dados na internet

#Mensagem de requesição do Cliente pode ter:
# Método http:
    # leitura (safe): get, head, options
    # escrita: post, put, patch, delete
#Normalmente, os modos de escrita vão com um corpo.
# 
# Para fazer uma requesição get, basta colocar a url (endereço) do servidor em um navegador (exemplo) e o que retorna será os dados enviados pelo servidor.
# Quando acessamos um site e vamos navegando dentro dele, a url vai mudando com uma / lá em cima. Essa / é a rota
# 
# Há casos também em que vamos acabar precisando de um cabeçalho, principalmente se for para mandar uma chave para acessar as informações que lá estão. 
# Cabeçalho -> (Content-Type, Authorization)

# A mensagem de resposta do servidor deve incluir dados como:
# - código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# - Os cabeçalhos HTTP (Content-Type, Accept)
# - O corpo da mensagem (Pode estar em vazio em alguns casos)
