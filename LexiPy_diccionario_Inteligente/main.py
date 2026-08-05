import customtkinter as ctk
from interfaz import  VentanaDiccionario

def main():

    ventana = ctk.CTk()

    VentanaDiccionario(ventana)
    
    ventana.mainloop()

if __name__ == "__main__":
    main()