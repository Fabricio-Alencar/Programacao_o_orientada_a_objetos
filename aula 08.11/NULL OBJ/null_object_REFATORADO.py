from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def enviar_email(self, mensagem):
        print(f"Enviando email para {self.email}: '{mensagem}'")

class ClienteNull(Cliente):
    def __init__(self):
        super().__init__("Cliente desconhecido", None)

    def enviar_email(self, mensagem):
        print(f"Nenhum cliente encontrado")

class ClienteFactory:
    def buscar_cliente(self, id): #implementar busca em banco
        if id == 1:
            return Cliente("João", "joão@gmail.com")
        else:
            return ClienteNull()
        
if __name__ == "__main__":
    factory = ClienteFactory()
    cliente1 = factory.buscar_cliente(1)
    cliente2 = factory.buscar_cliente(2)

    cliente1.enviar_email("Bem-vindo ao sistema!")