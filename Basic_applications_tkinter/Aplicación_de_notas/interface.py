import tkinter as tk
from tkinter import messagebox
import functions


class AplicacionNotas:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Aplicación de Notas")
        self.ventana.geometry("450x400")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#101291")

        # Lista donde se almacenan las notas
        self.notas = []

        self.crear_widgets()


    def agregar(self):

        nota = self.entry_nota.get()

        if functions.agregar_nota(self.notas, nota):

            self.lista_notas.insert(
                tk.END,
                f"Nota: {float(nota):.2f}"
            )

            self.entry_nota.delete(0, tk.END)


    def calcular_promedio(self):

        promedio = functions.calcular_promedio(
            self.notas
        )

        if promedio:
            self.lbl_resultado.config(
                text=f"Promedio: {promedio}"
            )


    def reiniciar(self):

        functions.reiniciar(
            self.notas
        )

        self.lista_notas.delete(
            0,
            tk.END
        )

        self.entry_nota.delete(
            0,
            tk.END
        )

        self.lbl_resultado.config(
            text="Promedio:"
        )


    def crear_widgets(self):

        titulo = tk.Label(
            self.ventana,
            text="Registro de Notas",
            font=("Arial", 16, "bold"),
            bg="lightsteelblue"
        )

        titulo.pack(pady=15)


        # Entrada de nota

        tk.Label(
            self.ventana,
            text="Ingrese una nota:",
            bg="lightsteelblue"
        ).pack()


        self.entry_nota = tk.Entry(
            self.ventana,
            width=20
        )

        self.entry_nota.pack(pady=5)


        # Botón agregar

        tk.Button(
            self.ventana,
            text="Agregar",
            width=15,
            command=self.agregar
        ).pack(pady=5)


        # Lista de notas

        self.lista_notas = tk.Listbox(
            self.ventana,
            width=25,
            height=6
        )

        self.lista_notas.pack(pady=10)


        # Botón promedio

        tk.Button(
            self.ventana,
            text="Calcular promedio",
            width=20,
            command=self.calcular_promedio
        ).pack(pady=5)


        # Resultado

        self.lbl_resultado = tk.Label(
            self.ventana,
            text="Promedio:",
            font=("Arial",12,"bold"),
            bg="lightsteelblue"
        )

        self.lbl_resultado.pack(pady=10)


        # Reiniciar

        tk.Button(
            self.ventana,
            text="Reiniciar",
            width=15,
            command=self.reiniciar
        ).pack(pady=5)


    def ejecutar(self):

        self.ventana.mainloop()