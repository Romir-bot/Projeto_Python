import sys
sys.path.append(" . ")

from src.models import pessoa

def test_concatenacao_nome_sobrenome():
    p1 = pessoa.Pessoa('Caio','Sobrenome', 22,'4353637738')
    assert p1.nome_completo() == 'Caio Sampaio'