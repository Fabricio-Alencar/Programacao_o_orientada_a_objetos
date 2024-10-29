from verificacoes import Validacoes 
import bcrypt 
class Pessoa():
    def __init__(self, nome:str, email:str,senha:str,telefone:str,tipo:str,cpf:str):
        self.nome = validar_nome(nome)
        self.email = validar_email(email)
        self.__senha = validar_senha(senha)
        self.telefone = validar_telefone(telefone)
        self.tipo = validar_tipo(tipo)
        self.cpf = validar(cpf) 
    def validar_senha(__senha):
        if len(__senha) < 8:
            print("A senha deve ter pelo menos 8 caracteres.")
            return False  # senha menor q 8 digitos
    
        if not re.search(r'[A-Z]',self.__senha):
            print("A senha deve conter pelo menos uma letra maiúscula.")
            return False # senha não possui letra maiúscula
    
        if not re.search(r'[a-z]', self.__senha):
            print("A senha deve conter pelo menos uma letra minúscula.")
            return False # senha não possui letra minúscula
    
        if not re.search(r'\d', self.__senha):
            print("A senha deve conter pelo menos um número.")
            return False # senha não possui números
        if not re.search(r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/~`-]', self.__senha):
            print("A senha deve conter pelo menos um caractere especial.")
            return 5 # senha não possui caractere especial
        
        print("Senha válida!")
        return True

    def set_senha(self):# lógica para validar a nova senha
        if validar_senha(self.__senha)==True:
            chave_secreta = Fernet.generate_key()
            fernet = Fernet(chave_secreta)
            return fernet.encrypt(self.__senha.encode()).decode()

class Paciente:
    def __init__(self, pessoa:Pessoa, nome:str, email:str,telefone:str,tipo:str, crm:str, especialidade:str):
        super().__init__(id, nome, email,telefone,tipo,cpf)
        self.pessoa = pessoa  
    def Cadastrar_Paciente(self):
        pass 
    def Visualizar_Paciente(self):
        pass
    def Alterar_Paciente(self):
        pass
    def Excluir_Paciente(self):
        pass


class Profissional:
    def __init__(self,pessoa:Pessoa, nome:str, email:str,telefone:str,tipo:str):
        super().__init__(id, nome, email,telefone,tipo,cpf)
        self.pessoa = pessoa
        self.crm = validar_crm(crm)
        self.especialidade = especialidade
    def Cadastrar_Profissional(self):
        pass 
    def Visualizar_Profissional(self):
        pass
    def Alterar_Profissional(self):
        pass
    def Excluir_Profissional(self):
        pass

class Consulta:
    def __init__(self, paciente: Paciente, profissional: Profissional, data:str,Hora:str, observacoes=None):
        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.hora = hora
        self.status = "Agendada"
        self.observacoes = observacoes
    def Agendar_Consulta(self):
        pass
    def Visualizar_Consulta(self):
        pass
    def Alterar_Consulta(self):
        pass
    def Cancelar_Consulta(self):
        pass

class Prontuario:
    def __init__(self, paciente: Paciente, profissional: Profissional, data:str,anotacoes_medicas:str,prescricoes:str):
        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.anotacoes_medicas = anotacoes_medicas
        self.prescricoes=prescricoes
    def Criar_Prontuario(self):
        pass
    def Visualizar_Prontuario(self):
        pass
    def Alterar_Prontuario(self):
        pass
    def Excluir_Prontuario(self):
        pass


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
        self.profissionais[crm] = profissional  # incluir profissional no dicionario
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