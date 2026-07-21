from tkinter import messagebox


def agregar_nota(lista_notas, nota):
    """
    Agrega una nota a la lista.
    """
    try:
        nota = float(nota)

        if nota < 0 or nota > 100:
            messagebox.showerror(
                "Error",
                "La nota debe estar entre 0 y 100."
            )
            return False

        lista_notas.append(nota)
        return True

    except ValueError:
        messagebox.showerror(
            "Error",
            "Ingrese una nota válida."
        )
        return False


def calcular_promedio(lista_notas):
    """
    Calcula el promedio de las notas.
    """
    if len(lista_notas) == 0:
        messagebox.showwarning(
            "Advertencia",
            "No hay notas registradas."
        )
        return ""

    promedio = sum(lista_notas) / len(lista_notas)
    return f"{promedio:.2f}"


def reiniciar(lista_notas):
    """
    Elimina todas las notas registradas.
    """
    lista_notas.clear()