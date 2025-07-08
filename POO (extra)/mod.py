# decoradores comuns:
    #classmethod
    # staticmethod

class MinhaClasse:
    valor = 20 #isso aqui chama-se atributo de classe e pode ser acessado de qualquer lugar, desde que esteja dentro da classe.
    def __init__(self):
        pass

    # para acessar, basta colocar self e o namespace para o nome do atributo
    def value(self):
        return self.valor
obj = MinhaClasse()
print(obj.valor)

# posso fazer diretamente pela classe tbm
print(MinhaClasse.valor)

#no entanto, é apenas nesses casos. Pois normalmente, precisariamos de uma instância para acessar determinado valor de uma classe.

#################### static metod -> método estático
#é um método de classe utilizado como decorador para indicar que um método de classe ou um conjunto não haverá parâmetros como cls ou self. Ou seja, é literal um método parado.
# Segundo o professor, não é um bom sinal quando há uam quantidade meio grandinha de métodos estáticos.

# vou criar um exemplo qualquer
class Matematica:
    @staticmethod
    def somar(x, y):
        return x+y
# agora, basta criar um objeto
realizar_soma = Matematica.somar(10, 20)
print(realizar_soma)

#já o classmethod, é normalmente utilizado quando queremos criar instância para a nossa própria classe, trocando o self por cls. EX:
#o classmethod não depende necessariamente de um objeto ou de uma instância (self) para existir.
# class Pessoaa:
# def__init__(self, nome, idade, sexo):
    # self.nome = nome
    # self.idade = idade
    # self.sexo = sexo

# @classmethod
# def criar_com_idade(cls, idade, sexo, altura_padrao=1.70):
    # nome = f"Pessoa{idade}{sexo.upper()}"  # Nome genérico só pra exemplo
    # pessoa = cls(nome, idade, sexo)
    # pessoa.altura = altura_padrao  # adiciona atributo extra
    # return pessoa
# 

# Criando uma pessoa com classmethod
# p = Pessoa.criar_com_idade(25, 'f')

# print(f"Nome: {p.nome}")
# print(f"Idade: {p.idade}")
# print(f"Sexo: {p.sexo}")

##############################