nome = str(input('Qual é o seu primeiro nome? '))
sobrenome = str(input("qual é o seu sobrenome? "))
idade = int(input('Qual é a sua idade? '))
anoNascimento = 2025 - idade
altura = float(input('altura?'))

maioridade = ''
if idade >= 18:
    maioridade = 'maior'
else:
    maioridade = 'menor'

print("Seu nome é {}, seu sobrenome é {}, sua idade é {} anos, sendo {} de idade, tendo {} metros de altura.".format(nome, sobrenome, idade, maioridade, altura ))



