#lin 1,5
# mat 3.5
# humanas   1  
#natureza   1.5
#redacao    2.5


nota_linguagem = 500
nota_matematica = 500
nota_humanas = 500
nota_natureza = 500
nota_redacao = 800

calculolin = int(nota_linguagem) * 1.5
calculomat = int(nota_matematica) * 3.5
calculohum = int(nota_humanas) * 1
calculonat = int(nota_natureza) * 1.5
calculored = int(nota_redacao) * 2.5

divisao_final = (calculolin + calculomat + calculohum + calculonat + nota_redacao) / 5

print(f'sua nota final foi {divisao_final}')

calcular_imposto = lambda x: x * 2

print(calcular_imposto(10))

preco = [100, 200, 300, 400, 500]
i = 0

print(preco)

for multiplicador in preco:
    preco[i] = preco[i] * 1000   
    i +=1
print(preco)

#mais um jeito de fazer

novas_cuisinhas = [10, 20 ,30, 40, 50]

#List Comprehension
uma_nova_lista = [produtos * 10 for produtos in novas_cuisinhas]
print(uma_nova_lista)

caceta = lambda x: x * 2

print(caceta(nota_humanas))
#list comprehension com if
imposto = [novo_imposto * 0.5 for novo_imposto in novas_cuisinhas if novo_imposto > 40]
 
print(imposto)