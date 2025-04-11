def media_ponderada(a,b,c,d,e,f):
    notas = [a, b, c]
    pesos = [d, e, f]

    for i in range(len(notas)):
        total += notas[i] * pesos[i] 

    return total / sum(pesos)

print(media_ponderada(7, 8, 9, 1, 2, 3))
