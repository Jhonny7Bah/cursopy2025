###################################################### revisão
from os import system
def cls():
    return system('cls')
#####closure
def soma(x):
    def interna(y):
        return x+y
    return interna

armazen = soma(10)
print(armazen(20))

####decorator
def subtracao(x, y):
    return x-y

def decorando(func):
    print('VAMOS SUBTRAIR!!!!!')
    def interna(*args, **kwargs):
        print('-'*25)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

inicializar = decorando(subtracao)

print(inicializar(20,5))# com decorator
print()#um espaço 
print(subtracao(20,5)) #sem decorator

cls()
####decorator com syntax sugar
def decorador(func):
    print('eu vou te decorar! muahahaha')
    def interna(*args):
        print('só mais uma decoração...')
        return func(*args)
    return interna
@decorador
def multiplicando(x, y):
    return x*y

print(multiplicando(10,20))

cls()
#list comprehension
lista = [
    f'o número agora é {num}'
    for num in range(11)
    if num > 4 
]
print(lista)

cls()
####map
valores = list(range(11))
print(valores)
conversaoSTR = list(map(str, valores))
print(conversaoSTR)

####
# syntax sugar com parâmetros


def decorator_com_parametros(a, b, c):
    print(f'os meus valores são: {a}, {b} e {c}, mano. ')
    return decoradora

def decoradora(func):
    def aninhada(*args, **kwargs):
        print('-'*50)
        from os import system
        system('color 02')
        resultado = func(*args, **kwargs)
        return resultado
    return aninhada

@decorator_com_parametros(1,2,3)
def realizar_divisao(x, y):
    return x//y

print(realizar_divisao(100,3))

cls()

#####syntax sugar com os parâmetros mais útil
def init_paramametros(a=None,b=None):
    print(f'os meus valores são: {a} e {b}')
    def externa(func):
        def interna(*args, **kwargs):
            a, b = args
            for __ in a, b:
                if not isinstance(__, (int, float)):
                    raise TypeError('Isso aq trata-se de uma potenciação e você informou um valor não numérico. ')
            print('lá vai a potenciaçãaaaao mano!!!!')
            return func(*args, **kwargs)
        return interna
    return externa

@init_paramametros(20,30)
def potenciacao(base, expoente):
    return base ** expoente

print(potenciacao(2,5))

###################
#dicionary comprehension
dicidici = {
    f'chave{x}':f'valor{x}'
    for x in range(10) 
}
system('color 07')
#uso do get
#lembrando que o get é necessário para buscar um valor diretamente pela chave em um dicionário
print(dicidici.get('chave5')) #retornou valor 5, ou seja, a chave5 existe.
print(dicidici.get('chavecarambaaaa')) #Quando a chave não existe, por padrão, ele retorna None.





