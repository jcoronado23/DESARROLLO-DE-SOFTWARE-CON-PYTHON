import customtkinter as ctk
from tkinter import messagebox
from modulos import DiccionarioInteligente


class VentanaAgregar(ctk.CTkToplevel):

    def __init__(self, ventana_padre, funcion_actualizar=None):
        super().__init__(ventana_padre)


        self.diccionario = DiccionarioInteligente()
        self.funcion_actualizar = funcion_actualizar
        
        self.title("Agregar Nueva Palabra")
        self.geometry("500x350")
        self.resizable(False, False)
        
        #ventana modal
        self.transient(ventana_padre)
        self.grab_set()
        self.focus_force()

        self.crearWidgets()

    def crearWidgets(self):

        # ---------- Título ----------
        self.lblTitulo = ctk.CTkLabel(
            self,
            text="Agregar Nueva Palabra",
            font=("Arial", 20, "bold")
        )
        self.lblTitulo.pack(pady=(20, 15))

        # ---------- Palabra ----------
        self.lblPalabra = ctk.CTkLabel(
            self,
            text="Palabra"
        )
        self.lblPalabra.pack(anchor="w", padx=30)

        self.entryPalabra = ctk.CTkEntry(
            self,
            width=420
        )
        self.entryPalabra.pack(padx=30, pady=(5, 15))

        # ---------- Significado ----------
        self.lblSignificado = ctk.CTkLabel(
            self,
            text="Significado"
        )
        self.lblSignificado.pack(anchor="w", padx=30)

        self.txtSignificado = ctk.CTkTextbox(
            self,
            width=420,
            height=120
        )
        self.txtSignificado.pack(padx=30, pady=(5, 20))

        # ---------- Botón ----------
        self.btnGuardar = ctk.CTkButton(
            self,
            text="Guardar",
            command=self.guardar
        )
        self.btnGuardar.pack()

    def guardar(self):

        palabra = self.entryPalabra.get().strip()

        significado = self.txtSignificado.get(
            "1.0",
            "end"
        ).strip()

        # Validaciones
        if palabra == "":
            messagebox.showwarning(
                "Advertencia",
                "Debe ingresar una palabra."
            )
            return

        if significado == "":
            messagebox.showwarning(
                "Advertencia",
                "Debe ingresar un significado."
            )
            return

        exito = self.diccionario.agregar_palabra(
            palabra,
            significado
        )

        if exito:

            messagebox.showinfo(
                "Éxito",
                "La palabra fue agregada correctamente."
            )

            if self.funcion_actualizar:
                self.funcion_actualizar()

            self.destroy()

        else:

            messagebox.showerror(
                "Error",
                "La palabra ya existe en el diccionario."
            )
            