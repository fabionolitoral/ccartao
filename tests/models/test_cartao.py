from ccartao.models.cartao import Cartao
from ccartao.models.bandeira_cartao import BandeiraCartao
from pytest import mark

@mark.test_models
def test_criacao_cartao():
    cartao = Cartao(numero_final="1234")
    assert cartao is not None

@mark.test_models
def test_numero_final_cartao():
    cartao = Cartao(numero_final="1234")
    assert cartao.numero_final == "1234"

@mark.test_models
def test_alterar_numero_final_cartao():
    cartao = Cartao(numero_final="1234")
    cartao.numero_final = "5678"
    assert cartao.numero_final == "5678"

@mark.test_models
def test_alterar_numero_final_cartao_vazio():
    cartao = Cartao(numero_final="1234")
    cartao.numero_final = ""
    assert cartao.numero_final == ""

@mark.test_models
def test_alterar_numero_final_cartao_nulo():
    cartao = Cartao(numero_final="1234")
    cartao.numero_final = None
    assert cartao.numero_final == None

@mark.test_models
def test_criar_cartao_visa_com_id_1():
    bandeira = BandeiraCartao(nome="Visa")
    cartao = Cartao(id=1, numero_final="1234", bandeira=bandeira)
    assert cartao.id == 1

@mark.test_models
def test_criar_cartao_visa_com_id_2():
    bandeira = BandeiraCartao(nome="Visa")
    cartao = Cartao(id=2, numero_final="1234", bandeira=bandeira)
    assert cartao.id == 2

@mark.test_models
def test_criar_cartao_visa_com_id_0():
    bandeira = BandeiraCartao(nome="Visa")
    cartao = Cartao(id=0, numero_final="1234", bandeira=bandeira)
    assert cartao.id == 0

@mark.test_models
def test_criar_cartao_visa_com_id_negativo():
    bandeira = BandeiraCartao(nome="Visa")
    cartao = Cartao(id=-1, numero_final="1234", bandeira=bandeira)
    assert cartao.id == -1

@mark.test_models
def test_criar_cartao_com_bandeira_visa():
    bandeira = BandeiraCartao(nome="Visa")
    cartao = Cartao(numero_final="1234", bandeira=bandeira)
    assert cartao.bandeira.nome == "Visa"

@mark.test_models
def test_criar_cartao_com_bandeira_mastercard():
    bandeira = BandeiraCartao(nome="Mastercard")
    cartao = Cartao(numero_final="1234", bandeira=bandeira)
    assert cartao.bandeira.nome == "Mastercard"

@mark.test_models
def test_criar_cartao_com_bandeira_amex():
    bandeira = BandeiraCartao(nome="Amex")
    cartao = Cartao(numero_final="1234", bandeira=bandeira)
    assert cartao.bandeira.nome == "Amex"

@mark.test_models
def test_criar_cartao_com_bandeira_diners():
    bandeira = BandeiraCartao(nome="Diners")
    cartao = Cartao(numero_final="1234", bandeira=bandeira)
    assert cartao.bandeira.nome == bandeira.nome

@mark.test_models
def test_criar_cartao_com_bandeira_nula():
    cartao = Cartao(numero_final="1234", bandeira=None)
    assert cartao.bandeira == None

@mark.test_models
def test_criar_cartao_com_bandeira_vazia():
    bandeira = BandeiraCartao(nome="")
    cartao = Cartao(numero_final="1234", bandeira=bandeira)
    assert cartao.bandeira.nome == ""


