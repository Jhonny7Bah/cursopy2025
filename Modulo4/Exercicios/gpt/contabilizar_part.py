# Por exemplo, se a pontuação mínima para ser convidado é 435 pontos, um competidor que tenha obtido 200 pontos na primeira fase e 235
# pontos na segunda fase será convidado para o curso na Unicamp.
# Já um competidor que tenha obtido 200 pontos na primeira fase e 234 pontos na segunda fase não será convidado.

def classificar_equipe(equipes: int, pont_min: int | float) -> int:
    equipes_classificadas = 0
    for __ in range(equipes):
        n1 = int(input('primeira nota? '))
        n2 = int(input('segunda nota? '))
        print(__)
        if n1 and n2:
             if n1 + n2 >= pont_min:
                 equipes_classificadas += 1
    return equipes_classificadas

# rodada_1 = classificar_equipe(3, 100)
# print(rodada_1)

#coloque esse programa em um list comprehension e use a função sum que resolve essa porra

listcom = sum([
    int(input('primeira nota?')) 
    for x in range(3)
])

print(listcom)