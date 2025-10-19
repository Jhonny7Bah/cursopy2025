# from time import sleep
# from os import system

# def fim_da_execucao():
#     sleep(3)
#     system('cls')

# idades = []
# while True:
#     try:
#         for entrada in range(3):

#             idades.append(int(input('Digite um valor: ')))    
#         idade_de_camila = sorted(idades)
#         print(f'a idade de Camila é: {idade_de_camila[1]}')
#         fim_da_execucao()
#     except ValueError:
#         idades.clear()
#         print('Digite uma idade válida. (as idadem foram resetadas! )')
#         fim_da_execucao()


# exercicios chatgpt
# A função map() serve para aplicar uma função a cada elemento de uma sequência iterável (lista, tupla, etc.). Ela não retorna uma lista diretamente, mas sim um iterador, o que significa que seu resultado precisa ser convertido 
# para list() se quisermos vê-lo como uma lista completa de uma vez.

# continueTente fazer um código que peça ao usuário 5 números e exiba o dobro de cada um deles usando map. Se precisar de ajuda, me avise! 😃
def dobrar(num):
    return num*2
lista = [10,20,30,40]
print(list(map(dobrar, lista)))


def dobrar(num):
    return num*2

numero = list(map(int, input('Digite apenas 5 números separados: ').split()))
print(list(map(dobrar, numero)))

# list -> tem que colocar o list para converter como lista, caso contrário, se ele for colocado fora de um iterador, o valor printado será a alocação na memória
# o caso do list é similar ao closure

# map -> função map, que será o nosso iterador (parecido com o for)

# no caso acima, int é um argumento para o parâmetro função. Em função, será colocado oq ele vai fazer com a lista, se é dobrar os valores, converter para outro tipo, etc.

# numero no caso é o argumento para o parâmetro 'sequência', onde será colocada a variavel da lista, da tupla, etc.