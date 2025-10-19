# Solicitar ao usuário um número inteiro n.
# Verificar todos os números de 1 até n para descobrir quais são primos.
# Exibir todos os números primos até n.

try:
    numero = int(input('Digite um número: '))
    armazenamento = 0
    for __ in range(1, numero):
        if numero % __ == 0:
            armazenamento +=1
    print('é primo') if armazenamento == 1 else print('não é primo')
except ValueError:
    print('Será aceito apenas números inteiros! ')