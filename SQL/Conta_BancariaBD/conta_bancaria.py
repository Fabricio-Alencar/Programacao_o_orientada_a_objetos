class ContaBancaria:

    def __init__(self, numero_conta:int, titular:str, saldo:float, limite:float):
        self.numero_conta = numero_conta
        self.__saldo = saldo #se tiver dois _ (underline) a conta esta protegida
        self.titular = titular
        self.__limite = limite
    
    def get_saldo(self)->float:
        return self.__saldo
    def set_saldo(self, saldo:float):
        self.__saldo = saldo
    def get_limite(self)->float:
        return self.__limite
    def set_limite(self, limite:float):
        self.__limite = limite
    def depositar(self,valor:float):
        if valor>0:
            self.__saldo += valor
        else:
            print("Valor inválido!")
    def sacar(self,valor:float):
        if valor>0 and valor<=( self.__saldo+self.__limite ):
            self.__saldo -= valor
        else:
            print("Valor inválido ou Saldo insuficiente!")
    def exibir_info(self):
        print(f"Conta: {self.numero_conta} \
                Titular: {self.titular} \
                Saldo: {self.__saldo} \
                Limite: {self.__limite}")

#conta = ContaBancaria(12345, "Evelyn", 6978, 10000)            
#conta.depositar(121.00)
#conta.sacar(3)
#print(conta.get_saldo())
#conta.exibir_info()