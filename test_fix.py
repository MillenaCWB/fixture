import pytest

@pytest.fixture
def lista_complexa():
    return [2,4,6,8,10]
    return sum(x * 2 for x in lista_complexa)

def test(lista_complexa):
    assert sum(lista_complexa) == 30

def test(lista_complexa):
    assert len(lista_complexa) == 5


def test(lista_complexa):
    assert lista_complexa[2] == 6