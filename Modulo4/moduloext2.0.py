#####################
def cls():
    ##limpando terminal
    from os import system, name
    if name == 'posix':
        return system('clear')
    return system('cls')
# Continuação...

# Web Scraping com Python usando requests e bs4 BeautifulSoup
# Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# Instalação
# pip install requests types-requests bs4

import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url) #busco o html
raw_html = response.text #faço o retorno
#e aqui eu já começo a fazer a raspagem
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# caso você quiser o título, basta executar essa funcao
def exemplo():
    # tô verificando se é None porque pode retornar duas coisas, sendo: None e o valor.
    if parsed_html.title is not None:
        #e aqui eu pego o título do texto da página
        print(parsed_html.title.text)


selecao_qualquer = parsed_html.select_one('#default > div > div > div > div > div.page-header.action > h1')
# print(selecao_qualquer)
#se eu quiser saber quem é a tag mãe dele:
print(selecao_qualquer.parent) # é o div a tag mãe.

####################Explicação de termo
# Dangling comma	(vírgula pendurada) ou Trailling comma (virgula final) nada mais é que uma prática realizada
# para deixar uma vírgula após o último elemento de uma lista, tupla, etc... EX:  
v0 = (1,2,3,4,)
v1 = [0,1,2,]
#como pode ver, funcionou normalmente.
# Dizem que deixa o código mais organizado e facilita na hora da leitura,
# Na hora de duplicar, ajuda também. 
print(v0,'\n',v1)

###########################################################################
## Selenium
# https://selenium-python.readthedocs.io/locating-elements.html
# Primeiro, vou precisar instalar um driver para uso. Como utilizarei o compre, com base nos requesitos do meu sistema,
# devo fazer a procura no seguinte site: https://developer.chrome.com/docs/chromedriver/downloads
# Agora, preciso instalar o selenium com o seguinte cmd:
# pip install selenium
def selenium1(): #coloquei dentro de uma função para não automatizar após a execução
    #agora, vamos chamar o módulo selenium
    from selenium import webdriver
    # Além do selenium, vamos precisar do service, que é um outro módulo complementar do selenium
    from selenium.webdriver.chrome.service import Service

    #agora, vamos precisar definir o caminho da pasta atual. Para isso, precisaremos do módulo path inicialmente
    from pathlib import Path
    #agora, vamos definir esse diretório
    PASTA_ATUAL = Path(__file__).parent
    #agora, vamos criar uma para o chromedrive
    CHROMEDRIVER = PASTA_ATUAL / 'M4Selenium' / 'chromedriver'

    #agora, vamos definir algumas opções.
    # Quando queremos abrir o chrome com algumas opções a mais ou a menos, fazemos uso de uma variável 
    # que guardará ChromeOptions. Essas opções faz parte do que você quer que o nevegador faça quando abrir. Por exemplo,
    # se você passa --headless, você não verá a interface do navegador. Se houvesse --disable-gpu, a gpu não seria utilizada durante o processo.
    #veja mais flags para options em: https://peter.sh/experiments/chromium-command-line-switches/
    chrome_opcoes = webdriver.ChromeOptions()
    #para indicar o serviço (driver) que estamos fazendo uso:
    chrome_servico = Service(executable_path=CHROMEDRIVER)
    #e para isso funcionar, precisamos passar todos os parâmetros anteriores em um lugar só:
    chrome_navegador = webdriver.Chrome(
        service=chrome_servico,
        options=chrome_opcoes,
    )

    #agora, para fazer uma simples demonstração, vou abrir um site qualquer
    chrome_navegador.get('https://youtube.com') #como pode ver, o site abre e após milésimos, ele fecha.
    #se fosse passado algo em options, como '--headless', a interface do navegador não iria abrir.
cls()
###########

