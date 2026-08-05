import customtkinter as ctk
from tkinter import messagebox
from modulos import DiccionarioInteligente


class VentanaEditar(ctk.CTkToplevel):

    def __init__(self, ventana_padre, funcion_actualizar=None):
        super().__init__(ventana_padre)
        
        # Convierte la ventana en modal
        self.transient(ventana_padre)
        self.grab_set()
        self.focus_force()

        self.diccionario = DiccionarioInteligente()
        self.funcion_actualizar = funcion_actualizar

        self.title("Editar Palabra")
        self.geometry("500x350")
        self.resizable(False, False)

        self.crearWidgets()

    def crearWidgets(self):

        # ---------- Título ----------
        self.lblTitulo = ctk.CTkLabel(
            self,
            text="Editar Palabra",
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

        # ---------- Nuevo significado ----------
        self.lblSignificado = ctk.CTkLabel(
            self,
            text="Nuevo significado"
        )
        self.lblSignificado.pack(anchor="w", padx=30)

        self.txtSignificado = ctk.CTkTextbox(
            self,
            width=420,
            height=120
        )
        self.txtSignificado.pack(padx=30, pady=(5, 20))

        # ---------- Botón ----------
        self.btnEditar = ctk.CTkButton(
            self,
            text="Actualizar",
            command=self.editar
        )
        self.btnEditar.pack()

    def editar(self):

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
                "Debe ingresar el nuevo significado."
            )
            return

        exito = self.diccionario.editar_palabra(
            palabra,
            significado
        )

        if exito:

            messagebox.showinfo(
                "Éxito",
                "La palabra fue actualizada correctamente."
            )

            if self.funcion_actualizar:
                self.funcion_actualizar()

            self.destroy()

        else:

            messagebox.showerror(
                "Error",
                "La palabra no existe en el diccionario."
            )