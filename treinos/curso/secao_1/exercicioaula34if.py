primeiro_valor = input('digite um valor ')
segundo_valor = input('digite outro valor ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior do que o {segundo_valor=}')
elif primeiro_valor < segundo_valor:
    print(f'{segundo_valor=} é maior do que o {primeiro_valor=} ')
else:
    print(f'ao que parece, {primeiro_valor=} e {segundo_valor} são iguais ou congruentes. ')