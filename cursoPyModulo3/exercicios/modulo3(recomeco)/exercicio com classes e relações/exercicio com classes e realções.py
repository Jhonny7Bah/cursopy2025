# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None
        self.fabricante = None
        pass

class Motor:
    def __init__(self, nome):
        self.nome = nome
        pass

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        pass

f1 = Fabricante('corsair')
m1 = Motor('Brabão')
c1 = Carro('Fusca')

c1.motor = m1
c1.fabricante = f1
print(f'{c1.nome} {c1.fabricante.nome} {c1.motor.nome} ')

#####
f2 = Fabricante('fiat')
m2 = Motor('Brabão')
c2 = Carro('uno')

c2.motor = m2
c2.fabricante = f2
print(f'{c2.nome} {c2.fabricante.nome} {c2.motor.nome} ')









