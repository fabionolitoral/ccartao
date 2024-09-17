from ccartao.models.model import Model

class BandeiraCartao(Model):
    def __init__(self, id:int=0, nome=""):
        self._id = id
        self._nome = nome

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value