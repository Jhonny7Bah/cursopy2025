# Objetivo: Praticar filtragem e aplicação de operações em elementos de uma lista.
# Tarefa:

# Crie uma lista com números de 1 a 20.
# Usando list comprehension, gere uma nova lista contendo o quadrado de cada número ímpar.
# Exemplo de saída (parcial): [1, 9, 25, ...]

lista = [n ** 2 for n in range(21) if n % 2 == 1]

for teste in range(21):
    if teste % 2 == 1: print(teste ** 2)

print(lista)