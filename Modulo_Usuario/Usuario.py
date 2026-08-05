from datetime import datetime

class Usuario:

    def __init__(self, cedula, nombre, anno_nacimiento, mes_nacimiento, dia_nacimiento):
        self.cedula = cedula
        self.nombre = nombre
        self.anno_nacimiento = anno_nacimiento
        self.mes_nacimiento = mes_nacimiento
        self.dia_nacimiento = dia_nacimiento    

    def mostrarDatos(self):

        try:
            fecha_nacimiento = datetime(self.anno_nacimiento, self.mes_nacimiento, self.dia_nacimiento)
            
            hoy = datetime.now()

            edad = hoy.year - fecha_nacimiento.year
            if( hoy.month, hoy.day ) < (fecha_nacimiento.month, fecha_nacimiento.day):
                edad -= 1

            nombre_mayuscula = self.nombre.upper()

            print(f"Cedula: {self.cedula}, y nombre: {nombre_mayuscula}, y su edad es {edad}") #console.log()

        except Exception:
            print("La fecha no tiene el formato correcto")
            
    def calcularEdad(self):
        try:
            fecha_nacimiento = datetime(self.anno_nacimiento, self.mes_nacimiento, self.dia_nacimiento)
            hoy = datetime.now()
            
            edad = hoy.year - fecha_nacimiento.year
            if(hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
                edad -= 1
                
            return edad
        
        except Exception:
            return None

        