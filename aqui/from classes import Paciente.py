from classes import Paciente
from classes import Profissional
from classes import Consulta
from classes import Prontuario
from DAO_BD import PacienteDAO
from DAO_BD import ProfissionalDAO
from DAO_BD import ConsultasDAO
from DAO_BD import ProntuarioDAO
from conexao_BD import ConexaoBD
from conta_bancaria import ContaBancaria
from dao_conta import ContaBancariaDAO

if __name__=='__main__':
    conexao = conexaoBD() #cria a conexão
    conexao.criar_tabela() #cria a tabela contas
    conexao = ConexaoBD()
    conexao.criar_tabela()

    profissinal_dao = ProfissionalDAO(conexao.conn)
    paciente_dao = PacienteDAO(conexao.conn)
    consulta_dao = ConsultasDAO(conexao.conn)
    prontuario_dao = ProntuarioDAO(conexao.conn)

    profissional_dao.cadastrar(
        nome="Dr. João",
        email="joao@clinica.com",
        senha="1234",
        telefone="99999-8888",
        tipo_usuario="profissional",
        especialidade="Cardiologia",
        crm="12345"
    )
    paciente_dao.cadastrar(
        nome="João",
        email="joaopaciente@email.com",
        senha="1245",
        telefone="123456789",
        tipo_usuario="paciente"
    )

    prof_dao.excluir("crm", "12345")
    paciente_dao.atualizar_atributo("id", 1, "telefone", "987654321")