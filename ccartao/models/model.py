class Model:
    def __init__(self, id:int=0):
        self._id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def __str__(self):
        return f'Model: {self.id}'