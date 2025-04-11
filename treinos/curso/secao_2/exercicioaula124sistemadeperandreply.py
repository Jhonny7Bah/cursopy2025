# #exercício de questão objetiva:

# def verificacao(numero_pergunta):
#     if resposta_player == numero_pergunta:
#         global acertos
#         acertos +=1
#         return 'Você acertou!'
#     else:
#         global erros
#         erros +=1
#         return 'Você errou'

# acertos,erros = 0, 0
# pergunta_01 = {
#     'Pergunta': 'Mário é gay? ',
#     'Opções': ('0) Sim', '1) Não'),
#     'Respostas': '0',
# }
# pergunta_02 = {
#     'Pergunta': '4 x 4 =  ',
#     'Opções': ('0) 14', '1) 20', '3) 16', '4) 37'),
#     'Respostas': '3'
# }
# #pergunta1
# print(f'{pergunta_01["Pergunta"]}\n\nOpções:')
# print(*pergunta_01['Opções'], sep='\n')
# resposta_player = input('Escolha uma opção: ')
# print(verificacao(pergunta_01['Respostas']))
# #pergunta2
# print(f'{pergunta_02["Pergunta"]}\n\nOpções:')
# print(*pergunta_02['Opções'], sep='\n')
# resposta_player = input('Escolha uma opção: ')
# print(verificacao(pergunta_02['Respostas']))

# print('Mofio, tu acertou', acertos, 'errou', erros)





#exercício de questão objetiva:

# def verificacao(numero_pergunta, acertos, erros):
#     if resposta_player == numero_pergunta:
#         acertos +=1
#         return 'Você acertou!'
#     else:
#         erros +=1
#         return 'Você errou'

# acertos,erros = 0, 0
# pergunta_01 = {
#     'Pergunta': 'Mário é gay? ',
#     'Opções': ('0) Sim', '1) Não'),
#     'Respostas': '0',
# }
# pergunta_02 = {
#     'Pergunta': '4 x 4 =  ',
#     'Opções': ('0) 14', '1) 20', '3) 16', '4) 37'),
#     'Respostas': '3'
# }
# #pergunta1
# print(f'{pergunta_01["Pergunta"]}\n\nOpções:')
# print(*pergunta_01['Opções'], sep='\n')
# resposta_player = input('Escolha uma opção: ')
# print(verificacao(pergunta_01['Respostas'], acertos, erros))
# # #pergunta2
# # print(f'{pergunta_02["Pergunta"]}\n\nOpções:')
# # print(*pergunta_02['Opções'], sep='\n')
# # resposta_player = input('Escolha uma opção: ')
# # print(verificacao(pergunta_02['Respostas']))

# print('Mofio, tu acertou', acertos, 'errou', erros)

#outra forma de resolver
def parar_execucao():
    from sys import exit
    exit()

acertos, erros = 0,0
perguntas = [{
    'questao':'1 + 1 = ',
    'opcoes': ['2', '3', '4'],
    'resposta':'0',
},
{
    'questao':'4 + 1 = ',
    'opcoes': ['2', '5', '4', '7'],
    'resposta':'1',
}
]
end = 0
while True:
    for pergunta in perguntas:
        print('Pergunta:', pergunta['questao'], '\n')

        for i, opcoes in enumerate(pergunta['opcoes']): #como aqui está sendo retornado uma tupla, para separar, irei usar duas var no for.
            print(f'{i}) {opcoes}')                     #se futuramente você esquecer, basta remover o 'i' na chamada do for.
        
        escolha = input('\nescolha uma opção: ')
        if int(escolha) > int(i):
            print('Você digitou uma opção inválida')
            continue
            

        elif escolha == pergunta['resposta']:
            if len(perguntas) == end: parar_execucao()
            print('Acertou 👍 \n')
            acertos+=1
            end +=1
            
            
            print(f'o valor de um é {len(perguntas)} e do outro é {end}')
        else:
            if len(perguntas) == end: parar_execucao()
            print('Errou ❌\n')
            erros+=1
            end +=1
        
print(f'Você acertou {acertos} e errou {erros}')




