from ccartao.models.model import Model
from ccartao.models.bandeira_cartao import BandeiraCartao

class Cartao(Model):

    def __init__(self, id:int=0, bandeira:BandeiraCartao=None, numero_final:int =0):
        self._id = id
        self._numero_final = numero_final
        self._bandeira = bandeira

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def numero_final(self):
        return self._numero_final

    @numero_final.setter
    def numero_final(self, value):
        self._numero_final = value

    @property
    def bandeira(self):
        return self._bandeira

    @bandeira.setter
    def bandeira(self, value):
        self._bandeira = value
