# i representa linha
# j representa coluna
# i, j = 1,1

# A2x3 = [ #matriz três linhas e duas colunas
#     [10, 11],
#     [13, 14],
#     [16, 17]
# ]
# print(A2x3[i][j])


matriz_A = [
    [2, 5, -3],
    [1, 0, 6],
]

matriz_B = [
    [3, 1, 4],
    [-8, 9, -10],
]
soma = []

contagem = 0
for elementos_matriz in range(len(matriz_A)):
    contagem += len(matriz_A[elementos_matriz])

i = 0
for __ in range(len(matriz_A[i])):
    soma.append(matriz_A[i][__] + matriz_B[i][__])
    if len(soma) == len(matriz_A[i]):
        i+=1
        for haha in range(len(matriz_A[i])):
            soma.append(matriz_A[i][haha] + matriz_B[i][haha])
    # soma.append() 
print(soma)