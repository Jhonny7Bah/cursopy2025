# 🧠 Desafio: Palíndromo
# Crie uma função que receba uma string e retorne True se ela for um palíndromo
# (ou seja, se ela lê da mesma forma de frente para trás e de trás para frente),
#  e False caso contrário.

# Exemplo:
# 
# entrada = "radar"
# saida_esperada = True
# 
# entrada = "python"
# saida_esperada = False

def is_palindromo(palavra: str) -> bool:
    tamanho = len(palavra)-1
    lista_invertida = []
    while tamanho >= 0:
        lista_invertida.append(palavra[tamanho])
        tamanho -=1
    juncao = ''.join(lista_invertida)
    
    if juncao == palavra:
        return True
    return False

print(is_palindromo('radar'))
print(is_palindromo('radarr'))

#solucao2 (modo pythônico ativado - boraa javeiro)
def palindromo_pythonico(palavra: str) -> bool:
    invertendo_palavra = palavra[::-1].lower().strip()

    if invertendo_palavra == palavra.lower().strip():
        return True
    return False

print(palindromo_pythonico('radar'))