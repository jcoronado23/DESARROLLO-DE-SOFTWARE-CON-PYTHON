import re

class FormatoCedulaError(Exception):
    """Se lanza cuando el valor no tiene el formato de X-XXXX-XXXX"""
    pass

def validar_cedula(cedula):

    formato = r'^\d-\d{4}-\d{4}'

    if not re.fullmatch(formato, cedula):
        raise FormatoCedulaError("El codigo debe tener el formato X-XXXX-XXXX. Ejemplo 4-0111-0222")

    return True
