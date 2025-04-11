# quant_megas = int(input('Quantos megas: '))
# quant_mes = int(input('Quantos meses: '))
# armazen = 0
# for __ in range(quant_mes):
#     meses = int(input('Quanto gastou no mês? ')) 
#     armazen += (quant_megas - meses)
# armazen+=quant_megas

# print(armazen)

#outra solução
# def internet_acumulativa(megas, quantidade_meses, *gastos_de_megas):
#     saldo = megas
#     for __ in range(*quantidade_meses):
#         saldo += megas - range(*gastos_de_megas)
#         return saldo
# print(internet_acumulativa(100, 2, 100))

megas, meses_acomulativos = int(input()), int(input()) 
saldo = megas

for __ in range(meses_acomulativos):
    uso_quantitativo_de_megas = int(input())
    saldo += (megas - uso_quantitativo_de_megas)
print(saldo)

