# Uma pesquisadora está realizando uma pesquisa para verificar quais são os estados que vendem álcool por um preço bom
# Para o preço do álcool ser bom, ele precisa ser <= 30% do preco da gasolina
# caso nenhum estado seja vantajoso, retorne *
# N -> quantos estados vou informar
# A -> álcool
# G -> gasosa

# #Exemplos
# Entrada
# 2
# AM 7.00 10.00
# RS 7.01 10.00
# Saída
# AM

# n = 2 #int(input('Quantos estados serão informados? '))
# dados = []
# for __ in range(n):
#     dados.append(input('Opa ').split())
# print(dados)
result = []

10/10 * 3
terra = [['am', 7, 10], ['sc', '8', '10']]

for __ in range(0, len(terra) +1):
    calc = (terra[__][2]/terra[__][2] * 3)
    result.append(terra[__][__] if terra[__][2] - calc >= terra[__][1] else '*')
print(result)
