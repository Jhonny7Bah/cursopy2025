# 🧠 Desafio: Números Únicos
# Crie uma função em Python que receba uma lista de números inteiros e retorne apenas os números que aparecem uma única vez, na mesma ordem em que aparecem na lista original.

# Exemplo:
# entrada = [4, 5, 9, 4, 9, 8, 7]
# saida_esperada = [5, 8, 7]

def numeros_validos(valores:list):
    #verificar se o tipo recebido é um inteiro
    for verificar_tipo in valores:
        if not isinstance(verificar_tipo, int):
            raise TypeError("É aceito apenas uma lista de inteiros!")
    
    valores_retornados = []
    for __ in valores:
        for verificar in valores_retornados:
            if __ == verificar:
                valores_retornados.remove(__)
            else:
                valores_retornados.append(__)
    return valores_retornados
    

print(numeros_validos([1,2]))



