class Usuario:
    
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        
    def mostrarDatos(self):
        print(f"Cedula: {self.cedula}, y nombre: {self.nombre}")