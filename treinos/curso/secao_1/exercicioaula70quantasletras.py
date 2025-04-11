frase = 'cacettttta'#'O python é uma linguagem de programação'\
    #'multiparadigma. ' \
    #'Python foi criado por Guido van Rossum '
'''

i = 0
var_vazia = ''
quantidade_apareceu_mais = 0



while i < len(frase):

    armazen = (frase.count(frase[i]))
    var_vazia += str(armazen)

    letra_atual = frase[i]
 
    if quantidade_apareceu_mais < int(armazen):
        quantidade_apareceu_mais = int(armazen)
        var_vazia = letra_atual
        

    print(armazen, letra_atual)
    i+=1
print(quantidade_apareceu_mais, var_vazia)
'''

'''
#verificar qual letra mais aparece
frase = 'O python é uma linguagem de programação'\
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum '

i = 0
armazenar_letra_maior = 0
armazenar_indice_letras = ''
inicial = 0
letra_maior = ''

while i < len(frase):
    armazen_contagem_das_letras = frase.count(frase[i]) #essa var salva a quantidade de vezes que a letra apareceu
    armazenar_indice_letras += str(armazen_contagem_das_letras) #essa var pega o salvamento de quantidade dado pela var anterior e armazena nela para não se perder
    armazenar_todas_as_letras = frase[i] #intera em todas as letras da variavel frase e salva

    if armazenar_todas_as_letras == ' ':
        i +=1
        continue

    if int(inicial) <= armazen_contagem_das_letras:
        inicial = armazen_contagem_das_letras
        letra_maior = armazenar_todas_as_letras

    
    
    i+=1
print('Meus parabéns irmão, você finalmente conseguiu\n'
      'A letra que mais apareceu foi o "{porra}"'.format(porra=letra_maior)
      )

'''

#terceira vez
#verificar que frase mais aparece na frase

frase = 'O python é uma linguagem de programação'\
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum '

i = 0
guardar_indices_da_letra = '' #vai armazenar como str os índices das letras
maior_indice_da_letra = 0 #o maior índice é dado como 0 e com o tempo, ele vai aumentando
maior_letra = '' #a maior letra será armazenada nessa variável  

while i < len(frase):
    numero_atual_letra = frase.count(frase[i]) #verifica a quantidade de vezes que uma letra aparece
    guardar_indices_da_letra += str(numero_atual_letra) #armazena a quantidade de vezes que uma letra aparece, com base na variavel anterior 
    
    if frase[i] == ' ': #verifica se há algum espaço na variável
        i +=1 
        continue #reinicia o while  

    elif numero_atual_letra >= maior_indice_da_letra: #se índice da letra for maior que o índice armazenado no momento
        maior_indice_da_letra = numero_atual_letra #(continuacao de cima) o maior índice é redefinido com base no índice que apareceu
        maior_letra = frase[i] #descobre quem a maior letra que apareceu com base no índice máximo. 
    
    i +=1 #aumenta de 1 em 1


print(
    'Parabéns mais uma vez! A maior letra encontrada na frase digitada foi {:-^3}'
      .format(maior_letra)) #informa a maior letra que aparece 