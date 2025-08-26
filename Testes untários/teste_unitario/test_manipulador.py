import pytest
import os
from manipulador import manipulador
@pytest.fixture
def manip():
    return manipulador()
def test_soma(manip):
    assert manip.soma(10,15)==25
    assert manip.soma(-5,5)==0
    assert manip.soma(-1.5,2.5)==1
def test_concatena(manip):
    assert manip.concatena("py","thon")=="python"
    assert manip.concatena(1,2)=="12"
    assert manip.concatena("foo",123)=="foo123"
def test_multiplica(manip):
    assert manip.multiplica(3,50)==150

@pytest.mark.parametrize("entrada,saida",[(0,1),(3,6),(5,120)])
def test_fatorial(manip,entrada,saida):
    assert manip.fatorial(entrada)==saida
def test_epar(manip):
    assert manip.ePar(2)==True
    assert manip.ePar(25)==None
    assert manip.ePar(10)==True
@pytest.fixture
def test_setup_teardown_arquivo():
    if os.path.exists('teste.txt'):
        os.remove('teste.txt')
    yield

    if os.path.exists('teste.txt'):
        os.remove('teste.txt')

def test_criar_arquivo(manip,test_setup_teardown_arquivo):
    assert manip.criar_arquivo('teste.txt','Hello World!')
def test_ler_arquivo(manip,test_setup_teardown_arquivo):
    assert manip.criar_arquivo('teste.txt','Hello World!')
    assert manip.ler_arquivo("teste.txt")=="Hello World!"