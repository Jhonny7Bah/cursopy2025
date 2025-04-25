# Um número perfeito é aquele cuja soma de seus divisores próprios (excluindo ele mesmo) é igual ao próprio número.
# Exemplos:
# 6 é um número perfeito porque seus divisores próprios são 1, 2, 3 e 1 + 2 + 3 = 6.
# Solicitar um número inteiro positivo do usuário.
# Calcular a soma dos divisores próprios desse número.
# Informar se ele é um número perfeito ou não

try:
    numero = int(input('Digite um número: '))
    armazen_contagem = 0
    for __ in range(1, numero):
        if numero % __ == 0: armazen_contagem += __
    print(' é um número perfeito') if armazen_contagem == numero else print('é não')
except ValueError: 
    print('Apenas números inteiros são aceitos. ')