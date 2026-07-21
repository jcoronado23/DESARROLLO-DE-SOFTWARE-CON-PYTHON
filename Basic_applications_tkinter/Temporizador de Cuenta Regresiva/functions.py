import tkinter as tk


def iniciar_cuenta(segundos, etiqueta, ventana):

    try:
        segundos = int(segundos)

        if segundos <= 0:
            etiqueta.config(text="Ingrese un valor mayor que 0")
            return

        cuenta_regresiva(segundos, etiqueta, ventana)

    except ValueError:

        etiqueta.config(text="Ingrese un número válido")


def cuenta_regresiva(tiempo, etiqueta, ventana):

    if tiempo >= 0:

        etiqueta.config(
            text=f"Tiempo restante: {tiempo} segundos"
        )

        ventana.after(
            1000,
            cuenta_regresiva,
            tiempo - 1,
            etiqueta,
            ventana
        )

    else:

        etiqueta.config(
            text="Tiempo terminado"
        )