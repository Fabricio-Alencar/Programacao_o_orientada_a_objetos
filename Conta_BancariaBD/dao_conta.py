#Padrão de Projeto = DAO data access object
class ContaBancariaDAO:
    def __init__(self,conn):
        self.conn = conn
        self.cursor = self.conn.cursor()
    def salvar_conta(self,conta):
        self.cursor.execute('''INSERT INTO contas 
                    (numero_conta, titular, saldo, limite) VALUES
                    ''',(conta.numero_cont, conta.titular,
                         conta.get_saldo, conta.get_limite))
        self.conn.commit()

    def listar_contas(self):
        self.cursor.execute('''SELECT * FROM users''')
        contas = self.cursor.fetchall()
        return contas