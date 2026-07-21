import tkinter as tk
from tkinter import ttk

import functions


class Conversor:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Conversor de Unidades")
        self.ventana.geometry("500x320")
        self.ventana.resizable(False, False)

        self.crear_widgets()

    def convertir(self):

        resultado = functions.convertir(
            self.entry_valor.get(),
            self.combo.get()
        )

        self.lbl_resultado.config(
            text=f"Resultado: {resultado}"
        )

    def crear_widgets(self):

        titulo = tk.Label(
            self.ventana,
            text="Conversor de Unidades",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=15)

        tk.Label(
            self.ventana,
            text="Ingrese el valor:"
        ).pack()

        self.entry_valor = tk.Entry(
            self.ventana,
            width=20
        )
        self.entry_valor.pack(pady=5)

        tk.Label(
            self.ventana,
            text="Conversión:"
        ).pack()

        self.combo = ttk.Combobox(
            self.ventana,
            width=30,
            state="readonly"
        )

        self.combo["values"] = (
            "Centímetros → Pulgadas",
            "Pulgadas → Centímetros",
            "Metros → Pies",
            "Pies → Metros",
            "Celsius → Fahrenheit",
            "Fahrenheit → Celsius"
        )

        self.combo.current(0)
        self.combo.pack(pady=10)

        tk.Button(
            self.ventana,
            text="Convertir",
            command=self.convertir
        ).pack(pady=10)
        

        self.lbl_resultado = tk.Label(
            self.ventana,
            text="Resultado:",
            font=("Arial", 12)
        )

        self.lbl_resultado.pack(pady=15)
        tk.Button(
            self.ventana,
            text="Limpiar",
            command=self.limpiar
        ).pack(pady=5)
        
    def limpiar(self):
        functions.limpiar(
            self.entry_valor,
            self.lbl_resultado,
            self.combo
        )

    def ejecutar(self):
        self.ventana.mainloop()