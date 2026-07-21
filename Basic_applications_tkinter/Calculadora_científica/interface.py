import tkinter as tk
import functions

class Calculadora:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Calculadora Científica")
        self.ventana.geometry("392x600")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="lightsteelblue")

        self.operacion = ""
        self.pantalla = tk.StringVar()

        self.crear_widgets()

    def agregar(self, texto):
        self.operacion = functions.agregar(
            self.operacion,
            self.pantalla,
            texto
        )

    def calcular(self):
        self.operacion = functions.calcular(
            self.operacion,
            self.pantalla
        )

    def limpiar(self):
        self.operacion = functions.limpiar(
            self.pantalla
        )

    def crear_widgets(self):

        entrada = tk.Entry(
            self.ventana,
            textvariable=self.pantalla,
            font=("Arial",20,"bold"),
            width=22,
            bd=20,
            justify="right"
        )

        entrada.place(x=10,y=60)

        color = "gray77"
        ancho = 11
        alto = 3

        botones = [
            ("0", 0, 17, 180),
            ("1", 1, 107, 180),
            ("2", 2, 197, 180),
            ("3", 3, 287, 180),

            ("4", 4, 17, 240),
            ("5", 5, 107, 240),
            ("6", 6, 197, 240),
            ("7", 7, 287, 240),

            ("8", 8, 17, 300),
            ("9", 9, 107, 300),
            ("π", "math.pi", 197, 300),
            (".", ".", 287, 300),

            ("+", "+", 17, 360),
            ("-", "-", 107, 360),
            ("*", "*", 197, 360),
            ("/", "/", 287, 360),

            ("√", "math.sqrt(", 17, 420),
            ("C", "C", 107, 420),
            ("EXP", "**", 197, 420),
            ("=", "=", 287, 420),

            ("(", "(", 17, 480),
            (")", ")", 107, 480),
            ("%", "%", 197, 480),
            ("ln", "math.log(", 287, 480)
        ]

        for texto, valor, x, y in botones:

            if valor == "=":
                comando = self.calcular

            elif valor == "C":
                comando = self.limpiar

            else:
                comando = lambda v=valor: self.agregar(v)

            tk.Button(
                self.ventana,
                text=texto,
                bg=color,
                width=ancho,
                height=alto,
                command=comando
            ).place(x=x, y=y)

        self.limpiar()

    def ejecutar(self):
        self.ventana.mainloop()