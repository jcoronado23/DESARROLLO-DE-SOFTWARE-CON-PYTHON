import tkinter as tk
from tkinter import ttk, messagebox
import RepositorioCredenciales
from InterfazUsuarios import VentanaUsuarios

class VentanaLogin:
    
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Iniciar Sesión")
        self.raiz.geometry("300x220")
        self.raiz.resizable(False, False)
        
        
        self.crearWidget()
        
    
    def crearWidget(self):
        tk.Label(self.raiz, text="Usuario:").pack(pady=(30,0))
        self.entry_usuario = tk.Entry(self.raiz)
        self.entry_usuario.pack()
        
        
        tk.Label(self.raiz, text="Contraseña:").pack(pady=(15,0))
        self.entry_contraseña = tk.Entry(self.raiz, show="*")
        self.entry_contraseña.pack()
        self.entry_contraseña.bind("<Return>", lambda evento: self.iniciarSecion())
        
        tk.Button(self.raiz, text="Ingresar", command=self.iniciarSecion).pack(pady=25)
        
        self.entry_usuario.focus_set() 
    
    def iniciarSecion(self):
        usuario = self.entry_usuario.get().strip()
        contraseña = self.entry_contraseña.get().strip()
        
        if usuario == "" or contraseña == "":
            messagebox.showwarning("Atencion", "Debe completar usuario y contrasenna") 
            return
        
        if RepositorioCredenciales.verificarCredenciales(usuario, contraseña):
            self.abrirVentanaPrincipal()
            
        else:
            messagebox.showerror("Error", "Usuario o contrasena incorrectos")
            self.entry_contraseña.delete(0, tk.END)
            
            
    def abrirVentanaPrincipal(self):
        for widget in self.raiz.winfo_children():
            widget.destroy()
            
        VentanaUsuarios(self.raiz)
    
raiz = tk.Tk()
app = VentanaLogin(raiz)
raiz.mainloop()