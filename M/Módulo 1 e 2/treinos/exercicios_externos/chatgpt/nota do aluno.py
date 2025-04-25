# Objetivo: Trabalhar com list comprehension e dicionários para extrair e transformar dados.
# Tarefa:

# Dada uma lista de dicionários representando alunos, onde cada dicionário tem as chaves "nome" e 
# "nota" (um valor numérico entre 0 e 100), crie uma nova lista de dicionários que inclua, além do nome, um novo campo "conceito".

# Use a seguinte regra para definir o conceito:
# Nota ≥ 90: A
# Nota entre 80 e 89: B
# Nota entre 70 e 79: C
# Nota entre 60 e 69: D
# Nota abaixo de 60: E
# Exemplo:
# Resultado esperado (parcial):
# [
#     {'nome': 'Ana', 'conceito': 'A'},
#     {'nome': 'Bruno', 'conceito': 'B'},
#     {'nome': 'Carlos', 'conceito': 'D'},
# ]


alunos = [
    {'nome': 'Ana', 'nota': 95},
    {'nome': 'Bruno', 'nota': 82},
    {'nome': 'Carlos', 'nota': 68},
    {'nome':'Joana', 'nota':75}
]
notas_alunos = [{'nome':aluno['nome'], 'conceito': 'A' if aluno['nota'] >= 90 else 'B' if aluno['nota'] >= 80 and aluno['nota'] <= 89 else 'C' if aluno['nota'] >= 70 and aluno['nota'] <= 79 else 'D' if aluno['nota'] >= 60 and aluno['nota'] <= 69 else 'E'} for aluno in alunos]
#apesar de ser um execício para fixação, em um projeto real, fazer uso de um list comprehension dessa forma é inadequando, pois ficou complexo para entender com facilidade, o que vai contra o objetivo do python, que é ser fácil, prático e relativamente rápido e compreensível o entendimento.
print(*notas_alunos, sep='\n')
#logo, abaixo vou deixar uma forma mais aceita para tal exercício proposto.

def respostar_dicionario(conceito): 
    dicionario_atualizado.append({'nome':notas['nome'], 'conceito':conceito })

print('')
dicionario_atualizado = []
for notas in alunos:
    if notas['nota'] >= 90:
        respostar_dicionario('A')
    elif notas['nota'] >= 80 and notas['nota'] <= 89:
        respostar_dicionario('B')
    elif notas['nota'] >= 70 and notas['nota'] <= 79:
        respostar_dicionario('C')
    elif notas['nota'] >= 60 and notas['nota'] <= 69:
        respostar_dicionario('D')
    elif notas['nota'] < 60:
        respostar_dicionario('E')
print(*dicionario_atualizado, sep='\n')

#última forma: 
#vamos tentar deixar o list comprehension mais visual:
print('')
ultima_forma = [
    {
        'nome':aluno['nome'], 'conceito': ('A' if aluno['nota'] >= 90 else
        'B' if aluno['nota'] >= 80 and aluno['nota'] <= 89 else
        'C' if aluno['nota'] >= 70 and aluno['nota'] <= 79 else
        'D' if aluno['nota'] >= 60 and aluno['nota'] <= 69 else
        'E' 
        )
    }
    for aluno in alunos
]
print(*ultima_forma, sep='\n')