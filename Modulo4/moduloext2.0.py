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


####### Selenium
# Primeiro, vou precisar instalar um driver para uso. Como utilizarei o compre, com base nos requesitos do meu sistema,
# devo fazer a procura no seguinte site: https://developer.chrome.com/docs/chromedriver/downloads
# Agora, preciso instalar o selenium com o seguinte cmd:
# pip install selenium

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

from time import sleep
# sleep(10)



# cls()