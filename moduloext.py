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

