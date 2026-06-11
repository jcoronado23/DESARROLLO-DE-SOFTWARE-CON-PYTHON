from datetime import datetime, date
import Usuario
import random

usuarios = []

#Mantenimiento de un CRUD (Create, Read, Update, Delete)

#CREATE
def crearUsuario():

    cedula = random.randint(100000000, 899999999)

    for usuario in usuarios:
        if usuario.cedula == cedula:
            print("Esta cedula ya esta en el registro")
            return

    nombre = input("Ingrese su nombre: ")

    anno = int(input("Ingrese su anno de nacimiento (dd): "))
    mes = int(input("Ingrese su mes de nacimiento (mm): "))
    dia = int(input("Ingrese su dia de nacimiento (yyyy): "))

    nuevo_usuario = Usuario.Usuario(cedula, nombre, anno, mes, dia )
    usuarios.append(nuevo_usuario)  

    print("Usuario agregado satisfactoriamente")

#READ 
def leerUsuarios():
    
    if len(usuarios) == 0:
        print("No hay usuarios en el sistema")
        return
    
    for usuario in usuarios:
        usuario.mostrarDatos()
    
def buscarUsuario(cedula):
    for usuario in usuarios:
        if usuario.cedula == cedula:
            return usuario
    
    return None

#UPDATE
def actualizarUsuario():

    cedula = input("Digite su cedula: ")
    usuario = buscarUsuario(cedula)

    if usuario:
        nombre = input("Digite su nuevo nombre: ")

        usuario.nombre = nombre
        print("Se ha actualizado con exito")

    else:
        print("No se ha encontrado el usuario que quiere modificar.")

def eliminarUsuario():
    cedula = input("Digite su cedula: ")
    usuario = buscarUsuario(cedula)

    if usuario:
        usuarios.remove(usuario)
        print("Se ha eliminado con exito")

    else:
        print("No se ha encontrado el usuario que quiere eliminar.")