# Exercício - Lista de tarefas com desfazer e refazer
#  Música para codar =)
#  Everybody wants to rule the world - Tears for fears
#  todo = [] -> lista de tarefas
#  todo = ['fazer café'] -> Adicionar fazer café
#  todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
#  desfazer = ['fazer café',] -> Refazer ['caminhar']
#  desfazer = [] -> Refazer ['caminhar', 'fazer café']
#  refazer = todo ['fazer café']
#  refazer = todo ['fazer café', 'caminhar']

from os import system
tarefas = []
armazenTarefas = []
ValorAlterado = False

def listagem():
    system('cls')
    print('\nTAREFAS:')
    for __ in tarefas: print(__)
    print('\nCOMANDOS: listar, desfazer, refazer')
    return

while True:
    comando = input('Digite uma tarefa ou comando: ').lower()
    
    if 'desfazer' in comando:
        if len(tarefas)>=1:
            ValorAlterado = True 
            tarefas.pop()
            listagem()
        else:
            print('Nada a desfazer!')
    elif 'listar' in comando: listagem()
    elif 'limpar' in comando: system('cls')
    elif 'refazer' in comando:
        if ValorAlterado:
            tarefas.append(armazenTarefas[-1])
            ValorAlterado = False
            listagem()
        else:
            system('cls')
            print('nada a refazer!')
    else:
        tarefas.append(comando)
        armazenTarefas.append(comando)
        listagem()
    
    #base de dados
    final = ' \nTAREFAS:)\n'
    from json import dump
    with open('base_de_dados_tarefa.json', 'w', encoding='utf8') as base_de_dados:
        dump(tarefas, base_de_dados,indent=2)