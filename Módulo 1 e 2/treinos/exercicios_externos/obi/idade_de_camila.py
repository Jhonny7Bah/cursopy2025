from time import sleep #sleep para esperar um tempo, em segundos
from os import system #paralimpar o terminal

def fim_da_execucao(): 
    sleep(3) #esperar antes de limpar o terminal
    system('cls')

idades = [] #armazenamento de idades
#no caso, o código abaixo rolará infinitamente
while True:
    try: #try and except para se caso o user digitar um valor não inteiro, logo, o except faria o tratamento
        for entrada in range(3): #são três meninas, logo o código abaixo pedirá três idades

            idades.append(int(input('Digite um valor: ')))    
        idade_de_camila = sorted(idades) #organiza as idades da menor para a maior
        print(f'a idade de Camila é: {idade_de_camila[1]}') #pega a idade do meio
        fim_da_execucao() #chama a função de limpeza
    except ValueError:
        idades.clear()
        print('Digite uma idade válida. (as idadem foram resetadas! )')
        fim_da_execucao()


