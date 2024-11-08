from abc import ABC, abstractmethod
class Pagamento:
    def __init__(self,estrategia):
        self.estrategia=estrategia
    def pagamento(self,valor):
        return self.estrategia.processar_pagamento(valor)

class FormaPagamentoStrategy(ABC):
    @abstractmethod
    def processar_pagamento(self,valor):
        pass

class CartaoCreditoStrategy:
    def __init__(self,numero_parcela):
        self.numero_parcela=numero_parcela
    def processar_pagamento(self,valor):
        valor_parcela= (valor/self.numero_parcela)
        return f'Pagamento de {valor_parcela} efetuado no credito com sucesso!\n'
        
class PayPalStrategy:
    def processar_pagamento(self,valor):
        return f"valor via PayPal de {valor} efetuado com sucesso!\n"
class transferenciaBancariaStrategy:
    def __init__(self,agencia:str):
        self.agencia=agencia
        
    def processar_pagamento(self,valor):
        return f"transferencia no valor de {valor} recebida com sucesso!\n"

if __name__=="__main__":
    print("***************")
    parcela=5
    FormaPagamento1=CartaoCreditoStrategy(parcela)
    pagamento1 = Pagamento(FormaPagamento1)
    valor1= 100
    valor_pagamento1=pagamento1.pagamento(valor1)
    print(valor_pagamento1)

    print("***************")

    FormaPagamento2=PayPalStrategy()
    pagamento2=Pagamento(FormaPagamento2)
    valor2= 200
    valorPagamento2=pagamento2.pagamento(valor2)
    print(valorPagamento2)

    print("***************")

    agencia="Santander"
    FormaPagamento3=transferenciaBancariaStrategy(agencia)
    Pagamento3=Pagamento(FormaPagamento3)
    valor3=540
    valorPagamento3=Pagamento3.pagamento(valor3)
    print(valorPagamento3)
    print("***************")
    

