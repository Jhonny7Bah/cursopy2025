# clientes , contas, banco(corrente, poupanca)
# o cliente pode sacar ou depositar na conta
# se o cliente tiver conta corrente, terá um x limite extra.

# conta corrente e poupanca serão duas classes
# Contas têm agência, número da conta e saldo
#  Contas devem ter método para
# Conta (super classe) deve ter o método sacar abstrato (Abstração e
# polimorfismo - as subclasses que implementam o método sacar)

# cliente -> nome, idade (getters.)
# Clinte tem conta (agregacão)


# Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
# Banco será responsável autenticar o cliente e as contas da seguinte maneira:
#     Banco tem contas e clentes (Agregação)
#     * Checar se a agência é daquele banco
#     * Checar se o cliente é daquele banco
#     * Checar se a conta é daquele banco
# Só será possível sacar se passar na autenticação do banco (descrita acima)
# Banco autentica por um método.

from abc import ABC, abstractmethod


####################
###    Pessoa    ###
####################
# Pessoa será o usuário comum
class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    # exibe o nome do usuário
    @property
    def nome(self):
        return self._nome

    # exibe a idade do usuário
    @property
    def idade(self):
        return self._idade


####################
###    Contas    ###
####################
class Conta(ABC):
    '''
    Conta será a classe mãe irá originar duas classes filhas que serão dadas
    como poupança e corrente. Seu objetivo é permitir a criação da conta do
    usuário em uma dessas duas vertentes. Ademais, será permitido também
    realizar o saque e depósito de forma controlada pós criação das contas
    em questão (CONSIDERE QUE ESTA CLASSE É ABSTRATA).
    '''
    @abstractmethod
    def __init__(self, agencia: str, numero: str, saldo: float = 0):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

    @abstractmethod
    def sacar(self, valor): ...

    @property
    def agencia(self):
        return self._agencia

    def depositar(self, valor):
        # verifica se o valor a ser depositado é positivo
        if valor > 0:
            print(f' {valor} foi depositado com sucesso! ')
            self._saldo += valor
        else:
            print('valor inválido')


class ContaCorrente(Conta):
    '''
    Conta corrente herda de Conta e seu limite_extra é dado como 50,
    sendo considerado no saque.
    '''
    limite_extra = 50.0

    def __init__(self, agencia: str, numero: str, saldo: float = 0):
        super().__init__(agencia, numero, saldo)

    def sacar(self, valor: float):
        '''
        O método sacar irá realizar uma análise tanto do saldo do usuário como
        do limite_extra. Se um desses dois for maior ou igual ao valor que o
        usuário quer sacar, então o saque será realizado. Caso contrário,
        a tentativa de saque será inválida.
        '''

        # se houver saldo, então será realizado o saque normalmente
        if self._saldo >= valor and valor >= 1:
            print(f' {valor} foi sacado com sucesso! ')
            self._saldo -= valor

        # se o saldo for insuficiente, mas o usuário tem limite_extra sobrando
        # então também será possível realizar o saque.
        elif self.limite_extra + self._saldo >= valor and valor >= 1:
            print(f' {valor} foi sacado com sucesso, juntamente com o extra ')
            # para essa conta matemática, é o seguinte:
            # - após uma subtração com o valor desejado, saldo ficará negativo.
            # - limite_extra é positivo, se realizado uma soma com o saldo, que
            #   agora é negativo, será realizado uma subtração.
            # - após isso, será necessário apenas redefinir o valor do saldo.

            self._saldo -= valor
            self.limite_extra += self._saldo
            self._saldo = 0

        #  se o valor do saldo for 0
        elif valor == 0:
            print(f'Não é possível sacar {valor} reais. Mínimo: 1 Real.')

        # caso o usuário realmente não tenha saldo nem limite, não poderá sacar
        else:
            print('sinto muito, saldo insuficiente.')


