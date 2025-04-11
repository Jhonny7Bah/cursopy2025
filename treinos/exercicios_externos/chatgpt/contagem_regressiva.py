# Solicitar ao usuário que insira um número inteiro.
# Exibir a contagem regressiva começando desse número até 0.
# A cada número, imprima o valor atual da contagem regressiva.
# Após a contagem, exiba a mensagem "Fim!".

try:
    valor = int(input('Digite um número: '))
    while valor > 0:
        print(valor)
        valor -=1
    print('fim!!')
except ValueError:
    print('Digite um número válido! ')