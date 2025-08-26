class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Paciente:
    def __init__(self, pessoa: Pessoa):
        self.pessoa = pessoa   

class Medico:
    def __init__(self, pessoa: Pessoa, crm, especialidade):
        self.pessoa = pessoa
        self.crm = crm
        self.especialidade = especialidade

class Consulta:
    def __init__(self, paciente: Paciente, medico: Medico, data_hora, observacoes=None):
        self.paciente = paciente
        self.medico = medico
        self.data_hora = data_hora
        self.observacoes = observacoes

class Menu:
    def __init__(self):
        self.medicos = {}  # dicionário médicos chave crm valor objeto medico
        self.pacientes = {}  # dicionário paciente chave cpf objeto paciente
        self.consultas = []  # lista de consulta

    def incluir_medico(self):
        nome = input("Nome: ")
        cpf = int(input("CPF: "))
        nascimento = input("Data Nascimento: ")
        crm = int(input("CRM: "))
        especialidade = input("Especialidade: ")
        pessoa = Pessoa(nome, cpf, nascimento)  # instanciar pessoa 
        medico = Medico(pessoa, crm, especialidade)  # instanciar medico
        self.medicos[crm] = medico  # incluir medico no dicionario
        return "Médico cadastrado com sucesso!"

    def incluir_paciente(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        nascimento = input("Data Nascimento: ")
        pessoa = Pessoa(nome, cpf, nascimento)  # instanciar pessoa 
        paciente = Paciente(pessoa)  # instanciar paciente
        self.pacientes[cpf] = paciente  # incluir paciente no dicionário
        return "Paciente cadastrado com sucesso!"
        
    def agendar_consulta(self):
        cpf_paciente = input("Qual paciente você deseja cadastrar [digite o CPF]?: ")
        crm_medico = input("Qual médico você deseja cadastrar [digite o CRM]?: ")
        data_hora = input("Data e hora da consulta: ")
        observacoes = input("Observações: ")
        
        if cpf_paciente in self.pacientes:
            paciente = self.pacientes[cpf_paciente]
        else: 
            return "Paciente não encontrado"
        
        if crm_medico in self.medicos:
            medico = self.medicos[crm_medico]
        else: 
            return "Médico não encontrado"
        
        consulta = Consulta(paciente, medico, data_hora, observacoes)
        self.consultas.append(consulta)  # Adiciona à lista de consultas
        return "Consulta cadastrada com sucesso!"

    def ver_agenda(self):
        if len(self.consultas) == 0:
            return "Não há consultas!"
        agenda = []
        for consulta in self.consultas:
            agenda.append(
                f"Consulta: {consulta.data_hora}\n"
                f"Paciente: {consulta.paciente.pessoa.nome}\n"
                f"Médico: {consulta.medico.pessoa.nome}\n"
                f"Observações: {consulta.observacoes}\n"
            )
        return "\n".join(agenda)

    def exibir_menu(self):
        while True:
            print("|             MENU              |")
            print("|INDICE|        FUNÇÃO          |")
            print("|   1  |     Incluir Médico     |")
            print("|   2  |    Incluir Paciente    |")
            print("|   3  |    Agendar Consulta    |")
            print("|   4  |       Ver Agenda       |")
            print("|   5  |          Sair          |")
            indice = int(input("Digite o índice da função que você deseja realizar: "))
            if indice == 5:
                print("Programa finalizado")
                break  
            elif indice == 1:
                print(self.incluir_medico())
            elif indice == 2:
                print(self.incluir_paciente())
            elif indice == 3:
                print(self.agendar_consulta())
            elif indice == 4:
                print(self.ver_agenda())
            else:
                print("Você digitou um índice inválido!")

if __name__ == '__main__':
    menu = Menu()
    menu.exibir_menu()
