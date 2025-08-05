# 🧠 Desafio Intermediário: Números Primos na Lista
# Crie uma função que receba uma lista de números inteiros e retorne uma nova lista
# contendo apenas os números primos.

# Exemplo:

# python
# Copiar
# Editar
# entrada = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# saida_esperada = [2, 3, 5, 7]

def numeros_primos(lista: list):
    def remover_multiplos(n: int, lista_semi: list = lista):
        filtro = lista[0]
        num = [
            valor for valor in lista_semi
            if valor % n != 0
        ]
        return {
                'primos':filtro,
                'lista_tratada':num
                }
    for __ in range(len(lista)):
        remover_multiplos(__)


print(numeros_primos([2, 3, 4, 5, 6, 7, 8, 9, 10]))