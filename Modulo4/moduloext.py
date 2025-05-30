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
print(calendar.day_name[calendar.weekday(2025, 5, 31)])
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
        print(pastas)