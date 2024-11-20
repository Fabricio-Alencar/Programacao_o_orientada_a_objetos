import sqlite3
from abc import ABC, abstractmethod

# Classe base para os DAOs
class BaseDAO(ABC):
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    @abstractmethod
    def tabela(self):
        pass

# Classe genérica para operações CRUD
class GenericDAO(BaseDAO):
    def cadastrar(self, **kwargs):
        try:
            colunas = ', '.join(kwargs.keys())
            valores = ', '.join(['?' for _ in kwargs.values()])
            mensagem = f"INSERT INTO {self.tabela()} ({colunas}) VALUES ({valores})"
            self.cursor.execute(mensagem, tuple(kwargs.values()))
            self.conn.commit()
            print(f"Registro cadastrado com sucesso na tabela {self.tabela()}!")
        except sqlite3.Error as e:
            self.conn.rollback()
            print(f"Erro ao cadastrar na tabela {self.tabela()}: {e}")
            return False

    def excluir(self, identificador, valor):
        try:
            mensagem = f"DELETE FROM {self.tabela()} WHERE {identificador} = ?"
            self.cursor.execute(mensagem, (valor,))
            if self.cursor.rowcount == 0:
                print(f"Nenhum registro encontrado com {identificador} = {valor}.")
                return False
            else:
                self.conn.commit()
                print(f"Registro excluído com sucesso da tabela {self.tabela()}!")
                return True
        except sqlite3.Error as e:
            self.conn.rollback()
            print(f"Erro ao excluir da tabela {self.tabela()}: {e}")
            return False

    def atualizar_atributo(self, identificador, id_valor, atributo, novo_valor):
        try:
            mensagem = f"UPDATE {self.tabela()} SET {atributo} = ? WHERE {identificador} = ?"
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

    def visualizar(self, **filtros):
        try:
            if filtros:
                condicoes = ' AND '.join([f"{coluna} = ?" for coluna in filtros.keys()])
                query = f"SELECT * FROM {self.tabela()} WHERE {condicoes}"
                self.cursor.execute(query, tuple(filtros.values()))
            else:
                query = f"SELECT * FROM {self.tabela()}"
                self.cursor.execute(query)

            registros = self.cursor.fetchall()
            colunas = [coluna[0] for coluna in self.cursor.description]

            dicionarios_registros = [
                {coluna: valor for coluna, valor in zip(colunas, registro)}
                for registro in registros
            ]

            return dicionarios_registros
        except Exception as e:
            print(f"Erro ao visualizar: {e}")
            return []

# Classes específicas para cada entidade
class UsuarioDAO(GenericDAO):
    def tabela(self):
        return "Usuario"

class ConsultasDAO(GenericDAO):
    def tabela(self):
        return "Consultas"

class ProntuarioDAO(GenericDAO):
    def tabela(self):
        return "Prontuario"

