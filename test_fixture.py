import pytest

@pytest.fixture
def lista_simples():
    return [1,2,3,4,5,6]

def test(lista_simples):
    assert sum(lista_simples) == 21

def test(lista_simples):
    assert len(lista_simples) == 6

def test(lista_simples):
    assert lista_simples[2] == 3