
###########################################################
# Enviando emails com python
#Esse meio pode mudar por algum motivo ao decorrer do tempo.
#Normalmente, para você fazer um processo de envio de email de forma estável, deve-se ter um servidor SMTP
#Vamos lá!

#Inicialmente, devo criar um dotenv para colocar as minhas informações lá. No caso, haverá um .env-example2 aí no código com as informações que deverá ser colocadas

#Após isso, deve-se ir a uma conta email  e ativar o IMAP nas configurações.


# Depois, deve-se criar uma senha de app
# link:https://support.google.com/accounts/answer/185833?hl=pt-BR

# Após gerar a senha de app, coloque ela lá no dotenv.

#Após essa configuração, vamos começar a codar:
#####
from dotenv import load_dotenv #módulo necessário para carregar o dotenv
from os import getenv #módulo necessário para pegar um dotenv em específico
#carrega o dotenv
load_dotenv()

#dados do remetente
remetente = getenv("FROM_EMAIL", "") #Coloco o meu email, apontando para as variaveis de ambiente.
destinatario = remetente #Nesse caso, vou mandar o email para mim mesmo.

#Configuração SMTP
#as informações abaixo é padrão do google
smpt_server = 'smtp.gmail.com'
smpt_port = 587 # Porta padrão para SMTP com TLS
smpt_username = getenv("FROM_EMAIL", "") #pego o meu email
smpt_password = getenv("EMAIL_PASSWORD", "") #pego a senha nas variáveis de ambiente (lá no dotenv)


#Agora, só temos que transformar o conteúdo em MIMEMultipart, que vai segregar entre from(de),
#  to(para), subject(assunto), etc. Que são as informações que colocamos em um email quando queremos mandar para alguém.
from email.mime.multipart import MIMEMultipart #importo a classe que possui os dicionários que irei incrementar
from email.mime.text import MIMEText

mensagemMIME = MIMEMultipart() #armazenando a classe em uma variável
#posteriormente, vou fazer as alterações, estando em conforme com oq eu quero.
mensagemMIME['From'] = remetente
mensagemMIME['To'] = destinatario
mensagemMIME['Subject'] = 'O assunto é sobre o assunto, sacou?'

#text que será enviado:
texto_enviar = '''
Olá, senhor! Tudo bem com a vossa senhoria? velho lhe informar que 
quando é somado 1 + 1, o resultado é 2, certo? Não é tão fácil quanto
parece realizar esse tipo de conta, mas é possível. 

'''
#agora, vou converter a mensagem em formato mime
mensagemMIME.attach(MIMEText(texto_enviar, 'plain'))

# após a conversão de tudo para o formato mime, basta fazer a conexão com o servidor. 
# Para isso, posso utilizar o context manager, que vai inicializar e posteriormente, encerrar a conexão.

#para se conectar com o servidor, vamos precisar de mais um módulo
import smtplib

#vamos inicializar a conexão, passando o servidor e a porta
with smtplib.SMTP(smpt_server, smpt_port) as server:
    server.starttls() #inicializa uma comunicação segura com os servidor
    server.login(smpt_username, smpt_password) #faz login no servidor com o meu email e senha de app
    server.send_message(mensagemMIME) #envio a mensagem
    print('email enviado com sucesso')

#Por fim, objetivo concluido com sucesso!!!
