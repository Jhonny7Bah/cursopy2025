# 🧠 Desafio: Contar Vogais
# Crie uma função que receba uma string e retorne quantas vogais ela contém (a, e, i, o, u).
# Não se preocupe com acentos.
# 
# entrada = "Python é divertido"
# saida_esperada = 6  # (y não conta, e o é ignorado por causa do acento)
# 

#modo tradicional
def contar_vogal(string: str) -> int:
    vogais = 'aeiou'
    quantidade = 0
    for realizar_conta in vogais:
         conta = string.lower().count(realizar_conta)
         quantidade += conta
    return quantidade

print(contar_vogal('aeiouU'))

#modo pythônico
def contar_vogais_pythonica(string: str) -> int:
     vogais = sum([
          string.lower().count(vogal) for vogal in 'aeiou'
     ])
     return vogais
print(contar_vogais_pythonica('aeiou'))