import tkinter as tk
from tkinter import ttk
import functions as fn
from tkinter import messagebox


class Ventana(tk.Tk):
    
    def __init__(self):
        super().__init__()
        # ==========================
        # Configuración de la ventana
        # ==========================
        self.title("Calcular Promedio de (3)Notas")
        self.geometry("900x450")
        self.resizable(False, False)
        
        self.notas = [None, None, None]
        
        self.crear_widgets()
        
    def crear_widgets(self):
        self.titulo()
        self.actualizar_datos()
            

    
    def agregar(self):
        print("Agregar nota")
        nota = fn.validar_nota(self.entry_nota.get())

        if nota is None:
            messagebox.showerror(
                "Error",
                "Ingrese una nota válida entre 0 y 100."
            )
            return

        if fn.agregar_nota(self.notas, nota):
            self.actualizar_datos()
            self.entry_nota.delete(0, tk.END)
        else:
            messagebox.showwarning(
                "Aviso",
                "Ya existen tres notas."
            )
                
    def actualizar_datos(self):
        print("Actualizar datos")
        self.lbl_nota1.config(
            text=f"Nota 1 = {self.notas[0] if self.notas[0] is not None else 'Vacío'}"
        )

        self.lbl_nota2.config(
            text=f"Nota 2 = {self.notas[1] if self.notas[1] is not None else 'Vacío'}"
        )

        self.lbl_nota3.config(
            text=f"Nota 3 = {self.notas[2] if self.notas[2] is not None else 'Vacío'}"
        )
        
    def titulo(self):
        
        self.title("Calcular Promedio de (3)Notas")
        # ======================================================
        # FRAME SUPERIOR
        # ======================================================
        self.frame_superior = tk.Frame(self)
        self.frame_superior.grid(row=0, column=0, padx=20, pady=15, sticky="ew")

        self.frame_superior.grid_columnconfigure(0, weight=1)

        # Título
        tk.Label(
            self.frame_superior,
            text="Calcular Promedio de (3)Notas",
            font=("Arial", 20, "bold")
        ).grid(row=0, column=0, pady=(0, 15))

        # Bienvenida
        self.frame_bienvenida = tk.Frame(
            self.frame_superior,
            padx=20,
            pady=15
        )

        self.frame_bienvenida.grid(row=1, column=0, sticky="ew")

        tk.Label(
            self.frame_bienvenida,
            text="Bienvenido al programa de cálculo del promedio de tres notas.\nIngrese las notas para comenzar.",
            font=("Arial", 11),
            justify="center"
        ).pack()

        # ======================================================
        # FRAME CONTENEDOR
        # ======================================================

        self.frame_contenido = tk.Frame(self)
        self.frame_contenido.grid(row=1, column=0, padx=20, pady=20)

        # ----------------------------
        # Frame izquierdo
        # ----------------------------

        self.frame_datos = tk.Frame(
            self.frame_contenido,
            padx=20,
            pady=20
        )

        self.frame_datos.grid(row=0, column=0, padx=40, sticky="n")

        self.lbl_nota1 = tk.Label(self.frame_datos, text="Nota 1 = Vacío")
        self.lbl_nota1.grid(row=0, column=0, sticky="w", pady=5)

        self.lbl_nota2 = tk.Label(self.frame_datos, text="Nota 2 = Vacío")
        self.lbl_nota2.grid(row=1, column=0, sticky="w", pady=5)

        self.lbl_nota3 = tk.Label(self.frame_datos, text="Nota 3 = Vacío")
        self.lbl_nota3.grid(row=2, column=0, sticky="w", pady=5)

        # ----------------------------
        # Frame derecho
        # ----------------------------

        self.frame_opciones = tk.Frame(
            self.frame_contenido,
            padx=20,
            pady=20
        )

        self.frame_opciones.grid(row=0, column=1, padx=80, sticky="n")

        # Agregar Nota

        self.btn_agregar = tk.Button(
            self.frame_opciones,
            text="Agregar Nota",
            width=15,
            command=self.agregar
        )
        self.btn_agregar.grid(row=0, column=0, padx=5, pady=10)

        self.entry_nota = tk.Entry(
            self.frame_opciones,
            width=18
        )

        self.entry_nota.grid(row=0, column=1, padx=5)
        

        # Editar Nota

        self.btn_editar = tk.Button(
            self.frame_opciones,
            text="Editar Nota",
            width=15,
            command=self.editar
        )

        self.btn_editar.grid(row=1, column=0, padx=5, pady=10)
        
        self.combo_notas = ttk.Combobox(
            self.frame_opciones,
            values=["Nota 1", "Nota 2", "Nota 3"],
            state="readonly",
            width=15
        )
        
        self.combo_notas.set("Seleccionar")
        self.combo_notas.grid(row=1, column=1, padx=5)

        self.entry_editar = tk.Entry(
            self.frame_opciones,
            width=18
        )

        self.entry_editar.grid(row=1, column=2, padx=5)
        
        
                
        # Promedio

        self.btn_promedio = tk.Button(
            self.frame_opciones,
            text="Promedio de Notas",
            width=15,
            command=self.calcular_promedio
        )

        self.btn_promedio.grid(row=2, column=0, padx=5, pady=15)

        self.lbl_resultado = tk.Label(
            self.frame_opciones,
            text="Resultado:"
        )
        self.lbl_resultado.grid(row=2, column=1, columnspan=2, sticky="w")
        
    def editar(self):
        indice = self.combo_notas.current()

        nueva_nota = fn.validar_nota(self.entry_editar.get())

        if nueva_nota is None:
            messagebox.showerror(
                "Error",
                "Ingrese una nota válida entre 0 y 100."
            )
            return

        self.notas[indice] = nueva_nota
        self.actualizar_datos()
        self.entry_editar.delete(0, tk.END)
    def calcular_promedio(self):
        promedio = fn.calcular_promedio(self.notas)

        if promedio is None:
            messagebox.showwarning(
                "Aviso",
                "Debe ingresar las tres notas."
            )
            return

        self.lbl_resultado.config(
            text=f"Resultado: {promedio:.2f}"
        )
