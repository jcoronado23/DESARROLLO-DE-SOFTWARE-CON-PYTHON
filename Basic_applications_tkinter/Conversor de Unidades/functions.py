from tkinter import messagebox


def convertir(valor, opcion):
    try:
        valor = float(valor)

        if opcion == "Centímetros → Pulgadas":
            return f"{valor / 2.54:.2f} pulgadas"

        elif opcion == "Pulgadas → Centímetros":
            return f"{valor * 2.54:.2f} cm"

        elif opcion == "Metros → Pies":
            return f"{valor * 3.28084:.2f} pies"

        elif opcion == "Pies → Metros":
            return f"{valor / 3.28084:.2f} m"

        elif opcion == "Celsius → Fahrenheit":
            return f"{(valor * 9/5) + 32:.2f} °F"

        elif opcion == "Fahrenheit → Celsius":
            return f"{(valor - 32) * 5/9:.2f} °C"

    except ValueError:
        messagebox.showerror(
            "Error",
            "Ingrese un número válido."
        )
        return ""
    
def limpiar(entry_valor, lbl_resultado, combo):
    entry_valor.delete(0, "end")
    lbl_resultado.config(text="Resultado:")
    combo.current(0)