class ContaPoupanca(Conta):
    '''
    Conta poupança é uma classe que herda de conta e seu limite_extra
    é dado como 0.

    '''

    def __init__(self, agencia: str, numero: str, saldo: float = 0):
        super().__init__(agencia, numero, saldo)

    # redifinição do sacar da classe mãe.
    def sacar(self, valor):
        if self._saldo >= valor and valor >= 1:
            print(f' {valor} foi sacado com sucesso! ')
            self._saldo -= valor

        elif valor == 0:
            print(f'Não é possível sacar {valor} reais. Mínimo: 1 Real.')

        else:
            print('valor inválido')

####################
###   Clientes   ###
####################


class Clientes(Pessoa):
    '''
    A classe cliente irá apenas realizar uma estrutura dos dados do usuário com
    agregação, com o intuito de garantir um controle melhor.
    '''

    def __init__(
        self,
        nome: str,
        idade: int,
        conta: ContaPoupanca | ContaCorrente
    ):

        self.conta = conta
        super().__init__(nome, idade)


####################
###    Banco     ###
####################

class Banco:
    '''
    O banco será o lugar por onde o usuário vai fazer solicitações, como:

    - sacar
    - depositar
    - autenticar
    - adicionar cliente
    - adicionar conta

    O usuário poderá gerenciar sua conta através dessa classe, contanto que
    realize os requisitos necessários.

    Um dos requisitos é a autenticação para realizar o saque ou depósito.
    Caso o usuário não tenha uma conta, ele pode criar normalmente para
    depois sim realizar a autenticação para usar sua conta como quiser.

    '''

    # agencias definidas por padrão pelo banco em questão quando a classe
    # inicializar
    def __init__(self):
        self.agencias = ['0001', '0002']
        self.contas = []
        self.clientes = []

    # como o próprio nome já diz: adiciona um próprio cliente após ele ter
    # sido criado pela classe Clientes.
    def adicionar_cliente(self, cliente: Clientes):
        self.clientes.append(cliente)

    # após o cliente ser criado, esse método irá incrementar o novo cliente
    # em nossa 'base de dados'
    def adicionar_conta(self, conta: ContaCorrente | ContaPoupanca):
        self.contas.append(conta)

    # autenticação da conta do usuário (não chame fora da classe)
    def _autenticar(
            self,
            cliente: Clientes,
            conta: ContaCorrente | ContaPoupanca,
            agencia: str,
    ):

        # verificação de existência.
        cliente_bool = cliente in self.clientes
        conta_bool = conta in self.contas
        agencia_bool = agencia in self.agencias

        if cliente_bool and conta_bool and agencia_bool:
            return True
        return False

    # pode realizar o saque + realiza autenticação
    def sacar(self, cliente: Clientes, valor):
        # realizando autenticação
        autenticacao = self._autenticar(
            cliente=cliente,
            conta=cliente.conta,
            agencia=cliente.conta.agencia
        )

        # verificando status
        if not autenticacao:
            return 'não autencicado'
        cliente.conta.sacar(valor=valor)

    # pode realizar o depósito + realiza autenticação
    def depositar(self, cliente: Clientes, valor):
        # realizando autenticação
        autenticacao = self._autenticar(
            cliente=cliente,
            conta=cliente.conta,
            agencia=cliente.conta.agencia
        )

        # verificando status
        if not autenticacao:
            return 'não autencicado'
        cliente.conta.depositar(valor=valor)


# criando o primeiro cliente
c1 = Clientes(
    'joao',
    18,
    ContaPoupanca(
        '0001',
        '838393939393'
    )
)

# criando o banco
banco_umcex = Banco()

# incrementando cliente no banco
banco_umcex.adicionar_cliente(c1)
banco_umcex.adicionar_conta(c1.conta)

# movimentando conta no banco
banco_umcex.sacar(c1, 20)
banco_umcex.depositar(c1, 50)
banco_umcex.sacar(c1, 20)
