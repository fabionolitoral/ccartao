# Business logic, data manipulation with API, etc. goes here
class Service:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Service: {self.name}'