import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Primera app")
ventana.geometry("400x220")

contador = 0

lbl = tk.Label(ventana, text="0", font=("Arial, 20"))
lbl.pack()


def crear_sumador(valor):
    def sumar():
        global contador
        contador += valor
        lbl.config(text=str(contador))
    return sumar
    
tk.Button(ventana, text="suma 5", command=crear_sumador(5)).pack()
tk.Button(ventana, text="suma 10", command=crear_sumador(10)).pack()


ventana.mainloop()