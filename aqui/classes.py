from verificacoes import Validacoes 
import bcrypt 
import re
from cryptography.fernet import Fernet  # Importa Fernet para criptografia

class Pessoa():
    def __init__(self, nome: str, email: str, senha: str, telefone: str, tipo_usuario: str):
        self.nome = nome
        self.email = email
        self.__senha = senha
        self.telefone = telefone
        self.tipo_usuario = tipo_usuario 

    def validar_senha(self):  # Corrigido a referência do método
        if len(self.__senha) < 8:
            print("A senha deve ter pelo menos 8 caracteres.")
            return False  # senha menor que 8 dígitos
    
        if not re.search(r'[A-Z]', self.__senha):
            print("A senha deve conter pelo menos uma letra maiúscula.")
            return False  # senha não possui letra maiúscula
    
        if not re.search(r'[a-z]', self.__senha):
            print("A senha deve conter pelo menos uma letra minúscula.")
            return False  # senha não possui letra minúscula
    
        if not re.search(r'\d', self.__senha):
            print("A senha deve conter pelo menos um número.")
            return False  # senha não possui números
        
        if not re.search(r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/~`-]', self.__senha):
            print("A senha deve conter pelo menos um caractere especial.")
            return False  # senha não possui caractere especial
        
        print("Senha válida!")
        return True

    def set_senha(self, nova_senha: str):  # Adicionado parâmetro para nova senha
        self.__senha = nova_senha  # Atualiza a senha
        if self.validar_senha():  # Corrigido a referência do método
            chave_secreta = Fernet.generate_key()
            fernet = Fernet(chave_secreta)
            self.__senha = fernet.encrypt(self.__senha.encode()).decode()
            return True  # Indica sucesso
        return False  # Indica falha

class Paciente(Pessoa):
    def __init__(self, nome: str, email: str, senha: str, telefone: str, tipo_usuario: str):
        super().__init__(nome, email, senha, telefone, tipo_usuario)  # Inicializa corretamente a classe pai

    def to_dict(self):
        return {
            'nome': self.nome,
            'email': self.email,
            'tipo_usuario': self.tipo_usuario,
            'telefone': self.telefone
        }

    def Cadastrar_Paciente(self):
        pass 

def Visualizar_Paciente(self):
    pass

def Alterar_Paciente(self):
    pass

def Excluir_Paciente(self):
    pass

class Profissional(Pessoa):
    def __init__(self, nome: str, email: str, senha: str, telefone: str, tipo_usuario: str, crm: str, especialidade: str):
        super().__init__(nome, email, senha, telefone, tipo_usuario)  # Inicializa corretamente a classe pai
        self.crm = crm  # Assume que crm é passado corretamente
        self.especialidade = especialidade

    def to_dict(self):
        return {
            'nome': self.nome,
            'email': self.email,
            'tipo_usuario': self.tipo_usuario,
            'telefone': self.telefone,
            'especialidade': self.especialidade,
            'crm': self.crm
        }
    def Cadastrar_Profissional(self):
        pass 

def Visualizar_Profissional(self):
        pass

def Alterar_Profissional(self):
        pass

def Excluir_Profissional(self):
        pass

class Consulta:
    def __init__(self, paciente: Paciente, profissional: Profissional, data: str, hora: str, observacoes=None):
        self.paciente = paciente
        self.profissional = profissional  # Corrigido para usar a variável correta
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
    def __init__(self, paciente: Paciente, profissional: Profissional, data: str, anotacoes_medicas: str, prescricoes: str):
        self.paciente = paciente
        self.profissional = profissional  # Corrigido para usar a variável correta
        self.data = data
        self.anotacoes_medicas = anotacoes_medicas
        self.prescricoes = prescricoes