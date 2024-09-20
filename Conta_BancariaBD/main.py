from conexoes_bd import conexaoBD
from conta_bancaria import ContaBancaria
from dao_conta import ContaBancariaDAO

if __name__=='__main__':
    conexao = conexaoBD() #cria a conexão
    conexao.criar_tabela() #cria a tabela contas

    conta1 = ContaBancaria(122223, "Nami", 10000, 20000) #cria a conta1
    conta2 = ContaBancaria(122224, "Sivir", 60000, 40000) #conta a conta2

    conta1.exibir_info() #exibe informações da conta1

    conta1.depositar(300) #deposita 300 na conta 1
    conta1.sacar(40) #saca 700 da conta1

    conta1.exibir_info() #exibe informações atualizadas

    conta_dao = ContaBancariaDAO(conexao) #cria objeto
    conta_dao.salvar_conta(conta1)
    conta_dao.salvar_conta(conta2)
