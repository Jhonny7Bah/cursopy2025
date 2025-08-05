# 🧠 Desafio: Sublistas Consecutivas
# Crie uma função em Python que receba uma lista e um número inteiro n, e retorne todas as
# sublistas consecutivas de tamanho n.

# entrada = [1, 2, 3, 4, 5]
# n = 3
# saida_esperada = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

def fatiamento(lista: list, n: int):
    fatia = []
    valor = 0

    for __ in lista:
        fatia.append(__)

        

print(fatiamento([1,2,3,4,5,6], 3))
