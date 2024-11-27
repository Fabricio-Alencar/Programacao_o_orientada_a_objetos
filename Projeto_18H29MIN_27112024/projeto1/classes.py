#from verificacoes import Validacoes
import re
#from cryptography.fernet import Fernet  # Importa Fernet para criptografia
from DAO_BD import ProntuarioDAO,UsuarioDAO,ConsultasDAO

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
'''
def validar_senha(self,senha):  # Corrigido a referência do método
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

def Visualizar_Usuario(usuario_dao, **filtros): #Redireciona para o DAO
  return usuario_dao.visualizar(**filtros) #Retorna dado(s) de acordo com os parâmetros indicados

def Alterar_Usuario(usuario_dao,identificador, id_valor, atributo, novo_valor):
    if usuario_dao.atualizar_atributo(identificador, id_valor, atributo, novo_valor): #Redireciona para o DAO
       return True #Retorna True se a alteração foi concluida
    return False   #Retorna False se a alteração foi NÃO concluida

def Excluir_Usuario(usuario_dao, identificador, id_valor):
    return usuario_dao.excluir(identificador, id_valor)  # Chama o método de exclusão

class Consulta:
    def __init__(self, paciente:Usuario, profissional:Usuario, data: str, hora: str, observacoes=None):
        self.paciente = paciente
        self.profissional = profissional  # Corrigido para usar a variável correta
        self.data = data
        self.hora = hora
        self.status = "Agendada"
        self.observacoes = observacoes

def Visualizar_Consulta(consultas_dao, **filtros): #Redireciona para o DAO
  return consultas_dao.visualizar(**filtros) #Retorna dado(s) de acordo com os parâmetros indicados

def Alterar_Consulta(consultas_dao,identificador, id_valor, atributo, novo_valor):
    if consultas_dao.atualizar_atributo(identificador, id_valor, atributo, novo_valor): #Redireciona para o DAO
       return True #Retorna True se a alteração foi concluida
    return False   #Retorna False se a alteração foi NÃO concluida

def Cancelar_Consulta(consultas_dao, identificador, id_valor):
    if consultas_dao.atualizar_atributo(identificador, id_valor): #Redireciona para o DAO
       return True #Retorna True se a exclusão foi concluida
    return False   #Retorna False se a exclusão foi NÃO concluida

class Prontuario:
    def __init__(self, paciente: Usuario, profissional: Usuario, data: str, anotacoes_medicas: str, prescricoes: str):
        self.paciente = paciente
        self.profissional = profissional  # Corrigido para usar a variável correta
        self.data = data
        self.anotacoes_medicas = anotacoes_medicas
        self.prescricoes = prescricoes

def Visualizar_Prontuario(prontuario_dao, **filtros):  #Redireciona para o DAO
  return prontuario_dao.visualizar(**filtros)  #Retorna dado(s) de acordo com os parâmetros indicados

def Alterar_Prontuario(prontuario_dao,identificador, id_valor, atributo, novo_valor):
    if prontuario_dao.atualizar_atributo(identificador, id_valor, atributo, novo_valor): #Redireciona para o DAO
       return True #Retorna True se a alteração foi concluida
    return False   #Retorna False se a alteração foi NÃO concluida

def Excluir_Prontuario(prontuario_dao, identificador, id_valor):
    if prontuario_dao.atualizar_atributo(identificador, id_valor): #Redireciona para o DAO
       return True #Retorna True se a exclusão foi concluida
    return False   #Retorna False se a exclusão foi NÃO concluida