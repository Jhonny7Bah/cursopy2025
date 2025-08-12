# 🧠 Desafio: Palavras Únicas e Contagem
# Crie uma função que:

# Receba uma string com uma frase (pode ter palavras repetidas).

# Retorne uma tupla com duas coisas:

# Uma lista ordenada com todas as palavras únicas (sem repetição, ordem alfabética).

# Um gerador que vá emitindo uma a uma as palavras da frase em ordem original,
#  mas sem repetir palavras já emitidas.

# entrada = "python é bom e python é poderoso"
# 
# saida_esperada = (
    # ['bom', 'é', 'poderoso', 'python'],   # <- lista única ordenada
    # <gerador que retorna: 'python', 'é', 'bom', 'poderoso'>  # <- sem repetir, na ordem original
# )
##############################################

def frase_ordenada(frase: str) -> list :
    separando_frase = frase.lower().split()
    filtrando_retorno = {x for x in separando_frase}
    filtrar_com_genetor = (x for x in filtrando_retorno)
    return sorted(filtrar_com_genetor)

print(frase_ordenada('python é bom e python é poderoso'))
