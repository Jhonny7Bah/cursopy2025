# Objetivo: Entender e aplicar o conceito de closure.
# Tarefa:

# Escreva uma função chamada criar_multiplicador que receba um número (o multiplicador) e retorne uma função que multiplica seu argumento por esse valor.
# Utilize essa função para criar, por exemplo, um "vezes três" e, em seguida, aplique essa função a uma lista de números (usando list comprehension ou map).
# Exemplo:
# vezes_tres = criar_multiplicador(3)
# # Aplicar a função vezes_tres a [1, 2, 3, 4] deve resultar em [3, 6, 9, 12]
def executa(funcao, *args):
    return funcao(*args)


def criar_multiplicador(numero):
    def multiplicando(valor):
        return valor * numero
    return multiplicando

multipicador = criar_multiplicador(5)
numeros = [n for n in range(20)]
resultado = [multipicador(n) for n in numeros]
print(resultado)



#em seguida, aplique essa função a uma lista de números (usando list comprehension ou map). não entendi essa parte, me explique sem dar a resposta. 

