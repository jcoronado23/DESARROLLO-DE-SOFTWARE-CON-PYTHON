import Usuario
import random
import misExcepciones
from conexion import obtenerConexion, crearTablaUsuario

usuarios = []
crearTablaUsuario()

#Mantenimiento de un CRUD (Create, Read, Update, Delete)

#CREATE
def crearUsuario(cedula, nombre, anno, mes, dia):

    #cedula = random.randint(100000000, 899999999)

    
    if nombre.strip() == "":
        return False, "EL nombre no puede estar vacío"

    try:

        anno = int(anno)
        mes = int(mes)
        dia = int(dia)

        cedula = misExcepciones.validar_cedula(cedula)

        #for usuario in usuarios:
        #    if usuario.cedula == cedula:
        #        print("Esta cedula ya esta en el registro")
        #        return

        conexion = obtenerConexion()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT cedula FROM usuario WHERE cedula = ?", (cedula,))
        if cursor.fetchone():
            conexion.close()
            return False, "Esta cedula ya esta en el registro"
        
        cursor.execute(
            "INSERT INTO usuario (cedula, nombre, anno_nacimiento, mes_nacimiento, dia_nacimiento) VALUES (?,?,?,?,?)",
            (cedula, nombre, anno, mes, dia)
        )
        conexion.commit()
        conexion.close()
        
        #nuevo_usuario = Usuario.Usuario(cedula, nombre, anno, mes, dia )
        #usuarios.append(nuevo_usuario)  

        return True, "Usuario agregado satisfactoriamente"

    except ValueError:
        return False, "Ingreso un valor con error, por ende no se agrego el usuario."
    except misExcepciones.FormatoCedulaError as fce:
        return False,str(fce)
    except:
        return False, "Contacte a su administrador"

#READ 
def leerUsuarios():
    conexion = obtenerConexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT cedula, nombre, anno_nacimiento, mes_nacimiento, dia_nacimiento FROM usuario")
    filas = cursor.fetchall()
    conexion.close()
    
    lista_usuarios = []
    for fila in filas:
        usuario = Usuario.Usuario(fila[0], fila[1], fila[2], fila[3], fila[4])
        lista_usuarios.append(usuario)
        
    return lista_usuarios 
    
    #if len(usuarios) == 0:
    #    print("No hay usuarios en el sistema")
    #    return
    
    #for usuario in usuarios:
    #    usuario.mostrarDatos()
    
def buscarUsuario(texto):
    try:
        #cedula = misExcepciones.validar_cedula(input("Ingrese su cedula con este formato 4-0111-0222: "))
        
        #for usuario in usuarios:
        #    if usuario.cedula == cedula:
        #        return usuario
        
        conexion = obtenerConexion()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT cedula, nombre, anno_nacimiento, mes_nacimiento, dia_nacimiento FROM usuario WHERE cedula = ?",
            (f"{texto}",)
        )
        
        filas = cursor.fetchall()
        conexion.close()
        
        return [Usuario.Usuario(f[0], f[1], f[2], f[3], f[4]) for f in filas]
        
        return None
    except misExcepciones.FormatoCedulaError as fce:
        print("Error", fce)



#UPDATE
def actualizarUsuario(cedula, nombre, anno, mes, dia):
    
    if nombre.strip() == "":
        return False, "EL nombre son requeridos"
    
    usuario = buscarUsuario(cedula)

    if not usuario:
        return False, "No se ha encontrado el usuario que quiere modificar"

    try:
        anno = int(anno)
        mes = int(mes)
        dia = int(dia)
        print(nombre)
        conexion = obtenerConexion()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE usuario SET nombre = ?, anno_nacimiento = ?, mes_nacimiento = ?, dia_nacimiento = ? WHERE cedula = ?",
            (nombre, anno, mes, dia, cedula)
        )
        conexion.commit()
        conexion.close()
        print("jai")
        return True, "Se ha actualizado con exito"
        
    except ValueError:
        return False, "La fecha no es valida"
    except Exception:
        return False, "Contacte a su administrador"
    
def eliminarUsuario(cedula):
    usuario = buscarUsuario(cedula)

    if not usuario:
        return False, "No se ha encontrado el usaurio que quiere eliminar"
        
    conexion = obtenerConexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuario WHERE cedula = ?", (cedula,))
    conexion.commit()
    conexion.close()
    
    return True, "Se ha eliminado con exito"