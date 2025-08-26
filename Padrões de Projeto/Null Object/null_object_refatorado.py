from abc import ABC, abstractmethod
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def enviar_email(self, mensagem):
        print(f"Enviando email para {self.email}: {mensagem}")

class ClienteNull(Cliente):
    def __init__(self):
        super().__init__("cliente desconhecido",None)
    def enviar_email(self,mensagem):
        print("nenhum cliente encontrado.")
        
class ClienteFactory:
    def buscar_cliente(slef,id):
        #implementar busca em banco
        if id ==1:
            return Cliente("joão","joao@gmail.com")
        else:
            return ClienteNull()

if __name__=="__main__":
    factory = ClienteFactory()
    cliente1 = factory.buscar_cliente(1)
    print("*************************************")
    cliente2= factory.buscar_cliente(2)
    mensagem="oiiiii"
    cliente1.enviar_email(mensagem)
    print("*************************************")
    cliente2.enviar_email(mensagem)
    print("*************************************")