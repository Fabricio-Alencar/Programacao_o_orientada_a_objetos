from abc import ABC, abstractmethod

class Pagamento:
    def __init__(self, forma_pagamento):
        self.forma_pagamento = forma_pagamento

    def efetuar_pagamento(self, valor):
        return self.forma_pagamento.processar_pagamento(valor)

class FormaDePagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

class CartaoCreditoStrategy(FormaDePagamento):
    def __init__(self, numero_parcelas, juros):
        self.numero_parcelas = numero_parcelas
        self.juros = juros

    def processar_pagamento(self, valor):
        juros_totais = valor * self.juros / 100 * self.numero_parcelas  
        total = valor + juros_totais  
        return f'Seu pedido será pago em {self.numero_parcelas} vezes, {self.juros}% de juros por parcela, com cartão de crédito.\n TOTAL: {total}\n'


class PayPalStrategy(FormaDePagamento):
    def __init__(self, taxa):
        self.taxa = taxa

    def processar_pagamento(self, valor):
        valor_taxa = valor * self.taxa /100 
        total = valor + valor_taxa
        return f'Seu pedido foi pago com Pay Pal com {self.taxa}% de taxa do banco.\n TOTAL: {total}\n'


class TransferenciaBancariaStrategy(FormaDePagamento):
    def __init__(self, taxa):
        self.taxa = taxa

    def processar_pagamento(self, valor):
        valor_taxa = valor * self.taxa /100 
        total = valor + valor_taxa

        return f'Seu pedido foi pago por Tranferência Bancáriacom com {self.taxa}% de taxa do banco.\n TOTAL: {total}\n'

if __name__ == "__main__":
    forma_pag1 = CartaoCreditoStrategy(10, 5)
    forma_pag2 = PayPalStrategy(10)
    forma_pag3 = TransferenciaBancariaStrategy(10)

    valor = 100000.00

    pagamento1 = Pagamento(forma_pag1)
    pagamento2 = Pagamento(forma_pag2)
    pagamento3 = Pagamento(forma_pag3)

    mensagem1 = pagamento1.efetuar_pagamento(valor)
    mensagem2 = pagamento2.efetuar_pagamento(valor)
    mensagem3 = pagamento3.efetuar_pagamento(valor)

    print(mensagem1)
    print(mensagem2)
    print(mensagem3)