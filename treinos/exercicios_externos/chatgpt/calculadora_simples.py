# Digite o primeiro número: 10
# Digite o segundo número: 5
# Escolha a operação:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
# Digite o número da operação desejada: 1
# Resultado: 10 + 5 = 15
try:
    numero_a, numero_b = float(input('Digite um número: ')), float(input('Digite outro número: '))
    operacao = input('''
    Escolha a operação:
    1) Soma
    2) Subtração
    3) Multiplicação
    4) Divisão
    ''')

    if operacao == '1':
        print(numero_a + numero_b)
    elif(operacao == '2'):
        print(numero_a - numero_b)
    elif(operacao == '3'):
        print(numero_a * numero_b)
    elif(operacao == '4'):
        if numero_b != 0:
            print(numero_a / numero_b)
        else:
            print('Não é possível fazer a divisão por 0')
    else:
        print('Não entendi')
except ValueError:
    print('Não foi possível realizar tal operação. Por favor, digite apenas números!')