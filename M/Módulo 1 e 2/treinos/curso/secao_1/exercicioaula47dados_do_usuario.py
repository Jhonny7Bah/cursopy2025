
nome_user = input('Qual é o seu nome? ')
idade_user = input('Qual a sua idade? ')
n = 0

if nome_user and idade_user:
    print('seria outra forma mais fácil de')

if nome_user != '' and idade_user != '':
    print('Seu nome é: {} \nSeu nome invertido é: {}\nSeu nome tem {} espaços'.format(
        nome_user, nome_user[::-1], nome_user.count(' ')
    ))
    if nome_user.count(' ') == 1:
        n = 1   
    elif nome_user.count(' ') == 2:
        n = 2
    elif nome_user.count(' ') == 3:
        n = 3
    else: 
        n = 4
    print('Seu nome tem {} letras'.format(int(len(nome_user)-n), ))
    print('A primeira letra do seu nome é{nome} \nA última letra do seu nome é {nome1}'.format(
       nome=nome_user[0], nome1=nome_user[-1] 
    ))
else:
    print('Desculpe, você deixou campos vazios. ')

