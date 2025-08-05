# 🧠 Desafio Fácil: Soma dos Pares
# Crie uma função que receba uma lista de números inteiros e retorne a soma de todos os números pares dessa lista.

# Exemplo:

# python
# Copiar
# Editar
# entrada = [1, 2, 3, 4, 5, 6]
# saida_esperada = 2 + 4 + 6 = 12

def somar_pares(lista):
    soma = sum([
        valor for valor in lista
        if valor % 2 == 0
    ])
    return soma

print(somar_pares(list(range(7))))