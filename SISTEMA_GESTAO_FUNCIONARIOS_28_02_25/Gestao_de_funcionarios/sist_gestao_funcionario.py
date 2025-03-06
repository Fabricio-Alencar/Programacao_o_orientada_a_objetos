from abc import ABC,abstractmethod

ADM_Cadastro = []
Professor_Cadastro = []
Tecnico_Cadastro = []

class Funcionario(ABC):
    def __init__(self, nome, horario, telefone, tipo):
        self.nome = nome
        self.horario = horario
        self.telefone = telefone
        self.tipo = tipo

    @abstractmethod
    def calcular_salario(self):
        pass

class Funcionario_Administrativo(Funcionario):
    def __init__(self, nome, horario, telefone, tipo, setor, nivel):
        super().__init__(nome, horario, telefone, tipo)
        self.setor = setor
        self.nivel = nivel

    def calcular_salario(self):
        salario_base = 3000  
        nivel =  {
            "Básico": 500,
            "Intermediário": 1000,
            "Avançado": 2000
        }
        bonus_setor = {
            "Financeiro": 1000,
            "Recursos Humanos": 800,
            "TI": 1200,
            "Marketing": 900
        }
        bonus = bonus_setor.get(self.setor)  # Valor padrão se o setor não estiver listado
        importancia = nivel.get(self.nivel)
        salario_total = salario_base + importancia + bonus
        return salario_total

class Professor(Funcionario):
    def __init__(self, nome, horario, telefone, tipo, carga, preco_por_hora):
        super().__init__(nome, horario, telefone, tipo)
        self.carga = carga
        self.preco_por_hora = preco_por_hora

    def calcular_salario(self):
        return self.carga * self.preco_por_hora * 4  # Considerando 4 semanas no mês

class Tecnico(Funcionario):
    def __init__(self, nome, horario, telefone, tipo, especializacao):
        super().__init__(nome, horario, telefone, tipo)
        self.especializacao = especializacao

    def calcular_salario(self):
        salario_base = 2000  # Salário base para um técnico genérico
        especialidade =  {
            "Informática": 500,
            "Mecânica": 500,
            "Automação Industrial": 900,
            "Farmácia": 400,
            "Enfermagem": 600,
            "Química": 700
        }
        importancia = especialidade.get(self.especializacao)
        salario_total = salario_base + importancia 
        return salario_total