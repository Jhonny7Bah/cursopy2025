#iterando strings com while 
user_name = input('digite o seu primeiro nome: ') #pergunta o nome do usuario
name_array = [] #variavel preparada para receber o nome do usuario como lista
x = 0 #variavel responsável para navegar no nome do usuario

for conversao_para_array in user_name: #conversão de str para array 
    name_array.append(user_name[x]) 
    x+=1

lista2 = ['*'] #nova lista para receber o conteúdo da lista anterior juntamente com o '*' após cada letra
contar_caracter = len(name_array) #conta quantas letras tem na array
x = 0 #reinicia o navegador 

while x < contar_caracter: #adiciona o conteúdo de nome array para lista2

    lista2.append(name_array[x])
    lista2.append('*')
    x+=1

conversao = ''.join(lista2) #converte de lista para str novamente. 

print(conversao)
