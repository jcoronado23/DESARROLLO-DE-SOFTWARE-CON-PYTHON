import tkinter as tk
import RepositorioUsuario
from tkinter import messagebox
from datetime import date
from tkcalendar import DateEntry

class VentanaCrearUsuario(tk.Toplevel):
    
    def __init__(self, ventana_padre, funcion_actualizar):
        super().__init__(ventana_padre)
        self.funcion_actualizar = funcion_actualizar
        
        
        self.title("Crear Usuario")
        self.geometry("300x300")
        self.resizable(False, False)
        
        self.crearWidget()
        
        #Para convertir esto en un modal.
        self.transient(ventana_padre)
        self.grab_set()
        
        
    def crearWidget(self):
        tk.Label(self, text="Cedula formato (4-0111-0222)").pack(pady=(15, 0))
        self.entry_cedula = tk.Entry(self)
        self.entry_cedula.pack()
        
        tk.Label(self, text="Nombre").pack(pady=(10, 0))
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()
        
        
        tk.Label(self, text="Fecha nacimiento").pack(pady=(10, 0))
        self.date_nacimiento = DateEntry(
            self,
            date_pattern ="dd/mm/yyyy",
            locale = "es_ES",
            maxdate = date.today()
        )
        self.date_nacimiento.pack()
        
        tk.Button(self, text="Guardar", command=self.guardar).pack(pady=20)
        

    def guardar(self):
        cedula = self.entry_cedula.get().strip()
        nombre = self.entry_nombre.get().strip()
        
        fecha = self.date_nacimiento.get_date()
        anno = fecha.year
        mes = fecha.month
        dia = fecha.day
        
        exito, mensaje = RepositorioUsuario.crearUsuario(cedula, nombre, anno, mes, dia)
        
        if exito:
            messagebox.showinfo("Exito", mensaje)
            self.funcion_actualizar()
            self.destroy()
        else:
            messagebox.showerror("Error", mensaje)