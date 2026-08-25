import customtkinter as ctk
from modulos import DiccionarioInteligente
from conexion import cargar
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
        
        # ==========================================================
        # ENCABEZADO / TÍTULO PRINCIPAL MODERNO
        # ==========================================================
        
        titulo = ctk.CTkLabel(
            self.raiz,
            text="LexiPy - Diccionario Inteligente",
            font=("Century Gothic", 26, "bold"), # Tipografía geométrica y sofisticada
            text_color="#FFFFFF" # Blanco puro para ambos modos (Claro/Oscuro)
        )
        titulo.pack(pady=(20, 10))
        
        
        # ==========================================================
        # FRAME DE BÚSQUEDA
        # ==========================================================

        frame_busqueda = ctk.CTkFrame(
            self.raiz,
            corner_radius=12
        )

        frame_busqueda.pack(
            fill="x",
            padx=30,
            pady=(5, 10)
        )


        # ----------------------------------------------------------
        # Fila principal del buscador
        # ----------------------------------------------------------

        frame_busqueda.columnconfigure(1, weight=1)

        self.lblBuscar = ctk.CTkLabel(
            frame_busqueda,
            text="🔎 Buscar palabra:",
            font=("Arial", 14, "bold")
        )

        self.lblBuscar.grid(
            row=0,
            column=0,
            padx=(20, 10),
            pady=12
        )


        self.txtBuscar = ctk.CTkEntry(
            frame_busqueda,
            width=400,
            height=35,
            placeholder_text="Ingrese la palabra a buscar..."
        )

        self.txtBuscar.grid(
            row=0,
            column=1,
            padx=10,
            pady=12,
            sticky="w"
        )


        self.btnBuscar = ctk.CTkButton(
            frame_busqueda,
            text="Buscar",
            width=100,
            height=35,
            corner_radius=8,
            fg_color="#800080",
            hover_color="#9932CC",
            command=self.buscar
        )

        self.btnBuscar.grid(
            row=0,
            column=2,
            padx=(10, 20),
            pady=12
        )


        # ----------------------------------------------------------
        # Panel flotante de sugerencias
        # ----------------------------------------------------------

        self.frame_sugerencias = ctk.CTkFrame(
            self.raiz,
            width=400,
            corner_radius=8,
            fg_color=("gray90", "gray20")
        )

        # Inicialmente oculto
        self.frame_sugerencias.place_forget()


        # Detectar lo que escribe el usuario
        self.txtBuscar.bind(
            "<KeyRelease>",
            self.autocompletar
        )
        
        
        # ==========================================================
        # FRAME DEL SIGNIFICADO
        # ==========================================================
        
        frame_significado = ctk.CTkFrame(self.raiz, corner_radius=12)
        frame_significado.pack(fill="x", padx=30, pady=(0, 10))
        
        ctk.CTkLabel(
            frame_significado,
            text="📖 Significado",
            font=("Arial", 16, "bold")
        ).pack(anchor="w", padx=10, pady=(10, 5))
        
        self.txtSignificado = ctk.CTkTextbox(
            frame_significado,
            height=100, corner_radius=8, wrap="word", font=("Arial", 14)
        )
        
        self.txtSignificado.pack(
            fill="x",
            padx=10,
            pady=(0, 10)
        )
        
        # ==========================================================
        # FRAME INFERIOR
        # ==========================================================
        
        frame_inferior = ctk.CTkFrame(self.raiz, corner_radius=12)
        frame_inferior.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # ==========================================================
        # PANEL DE BOTONES
        # ==========================================================
        
        frame_botones = ctk.CTkFrame(frame_inferior, width=200, corner_radius=12)
        frame_botones.pack(side="left", padx=(20, 10), fill="y", pady=10)
        
        lbl_acciones = ctk.CTkLabel(
        frame_botones,
        text="Acciones",
        font=("Arial", 17, "bold")
        )
        lbl_acciones.pack(
            pady=(15, 15)
        )

        # Botón Agregar
        ctk.CTkButton(
            frame_botones,
            text="➕ Agregar",
            width=180,
            height=40,
            corner_radius=8,
            fg_color="#4CAF50",
            hover_color="#45a049",
            command=self.agregar
        ).pack(pady=8)

        # Botón Editar
        ctk.CTkButton(
            frame_botones,
            text="✏️ Editar",
            width=180,
            height=40,
            corner_radius=8,
            command=self.editar
        ).pack(pady=8)

        # Botón Eliminar
        ctk.CTkButton(
            frame_botones,
            text="🗑️ Eliminar",
            width=180,
            height=40,
            corner_radius=8,
            fg_color="#C0392B",
            hover_color="#962D22",
            command=self.eliminar
        ).pack(pady=8)
        
        # ==========================================================
        # PANEL REPORTE (Derecho)
        # ==========================================================
        
        frame_reporte = ctk.CTkFrame(frame_inferior, corner_radius=12)
        frame_reporte.pack(side="right", fill="both", expand=True, padx=(10, 20), pady=10)
        
        lbl_reporte = ctk.CTkLabel(
        frame_reporte,
        text="📄  Reporte",
        font=("Arial", 17, "bold")
        )
        lbl_reporte.pack(
            anchor="w",
            padx=15,
            pady=(15, 5)
        )
        
        # --- SUB-FRAME PARA ALINEAR LOS BOTONES EN FILA ---
        frame_botones_reporte = ctk.CTkFrame(frame_reporte, fg_color="transparent")
        frame_botones_reporte.pack(anchor="w", padx=10, pady=(0, 10))
        
        ctk.CTkButton(
            frame_botones_reporte,
            text="Generar reporte",
            width=180,
            height=40,
            # Color ROjo Fuerte para el botón de reporte
            fg_color="#FF4500",
            hover_color="#FF6347",
            corner_radius=20,
            command=self.reporte
        ).pack(side="left", padx=(370, 240))
        
        ctk.CTkButton(
            frame_botones_reporte,
            text="🧹 Limpiar ",
            width=100,
            height=40,
            corner_radius=20,
            fg_color="#555555",
            hover_color="#444444",
            command=self.limpiar
        ).pack(side="left")
        
        # Caja de Texto del Reporte (queda abajo de ambos botones)
        self.txtReporte = ctk.CTkTextbox(
            frame_reporte,
            corner_radius=8,
            wrap="word",
            font=("Arial", 13),
            width=450,
            height=300
        )

        self.txtReporte.pack(
            padx=10,
            pady=(0, 10),
            fill="both",
            expand=True
        )
    def posicionar_sugerencias(self):

        # Actualizar la ventana para obtener posiciones correctas
        self.raiz.update_idletasks()

        # Posición del Entry respecto a la ventana principal
        x = (
            self.txtBuscar.winfo_rootx()
            - self.raiz.winfo_rootx()
        )

        y = (
            self.txtBuscar.winfo_rooty()
            - self.raiz.winfo_rooty()
            + self.txtBuscar.winfo_height()
            + 5
        )

        # Colocar el panel debajo del Entry
        self.frame_sugerencias.place(
            x=x,
            y=y
        )

        # Colocarlo por encima de los demás widgets
        self.frame_sugerencias.lift()
        
    def autocompletar(self, evento=None):

        texto = self.txtBuscar.get().strip()

        # Si no hay texto, ocultamos las sugerencias
        if texto == "":
            self.frame_sugerencias.place_forget()
            return

        # Cargar las palabras del diccionario
        diccionario = cargar()

        palabras = diccionario.keys()

        # Buscar palabras que comiencen con lo escrito
        coincidencias = [
            palabra for palabra in palabras
            if palabra.lower().startswith(texto.lower())
        ]

        # Mostrar máximo 5 sugerencias
        coincidencias = coincidencias[:5]

        # Eliminar sugerencias anteriores
        for widget in self.frame_sugerencias.winfo_children():
            widget.destroy()

        # Si no hay coincidencias
        if not coincidencias:
            self.frame_sugerencias.place_forget()
            return

        # Crear los botones de sugerencias
        for palabra in coincidencias:

            boton = ctk.CTkButton(
                self.frame_sugerencias,
                text=palabra,
                anchor="w",
                height=32,
                fg_color="transparent",
                hover_color=("#D9D9D9", "#333333"),
                text_color=("#222222", "#FFFFFF"),
                command=lambda p=palabra: self.seleccionar_sugerencia(p)
            )

            boton.pack(
                fill="x",
                padx=5,
                pady=2
            )

        # Posicionar el panel como una capa flotante
        self.posicionar_sugerencias()
        
    
    def seleccionar_sugerencia(self, palabra):

        # Colocar la palabra seleccionada en el buscador
        self.txtBuscar.delete(0, "end")

        self.txtBuscar.insert(
            0,
            palabra
        )

        # Ocultar las sugerencias
        self.frame_sugerencias.place_forget()

        # Cursor al final
        self.txtBuscar.icursor("end")
        
        
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
        self.limpiar()
    
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