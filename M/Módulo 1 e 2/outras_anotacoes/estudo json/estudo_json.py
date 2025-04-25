# json - javascript object notation
#json é um banco de dados, uma estrutura de dados com o intuito de manipular ou armazenar dados.
#no caso abaixo, vou demonstar inicialmente como salvar o dicionário a seguir em um json

#o jason pode ter os seguites tipos de dados:
# int - 123
# float - 1.4
# str - 'opa'
# null - um não valor, falsy
# bool - False
# list - []
# dict - {'opa':'slk',}

{
    "name":"Joana",
    "lastName":"Torres",
    "age":32,
    "adress":[{"adress_one": "Av Brasil"}, {"adress_two":"Beco da Matanca"}]
}
#o exemplo acima demostra a forma como uma série de informações é incrementada no json.
#é bem similar ao dict de python, mas tem diferenças. Por exemplo, no dict, temos keys e values, podendo ser colocado com aspas simples e duplas quando str
#no json, tem que ser aspas duplas para chave e valor.
#outra coisa é que no python, podemos colocar uma vírgula após definir uma key e value e não colocar mais nada. No json, se você colocar uma virgula, significa que você colocará mais uma chave e valor. Se não fizer, o código quebra.

pessoa = {
    'nome':'Carlos',
    'sobrenome':'Santos'
}
from os import path
import json
BASE_DIR = path.dirname(__file__)
save_to = path.join(BASE_DIR, 'arquivo_python.json')
with open(save_to, 'w') as file:
    json.dump(pessoa, file, indent=2)
#acima, salvei o que estava presente no dict pessoas em um .json, ou seja, eu criei e salvei.

#abaixo, vou mostrar como eu pego o que estiver em um json e coloco em um python.
BASE = path.dirname(__file__) 
JSON_FILE = path.join(BASE, 'arquivo_python.json')

with open(JSON_FILE, 'r') as files:
    puxada = json.load(files)
print(puxada)


print('cacetinha','aoba',sep=' TOMA ')
