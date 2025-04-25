# Exercício - Salve sua classe em JSON
 # Salve os dados da sua classe em JSON
 # e depois crie novamente as instâncias
 # da classe com os dados salvos
 # Faça em arquivos separados.
import json

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
p1 = Pessoa('João', 'Cardoso')

def fazerDUMP():
    CAMINHO = 'D:\\Ghost\\Usuário\\Desktop\\cursoPyModulo3\\exercicios\\modulo03\\BASE.json'
    with open(CAMINHO, 'w', encoding='utf8') as salvar:
        json.dump(p1.__dict__, salvar, indent=2, ensure_ascii=True)
    print(p1.nome)
    print(p1.sobrenome)

if __name__ == '__main__':
    fazerDUMP()


        

