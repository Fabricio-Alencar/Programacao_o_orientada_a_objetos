import sqlite3

#Cria uma conexão com o banco de dados que possui 4 tabelas: 
# pessoa (tabela generalizadora) Pessoa e Profissional (tabela especializadoras)
# Tabela de consultas e tabela de Prontuario.
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
                CREATE TABLE IF NOT EXISTS Pessoa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                senha TEXT UNIQUE NOT NULL,
                telefone TEXT NOT NULL,
                cpf TEXT NOT NULL,
                tipo TEXT NOT NULL)''')
                self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Paciente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_pessoa_FK INTEGER,
                FOREIGN KEY (id_pessoa_FK) REFERENCES Pessoa(id))''')
                self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Profissional (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                especialidade TEXT NOT NULL,
                crm TEXT UNIQUE NOT NULL,
                id_pessoa_FK INTEGER,
                FOREIGN KEY (id_pessoa_FK) REFERENCES Pessoa(id))''')
                self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Consultas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data DATE NOT NULL,
                hora TIME NOT NULL,
                status Text NOT NULL,
                observacoes TEXT,
                id_paciente_FK INTEGER,
                id_pROFISSIONAL_FK INTEGER,
                FOREIGN KEY (id_profissional_FK) REFERENCES Profissional(id),
                FOREIGN KEY (id_paciente_FK) REFERENCES Paciente(id))''')
                self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Prontuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data DATE NOT NULL,
                anotacoes_medicas Text NOT NULL,
                prescricoes TEXT,
                id_paciente_FK INTEGER,
                id_profissional_FK INTEGER,
                id_consulta_FK,
                FOREIGN KEY (id_profissional_FK) REFERENCES Profissional(id),
                FOREIGN KEY (id_consulta_FK) REFERENCES Consultas(id),
                FOREIGN KEY (id_paciente_FK) REFERENCES Paciente(id))''')
                self.conn.commit()
                print("Tabelas criadas com sucesso!")
            except sqlite3.Error as e:
                print("Erro ao criar tabelas!")
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