from abc import ABC, abstractmethod

class Pagamento:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def processar_pagamento(self, valor):
        return self.estrategia.calculo_tarifa(valor)

class EstrategiaCalculoTarifa(ABC):
    @abstractmethod
    def calculo_tarifa(self, valor):
        pass

class TarifaPadraoStrategy(EstrategiaCalculoTarifa):
    def __init__(self, taxa):
        self.taxa = taxa

    def calculo_tarifa(self, valor):
        return valor * self.taxa /100 

class TarifaVipStrategy(EstrategiaCalculoTarifa):
    def __init__(self, taxa):
        self.taxa = taxa

    def calculo_tarifa(self, valor):
        return self.taxa

class TarifaEspecialStrategy(EstrategiaCalculoTarifa):
    def __init__(self, taxa):
        self.taxa = taxa

    def calculo_tarifa(self, valor):
        return valor * self.taxa

if __name__ == "__main__":
    tarifa = TarifaPadraoStrategy(2.0)
    pagamento = Pagamento(tarifa)
    valor = 100000.00
    valor_taxa = pagamento.processar_pagamento(valor)
    print(valor_taxa)