def SeleniumWW():
    #mesma estrutura anterior
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By #esse módulo vai ser útil para selecionar um elemento dentro da página
    from selenium.webdriver.support.wait import WebDriverWait #Como os elementos não aparecem de imediato, vamos precisar de algo que vai fazer com que o código dê um tempo de espera para o elemento aparecer.
    from selenium.webdriver.support import expected_conditions as EC

    #definimos o caminho do webdrive
    from pathlib import Path
    PASTA_ATUAL = Path(__file__).parent
    CHROMEDRIVER = PASTA_ATUAL / 'M4Selenium' / 'chromedriver'

    #agora os parâmetros
    chrome_opcoes = webdriver.ChromeOptions()
    chrome_servico = Service(executable_path=CHROMEDRIVER)
    chrome_navegador = webdriver.Chrome(
        service=chrome_servico,
        options=chrome_opcoes,
    )

    #e o comando abaixo, para abrir o navegador na url seguinte:
    chrome_navegador.get('https://www.youtube.com/')

    #por fim, vamos iniciar a automação com uma busca simples por tags de nome, que no caso abaixo, será para
    # um input padrão lá na barra de pesquisa do yt
    from time import sleep
    procurar_input = WebDriverWait(chrome_navegador, 10).until( #aguarda 10 segundos para dar tempo para a tag aparecer
        EC.presence_of_element_located(
            (By.NAME, 'search_query') #busca por uma tag name 
        )
    )
    #a tag search_query é um input, ou seja, após localizada, vamos escrever alguma coisa.
    procurar_input.send_keys('hello world!!!!!!!!!!!!!!!!!!') #esse comando pode ser utilizado para escrever algo atraés da tag
    sleep(3) #e após escrever, ele aguarda 3 segundos. 

    ####################
    #Mas e se eu quisesse fazer uso de alguma tecla do teclado?
    from selenium.webdriver.common.keys import Keys
    #agora, após aquele hello world, ele vai apertar enter.
    procurar_input.send_keys(Keys.ENTER)
    sleep(3) #apenas para que a execução não acabe de imediato

    #agora, vou fazer uma coleta dos resultados que me ocorreram
    resultado_pesquisas = chrome_navegador.find_element(By.ID, 'contents')

    #agora, vou filtrar apenas pelo elemento que guarda o link (normalmente é a tag "a")
    links = resultado_pesquisas.find_elements(By.TAG_NAME, "a")
    links[0].click()
    sleep(3)

    #voltar aqui no futuro, pois pode ser que a função de efetuar o click em vídeo acabe se tornando obsoleta!

    '''
    Com o Selenium aprendido, vou deixá-lo dentro de uma função, para que não fique executando e atrapalhando
    o restante do código.
    '''

#############################################################################################
# Resuminho do Luiz:
# 
# Usando subprocess para executar e comandos externos
# subprocess é um módulo do Python para executar
# processos e comandos externos no seu programa.
# O método mais simples para atingir o objetivo é usando subprocess.run().
# Argumentos principais de subprocess.run():
# - stdout, stdin e stderr -> Redirecionam saída, entrada e erros
# - capture_output -> captura a saída e erro para uso posterior
# - text -> Se True, entradas e saídas serão tratadas como texto
# e automaticamente codificadas ou decodificadas com o conjunto
# de caracteres padrão da plataforma (geralmente UTF-8).
# - shell -> Se True, terá acesso ao shell do sistema. Ao usar
# shell (True), recomendo enviar o comando e os argumentos juntos.
# - executable -> pode ser usado para especificar o caminho
# do executável que iniciará o subprocesso.
# Retorno:
# stdout, stderr, returncode e args
# Importante: a codificação de caracteres do Windows pode ser
# diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
# mac, use utf_8.
# Comando de exemplo:
# Windows: ping 127.0.0.1
# Linux/Mac: ping 127.0.0.1 -c 4

#importando módulo
import subprocess

#vamos listar um comando que ele vai executar (caso linux)
comando = ['ping', '127.0.0.1', '-c', '4']

#e agora, vamos executar o comando acima
processo = subprocess.run(
    comando,
    #esse cmd abaixo não tinha antes
    capture_output=True, #o intuito desse cmd é capturar e exibir a saída
    #aqui eu posso passar:
    # text=True -> ele iria pegar automaticamente a codificação do seu SO, evitando o uso do decode (No windows pode não funcionar bem)

    #e poderia passar também
    # encoding='utf_8' -> isso evitaria o uso dos comandos acima, já que a saída já iria utilizar, por padrão,o nome da codificação que vocẽ informar como argumento.
)

#agora, vamos fazer a visualização
print(processo) #aqui ele mostra todas as informações referente ao processo. 
# No entanto, caso eu queira filtrar, bastaria digitar o nome do atributo
print(processo.args) #para visualizar os argumentos
print(processo.stdout) #para visualizar a saída
print(processo.stderr) #mostra os erros erro (se não houver, o retorno será vazio)
print(processo.returncode) #retorna um bool em caso de ocorrência de erro

cls()
#vou colocar um argumento no parâmetro capture_output
# Agora, quando eu fizer uso do strout, ele vai retornar o texto formatado de forma estranha.
print(processo.stdout)

# É por isso que vamos ter que tratar, seja através a inserção de um segundo parâmetro, que é o caso do text=True
# Ou  fazemos uso do método decode, sendo:

cls()
print(processo.stdout.decode('utf_8'))#aqui você deve colocar o nome do encoding (codificação) que o seu SO utiliza
#no windows, a codificação utf8 pode não funcionar bem e com base nos testes do Luiz, o que mais funcionou foi a codificação cp850

#Caso você tente fazer alguma coisa através do módulo sobprocess e começar a dar pau, mesmo estando com a syntax correta, volte na aula 321

############### curiosidade à parte
'''Outra forma de descobrir qual SO estou usando, com base no kernel'''
import sys
print(sys.platform) #no meu caso, retornou linux


####################################################################################################################


