# # ler dois valores e exibe o maior num
# valor_1, valor_2 = 10, 15#int(input('digite o primeiro número: ')), int(input('digite o segundo número: '))
# resultado = valor_1 if valor_1 > valor_2 else valor_2
# print(resultado)
# #outra forma
# def verificacao_maior_numero (x, y):
#     result = x if x > y else y
#     return result

# print(verificacao_maior_numero(14654, 17))

###################
# 10: quant_megas              saida: 130
# 3: quant_meses
# 4: mes_1
# 5: mes_2
# 2: mes_3

# calc: quant_megas - mese(1, 2, 3)

quant_megas = int(input('Quantos megas: '))
quant_mes = int(input('Quantos meses: '))
armazen = 0
for __ in range(quant_mes):
    meses = int(input('Quanto gastou no mês? ')) 
    armazen += (quant_megas - meses)
armazen+=quant_megas

print(armazen)