def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return 'a divisão por 0 não é permitida'
    return a / b

def principal():
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    terra = input('Vc quer: \n'
                  '[A]dicionar\n'
                  '[S]ubtrair\n'
                  '[M]ultiplicar\n'
                  '[D]Dividir ')
    
    if terra.upper().startswith('A'):
        return soma(a, b)
    elif terra.upper().startswith('S'):
        return subtracao(a, b)
    elif terra.upper().startswith('M'):
        return multiplicacao(a, b)
    elif terra.upper().startswith('D'):
        return divisao(a, b)
while True:
    print(principal())
    continuacao = input('\nquer continuar? \n[S]im\n[N]ão\n')
    if continuacao.lower().startswith('n'):
        break 
