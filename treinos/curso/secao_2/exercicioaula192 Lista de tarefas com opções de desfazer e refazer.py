# Exercício - Lista de tarefas com desfazer e refazer
 # Música para codar =)
 # Everybody wants to rule the world - Tears for fears
 # todo = [] -> lista de tarefas
 # todo = ['fazer café'] -> Adicionar fazer café
 # todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
 # desfazer = ['fazer café',] -> Refazer ['caminhar']
 # desfazer = [] -> Refazer ['caminhar', 'fazer café']
 # refazer = todo ['fazer café']
 # refazer = todo ['fazer café', 'caminhar']


############################################
# def execucao(comando):
#     return comando

# tarefas = ['fds', 'gayzao']

# comandos = input('Comandos: listar, desfazer, refazer\n'
#       'Digite uma tarefa ou comando: ').lower()

# possibilidades = {
#     'listar': print(tarefas),
#     'desfazer': tarefas.clear,
#     'refazer': None,
# }

# # for key, values in possibilidades.items():
# #     if comandos == key:
# #         print(comandos, key)
# #         execucao(values)
# #         break
# #     else:
#         # print(tarefas)
#         # print('tem nada igual não.')
# print(tarefas)
# print('tem nada igual não.')

##########################solução incompleta

#

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
