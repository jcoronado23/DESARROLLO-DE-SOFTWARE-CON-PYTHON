

def agregar_nota(lista_notas, nota):
    for i in range(len(lista_notas)):
        if lista_notas[i] is None:
            lista_notas[i] = nota
            return True
    return False


def editar_nota(lista_notas, indice, nueva_nota):
    if 0 <= indice < len(lista_notas):
        lista_notas[indice] = nueva_nota
        return True
    return False

# Calcular promedio de tres notas
def calcular_promedio(lista_notas):
    if None in lista_notas:
        return None

    return sum(lista_notas) / len(lista_notas)


def validar_nota(nota):
    try:
        nota = float(nota)

        if 0 <= nota <= 100:
            return nota

        return None

    except ValueError:
        return None
    
def calcular_promedio(lista_notas):
    if None in lista_notas:
        return None

    return sum(lista_notas) / len(lista_notas)