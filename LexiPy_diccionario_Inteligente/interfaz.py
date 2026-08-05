import customtkinter as ctk
from modulos import DiccionarioInteligente
from ventana_agregar import VentanaAgregar
from ventana_editar import VentanaEditar
from ventana_eliminar import VentanaEliminar
from tkinter import messagebox

class VentanaDiccionario:

    def __init__(self, raiz):

        self.raiz = raiz
        self.diccionario = DiccionarioInteligente()

        self.raiz.title("LexiPy - Diccionario Inteligente")
        self.raiz.geometry("1200x700")
        
        ctk.set_appearance_mode("System")      # Light, Dark o System
        ctk.set_default_color_theme("blue")

        self.crearWidget()
        
    
    def crearWidget(self):
        # Aquí tú colocarás los widgets
        #creación de frame busqueda
        
        titulo = ctk.CTkLabel(
            self.raiz,
            text="LexiPy - Diccionario Inteligente",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=20)
        
        
        # Frame búsqueda
        frame_busqueda = ctk.CTkFrame(self.raiz)
        frame_busqueda.pack(fill="x", padx=20, pady=20)
        
        
        frame_significado = ctk.CTkFrame(self.raiz)
        frame_significado.pack(fill="x", padx=20, pady=10)
        
        self.lblBuscar = ctk.CTkLabel(
            frame_busqueda,
            text="Buscar palabra:"
        )
        

        self.txtBuscar = ctk.CTkEntry(
            frame_busqueda,
            width=300
        )

        self.btnBuscar = ctk.CTkButton(
            frame_busqueda,
            text="Buscar",
            command=self.buscar
        )
        
        # Título
        ctk.CTkLabel(
            frame_significado,
            text="Significado",
            font=("Arial", 16, "bold")
        ).pack(anchor="w", padx=10, pady=(10, 5))
        
        self.txtSignificado = ctk.CTkTextbox(
            frame_significado,
            height=100, wrap="word"
        )
        
        self.txtSignificado.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )
        self.lblBuscar.pack(side="left", padx=10)

        self.txtBuscar.pack(side="left", padx=10)

        self.btnBuscar.pack(side="left", padx=10)
        
        frame_inferior = ctk.CTkFrame(self.raiz)
        frame_inferior.pack(fill="both", expand=True, padx=20, pady=20)

        frame_botones = ctk.CTkFrame(frame_inferior)
        frame_botones.pack(side="left", padx=20, fill="y")

        frame_reporte = ctk.CTkFrame(frame_inferior)
        frame_reporte.pack(side="right", fill="both", expand=True)
        
        #Creación de botones
        
        ctk.CTkButton(
            frame_botones,
            text="Agregar",
            width=180,
            command=self.agregar
        ).pack(pady=8)

        ctk.CTkButton(
            frame_botones,
            text="Editar",
            width=180,
            command=self.editar
        ).pack(pady=8)

        ctk.CTkButton(
            frame_botones,
            text="Eliminar",
            width=180,
            command=self.eliminar
        ).pack(pady=8)

        ctk.CTkButton(
            frame_botones,
            text="Limpiar",
            width=180,
            command=self.limpiar
        ).pack(pady=8)
        
        ctk.CTkButton(
            frame_reporte,
            text="Generar reporte",
            width=180,
            command=self.reporte
        ).pack(pady=10)
        
        self.txtReporte = ctk.CTkTextbox(
            frame_reporte,
            width=450,
            height=300
        )

        self.txtReporte.pack(
            padx=10,
            pady=10,
            fill="both",
            expand=True
        )
                
    
    def buscar(self):

        palabra = self.txtBuscar.get().strip()

        if palabra == "":
            messagebox.showwarning(
                "Advertencia",
                "Ingrese una palabra."
            )
            return


        significado = self.diccionario.buscar_palabra(palabra)


        self.txtSignificado.delete(
            "1.0",
            "end"
        )


        if significado:

            self.txtSignificado.insert(
                "end",
                significado
            )

        else:

            self.txtSignificado.insert(
                "end",
                "La palabra no existe."
            )
            
    #Metodo Actulizar
    def actualizar(self):
        self.limpiar
    
    def agregar(self):
        VentanaAgregar(
            self.raiz,
            self.actualizar
        )
        
    def editar(self):
        VentanaEditar(
            self.raiz,
            self.actualizar
        )

    def eliminar(self):
        VentanaEliminar(
            self.raiz,
            self.actualizar
        )
        
    def reporte(self):

        ruta = self.diccionario.generar_reporte()

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            self.txtReporte.delete(
                "1.0",
                "end"
            )

            self.txtReporte.insert(
                "end",
                contenido
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def limpiar(self):

        self.txtBuscar.delete(0, "end")

        self.txtSignificado.delete("1.0", "end")

        self.txtReporte.delete("1.0", "end")