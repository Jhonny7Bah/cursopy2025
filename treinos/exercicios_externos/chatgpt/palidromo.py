from string import ascii_letters
# Crie um programa que verifique se uma palavra ou frase é um palíndromo, ou seja, que pode ser lida da mesma forma de trás para frente, ignorando espaços e pontuação.

# Requisitos:

# Solicite ao usuário que insira uma palavra ou frase.
# Verifique se a palavra ou frase é um palíndromo.
# O programa deve ignorar espaços, pontuação e maiúsculas/minúsculas.
# Exiba se a entrada é ou não um palíndromo.
pontuacao = '. , ! @ # $ % " * ( ) [ ] { } : ; ? / \ | '.split()

palavra = 'A man, a plan, a canal, Panama '.lower()
palavra_lista = []

for tratamento in range(len(pontuacao)):
    palavra = palavra.replace(pontuacao[tratamento], '').replace(' ', '')
for __ in palavra: palavra_lista.append(__)


palavra_formada = []
i = -1
for juntando in palavra:
    palavra_formada += palavra[i]
    i-=1
    
confirmacao = 'é palíndromo' if palavra_lista == palavra_formada else 'não é um palidromo! '
print(confirmacao)
print(palavra_lista, '\n', palavra_formada)