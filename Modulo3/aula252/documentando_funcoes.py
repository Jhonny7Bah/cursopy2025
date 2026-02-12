"""Este módulo apenas vai exemplificar o uso de uma função com docstring

No geral, haverá somente duas funções.
"""

def multiplica(
    x: int | float,
    y: int | float,
    z: int | float | None = None
) -> int | float:
    """Multiplica x, y e/ou z

    Multiplica x e y. Se z for enviado, multiplica x, y, z.
    """
    if z is None:
        return x * y
    return x * y * z

# eu não ia mostrar outra forma de usar doc numa função, mas farei abaixo:
def subtracao(x, y):
    """ Essa função realizará uma
        subtração entre x e y.
    
    :param x: primeiro número    
    :type x: int ou float
    :param y: segundo número    
    :type y: int ou float
    
    :return y: subtração de x - y
    :return_type: int ou float
    """

    return x-y
