from datetime import datetime, timedelta
from json import load
from armazenar_no_banco_de_dados import path

with open(path, 'r') as read: #fazendo a leitura da base de dados
    database = load(read)
fmt = '%d-%m-%Y %H:%M:%S'

add_one_day = datetime.fromtimestamp(database[0]['Time']) + timedelta(hours=3, minutes=13)
#obtendo a hora que a pessoa inseriu seus dados na planilha e adicionando mais um dia
formato_no_microseconds_base = add_one_day.strftime(fmt)
#convertendo para o nosso formato de dia e horas, removendo os microsegundos
#acima é o formato da dia e hora agora, porém sem os microsegundos tbm

print(formato_no_microseconds_base)
while True:
    moment_now = datetime.now().strftime(fmt)
    if formato_no_microseconds_base == moment_now:
        print('Olá, fulado! Tudo bem? ')
        break