# Ótima escolha! Vamos começar com o Desafio 2: Contagem de Vogais.

# Aqui está a ideia do que precisamos fazer:

# Solicitar ao usuário que insira uma frase.
# Contar quantas vogais (a, e, i, o, u) existem na frase.
# Exibir o número total de vogais.

frase = input('Digite uma frase: ').lower()
vogais= 'aeiouáàâãéêóô'
quantidade = 0

for vogal in vogais:
    quantidade += frase.count(vogal)
print(f'o número de vogais na frase é: {quantidade}')