# 🧠 Desafio: Números Únicos
# Crie uma função em Python que receba uma lista de números inteiros e retorne apenas
# os números que aparecem uma única vez, na mesma ordem em que aparecem na lista original.

# Exemplo:
# entrada = [4, 5, 9, 4, 9, 8, 7]
# saida_esperada = [5, 8, 7]


#solução 1
def numeros_validos(valores:list):
    retorno = [] 
    #itera sobre os valores
    for iterador in valores:
        #verificar se o tipo recebido é um inteiro
        if not isinstance(iterador, int):
            raise TypeError("É aceito apenas uma lista de inteiros!")
        #verifica se a quantidade de um valor específico é um.
        if valores.count(iterador) == 1:
            retorno.append(iterador)
    #retorna a lista
    return retorno

print(numeros_validos([1,2,2]))

#solução 2
from collections import Counter

#criando a tal função exigida
def numeros_validos2(lista :list):
    #vai retornar um dicionário informando a quantidade de vezes que o número aparece
    quantidade_de_vezes = Counter(lista) #couter vai retornar um dicionário contendo a quantidade de vezes que um valor aparece
    #após saber a quantidade de vezes, basta filtrar
    lista_formatada = [
        #iterando diretamente na lista (para manter a ordem)
        valor for valor in lista
        #se a quantidade de ocorrências for 1, significa que o valor não se repetiu
        if quantidade_de_vezes[valor] == 1
    ]
    #agora só basta retornar a lista.
    return lista_formatada

print(numeros_validos2([1,2,3,3]))

