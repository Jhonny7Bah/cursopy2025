#sem def
n1 = 1, 10+2
for __ in range(2, n1[1]): print(f'{n1[0] * __} number')

#com def
def duplicar(x):
    print(x*2)
    def triplicar():
        print(x*3)
        def quadruplicar():
            print(x*4)
        return quadruplicar()
    return triplicar()
print(duplicar(10))

#outra forma
def crescer_num(x):
    limite = 30 + 2
    for __ in range(2, limite):
        print(x * __)
print(crescer_num(1))

#outra forma
def criar_funcoes(multiplicador):
    def multiplicar(numero):
         return multiplicador * numero
    return multiplicar

duplicarrrr = criar_funcoes(2) #multplicador
print(duplicarrrr(3)) #numero