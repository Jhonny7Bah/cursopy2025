def soma(x, y):
    return x + y
#como esse módulo será importado, o código que estiver fora do escopo da condição será executado no ato da importação.
#é devido a isso que eu coloquei os prints de teste dentro de uma condição, que é o __name__, onde será executado apenas quando a execução vier deste módulo.
if __name__ == '__main__': 
    print(soma(40,20))
    print(soma(40,20))
    print(soma(40,20))
    print(soma(40,20))
    print(soma(40,20))
