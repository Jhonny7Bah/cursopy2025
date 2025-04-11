#ex1
try:
    numero = int(input('Digite um número: '))
    if numero % 2 == 0: 
        print(f'o número {numero} é par.')
    else:
        print(f'o número {numero} é ímpar. ')
    print(numero.is_integer()) #outra forma de verificar se o numero é inteiro. Basta colocar 
    #isso em um if

except:
    print('Você provavelmente digitou uma letra ou um número decimal.\nDigite apenas números inteiros. ')

#ex2

try:
    horario = int(input('Que horas são? digite apenas os dois primeiros números: '))
    if horario >= 0 and horario <= 11:
        print('Bom dia mano')
    
    elif horario > 11 and horario <= 17:
        print('Boa tarde, brother!')
    elif horario > 17 and horario <= 23:
        print('Não tem jeito, boa noite!')
    else:
        print('que horário esquisito da poxa mané!')

except:
    print('Você provavelmente digitou uma letra ou um número decimal.\nDigite apenas números inteiros. ')

#ex3
nome_do_user = input('Digite o seu primeiro nome: ')
tratamento_do_nome = len(nome_do_user)

if tratamento_do_nome <= 4 and tratamento_do_nome >=1:
    print('Que nome curto hein mano')
elif tratamento_do_nome < 1:
    print('Você não digitou nada mano ')
elif tratamento_do_nome == 5 or tratamento_do_nome == 6:
    print('A quantidade de letras no seu nome é até que normal')
else:
    print('nome grande da poxa slk mané ')

