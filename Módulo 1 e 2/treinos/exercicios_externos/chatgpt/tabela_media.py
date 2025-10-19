nome_do_aluno = ['João', 'Maria', 'Pedro', 'Ana', 'Carla']
Nota_1 = [7.5, 9.0, 6.0, 8.5, 5.0]
Nota_2 = [8.0, 8.5, 5.5, 9.0, 4.5]
Nota_3 = [6.5, 7.0, 7.0, 9.5, 6.0]
media = [
    (Nota_1[n] + Nota_2[n] + Nota_3[n]) / 3
    for n in range(len(nome_do_aluno)) 
]
print(media)
aprovacao = [
    'aprovado' if num >= 7 else 'reprovado'
    for num in media
]
print(aprovacao)
# média?
# resultado >= 7?
casa = 7.666666666666
print('{:.1f}'.format(casa))