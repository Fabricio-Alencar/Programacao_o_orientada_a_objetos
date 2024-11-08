from abc import ABC, abstractmethod
class Pagamento:
    def __init__(self,estrategia):
        self.estrategia=estrategia
    def processar_pagamento(self,valor):
        return self.estrategia.Calculo_tarifa(valor) #vc vai sempre chamar a pagamento
#a estratégia que voce quer vai ser chamada nesse return
class EstrategiaCalculoTarifa(ABC):
    @abstractmethod
    def Calculo_tarifa(self,valor):
        pass

class TarifaPadraoStrategy(EstrategiaCalculoTarifa):
    def __init__(self,taxa):
        self.taxa= taxa
    def Calculo_tarifa(self,valor):
        return valor*self.taxa/100 #a divisao por 100 é para o cliente digitar sem precisar 0.1 ou 0.2

class TarifaVipStrategy(EstrategiaCalculoTarifa):
    def __init__(self,taxa):
        self.taxa= taxa 
    def Calculo_tarifa(self,valor):
        return valor

class TarifaEspecialStrategy(EstrategiaCalculoTarifa):
    def __init__(self,taxa):
        self.taxa= taxa
    def Calculo_tarifa(self,valor):
        return valor*self.taxa

if __name__=="__main__":
    tarifa = TarifaPadraoStrategy(2.0)
    pagamento = Pagamento(tarifa)
    valor=100000.00
    valor_taxa=pagamento.processar_pagamento(valor)
    print(valor_taxa)