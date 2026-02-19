"""
Esse módulo é apenas uma exemplificacão de documentacao para classes.
"""

class divisao_doc:
    """
    Essa classe é responsável por gerenciar divisões de valores
    de forma responsável, tratando apenas números inteiros.
    """
    def __init__(self, a:int, b:int) -> float:
        """
        Inicializa o construtor com os argumentos passados.
        
        :param a: primeiro valor
        :type a: int
        :param b: segundo valor
        :type b: int
        """
    
        self.valor_a = a
        self.valor_b = b
    
    def calculo(self):
        """
        Verifica o tipo dos argumentos passados e se forem inteiros, então
        realiza uma divisão.
        
        :return: divisão entre o primeiro valor e o segundo
        :rtype: float
        :raises TypeError: Se algum dos argumentos não for inteiro.
        """

        # verifica o tipo dos dados informados
        if not type(all(x,int) for x in (self.valor_a, self.valor_b)):
            raise TypeError('será aceito somente valores inteiros')

        return self.valor_a / self.valor_b
