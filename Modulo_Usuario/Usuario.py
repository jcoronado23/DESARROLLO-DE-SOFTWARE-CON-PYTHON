from datetime import datetime

class Usuario:

    def __init__(self, cedula, nombre, anno_nacimiento, mes_nacimiento, dia_nacimiento):
        self.cedula = cedula
        self.nombre = nombre
        self.anno_nacimiento = anno_nacimiento
        self.mes_nacimiento = mes_nacimiento
        self.dia_nacimiento = dia_nacimiento    

    def mostrarDatos(self):

        fecha_nacimiento = datetime(self.anno_nacimiento, self.mes_nacimiento, self.dia_nacimiento)

        hoy = datetime.now()

        edad = hoy.year - fecha_nacimiento.year
        if( hoy.month, hoy.day ) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1

        print(f"Cedula: {self.cedula}, y nombre: {self.nombre}, y su edad es {edad}")