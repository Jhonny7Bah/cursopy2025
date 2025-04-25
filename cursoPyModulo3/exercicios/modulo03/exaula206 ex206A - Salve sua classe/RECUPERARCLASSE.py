import json
from SALVARCLASSE import Pessoa, fazerDUMP
#o fazer dump vai ser útil quando eu quiser que ele execute o SALVARCLASSE novamente com o inuito de salvar mais uma nova class.

CAMINHO = 'D:\\Ghost\\Usuário\\Desktop\\cursoPyModulo3\\exercicios\\modulo03\\BASE.json'
with open(CAMINHO, 'r') as recuperacao:
    dados = json.load(recuperacao)

#como pode ver, a duplicata foi um sucesso!
print('-'*10)
duplicata = Pessoa(**dados)
print(duplicata.nome)
print(duplicata.sobrenome)

