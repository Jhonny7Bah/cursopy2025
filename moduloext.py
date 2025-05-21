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