# creación de programa que llame a las variables globales y las imprima en pantalla

from Globales import Nombre, Edad, Ciudad, ID


# Función para imprimir las variables globales
def imprimir_variables():
    print('Información de Usuario 😉:\n')
    print(f'Nombre: {Nombre}')
    print(f'Edad: {Edad}')
    print(f'Ciudad: {Ciudad}')
    print(f'ID: {ID}')
    print('\n¡Gracias por ver mi información! ✌️😊')
imprimir_variables()