import sqlite3

#Checar esse valores UNIQUE pq estão dando xabu

class ConexaoBD:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("banco2.db")
            self.cursor = self.conn.cursor()
            print("Conexão estabelecida com sucesso!")
        except sqlite3.Error as e:
            print("Erro ao conectar ao Banco de Dados.", e)

    def criar_tabela(self):
        if self.conn:
            try:
                # Criar tabela Paciente
                self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Paciente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    senha TEXT UNIQUE NOT NULL,
                    telefone TEXT NOT NULL,
                    tipo_usuario TEXT NOT NULL
                )''')

                # Criar tabela Profissional
                self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Profissional (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    senha TEXT UNIQUE NOT NULL,
                    telefone TEXT NOT NULL,
                    tipo_usuario TEXT NOT NULL,
                    especialidade TEXT NOT NULL,
                    crm TEXT UNIQUE NOT NULL
                )''')

                #Cria tabela Consultas
                self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Consultas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data DATE NOT NULL,
                    hora TIME NOT NULL,
                    status TEXT NOT NULL,
                    observacoes TEXT,
                    id_paciente_FK INTEGER,
                    id_profissional_FK INTEGER,
                    FOREIGN KEY (id_profissional_FK) REFERENCES Profissional(id),
                    FOREIGN KEY (id_paciente_FK) REFERENCES Paciente(id)
                )''')

                #Cria tabela Prontuario
                self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Prontuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data DATE NOT NULL,
                    anotacoes_medicas TEXT NOT NULL,
                    prescricoes TEXT,
                    id_paciente_FK INTEGER,
                    id_profissional_FK INTEGER,
                    id_consulta_FK INTEGER,
                    FOREIGN KEY (id_profissional_FK) REFERENCES Profissional(id),
                    FOREIGN KEY (id_consulta_FK) REFERENCES Consultas(id),
                    FOREIGN KEY (id_paciente_FK) REFERENCES Paciente(id)
                )''')


                self.conn.commit()
                print("Tabelas criadas com sucesso!")
            except sqlite3.Error as e:
                print("Erro ao criar tabelas!", e)
        else:
            print("Não há conexão com o Banco de Dados.")

    def fechar_conexao(self):
        if self.conn:
            try:
                self.conn.close()
                print("Conexão encerrada com o Banco de Dados.")
            except sqlite3.Error as e:
                print("Não foi possível fechar a conexão!", e)
