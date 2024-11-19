import sqlite3
from abc import ABC, abstractmethod

#Classe base para os DAOs
class BaseDAO(ABC):
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    @abstractmethod
    def tabela(self):
        pass

#Classe genérica para operações CRUD
class GenericDAO(BaseDAO):
    def cadastrar(self, **kwargs): #Usei um kwargs(dicionario) para o total de atributos de cada tabela se "ajustar" ao total de dados inseridos
        try:
            colunas = ', '.join(kwargs.keys())  # Cria uma string contendo as chaves separadas por vírgulas, ex.: "nome, tipo, especialidade"
            valores = ', '.join(['?' for _ in kwargs.values()])  # Cria uma string com o mesmo número de "?" que o número de atributos, separando-os por vírgulas, ex.: "?, ?, ?"
            mensagem = f"INSERT INTO {self.tabela()} ({colunas}) VALUES ({valores})"  # Monta a mensagem de inserção
            self.cursor.execute(mensagem, tuple(kwargs.values()))  # Executa a inserção. tuple --> pega os valores e coloca em uma ""lista"""
            self.conn.commit()  # Confirma a inserção
            print(f"Registro cadastrado com sucesso na tabela {self.tabela()}!")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar na tabela {self.tabela()}: {e}")
            return False

    def excluir(self, identificador, valor): #Manda o indentificador (id,crm..), e o valor deste identificador (1(id), 24563434(crm), ...)
        try:
            mensagem = f"DELETE FROM {self.tabela()} WHERE {identificador} = ?" #Monta a mensagem de exclusão
            self.cursor.execute(mensagem, (valor,)) #Executa a exclusão
            if self.cursor.rowcount == 0: #Nenhuma modificção foi feita
                print(f"Nenhum registro encontrado com {identificador} = {valor}.")
                return False
            else:
                self.conn.commit() # Confirma a exclusão
                print(f"Registro excluído com sucesso da tabela {self.tabela()}!")
                return True
        except sqlite3.Error as e:
            print(f"Erro ao excluir da tabela {self.tabela()}: {e}")
            return False

    def atualizar_atributo(self, identificador, id_valor, atributo, novo_valor):
          # identificador = nome da coluna que será utilizada para localizar o registro (ex: 'id'); ---Usuario
          # id_valor = valor que identifica o registro a ser atualizado (ex: '123'); ---Usuario
          # atributo = nome da coluna que será atualizada (ex: 'nome'); ----Atributo
          # novo_valor = novo valor a ser atribuído ao atributo (ex: 'João').  ----Atributo
        try:
            mensagem = f"UPDATE {self.tabela()} SET {atributo} = ? WHERE {identificador} = ?" # Monta uma mensagem de atualização
            self.cursor.execute(mensagem, (novo_valor, id_valor))
            if self.cursor.rowcount == 0:
                print(f"Nenhum registro encontrado com {identificador} = {id_valor}.")
                return False
            else:
                self.conn.commit()
                print(f"Atributo '{atributo}' atualizado com sucesso na tabela {self.tabela()}!")
                return True
        except sqlite3.Error as e:
            print(f"Erro ao atualizar na tabela {self.tabela()}: {e}")
            return False

    def visualizar(self, **filtros):  #Arrumar o vizualizar
        try:
            if filtros:
                condicoes = ' AND '.join([f"{coluna} = ?" for coluna in filtros.keys()])
                query = f"SELECT * FROM {self.tabela()} WHERE {condicoes}"
                self.cursor.execute(query, tuple(filtros.values()))
            else:
                query = f"SELECT * FROM {self.tabela()}"
                self.cursor.execute(query)
            registros = self.cursor.fetchall()
            return registros
        except sqlite3.Error as e:
            print(f"Erro ao visualizar registros na tabela {self.tabela()}: {e}")
            return []

# Classes específicas para cada entidade
# Todas as classes podem utilizar os métodos sa classe GenericDAO (métodos CRUD)
class PacienteDAO(GenericDAO):
    def tabela(self):
        return "Paciente"

class ProfissionalDAO(GenericDAO):
    def tabela(self):
        return "Profissional"

class ConsultasDAO(GenericDAO):
    def tabela(self):
        return "Consultas"

class ProntuarioDAO(GenericDAO):
    def tabela(self):
        return "Prontuario"
