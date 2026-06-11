from datetime import datetime, date
import os
#Solicite la fecha de nacimiento al usuario
#Función para calcular la edad en años y edad en días
# Función para determinar cuantos días faltan para el próximo cumpleaños

#Limpiar la consola
os.system('cls' if os.name == 'nt' else 'clear')
nombre_de_usuario = input("Ingrese su nombre: ")
fecha_nacimiento_dia = input("Ingrese su día de nacimiento (dd): ")
fecha_nacimiento_mes = input("Ingrese su mes de nacimiento (mm): ")
fecha_nacimiento_anio = input("Ingrese su año de nacimiento (yyyy): ")
fecha_nacimiento = f"{fecha_nacimiento_dia}/{fecha_nacimiento_mes}/{fecha_nacimiento_anio}"

#Validar la fecha de nacimiento ingresada por el usuario
while True:
    try:
        datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
        break
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Fecha de nacimiento no válida. Por favor, ingrese una fecha en el formato dd/mm/yyyy.")
        fecha_nacimiento_dia = input("Ingrese su día de nacimiento (dd): ")
        fecha_nacimiento_mes = input("Ingrese su mes de nacimiento (mm): ")
        fecha_nacimiento_anio = input("Ingrese su año de nacimiento (yyyy): ")
        fecha_nacimiento = f"{fecha_nacimiento_dia}/{fecha_nacimiento_mes}/{fecha_nacimiento_anio}"

#Definir la clase Edad con los métodos para calcular la edad exacta y los días para el próximo cumpleaños
class Edad:
    #Limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')
    
    def __init__(self, fecha_nacimiento):
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
    
    def nombre_usuario(self):
        if nombre_de_usuario.strip() == "":
            return "Usuario"
        return nombre_de_usuario
    
    
#Función calcular la edad exacta, si hay un error la función devuelve la pregunta para ingresar la fecha de nacimiento nuevamente
    def calcular_edad_exacta(self):
        hoy = date.today()
        edad_en_años = hoy.year - self.fecha_nacimiento.year
        
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad_en_años -= 1
        
        edad_en_dias = (hoy - self.fecha_nacimiento).days
        
        return edad_en_años, edad_en_dias

    def dias_para_cumpleaños(self):
        hoy = date.today()
        
        proximo_cumpleaños = date(hoy.year, self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        if proximo_cumpleaños < hoy:
            proximo_cumpleaños = date(hoy.year + 1, self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        
        return (proximo_cumpleaños - hoy).days

edad = Edad(fecha_nacimiento)
dias_faltantes = edad.dias_para_cumpleaños()

print('--- Cálculo de Edad del Usuario ---\n')
print(f'Hola, {edad.nombre_usuario()}! 🎂\n')
print(f'Fecha de nacimiento: {fecha_nacimiento}')
print(f'Años del usuario: {edad.calcular_edad_exacta()[0]}')
print(f'Días total del usuario: {edad.calcular_edad_exacta()[1]}')
print(f'Días para el próximo cumpleaños: {dias_faltantes}...🎊 🎊 \n')
print('¡Felicidades ya casi cumple años!🎉')