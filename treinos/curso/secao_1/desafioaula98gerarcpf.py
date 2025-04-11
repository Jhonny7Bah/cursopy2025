# #verificacao para o user
# cpf_digitado = input('Digite o seu cpf: ')#'74682489070'
# i = 0
# cpf = []
# while i <= 8:
#     cpf.append(cpf_digitado[i])
#     i +=1

# cpf_lista_int = list(map(int, cpf))

# #cálculo do primeiro dígito do cpf

# cpf_tratado1 = []
# contador_regressivo = 10
# i = 0
# for primeiracont in cpf_lista_int:
#     cpf_tratado1.append(contador_regressivo*cpf_lista_int[i])
#     i+=1
#     contador_regressivo -=1
# soma1 = sum(cpf_tratado1) * 10 % 11
# resultado_dig1 = soma1 if soma1 <= 9 else 0
# cpf_lista_int.append(resultado_dig1)

# #segunda conta
# cpf_tratado2 = []
# contador_regressivo = 11
# i = 0
# for segunda_conta in cpf_lista_int:
#     cpf_tratado2.append(contador_regressivo * cpf_lista_int[i])
#     i+=1
#     contador_regressivo -=1
# soma2 = sum((cpf_tratado2) * 10) % 11
# resultado_dig2 = soma2 if soma2 <= 9 else 0
# cpf_lista_int.append(resultado_dig2)
# #conversão de srt para list e int para str
# i = 0
# cpf_digitado_list = []
# for conversao_digitado in cpf_digitado:
#     cpf_digitado_list.append(cpf_digitado[i])
#     i+=1

# cpf_digitado_list = list(map(int, cpf_digitado_list))

    
# if cpf_lista_int == cpf_digitado_list:
#     print('o cpf {} é válido!'.format(cpf_digitado))
# else:
#     print('o cpf {} é inválido!'.format(cpf_digitado))
# #números repetidos é dado como válido

# validação de cpf (código mais limpo)
import re

cpf_digitado = re.sub(r'[^0-9]', '', '104.686.285-50')

nove_digitos = cpf_digitado[:9]

resultado1 = 0
contagem1 = 10

for digito1 in nove_digitos:
    resultado1 += int(digito1) * contagem1
    contagem1 -= 1
calc1 = resultado1 * 10 % 11

result_dig_one = calc1 if calc1 <= 9 else 0
#segundo digito

dez_digitos = nove_digitos + str(calc1)

resultado2 = 0
contagem2 = 11
for digito2 in dez_digitos:
    resultado2 += int(digito2) * contagem2
    contagem2 -= 1
calc2 = resultado2 * 10 % 11
result_dig_two = calc2 if calc2 <= 9 else 0
#verificação de validade
if cpf_digitado == dez_digitos + str(calc2):
    print('cpf válido')
else:
    print('se fufu')

#gerador de cpf
# import re
# import random

# for gerador in range(10000000000): #vai gerar 80 cpfs
#     armazenar_cpf = ''
#     for _ in range(9):
#         armazenar_cpf += str(random.randint(0, 9))


#     nove_digitos = armazenar_cpf

#     resultado1 = 0
#     contagem1 = 10

#     for digito1 in nove_digitos:
#         resultado1 += int(digito1) * contagem1
#         contagem1 -= 1
#     calc1 = resultado1 * 10 % 11

#     result_dig_one = calc1 if calc1 <= 9 else 0
#     #segundo digito

#     dez_digitos = nove_digitos + str(calc1)

#     resultado2 = 0
#     contagem2 = 11
#     for digito2 in dez_digitos:
#         resultado2 += int(digito2) * contagem2
#         contagem2 -= 1
#     calc2 = resultado2 * 10 % 11
#     result_dig_two = calc2 if calc2 <= 9 else 0
#     #verificação de validade
#     print(dez_digitos + str(calc2))
