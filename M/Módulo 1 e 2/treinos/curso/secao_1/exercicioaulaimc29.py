#fazer calculo de imc

nome = str(input('Qual é o seu nome? '))
altura = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))
imc = peso / altura ** 2


print('\n\n{} tem {} de Altura\nPesa {} quilos e seu IMC é \n{:.2f}'.format(nome, altura, peso, imc))