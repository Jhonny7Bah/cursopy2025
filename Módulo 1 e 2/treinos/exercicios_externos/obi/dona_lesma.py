# tamanho_muro = 10000
# subida = 100
# escorregamento = 50
# calc = 0
# cont = 0
# teste = subida - escorregamento

# while calc <= tamanho_muro:
#     calc += (subida - escorregamento)
#     cont += 1

# print(calc, cont)

# print(9950 / teste)
# print(12 /3)
# calc = 0
# if calc <= 30:
#     calc += 7 - 4
#     calc += 7 - 4
#     calc += 7 - 4
#     calc += 7 - 4
#     calc += 7 - 4
#     calc += 7 - 4
#     calc += 7 - 4
#     calc += 7 - 4
#     calc += 7 
# print(calc)
#calculos acima foi feito para pensar na lógica do programa abaixo, logo, desconsidere. 
tamanho_muro = 10000
subida_dia = 100
descida_noite = 50
progresso, dias_percorridos = 0, 0

while True:
    if progresso + subida_dia >= tamanho_muro:
        progresso += subida_dia
        dias_percorridos +=1
        break
    else: 
        progresso += subida_dia-descida_noite
        dias_percorridos +=1

print(progresso, dias_percorridos)


