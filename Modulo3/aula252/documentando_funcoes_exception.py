"""Este módulo demonstra como documentar EXCEÇÕES (Raises).
"""

# -------------------------------------------------------------------------
# 1. Google Style
# -------------------------------------------------------------------------
def funcao_google(x: int, y: int) -> int:
    """Realiza uma operação, mas falha se y for 2.

    Args:
        x (int): O primeiro número.
        y (int): O segundo número.

    Returns:
        int: O resultado da operação.

    Raises:
        ValueError: Se y for igual a 2.
    """
    if y == 2:
        raise ValueError("y não pode ser 2 neste sistema")
    return x + y


# -------------------------------------------------------------------------
# 2. NumPy Style 
# -------------------------------------------------------------------------
def funcao_numpy(x: int, y: int) -> int:
    """
    Realiza uma operação, mas falha se y for 2.

    Parameters
    ----------
    x : int
        O primeiro número.
    y : int
        O segundo número.

    Returns
    -------
    int
        O resultado da operação.

    Raises
    ------
    ValueError
        Se o valor de y for estritamente igual a 2.
    """
    if y == 2:
        raise ValueError("y não pode ser 2 neste sistema")
    return x + y


# -------------------------------------------------------------------------
# 3. Padrão reST - reStructuredText
# -------------------------------------------------------------------------
def funcao_padrao(x: int, y: int) -> int:
    """Realiza uma operação, mas falha se y for 2.

    :param x: O primeiro número.
    :type x: int
    :param y: O segundo número.
    :type y: int
    :return: O resultado da operação.
    :rtype: int
    :raises ValueError: Se y for igual a 2.
    """
    if y == 2:
        raise ValueError("y não pode ser 2 neste sistema")
    return x + y
