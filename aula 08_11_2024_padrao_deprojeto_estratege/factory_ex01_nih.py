from abc import ABC, abstractmethod
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    def get_cliente(self):
        return f"{self.nome}"
        
class ClienteNull(Cliente):
    def __init__(self):
        super().__init__("cliente desconhecido",None)
    def get_cliente(self):
        return f"Erro:Cliente não encontrado."

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def get_produto(self):
        return f"{self.nome}"
class ProdutoNull(Produto):
    def __init__(self):
        super().__init__("Produto desconhecido",None)
    def get_produto(self):
        return f"Erro: Produto não encontrado."

class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade
    def get_endereco(self):
        return f"{self.rua}, {self.cidade}"

class EnderecoNull(Endereco):
    def __init__(self):
        super().__init__("Rua Desconhecida","Cidade Desconhecida")
    def get_endereço(self):
        return"Erro: Endereço de entrega não encontrado."


class Factory:
    def buscar_cliente(self,id):
        if id == 1:
            return Cliente("João", "joao@example.com")
        else:
            return ClienteNull()
    def buscar_produto(self,codigo):
        if codigo == "ABC":
            return Produto("Produto A", 100.0)
        else:
            return ProdutoNull()
    def buscar_endereco(self,cliente):
        if cliente and cliente.nome == "João":
            return Endereco("Rua Principal", "Cidade Exemplo")
        else:
            return EnderecoNull()

    
def processar_pedido(cliente,produto,endereco):

    print(f"Pedido processado para {cliente.get_cliente()}. Produto: {produto.get_produto()}. Entrega: {endereco.get_endereco()}.")

if __name__=="__main__":
    factory=Factory()
    produto1=factory.buscar_produto("ABC")
    produto2=factory.buscar_produto(1234)
    cliente1=factory.buscar_cliente(1)
    cliente2=factory.buscar_cliente(2)   
    endereco1=factory.buscar_endereco(cliente1)
    endereco2=factory.buscar_endereco(cliente2)

    processar_pedido(cliente1,produto1,endereco1)

    print("******************")
    processar_pedido(cliente2,produto2,endereco2)
