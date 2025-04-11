# Desafio 11: Somar Digitos de um Número até Chegar em um Único Dígito
# Requisitos:

# Solicite ao usuário um número inteiro n.
# Some os dígitos desse número. Se o resultado for maior que 9, continue somando os dígitos do resultado até que ele seja um único dígito.
# Exiba esse único dígito.
# Exemplo:

# Se a entrada for 38, a soma dos dígitos é 3 + 8 = 11 e então 1 + 1 = 2. O resultado final é 2.

numero = '38'
numero_separado = []
for __ in range(2):
    numero_separado.append(numero[__])

conversao_int = list(map(int, numero_separado))

for calculo in range(len(conversao_int)):
    calc = sum(conversao_int)
    while calc > 9:
        numero_separado = []
        for __ in range(2):
             numero_separado.append(conversao_int[__])
        conversao_int = list(map(int, numero_separado))
print(conversao_int)


