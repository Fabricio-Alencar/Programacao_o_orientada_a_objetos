import uuid

class Pessoa:
    def __init__(self,nome,cpf,email):
        self.nome=nome
        self.cpf=cpf
        self.email=email

class Cliente:
    """ Representa um cliente do e-commerce, associado a uma pessoa. atributos: pessoa, id_cliente"""
    # construtor da classe utilize a função uuid.uuid4() para gerar um identificador único 
    def __init__(self,pessoa:Pessoa):
        self.pessoa=pessoa
        self.id_cliente = str(uuid.uuid4())

class Produto:
    """ Representa um produto disponível para venda. atributos: nome, preco, estoque"""
    def __init__(self,nome,preco,estoque):
        self.nome=nome
        self.preco=preco
        self.estoque=estoque

class ItemPedido:
    """ Representa um item dentro de um pedido. Contém um produto e uma quantidade. atributos: produto, quantidade"""
    # construtor da classe
    def __init__(self,produto:Produto,quantidade):
        self.produto=produto
        self.quantidade=quantidade

    def calcular_total(self):
        total=0
        for i in range(len(self.itens)):
            total+= self.itens[i].produto.preco*self.itens[i].quantidade
        return total

class Pedido:
    """ Representa um pedido realizado por um cliente. Contém o cliente e uma lista de itens. atrubutos: cliente, itens"""
    # construtor da classe
    def __init__(self, cliente:Cliente):
        self.cliente=cliente
        self.itens=[]

    # método adicionar_item recebe produto e quantidade
    def adicionar_item(self, item):
        if item.produto.estoque >= item.quantidade:
            self.itens.append(item)
            item.produto.estoque -= item.quantidade  # Diminui o estoque do produto
        else:
            print(f'O produto: {item.produto.nome} está sem estoque suficiente')
    # método calcular_total retorna a soma dos totais dos itens
    def calcular_total(self):
        total=0
        for i in range(len(self.itens)):
            total+= self.itens[i].produto.preco*self.itens[i].quantidade
        return total


class Menu:
    """ Gerencia o e-commerce, permitindo o cadastro de clientes, produtos e pedidos. atributos: clientes, produtos, pedidos"""
    # construtor da classe
    def __init__(self):
        self.clientes ={}
        self.produtos={}
        self.pedidos=[]
    # método cadastrar_cliente recebe nome, cpf, 
    def cadastrar_cliente(self, nome, cpf, email):
        if cpf not in self.clientes:
            pessoa = Pessoa(nome, cpf, email)  # Cria uma instância de Pessoa
            cliente = Cliente(pessoa)  # Passa a instância de Pessoa para Cliente
            self.clientes[cpf] = cliente
            print(f'Cliente {nome} cadastrado com sucesso!')
        else:
            print('O CPF informado já está vinculado a um cadastro')
    # método cadastrar_produto recebe nome, preco, estoque
    def cadastrar_produto(self, nome, preco, estoque):
        if nome not in self.produtos:  
            preco = float(preco)  # Converte para float
            estoque = int(estoque)  # Converte para int
            produto = Produto(nome, preco, estoque)
            self.produtos[nome] = produto 
            print(f'Produto {nome} cadastrado com sucesso')
        else:
            print('Este produto já foi cadastrado')
    # método criar_pedido recebe cpf do cliente
    def criar_pedido(self, cpf):
        if cpf in self.clientes:
            pedido = Pedido(self.clientes[cpf]) #aqui ele vai no dic e pega o cliente que possui esse cpf
            print('pedido realizado com sucesso!')
            return pedido
        else:
            print("Cliente não encontrado.")
            return None
    # método listar_pedidos retorna os pedidos
    def visualizar_pedidos(self):
        if not self.pedidos:
            print("Nenhum pedido encontrado.")
            return
        for pedido in self.pedidos:
            print(f"\nPedido do cliente {pedido.cliente.pessoa.nome}:")
            for item in pedido.itens:
                print(f" - {item.produto.nome}: {item.quantidade} unidades (Estoque atual: {item.produto.estoque})")
            print(f"Total: R${pedido.calcular_total():.2f}")
    # método exibir_menu exibe o menu e executa as opções escolhidas
    def exibir_menu(self):
        while True:
            print("\n" + "═" * 40)
            print("🌟  BEM-VINDO AO MENU DO E-COMMERCE  🌟")
            print("═" * 40 + "\n")
            print("📋  1. Cadastrar Cliente")
            print("🛒  2. Cadastrar Produto")
            print("📦  3. Criar Pedido")
            print("📜  4. Visualizar Pedidos")
            print("🚪  5. Sair")
            print("═" * 40 + "\n")
    
            escolha = input("Escolha uma opção (1-5): ")

            if escolha== "1":
                nome= input('Insira o nome do cliente: ')
                cpf= input('Insira o cpf do cliente: ')
                email= input('Insira o email do cliente: ')
                self.cadastrar_cliente(nome,cpf,email)
            elif escolha == "2":
                nome=input('insira o nome do produto: ')
                preco=input('insira o preço do produto (em reais): ')
                estoque=input('insira a quantidadde de estoque do produto: ')
                self.cadastrar_produto(nome,preco,estoque)
            elif escolha == "3":
                cpf = input('Digite o CPF do cliente: ')
                cliente_encontrado = None 
                for cliente in self.clientes.values():
                    if cliente.pessoa.cpf == cpf:
                        cliente_encontrado = cliente  # Armazena o cliente encontrado
                        break
                if cliente_encontrado:
                    pedido = Pedido(cliente_encontrado)  # Cria o pedido com o cliente encontrado
                    while True:
                        produto_nome = input('Digite o nome do produto ou (sair) para finalizar o pedido: ')
                        if produto_nome in self.produtos:
                            quantidade = int(input("Digite a quantidade: "))
                            pedido.adicionar_item(ItemPedido(self.produtos[produto_nome], quantidade))
                        elif produto_nome.lower() == 'sair':
                            break
                        else:
                            print('Desculpe, produto não encontrado!')
                    self.pedidos.append(pedido)  # Adiciona o pedido à lista de pedidos
                else: 
                    print("O CPF solicitado não está cadastrado!")
            elif escolha == "4":
                self.visualizar_pedidos()
            elif escolha == '5':
                print('saindo do sistema...')
                break
            else:
                print('Opção invalida. Porfavor, escolha um número entre 1 e 5')








if __name__ == "__main__":
    menu = Menu()
    menu.exibir_menu()

