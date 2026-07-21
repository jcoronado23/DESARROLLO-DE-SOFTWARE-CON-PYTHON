import tkinter as tk

#Crear una ventana, definir su tamaño y título
ventana = tk.Tk()
ventana.title("Mi Primera app")
ventana.geometry("400x220")

contador = 0
# lbl para mostrar el valor del contador
lbl = tk.Label(ventana, text="0", font=("Arial", 20))
lbl.pack()

# Funcion para crear un sumador que sume un valor específico al contador
def crear_sumador(valor):
    def sumar():
        global contador
        contador += valor
        lbl.config(text=str(contador))
    return sumar

# Botones para sumar 5 y 10 al contador
tk.Button(ventana, text="suma 5", command=crear_sumador(5)).pack()
tk.Button(ventana, text="suma 10", command=crear_sumador(10)).pack()


ventana.mainloop()