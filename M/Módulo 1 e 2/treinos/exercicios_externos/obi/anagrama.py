#primeira forma
# p1 = 'casa'
# p2 = 'saca'

# lista_vazia = []


# print(p1 in p2)


# for __ in p1:
#      lista_vazia.append(__)
# print(lista_vazia)

# i = 0
# for p22 in p2:
#     if lista_vazia[i] in p2:
#           print('tem')
#     else:
#          print('tem não')
#     i+=1
#outra forma
# p1 = 'casa'
# p2 = 'saca'

# lista_vazia = []

# i = 0
# for __ in p1:
#      lista_vazia.append(__)
#      if lista_vazia[i] in p2:
#           print('tem')
#      else:
#          print('tem não')
#      i+=1

#outra forma
# p1 = 'casa'
# p2 = 'saca'
# for __ in p1:
#      if __ in p2:
#           print('tem')
#      else:
#          print('tem não')

#outra forma
# def anagrama(palavra_A, palavra_B):
#     for iteracao in palavra_A:
#         if iteracao in palavra_B and len(palavra_A) == len(palavra_B):
#             return 'S'
#         return 'N'
# print(anagrama('casa', 'sacaa'))
# print(anagrama('a', 'b'))
# print(anagrama('aca aaa bb b', 'ba.ba,aab ac'))
# print(anagrama('portal coral', 'claro trapo'))

#outra forma
# 

def anagrama(palavra_a, palavra_b):
    lista_vazia = []
    i, c= 0, 1
    for __ in palavra_a:
        lista_vazia.append(__)
        if lista_vazia[i] in palavra_b and len(palavra_a) == len(palavra_b): c+=1
        i+=1
        return(c)
        # return 'S' if c == len(palavra_a) else 'N'
print(anagrama('casa', 'casa'))
