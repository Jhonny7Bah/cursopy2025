lista_compras = []
valor = None
indice_apagar = None
import os

while True:
    dado_digitado = input('[i]nserir [a]pagar [l]istar: ')
    #se o valor digitado for i
    if dado_digitado.lower().startswith('i'):
        valor = input('Valor: ')
        lista_compras.append(valor)
        os.system('cls')
        #se for a
    elif dado_digitado.lower().startswith('a'):
        #verificando se tem algo na lista para ser apagado
        if lista_compras == []:
            print('Não tem nada para apagar. ')

        else:
            indice_apagar = input('Qual indice deseja apagar? ')
            if indice_apagar.isnumeric():
                #verificando se o número do índice digitado existe para ser apagado
                if len(lista_compras) <= int(indice_apagar):
                    print('Não tem esse índice na lista')
                #apagando item da lista
                else:
                    del lista_compras[int(indice_apagar)]
        
            else:
                print('Esse índice não é um número ')

    #começando com l
    elif dado_digitado.lower().startswith('l'):
        #verificando se há algo na lista
        if lista_compras == []:
            print('Não tem nada na sua lista')
        else:
            os.system('cls')
            mostrar_lista = enumerate(lista_compras)
            for _ in lista_compras:
                print(next(mostrar_lista))
                
        
    elif dado_digitado == 'j':
        break

    else:
        print('Digite apenas i, a ou l\n')