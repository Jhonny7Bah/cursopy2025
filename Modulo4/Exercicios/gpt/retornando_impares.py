# 🧠 Desafio Fácil: Contar Ímpares
# Crie uma função que receba uma lista de números inteiros e retorne quantos números ímpares ela contém.

# Exemplo:

# python
# Copiar
# Editar
# entrada = [1, 2, 3, 4, 5, 6]
# saida_esperada = 3  # porque 1, 3 e 5 são ímpares

def quantidade_impares(lista: list):
    qtds_impares = len([
        impares for impares in lista
        if impares % 2 == 1
    ])
    return qtds_impares
print(quantidade_impares(list(range(7))))