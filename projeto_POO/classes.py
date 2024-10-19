
class Pessoa():
    def __init__(self, nome:str, email:str,senha:str,telefone:str,tipo:str,cpf:str):
        self.nome = nome
        self.email = email
        self.__senha = senha
        self.telefone = telefone
        self.tipo = tipo
        self.cpf = cpf     

class Paciente:
    def __init__(self, pessoa:Pessoa, nome:str, email:str,senha:str,telefone:str,tipo:str, crm:str, especialidade:str):
        super().__init__(id, nome, email,senha,telefone,tipo,cpf)
        self.pessoa = pessoa   

class Profissional:
    def __init__(self,pessoa:Pessoa, nome:str, email:str,senha:str,telefone:str,tipo:str):
        super().__init__(id, nome, email,senha,telefone,tipo,cpf)
        self.pessoa = pessoa
        self.crm = crm
        self.especialidade = especialidade

class Consulta:
    def __init__(self, paciente: Paciente, profissional: Profissional, data:str,Hora:str, observacoes=None):
        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.hora = hora
        self.status = "Agendada"
        self.observacoes = observacoes

class Prontuario:
    def __init__(self, paciente: Paciente, profissional: Profissional, data:str,anotacoes_medicas:str,prescricoes:str):
        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.anotacoes_medicas = anotacoes_medicas
        self.prescricoes=prescricoes


class Menu:
    def __init__(self):
        self.Profissionais = {}  # dicionário médicos chave crm valor objeto medico
        self.pacientes = {}  # dicionário paciente chave cpf objeto paciente
        self.consultas = []  # lista de consulta
        self.prontuario = [] # lista de prontuario

    def incluir_profissional(self):
        nome = input("Nome: ")
        cpf = int(input("CPF: "))
        crm = int(input("CRM: "))
        especialidade = input("Especialidade: ")
        pessoa = Pessoa(nome, email,senha,telefone,tipo,cpf)  # instanciar pessoa 
        profissional = Profissional(pessoa, crm, especialidade)  # instanciar Profissional
        self.profissional[crm] = profissional  # incluir profissional no dicionario
        return "Profissional cadastrado com sucesso!"

    def incluir_paciente(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        pessoa = Pessoa(nome, email,senha,telefone,tipo,cpf)  # instanciar pessoa 
        paciente = Paciente(pessoa)  # instanciar paciente
        self.pacientes[cpf] = paciente  # incluir paciente no dicionário
        return "Paciente cadastrado com sucesso!"
        
    def agendar_consulta(self):
        cpf_paciente = input("Qual paciente você deseja cadastrar [digite o CPF]?: ")
        crm_medico = input("Qual médico você deseja cadastrar [digite o CRM]?: ")
        data = input("Data da consulta: ")
        hora = input("Hora da consulta: ")
        observacoes = input("Observações: ")
        
        if cpf_paciente in self.pacientes:
            paciente = self.pacientes[cpf_paciente]
        else: 
            return "Paciente não encontrado"
        
        if crm_medico in self.Profissional:
            medico = self.Profissional[crm_medico]
        else: 
            return "Médico não encontrado"
        
        consulta = Consulta(paciente, medico, data, hora, observacoes)
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
                f"Médico: {consulta.profissional.pessoa.nome}\n"
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
                print(self.incluir_profissional())
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