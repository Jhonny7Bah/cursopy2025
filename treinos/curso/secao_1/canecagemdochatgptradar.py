velocidade_carro = 80 #essa e a velocidade atual do carro 
RADAR_LIMITE = 80
MARGEM_DE_ERRO = 2

VERIFICACAO_A = velocidade_carro <= (RADAR_LIMITE + MARGEM_DE_ERRO)
VERIFICACAO_B = velocidade_carro >= (RADAR_LIMITE - MARGEM_DE_ERRO)

if VERIFICACAO_A and VERIFICACAO_B:
    print('sem multa, quem sabe na proxima ')
else:
    print('se lascou todinho, tome multa!')
