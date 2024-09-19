from ccartao.models.model import Model

class BandeiraCartao(Model):
    def __init__(self, id:int=0, nome=""):
        super().__init__(id)
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value