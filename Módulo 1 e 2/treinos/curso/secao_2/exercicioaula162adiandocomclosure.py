def somando(x):
    def soma(y):
        return x + y
    return soma

def multiplicando(x):
    def multiplica(y):
        return x * y
    return multiplica
        

def executa(funcao, *args):
    return funcao(*args)


soma_cinco = executa(somando, 5)
multiplica_10 = executa(multiplicando, 10)
print(soma_cinco(6))
print(multiplica_10(10))
