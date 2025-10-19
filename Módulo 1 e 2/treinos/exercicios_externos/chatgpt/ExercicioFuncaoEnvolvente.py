def envolvedor(funcao_original):
    def nova_funcao(*args):
        print('Início da Execução!!')
        resultado = funcao_original(*args)
        print('fim da execução!!!')
        return resultado
    return nova_funcao

def soma(x,y):
    return x + y

soma_envolvida = envolvedor(soma)
print(soma_envolvida(10,20))

#agopra eu sei oq é de fato um decorator. 
