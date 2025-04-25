#iterando strings com while 
user_name = input('digite o seu primeiro nome: ') #pergunta o nome do usuario
name_array = [] #variavel preparada para receber o nome do usuario como lista
x = 0 #variavel responsável para navegar no nome do usuario
lista2 = ['*'] #nova lista para receber o conteúdo da lista anterior juntamente com o '*' após cada letra
contar_caracter = len(user_name) #conta quantas letras tem na array


while x < len(user_name): #conversão de str para array
    name_array.append(user_name[x]) 
    x+=1

x = 0 #reinicia o navegador 

while x < contar_caracter: #adiciona o conteúdo de nome array para lista2

    lista2.append(name_array[x])
    lista2.append('*')
    x+=1

conversao = ''.join(lista2) #converte de lista para str novamente. 

print(conversao)

#outra forma de fazer mais simples 
x = 0
novonome = ''
for teste in user_name:
    caceta = user_name[x]
    novonome += f'*{caceta}'
    x+=1

print(novonome)
