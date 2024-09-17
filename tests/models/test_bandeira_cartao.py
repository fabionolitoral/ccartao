from ccartao.models.bandeira_cartao import BandeiraCartao
from pytest import mark

@mark.test_models
def test_criacao_bandeira_cartao():
    bandeira = BandeiraCartao(nome="Visa")
    assert bandeira is not None

@mark.test_models
def test_nome_bandeira_cartao():
    bandeira = BandeiraCartao(nome="Visa")
    assert bandeira.nome == "Visa"

@mark.test_models
def test_alterar_nome_bandeira_cartao():
    bandeira = BandeiraCartao(nome="Visa")
    bandeira.nome = "Mastercard"
    assert bandeira.nome == "Mastercard"

@mark.test_models
def test_alterar_nome_bandeira_cartao_vazio():
    bandeira = BandeiraCartao(nome="Visa")
    bandeira.nome = ""
    assert bandeira.nome == ""

@mark.test_models
def test_criar_bandeira_cartao_visa_com_id_1():
    bandeira = BandeiraCartao(id=1, nome="Visa")
    assert bandeira.id == 1

@mark.test_models
def test_criar_bandeira_cartao_visa_com_id_2():
    bandeira = BandeiraCartao(id=2, nome="Visa")
    assert bandeira.id == 2

@mark.test_models
def test_criar_bandeira_cartao_visa_com_id_0():
    bandeira = BandeiraCartao(id=0, nome="Visa")
    assert bandeira.id == 0

@mark.test_models
def test_criar_bandeira_cartao_visa_com_id_negativo():
    bandeira = BandeiraCartao(id=-1, nome="Visa")
    assert bandeira.id == -1

@mark.test_models
def test_criar_bandeira_cartao_visa_com_id_nulo():
    bandeira = BandeiraCartao(id=None, nome="Visa")
    assert bandeira.id == None