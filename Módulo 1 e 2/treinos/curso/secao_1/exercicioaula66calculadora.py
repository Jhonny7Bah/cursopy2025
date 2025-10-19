 #fazer uma calculadora de (+ - / *)
while True:

    try: #caso o user digite algo diferente de um num, o while vai reiniciar

        print('\nCaso queira sair, digite "sair". ')
        digito1 = input('digite um número: ') #pega o dígito do user
        
        if digito1.lower() == 'sair': #caso ele digite sair, irá sair tudo em minusculo
            break 

        else:
            num1 = float(digito1)
            operador = str(input('Digite um operador: '))
            if operador == 'sair':
                break

            elif operador != '+' and operador != '-' and operador != '/' and operador != '*':
                print('Você digitou um operador diferente. Vamos tentar de novo! \n')
                continue

        digito2 = input('Digite outro número: ')
        if digito2.lower() == 'sair':
            break
        else:
            num2 = float(digito2)

        if operador == '+':
            print('o número {} {} {} = {}'.format(num1, operador, num2, num1+num2))    
        elif operador == '-':
            print('o número {} {} {} = {}'.format(num1, operador, num2, num1-num2))
        elif operador == '/':
            if num2 == 0:
                print('Não é possível dividir por 0')
            else:
                print('o número {} {} {} = {}'.format(num1, operador, num2, num1/num2))

        elif operador == '*':
            print('o número {} {} {} = {}'.format(num1, operador, num2, num1*num2))
        else:
            print('Não entendi')
    except ValueError:
        print('Entrada inválida, tente digitar um número válido ou aperte "sair".\n ')

