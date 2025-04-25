#o objetivo deste exercício é tornar a última letra dos nomes fornecidos em uma lista maiúscula.

lista = ['João', 'Mária', 'Carla', 'José', 'Alexandro']

def forma1():
    conversao = [f'{lista[n][:-1].lower()}{lista[n][-1].upper()}' for n in range(len(lista))]
    print(conversao)
#um pouco mais limpa
def forma2():
    conversao = [f'{n[:-1].lower()}{n[-1].upper()}' for n in lista]
    print(conversao)
forma2()

# numeros = '25'
# inversao = numeros[::-1]#52
# num_1 = int(numeros)
# num_2 = int(inversao)

# print(num_1 + num_2)