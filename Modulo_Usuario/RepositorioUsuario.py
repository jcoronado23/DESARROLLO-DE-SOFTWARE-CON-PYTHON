import Usuario
import random
import misExcepciones
from conexion import obtenerConexion, crearTablaUsuario

usuarios = []
crearTablaUsuario()

#Mantenimiento de un CRUD (Create, Read, Update, Delete)

#CREATE
def crearUsuario():

    #cedula = random.randint(100000000, 899999999)

    

    nombre = input("Ingrese su nombre: ")

    try:

        anno = int(input("Ingrese su anno de nacimiento: "))
        mes = int(input("Ingrese su mes de nacimiento: "))
        dia = int(input("Ingrese su dia de nacimiento: "))

        cedula = misExcepciones.validar_cedula(input("Ingrese su cedula con este formato 4-0111-0222: "))

        for usuario in usuarios:
            if usuario.cedula == cedula:
                print("Esta cedula ya esta en el registro")
                return

        nuevo_usuario = Usuario.Usuario(cedula, nombre, anno, mes, dia )
        usuarios.append(nuevo_usuario)  

        print("Usuario agregado satisfactoriamente")

    except ValueError:
        print("Ingreso un valor con error, por ende no se agrego el usuario.")
    except misExcepciones.FormatoCedulaError as fce:
        print("Error", fce)

#READ 
def leerUsuarios():
    conexion = obtenerConexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT cedula, nombre, anno_nacimiento, mes_nacimiento, dia_nacimiento FROM usuario")
    filas = cursor.fetchall()
    conexion.close()
    
    
    for fila in filas:
        usuario = Usuario.Usuario(fila[0], fila[1], fila[2], fila[3], fila[4])
        usuarios.append(usuario)
        
    
    if len(usuarios) == 0:
        print("No hay usuarios en el sistema")
        return
    
    for usuario in usuarios:
        usuario.mostrarDatos()
    
def buscarUsuario():
    try:
        cedula = misExcepciones.validar_cedula(input("Ingrese su cedula con este formato 4-0111-0222: "))
        for usuario in usuarios:
            if usuario.cedula == cedula:
                return usuario
        
        return None
    except misExcepciones.FormatoCedulaError as fce:
        print("Error", fce)



#UPDATE
def actualizarUsuario():
    usuario = buscarUsuario()

    if usuario:
        nombre = input("Digite su nuevo nombre: ")

        usuario.nombre = nombre
        print("Se ha actualizado con exito")

    else:
        print("No se ha encontrado el usuario que quiere modificar.")

def eliminarUsuario():
    usuario = buscarUsuario()

    if usuario:
        usuarios.remove(usuario)
        print("Se ha eliminado con exito")

    else:
        print("No se ha encontrado el usuario que quiere eliminar.")