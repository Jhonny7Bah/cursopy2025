"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'bandido' #palavra chave
array_oculto = ['*'] * len(palavra_secreta) 
tentativas = 0 

while True:
    palpite_player = input('Digite uma letra: ')
    #verifica se foi digitado apenas uma letra
    if len(palpite_player) > 1:
        print('Digite apenas uma letra. ')
        continue

    else:
        #atualiza o array oculto se o palpite estiver correto
        for i in range(len(palavra_secreta)):

            if palavra_secreta[i] == palpite_player:
                array_oculto[i] = palpite_player 
    # Incrementa o número de tentativas
    tentativas +=1
     # Mostra o progresso do jogador 
    conversao = ''.join(array_oculto)
    print(conversao)
    # Verifica se o jogador completou a palavra secreta
    if conversao == palavra_secreta: break
os.system('cls') #utiliza comandos do prompt
print(f'\nParabéns, você conseguiu após {tentativas} tentativas!')