import tkinter as tk
import functions


class Temporizador:

    def __init__(self):

        self.ventana = tk.Tk()

        self.ventana.title(
            "Temporizador de Cuenta Regresiva"
        )

        self.ventana.geometry(
            "400x300"
        )

        self.ventana.resizable(
            False,
            False
        )

        self.ventana.configure(
            bg="#340C78"
        )


        self.crear_widgets()


    def iniciar(self):

        functions.iniciar_cuenta(
            self.entry_segundos.get(),
            self.lbl_tiempo,
            self.ventana
        )


    def crear_widgets(self):

        titulo = tk.Label(
            self.ventana,
            text="Temporizador",
            font=("Arial",18,"bold"),
            bg="#340C78",
            fg="white"
        )

        titulo.pack(
            pady=20
        )


        tk.Label(
            self.ventana,
            text="Ingrese segundos:",
            bg="#340C78",
            fg="white",
            font=("Arial",12)
        ).pack()


        self.entry_segundos = tk.Entry(
            self.ventana,
            width=15,
            font=("Arial",12)
        )

        self.entry_segundos.pack(
            pady=10
        )


        tk.Button(
            self.ventana,
            text="Iniciar temporizador",
            width=20,
            command=self.iniciar
        ).pack(
            pady=10
        )


        self.lbl_tiempo = tk.Label(
            self.ventana,
            text="Tiempo restante:",
            font=("Arial",14,"bold"),
            bg="#340C78",
            fg="white"
        )

        self.lbl_tiempo.pack(
            pady=20
        )


    def ejecutar(self):

        self.ventana.mainloop()