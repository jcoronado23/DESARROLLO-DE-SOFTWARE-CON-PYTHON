import customtkinter as ctk
from tkinter import messagebox
from modulos import DiccionarioInteligente


class VentanaEliminar(ctk.CTkToplevel):

    def __init__(self, ventana_padre, funcion_actualizar=None):
        super().__init__(ventana_padre)

        # Convierte la ventana en modal
        self.transient(ventana_padre)
        self.grab_set()
        self.focus_force()
        
        self.diccionario = DiccionarioInteligente()
        self.funcion_actualizar = funcion_actualizar

        self.title("Eliminar Palabra")
        self.geometry("450x220")
        self.resizable(False, False)

        self.crearWidgets()

    def crearWidgets(self):

        # ---------- Título ----------
        self.lblTitulo = ctk.CTkLabel(
            self,
            text="Eliminar Palabra",
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
            width=350
        )
        self.entryPalabra.pack(padx=30, pady=(5, 20))

        # ---------- Botón ----------
        self.btnEliminar = ctk.CTkButton(
            self,
            text="Eliminar",
            fg_color="red",
            hover_color="darkred",
            command=self.eliminar
        )
        self.btnEliminar.pack()

    def eliminar(self):

        palabra = self.entryPalabra.get().strip()

        if palabra == "":
            messagebox.showwarning(
                "Advertencia",
                "Debe ingresar una palabra."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Desea eliminar la palabra '{palabra}'?"
        )

        if not confirmar:
            return

        exito = self.diccionario.eliminar_palabra(palabra)

        if exito:

            messagebox.showinfo(
                "Éxito",
                "La palabra fue eliminada correctamente."
            )

            if self.funcion_actualizar:
                self.funcion_actualizar()

            self.destroy()

        else:

            messagebox.showerror(
                "Error",
                "La palabra no existe en el diccionario."
            )