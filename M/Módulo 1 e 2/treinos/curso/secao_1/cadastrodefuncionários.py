

salas = [ #lista dentro de lista
    #0          #1
    ['Carlos', 'André'], #0
    #0          #1
    ['juliano', 'Carlão'], #1
    #0
    ['Coroi', (10, 20, 30)] #2 também consigo incrementar uma tupla dentro da lista

]
print(salas[1][1]) #irá ser printado carlão
print(salas[2][1][2]) #imprimindo o 30 presente na tupla


for sala in salas: #para cada itens na variável salas
    for aluno in sala: #percorra todos os elementos e armazene em "sala"
        print(aluno) #exiba os elementos um a um
