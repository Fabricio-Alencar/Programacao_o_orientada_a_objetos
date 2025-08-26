import sqlite3

class conexaoBD:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("banco.db")
            self.cursor = self.conn.cursor()
            print("Conexão estabelecida com sucesso!")
        except sqlite3.Error as e:
            print("Erro ao conectar o Banco de Dados.") 

    def criar_tabela(self):
        if self.conn:
            try:
                self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS contas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero_conta INTEGER NOT NULL,
                titular TEXT NOT NULL,
                saldo REAL NOT NULL,
                limite REAL NOT NULL)''')
                self.conn.commit()
                print("Tabela criada com sucesso!")
            except sqlite3.Error as e:
                print("Erro ao criar tabela!")
        else:
            print("Não há conexão com o Banco de Dados.")

    def  fechar_conexao(self):
        if self.conn:
            try:
                self.conn.close()
                print("Conexao encerrrada com o Banco de Dados.")
            except sqlite3.Error as e:
                print("Não foi possivel fechar a conexão!")

#conexao = conexaoBD()
#conexao.criar_tabela()
#conexao.fechar_conexao()