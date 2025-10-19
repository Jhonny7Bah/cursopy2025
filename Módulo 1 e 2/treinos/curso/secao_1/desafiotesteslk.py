#cálculo do primeiro digito do cpf

cpf = '74682489070'
mult_inicial = 10
array = []
x = 0

for conversor_array in range(0, 9):
    array.append(cpf[x])
    x +=1
   
array_conversao_inteiro = list(map(int, array))

array_multiplicado = []
x = 0 
valor_da_multiplicacao = 10

for multiplicacao_oposta in range(0, 9):
    array_multiplicado.append(array_conversao_inteiro[x] * valor_da_multiplicacao )
    x +=1
    valor_da_multiplicacao -=1

resultado_do_final_da_conta = sum(array_multiplicado) * 10 % 11

if resultado_do_final_da_conta < 9:
    print('até aq deu certo mano')

