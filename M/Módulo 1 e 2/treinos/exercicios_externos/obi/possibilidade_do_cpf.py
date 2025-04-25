import itertools

def calcular_digitos(cpf_parcial):
    """
    Recebe os 9 primeiros dígitos do CPF (como string) e calcula os 2 dígitos verificadores.
    """
    # Primeiro dígito verificador
    soma = sum(int(cpf_parcial[i]) * (10 - i) for i in range(9))
    d1 = (soma * 10) % 11
    if d1 == 10:
        d1 = 0

    # Segundo dígito verificador
    soma = sum(int(cpf_parcial[i]) * (11 - i) for i in range(9))
    soma += d1 * 2
    d2 = (soma * 10) % 11
    if d2 == 10:
        d2 = 0

    return str(d1), str(d2)

def validar_cpf(cpf):
    """
    Verifica se o CPF (string com 11 dígitos) é válido.
    """
    if len(cpf) != 11:
        return False
    d1, d2 = calcular_digitos(cpf[:9])
    return cpf[9] == d1 and cpf[10] == d2

def limpar_padrao(padrao):
    """
    Remove quaisquer caracteres que não sejam dígitos ou '*' do padrão.
    """
    return ''.join(c for c in padrao if c.isdigit() or c == '*')

def gerar_cpfs(padrao, regiao='5'):
    """
    Gera todos os CPFs válidos que se encaixam no padrão fornecido,
    filtrando para que o nono dígito (posição 9) seja igual ao especificado em 'regiao'.
    Por padrão, 'regiao' é '5' (Bahia e Sergipe).
    
    Exemplo de padrão: "***526225**"
    """
    padrao = limpar_padrao(padrao)
    if len(padrao) != 11:
        print("O padrão deve conter 11 caracteres (dígitos ou '*').")
        return []
    
    # Se o dígito na posição 9 já estiver definido e não corresponder à região desejada,
    # não há possibilidade de gerar CPFs válidos para essa filtragem.
    if padrao[8] != '*' and padrao[8] != regiao:
        print("O padrão não corresponde à região fiscal desejada.")
        return []
    
    # Índices dos caracteres desconhecidos
    indices = [i for i, c in enumerate(padrao) if c == '*']
    cpfs_validos = []
    
    # Itera sobre todas as combinações possíveis para os dígitos desconhecidos
    for combinacao in itertools.product('0123456789', repeat=len(indices)):
        lista_cpf = list(padrao)
        for i, digito in zip(indices, combinacao):
            lista_cpf[i] = digito
        cpf_str = ''.join(lista_cpf)
        
        # Filtra: o nono dígito deve ser igual ao da região desejada (ex: '5' para Sergipe)
        if cpf_str[8] != regiao:
            continue
        
        if validar_cpf(cpf_str):
            cpfs_validos.append(cpf_str)
    return cpfs_validos

# Exemplo de uso:
padrao = "***526225**"  # Padrão com '*' para os dígitos desconhecidos
cpfs = gerar_cpfs(padrao, regiao='5')  # '5' indica CPFs registrados em Sergipe (ou Bahia)

print("Possíveis CPFs (filtrados para a região com dígito '5'):")
for cpf in cpfs:
    print(cpf)
