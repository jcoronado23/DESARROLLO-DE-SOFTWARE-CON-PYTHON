import tkinter as tk
from tkinter import ttk, messagebox
import RepositorioUsuario
import VentanaCrearUsuario
import VentanaEditarUsuario

class VentanaUsuarios:
    
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Mostrar Usuarios")
        self.raiz.geometry("800x400")
        
        self.crearWidget()
        self.cargarUsuarios()
        
        
    def crearWidget(self):
        

        #Construir el buscar
        
        
        
        barra = tk.Menubutton(
            self.raiz,
            text="Mantenimiento",
            relief="raised",
            padx=12,
            pady=5)
        barra.pack(side="top", padx=(0,15))
        
        #self.raiz.config(menu=barra)
        
        m_usuarios = tk.Menu(barra, tearoff=0)
        m_usuarios.add_command(label="Crear Usuario", command=self.abrir_FormularioCrear, accelerator="Ctrl+A")
        m_usuarios.add_separator()
        m_usuarios.add_command(label="Modificar Usuario", command=self.abrirFormularioModificar)
        m_usuarios.add_command(label="Eliminar Usuario", command=self.eliminarUsuario)
        
        #barra.add_cascade(label="Mantenimiento de Usuarios", menu=m_usuarios)
        barra.config(menu=barra)
        #menu ["menu"] = m_usuarios
        
        frame_busqueda = tk.Frame(self.raiz)
        frame_busqueda.pack(pady=10, fill="x", padx=10)
        
        tk.Label(frame_busqueda, text="Buscar por nombre:").pack(side="left", padx=(0,5))
        
        self.entry_busqueda = tk.Entry(frame_busqueda)
        self.entry_busqueda.pack(side="left", padx=5, expand=True, fill="x")
        
        self.entry_busqueda.bind("<Return>", lambda evento: self.buscarUsuarios())
        
        tk.Button(frame_busqueda, text="Buscar", command=self.buscarUsuarios).pack(side="left", padx=5)
        tk.Button(frame_busqueda, text="Mostrar todos", command=self.cargarUsuarios).pack(side="left", padx=5)
        tk.Button(frame_busqueda, text="Crear Usuario", command=self.abrir_FormularioCrear).pack(side="left", padx=5)
        tk.Button(frame_busqueda, text="Modificar Usuario", command=self.abrirFormularioModificar).pack(side="left", padx=5)
        tk.Button(frame_busqueda, text="Eliminar Usuario", command=self.eliminarUsuario).pack(side="left", padx=5)
        
        #Construcción de la tabla
        columnas = ("cedula", "nombre", "edad")
        self.tabla = ttk.Treeview(self.raiz, columns=columnas, show="headings")
        
        self.tabla.heading("cedula", text="Cedula")
        self.tabla.heading("nombre", text="Nombre del Usuario")
        self.tabla.heading("edad", text="Edad Calculada")
        
        self.tabla.column("cedula", width=150)
        self.tabla.column("nombre", width=250)
        self.tabla.column("edad", width=80, anchor="center")
        
        self.tabla.pack(expand=True, fill="both", padx=10, pady=(0, 10))
        
    def limpiarTabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        
    def insertarUsuariosEntabla(self, lista_usuarios):
        self.limpiarTabla()
        
        if(len(lista_usuarios) == 0):
            self.tabla.insert("", "end", values=("", "No hay usuarios", ""))
        
        for usu in lista_usuarios:
            edad = usu.calcularEdad()
            edad_mostrar = edad if edad is not None else "N/D"
            self.tabla.insert("", "end", values=(usu.cedula, usu.nombre, edad_mostrar))
        
    def cargarUsuarios(self):
        lista_usuarios = RepositorioUsuario.leerUsuarios()
        self.insertarUsuariosEntabla(lista_usuarios)
        
    def buscarUsuarios(self):
        texto = self.entry_busqueda.get().strip()
        
        if texto == "":
            self.cargarUsuarios()
            return
        
        lista_usuarios = RepositorioUsuario.buscarUsuario(texto)
        self.insertarUsuariosEntabla(lista_usuarios)
        
    def abrir_FormularioCrear(self):
        VentanaCrearUsuario.VentanaCrearUsuario(self.raiz, self.cargarUsuarios)
        
    def abrirFormularioModificar(self):
        
        seleccionado = self.tabla.selection()
        
        if not seleccionado:
            messagebox.showwarning("Atencion", "No ha seleccionado ningun registro en la tabla ")
            return
        
        fila = self.tabla.item(seleccionado[0])
        cedula = fila["values"][0]
        
        if cedula == "":
            return
        
        usuario = RepositorioUsuario.buscarUsuario(cedula)
        
        if usuario is None:
            messagebox.showerror("Error", "El usuario no se encontro")
            return
        
        VentanaEditarUsuario.VentanaEditarUsuario(self.raiz, self.cargarUsuarios, usuario[0])
    
    def eliminarUsuario(self):
        
        cedula = self.obtenerCedulaSeleccionada()
        if cedula is None:
            return
        
        confirmar = messagebox.askyesno(
            "Confirmar eliminar",
            f"¿Está seguro de eliminar el usuario con cédula {cedula}?"
        )
        
        if not confirmar:
            return
        
        exito, mensaje = RepositorioUsuario.eliminarUsuario(cedula)
        
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.cargarUsuarios()
            
        else:
            messagebox.showerror("Error", mensaje)
    
    def obtenerCedulaSeleccionada(self):
        seleccionado = self.tabla.selection()
        
        if not seleccionado:
            messagebox.showwarning("Atencion", "No ha seleccionado ningun registro en la tabla ")
            return None
        
        fila = self.tabla.item(seleccionado[0])
        cedula = fila["values"][0]
        
        if cedula == "":
            return None
        
        return cedula
        
raiz = tk.Tk()
app = VentanaUsuarios(raiz)
raiz.mainloop()