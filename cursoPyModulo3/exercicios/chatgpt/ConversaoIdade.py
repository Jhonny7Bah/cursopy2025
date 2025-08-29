# ### Exercício

# Crie uma classe `Pessoa` que:

# * tenha `nome` e `idade` como atributos.
# * permita criar uma instância **normalmente** (`Pessoa("Ana", 30)`).
# * tenha um **factory method** chamado `from_ano_nascimento(nome, ano)` 
# que receba o nome e o ano de nascimento, calcule a idade (considerando 2025), e retorne a instância.

# ### Objetivo

# Você precisa implementar o método `from_ano_nascimento` usando `@classmethod` e `cls`.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    #método ano nascimento
    def from_birth_year(cls, name, year):
        birth_year = 2025 - year
        return cls(name, birth_year)

p1 = Person('João', 18)
print(p1.name, p1.age)

p2 = Person.from_birth_year('Pedro', 1995)
print(p2.name, p2.age)
