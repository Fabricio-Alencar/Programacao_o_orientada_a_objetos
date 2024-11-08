from abc import ABC, abstractmethod

class ProcessarPedidos(ABC):
    @abstractmethod
    def processar_pedido(self):
        pass

class Cliente(ProcessarPedidos):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def processar_pedido(self):
        print(f"Pedido processado para {self.nome}!")

class ClienteNull(Cliente):
    def __init__(self):
        super().__init__("Cliente desconhecido", None)

    def processar_pedido(self):
        print("Pedido não processado - Cliente inexistente.")

class ClienteFactory:
    def get_operation(self, id):
        if id == 1:
            return Cliente("João", "joão@gmail.com")
        else:
            print('Pedido para cliente não processado.')
            return ClienteNull()   

class Produto(ProcessarPedidos):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def processar_pedido(self):
        print(f"Pedido: {self.nome}, {self.preco} processado!")

class ProdutoNull(Produto):
    def __init__(self):
        super().__init__("Produto não encontrado", None)

    def processar_pedido(self):
        print("Pedido não processado - Produto inexistente.")

class ProdutoFactory:
    def get_operation(self, codigo):
        if codigo == "ABC":
            return Produto("Produto A", 100.0)
        else:
            print('Pedido para produto não processado.')
            return ProdutoNull()

class Endereco(ProcessarPedidos):
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

    def processar_pedido(self):
        print(f"Pedido processado para endereço: {self.rua}, {self.cidade}.")

class EnderecoNull(Endereco):
    def __init__(self):
        super().__init__("Endereço desconhecido", None)

    def processar_pedido(self):
        print("Pedido não processado - Endereço inexistente.")

class EnderecoFactory:
    def get_operation(self, cliente):
        if cliente and cliente.nome == "João":
            return Endereco("Rua Principal", "Cidade Exemplo")
        else:
            print('Pedido para endereço não processado.')
            return EnderecoNull()

if __name__ == "__main__":
    cliente_factory = ClienteFactory()
    produto_factory = ProdutoFactory()
    endereco_factory = EnderecoFactory()

    cliente1 = cliente_factory.get_operation(1)  
    cliente2 = cliente_factory.get_operation(2)  

    produto1 = produto_factory.get_operation('ABC')  
    produto2 = produto_factory.get_operation('CBA')  

    endereco1 = endereco_factory.get_operation(cliente1)  
    endereco2 = endereco_factory.get_operation(cliente2) 

    print()
    print('************************************')
    print()

    cliente1.processar_pedido()
    cliente2.processar_pedido()

    produto1.processar_pedido()
    produto2.processar_pedido()

    endereco1.processar_pedido()
    endereco2.processar_pedido()

