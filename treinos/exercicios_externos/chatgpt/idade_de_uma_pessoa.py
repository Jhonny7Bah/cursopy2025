hoje = {
    'dia':18,
    'mes': 2,
    'ano':2025,
}
nascimento = {
    'dia':24,
    'mes': 2,
    'ano':1970,
}

ano_do_cidadao = hoje['ano'] - nascimento['ano']
print(ano_do_cidadao)
if hoje['mes'] < nascimento['mes']:
    ano_do_cidadao-=1

elif hoje['mes'] == nascimento['mes']:
    if hoje['dia'] < nascimento['dia']:
        ano_do_cidadao -=1
print(ano_do_cidadao)