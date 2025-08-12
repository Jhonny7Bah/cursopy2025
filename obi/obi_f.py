# Você foi contratado pela Coordenação da OBI para fazer um programa que, dados os números de pontos obtidos
# por cada competidor em cada uma das fases, e o número mínimo de pontos para ser convidado,
#  determine quantos competidores serão convidados para o curso na Unicamp. Você deve considerar que

# todos os competidores participaram das duas fases;
# o total de pontos de um competidor é a soma dos pontos obtidos nas duas fases.
# Por exemplo, se a pontuação mínima para ser convidado é 435 pontos,
#  um competidor que tenha obtido 200 pontos na primeira fase e 235 pontos na segunda fase será convidado para o curso
#  na Unicamp. Já um competidor que tenha obtido 200 pontos na primeira fase e 234 pontos na segunda fase não será convidado.

# A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão.
# A primeira linha da entrada contém dois números inteiros N e P, representando
# respectivamente o número de competidores e o número mínimo de pontos para ser convidado.
# Cada uma das N linhas seguintes contém dois números inteiros X e Y indicando a pontuação de um 
# competidor em cada uma das fases.


# Seu programa deve imprimir na saída padrão uma única linha contendo um único inteiro,
# indicando o número de competidores que serão convidados a participar do curso na Unicamp.

#------------------------------------------------------------------------

#tratando para o caso do usuário digitar algo que não seja número
try:
    N = int(input('Informe o número de competidores: '))
    #definindo o número de competidores
    
    #definindo a pontuação mínima
    P = int(input('Informe a pontuação mínima : '))

    #verificando quem foi aprovado
    aprovados = sum(
        1
        for __ in range(N)
        if int(input('digite sua primeira nota')) + int(input('digite a sua segunda nota: ')) >= P)
    
    #exibindo o número de aprovados
    print(aprovados)

#caso o usuário digite algum valor que não seja inteiro
except ValueError:
    print('é permitido apenas número. ')

