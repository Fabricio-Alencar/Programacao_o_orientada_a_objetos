import pytest
import os
from cadastro_usuario import CadastroUsuario

@pytest.fixture
def usuario_valido():
    return CadastroUsuario("Maria José", "234.234.456-99", "22/07/2004", "Criseida", "(55)8765-9876", "12345678")

@pytest.fixture   
def usuario_invalido():
    return CadastroUsuario("João", "23.234.456-99", "22/07/200", "None", "(5)8765-9876", "1234568")

def test_instanciacao(usuario_valido):
    assert usuario_valido.nome == "Maria José"
    assert usuario_valido.cpf == "234.234.456-99"
    assert usuario_valido.nascimento == "22/07/2004"
    assert usuario_valido.endereco == "Criseida"
    assert usuario_valido.telefone == "(55)8765-9876"
    assert usuario_valido.senha == "12345678"

def test_validar_nome(usuario_valido, usuario_invalido):
    assert usuario_valido.validar_nome() == True
    assert usuario_invalido.validar_nome() == False

def test_validar_cpf(usuario_valido, usuario_invalido):
    assert usuario_valido.validar_cpf() == True
    assert usuario_invalido.validar_cpf() == False

def test_validar_nascimento(usuario_valido, usuario_invalido):
    assert usuario_valido.validar_nascimento() == True
    assert usuario_invalido.validar_nascimento() == False

def test_validar_telefone(usuario_valido, usuario_invalido):
    assert usuario_valido.validar_telefone() == True
    assert usuario_invalido.validar_telefone() == False

def test_validar_senha(usuario_valido, usuario_invalido):
    assert usuario_valido.validar_senha() == True
    assert usuario_invalido.validar_senha() == False

def test_mostrar_info(usuario_valido, usuario_invalido): 
    assert usuario_valido.mostrar_info() == f'Nome: {usuario_valido.nome}\nCPF: {usuario_valido.cpf}\nData de Nascimento: {usuario_valido.nascimento}\nTelefone: {usuario_valido.telefone}\nEndereço: {usuario_valido.endereco}\n'
    assert usuario_invalido.mostrar_info() == False

@pytest.fixture
def setup_teardown_arquivo(usuario_valido):
    nome_arquivo = f"cadastro_{usuario_valido.cpf}.txt"
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
    yield
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)

def test_gravar_info_sucesso(usuario_valido, setup_teardown_arquivo):
    assert usuario_valido.gravar_info() == True
    nome_arquivo = f"cadastro_{usuario_valido.cpf}.txt"
    assert os.path.exists(nome_arquivo) == True
    
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        assert "Nome: Maria José" in conteudo
        assert "CPF: 234.234.456-99" in conteudo
        assert "Data de Nascimento: 22/07/2004" in conteudo
        assert "Telefone: (55)8765-9876" in conteudo
        assert "Endereço: Criseida" in conteudo

def test_gravar_info_falha(usuario_invalido):
    assert usuario_invalido.gravar_info() == False
    nome_arquivo = f"cadastro_{usuario_invalido.cpf}.txt"
    assert not os.path.exists(nome_arquivo)
                            
