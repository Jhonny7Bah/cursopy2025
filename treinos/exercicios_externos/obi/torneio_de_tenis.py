# participantes que venceram 5 ou 6 jogos serão colocados no Grupo 1;
# participantes que venceram 3 ou 4 jogos serão colocados no Grupo 2;
# participantes que venceram 1 ou 2 jogos serão colocados no Grupo 3;
# participantes que não venceram nenhum jogo não serão convidados a continuar com os treinamentos.

# V V P P P V > 2


def verificacao_de_grupo(vitorias='ppppp'): #ppppp no caso é o valor padrão caso a chamada da função não tiver nenhum argumento.

    contagem = vitorias.lower().count('v') #contagem da quantidade de vitórias do time

    if contagem == 5 or contagem == 6:
        return 1 #grupo 1: 6 ou 5 vitórias
    elif contagem >=3 and contagem <=4:
        return 2 #grupo 2: 3 ou 4 vitórias
    elif contagem >= 1 and contagem <= 2:
        return 3 #grupo 3: 1 ou 2 vitórias
    else: 
        return -1 #nenhuma vitória
print(verificacao_de_grupo('VVppv')) #chamada da função com quantidade de vitórias