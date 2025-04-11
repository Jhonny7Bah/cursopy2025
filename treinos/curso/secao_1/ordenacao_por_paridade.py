
array = []
arrayimpar = []
arraypar = []

for vai in range (0, 10):
    numeros_digitados = int(input('digite os números: '))
    array.append(numeros_digitados)

    if numeros_digitados % 2 == 0:
        arraypar.append(numeros_digitados)
    else:
        arrayimpar.append(numeros_digitados)

    
arrayimpar = sorted(arrayimpar)
arraypar = sorted(arraypar)

array_final = arraypar + arrayimpar

print(array_final)



'''
array = [0, 14, 16, 20, 13]

i = 0
tempar = 0
for tratamentopar in range(0, len(array)):
    if(array[i] % 2 == 0 ):
        tempar +=1
    i +=1
array = sorted(array[0:tempar])

i = 0
temimpar = 0
for tratamentoimpar in range(0, len(array)):
    if array[i] % 2 == 1:
        temimpar +=1
    i +=1

array = sorted(array[tempar+1:])

print(array)

'''