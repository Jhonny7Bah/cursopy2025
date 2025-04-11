#faça uma função que multiplica todos os argumentos entre si na chamada da função
def multiplicador(*args):
    multiplicacao = 1
    for __ in range(len(args)):
        multiplicacao *= args[__]
        total = multiplicacao
    return total 

print(multiplicador(10,10))
print()

#faça uma função que verifica se o número é impar ou par
def paridade(num):
    teste = 'é par' if num % 2 == 0 else 'é impar' #vou utilizar uma operação ternária para verificar a paridade
    return teste
print(paridade(45))




#função multiplicadora que faz a mult de forma mais limpa e simples que a solução anterior.
def mulptiplicando(*args):
    total = 1 # começando de 1 pq qualquer numero multiplicado por 1 é 0, logo a multiplicação daria errado

    for mult in args: #mult em um for acaba se tornando um iterável devido a args.
        #pois o for diz: para cada varmult presente no range args, faça isso:]
        #então, o for mult vai se repetir conforme a quantidade de elementos presente em args.
        #além disso, mult uma hora vai ser 100, outra hora vai ser 20, outra será 30.
        total *= mult #por isso, dá pra realizar a multiplicação diretamente de mult.
    return total   
print(mulptiplicando(100, 20, 30))

