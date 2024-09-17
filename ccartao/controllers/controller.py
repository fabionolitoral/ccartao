# Controller (MVC) example
class Controller:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Controller: {self.name}'