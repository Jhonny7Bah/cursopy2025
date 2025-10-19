 # Exercício - Unir listas
 # Crie uma função zipper (como o zipper de roupas)
 # O trabalho dessa função será unir duas
 # listas na ordem.
 # Use todos os valores da menor lista.
 # Ex.:
 # ['Salvador', 'Ubatuba', 'Belo Horizonte']
 # ['BA', 'SP', 'MG', 'RJ']
 # Resultado
 # [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# solução_1
lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']

def funcao_zipper():
    lista_maior = []
    try:
        for __ in range(0, len(lista_2)):
            lista_maior.append((lista_1[__], lista_2[__]))
    except IndexError:
        print(lista_maior)
funcao_zipper()

# solucao_2
def zipper(lista_1, lista_2):
        armazenamento = [
            (lista_1[i], lista_2[i]) 
            for i in range(0, len(lista_1))
        ]
        return armazenamento
print(zipper(['Salvador', 'Ubatuba', 'Belo Horizonte'], 
       ['BA', 'SP', 'MG', 'RJ']
       ))

#solução 3
#uso do min e max: min -> mínimo, max -> máximo,ou seja, posso oferecer dois valores a eles e eles me dirão quem é o maior ou quem é o menor. ex:
print(min(1, 10)) #retornou 1 pq o mínimo realmente é 1
print(max(1, 10)) #retornou 10 porque entre 1 e 10, 10 é maior.
#logo, vamos resolver o nosso exercício!

def zipperMin(lista_1, lista_2):
     valor_minimo = min(len(lista_1), len(lista_2))
     return [
          (lista_1[i], lista_2[i])
          for i in range(valor_minimo) #aqui, fazemos uso do min para saber quem é o valor mínimo e assim, não quebrar a função.
     ]
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipperMin(l1, l2))

# solucão_4
#podemos fazer do jeito mais rápido, que é através da função zip.
#a função zip faz uso do conceito de interator, ou seja, se eu quiser avançar, precisarei fazer uso do next ou se eu quiser fazer mais rápido, posso converter ela em uma list ou iterar em um for.
zipper_quatro = zip(l1, l2)
print(zipper_quatro) #iterator, como pode ver
print(list(zipper_quatro)) #convertendo em uma lista, poderei ver claramente o que tem aqui.

#solução 5
#posso fazer uso do módulo intertools, mais especificamente, da função zip longest, que diferentemente do que estamos fazendo, ele irá fazer uma busca da lista maior e usar como base.
#lembrando que esse módulo também trabalha com os conceitos de iterator, logo, vou precisar converter em uma list ou em um for.
from itertools import zip_longest
sol = []
for resol_5 in zip_longest(l1, l2):
     sol.append(resol_5)
     print(sol)
#fiz uso do for para praticar o iterator através dele.
#como viu, ele usou como base a lista maior, e como nela não havia um nome de cidade(como as outras), retornou None.
#se você não quiser que ela retorne none, basta fornecer um argumento para o parâmetro fill value(valor de prenchimento), que ao invés de ser none, será o valor que você irá informar. ex:
print(list(zip_longest(l1, l2, fillvalue='Não existe')))
#exercício concluido!!!!!!!!!
