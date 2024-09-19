class ModelError(Exception):
    """Exceção base para erros relacionados aos modelos."""
    pass

class ModelNotFoundError(ModelError):
    """Exceção levantada quando um modelo não é encontrado."""
    pass

class ValidationError(ModelError):
    """Exceção levantada em casos de erro de validação."""
    pass