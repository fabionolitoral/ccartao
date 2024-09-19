from ccartao.models.model import Model
from ccartao.models.bandeira_cartao import BandeiraCartao
from ccartao.models.exceptions import ModelError

class Cartao(Model):

    def __init__(self, id:int=0, bandeira:BandeiraCartao=None, numero_final:int =0, data_vencimento:int=1):
        self._id = id
        self._numero_final = numero_final
        self._bandeira = bandeira
        self._data_vencimento = data_vencimento

    @property
    def data_vencimento(self):
        return self._data_vencimento

    @data_vencimento.setter
    def data_vencimento(self, value:int):
        if value < 1 or value > 31:
            raise ModelError("Data de vencimento deve estar entre 1 e 31.")

        self._data_vencimento = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value:int):
        self._id = value

    @property
    def numero_final(self):
        return self._numero_final

    @numero_final.setter
    def numero_final(self, value:int):
        self._numero_final = value

    @property
    def bandeira(self):
        return self._bandeira

    @bandeira.setter
    def bandeira(self, value:BandeiraCartao):
        self._bandeira = value
