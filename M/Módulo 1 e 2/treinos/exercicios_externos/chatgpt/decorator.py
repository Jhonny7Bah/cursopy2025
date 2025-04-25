# ex:
def funcao_decoradora(func): #criei uma função que receberá outra função
    def interna(*args): #aplicaremos o conceito de high order functions e closure para adiar a execução dessa função.
    #ademais, nesse caso vamos trabalhar com argumentos não nomeados, que serão os argumentos informados para a função que vamos derivar.    
        resultado = func(*args) #aqui vamos armazenar a execução a função que iremos receber como argumento e decorar.
        #lembrando que *args como parâmetro vai empacotar argumentos não nomeados, já o *args fora dos parâmetros, vai desempacotar seguindo uma orde posicional 
        return resultado #agora, executamos a função soma, já que é ela que vamos decorar.
    return interna #aqui, adiamos a execução da função intera para não quebrar o código. Isso é closure, só para deixar claro.

#agora, vamos declarar a função soma
def soma(x, y):
    return x+y #aqui, efetivamos a soma.


#agora, vamos colocar o decorator em prática, através de uma variável:
decorator_somador = funcao_decoradora(soma) #aqui, informo para ele quem ele vai decorar
print(decorator_somador(10,20))
