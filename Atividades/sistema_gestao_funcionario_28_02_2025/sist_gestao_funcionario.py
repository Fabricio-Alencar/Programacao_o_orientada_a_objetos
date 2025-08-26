from abc import ABC,abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, horas_trabalhadas, sexo, cpf, telefone):
        self.nome = nome
        self.sexo = sexo
        self.horas_trabalhadas = horas_trabalhadas
        self.cpf = cpf
        self.telefone = telefone

    @abstractmethod
    def calcular_salario(self):
        


class Funcionario_Administrativo(Funcionario):
    def __init__(self, nome, salario, sexo, cpf, telefone, preco_por_hora):
        super().__init__(nome, salario, sexo, cpf, telefone)

def calcular_salario(self):
    return self.horas_trabalhadas * 14,76


class Professor(Funcionario):
    def __init__(self, nome, salario, sexo, cpf, telefone):
        super().__init__(nome, salario, sexo, cpf, telefone)

    def calcular_salario(self):
        return self.horas_trabalhadas * 21,95


class Tecnicos(Funcionario):
    def __init__(self, nome, salario, sexo, cpf, telefone, especializacao):
        super().__init__(nome, salario, sexo, cpf, telefone)
        self.especializacao = especializacao

    def calcular_salario(self):
        return self.horas_trabalhadas * 5,00