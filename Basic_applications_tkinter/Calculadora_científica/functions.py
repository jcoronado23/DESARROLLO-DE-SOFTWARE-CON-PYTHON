import math


def agregar(operacion, pantalla, texto):
    operacion += str(texto)
    pantalla.set(operacion)
    return operacion


def calcular(operacion, pantalla):
    try:
        resultado = str(eval(operacion, {"math": math}))
        pantalla.set(resultado)
        return resultado
    except Exception:
        pantalla.set("ERROR")
        return ""


def limpiar(pantalla):
    pantalla.set("0")
    return ""