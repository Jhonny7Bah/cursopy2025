# ##verificar se o número é par
# import os

# inicio = input('Digite o número a ser começado: ')
# fim = input('Digite o último número que quer que ele pare: ')

# tratamento = [int(inicio), int(fim)+1
#     ]

# for teste in range(tratamento[0], tratamento[1], 2): print(teste)
#numero primo é todo aquele divisível por 1 e por ele mesmo
#num_digitado = 2

# x / y = r
# x = numeroFixo
# y = numeroQualquerDentrodoFor 
# r = resultado que será verificado em um if

# ex:

# 2 / y(y+=1) = r(se inteiro, vai acrescentar valor na variavel Uminteiro)

# se a variavel Uminteiro:
# >2 não é primo
# <2 não é primo
# == 2 
# r tem que ser inteiro para ser primo

# primeirospassos:
# perguntar o número (x) para o user
# rodar um for com indice embutido realinzado a divisao x / y, aumentando os indices de 1 em 1
# cria uma variavel vazia
# cria um if com a condição de que se o resultado presente no for acabar sendo inteiro, incrementar na variavel
# ao final, coloca um if verificando se essa variavel == 2. se verdadeiro, o número é primo, se falso, o número n é primo.


#saber se o número  é perfeito
# num_digitado = 2
# i = 1
# armazen = 0
# nome = 2/5

# for __ in range(0, 5):
#     calc = num_digitado / i
#     if num_digitado.is_integer():
#         armazen +=1
#     i+=1   
# print(armazen)

# print(nome.is_integer()) o erro dessa lógica foi que 2 é múltiplo de qualquer par




# sequencia de fibonacci
#1 1 2 3 5 8 
# o próximo número é a soma dos dois anteriores
# import time 
# #pergunto ao user até onde ele quer a sequencia 
# numero_digitado = int(input('Digite um número: '))
# inicio = time.time()
# sequencia = [0, 1]
# #faço a sequência com base nos números iniciais
# for calc in range(numero_digitado-2):
#     soma = sequencia[-2] + sequencia[-1]
#     sequencia.append(soma)
# #informo a sequencia
# print('Sequência de Fibonacci até o {}º termo:'.format(numero_digitado)) 
# for i in range(len(sequencia)):
#     print(f'{i+1}º termo: {sequencia[i]}')
# fim = time.time()

# print(fim-inicio)

from os import system
from time import sleep

def apagar():
    print('Isso não é um número inteiro! \n')
    sleep(2)
    system('cls')

while True:
    verificador = input('Selecione as opções: \n'
        '[A]gerador número primo\n'        
        '[B]verificador de número primo\n')

    if verificador.upper().startswith('A'):
        #gerador de numero primo
        num_primo = '' 
        teste = 2 #numero primo digitado
        validacao = 0
        try:
            quantidade = int(input('Digite apenas número(s): ')) #ate que número será contado
            for _ in range(quantidade):
                for gen in range(1, quantidade):
                    if teste % gen == 0:
                        validacao += 1
                if validacao == 2:
                    num_primo += f'{str(teste)} ' 

                teste +=1
                validacao = 0
            print(num_primo)
        except ValueError:
            apagar()
            
            
    elif verificador.upper().startswith('B'):

        #     algoritmo do num primo (funcional)
        # verificador num primo
        while True:
            try:
                num_digitado = int(input('digite um número: '))
                divisoes_possiveis = 0
                indice = 1
                while indice < 100:
                    if num_digitado % indice == 0:
                        divisoes_possiveis += 1
                    indice += 1
                if divisoes_possiveis == 2:
                    print(f'o número: {num_digitado} é primo. ')
                else:
                    print(f'o número: {num_digitado} é não é primo. ')

                saida = input('Deseja continuar? [S]im [N]ão\n')
                if saida.upper().startswith('N'):
                    system('cls')
                    break
            except ValueError:
                apagar()
    else:
        apagar()



