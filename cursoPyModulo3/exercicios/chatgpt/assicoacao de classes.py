
'''
📝 Exercício: Associação entre classes
Crie duas classes:

Cliente: que tem os atributos nome e email.

Pedido: que tem os atributos id e produto.

A associação será: um cliente pode fazer um pedido, ou seja, um objeto da classe Pedido deve referenciar um objeto da classe Cliente.

Requisitos:
A classe Pedido deve receber um objeto Cliente como atributo.

Implemente um método em Pedido que imprima os dados do pedido junto com os dados do cliente.

Crie um cliente e dois pedidos associados a esse cliente. Imprima os detalhes.
'''
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Pedido:
    def __init__(self, id, produto, cliente=None):
        self.id = id
        self.produto = produto
        self.cliente = cliente
    
    def chamar_cliente(self):
        print(f'''
Pedido {self.id}: Produto = {self.produto}
Cliente: {self.cliente.nome} (Email: {self.cliente.email})
''')

#cliente
cliente1 = Cliente('Maria', 'maria@gmail.com')

#pedido um
pedido1 = Pedido('101', 'notebook', cliente1)
print(pedido1.chamar_cliente())

#pedido2
pedido2 = Pedido('102', 'Smartphone', cliente1)
print(pedido2.chamar_cliente())
        


