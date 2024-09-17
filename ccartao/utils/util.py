from datetime import datetime

# Funções utilitárias
class Util:
    @staticmethod
    def get_date():
        return datetime.now().strftime('%Y-%m-%d')