import tkinter as tk
import RepositorioUsuario
from tkinter import messagebox
from datetime import date
from tkcalendar import DateEntry

class VentanaEditarUsuario(tk.Toplevel):
    
    def __init__(self, ventana_padre, funcion_actualizar, usuario):
        super().__init__(ventana_padre)
        self.usuario = usuario
        self.funcion_actualizar = funcion_actualizar
        
        self.title("Editar Usuario")
        self.geometry("300x320")
        
        self.resizable(False, False)
        
        self.crearWidgets()
        
        self.transient(ventana_padre)
        self.grab_set()
        
    def crearWidgets(self):
        tk.Label(self, text="Cedula formato (4-0111-0222)").pack(pady=(15, 0))
        self.entry_cedula = tk.Entry(self)
        self.entry_cedula.insert(0, self.usuario.cedula)
        self.entry_cedula.config(state="disabled")
        self.entry_cedula.pack()
        
        tk.Label(self, text="Nombre").pack(pady=(10, 0))
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.insert(0, self.usuario.nombre)
        self.entry_nombre.pack()
        
        
        tk.Label(self, text="Fecha nacimiento").pack(pady=(10, 0))
        self.date_nacimiento = DateEntry(
            self,
            date_pattern ="dd/mm/yyyy",
            locale = "es_ES",
            maxdate = date.today()
        )
        
        self.date_nacimiento.set_date(date(self.usuario.anno_nacimiento, self.usuario.mes_nacimiento, self.usuario.dia_nacimiento))
        self.date_nacimiento.pack()
        
        tk.Button(self, text="Guardar", command=self.modificar).pack(pady=20)
        
    def modificar(self):
        #cedula = self.entry_cedula.get().strip()
        nombre = self.entry_nombre.get().strip()

        fecha = self.date_nacimiento.get_date()
        anno = fecha.year
        mes = fecha.month
        dia = fecha.day
        print(nombre)
        exito, mensaje = RepositorioUsuario.actualizarUsuario(self.usuario.cedula, nombre, anno, mes, dia)

        if exito:
            messagebox.showinfo("Exito", mensaje)
            self.funcion_actualizar()
            self.destroy()
        else:
            messagebox.showerror("Error", mensaje)