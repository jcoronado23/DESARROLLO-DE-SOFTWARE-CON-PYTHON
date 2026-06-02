import datetime

# Función para imprimir la fecha y hora actual

def imprimir_fecha_hora():
    ahora = datetime.datetime.now()
    print('\n¡Hola, Aquí tienes la fecha y hora. Feliz día! 🌞 😴💤\n')
    print("Fecha y hora actual:", ahora.strftime("%Y-%m-%d %H:%M:%S") + "\n")

imprimir_fecha_hora()