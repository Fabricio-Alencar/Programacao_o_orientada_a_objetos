#from verificacoes import Validacoes
import re
#from cryptography.fernet import Fernet  # Importa Fernet para criptografia
from DAO_BD import ProntuarioDAO,UsuarioDAO,ConsultasDAO
from conexao_BD import ConexaoBD

class Usuario():
    def __init__(self,nome: str, email: str, senha: str, telefone: str, tipo_usuario: str, id:int=None, especialidade:str=None, crm:str=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.tipo_usuario = tipo_usuario
        self.especialidade = especialidade
        self.crm = crm

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'tipo_usuario': self.tipo_usuario,
            'telefone': self.telefone,
            'especialidade': self.especialidade,
            'crm': self.crm
        }

    '''def validar_senha(self):  # Corrigido a referência do método
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
        return False  # Indica falha'''

    def Cadastrar_Usuario(self):
        pass

def Visualizar_Usuario(usuario_dao, **filtros):
  return usuario_dao.visualizar(**filtros)

def Alterar_Usuario(self):
        pass

def Excluir_Usuario(self):
        pass

class Consulta:
    def __init__(self, paciente:Usuario, profissional:Usuario, data: str, hora: str, observacoes=None):
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
    def __init__(self, paciente: Usuario, profissional: Usuario, data: str, anotacoes_medicas: str, prescricoes: str):
        self.paciente = paciente
        self.profissional = profissional  # Corrigido para usar a variável correta
        self.data = data
        self.anotacoes_medicas = anotacoes_medicas
        self.prescricoes = prescricoes
    def Criar_Prontuario(self):
        pass

def Visualizar_Prontuario(self):
        pass

def Alterar_Prontuario(self):
    pass

def Excluir_Prontuario(self):
    pass