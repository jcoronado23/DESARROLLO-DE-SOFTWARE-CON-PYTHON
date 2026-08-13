import hashlib
from conexion import obtenerConexion, crearTablaCredenciales

usuario_defecto = "admin"
contrasena_defecto = "admin123"


def hashearContraseña(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def crearUsuarioAdminDefecto():
    conexion = obtenerConexion()
    cursor = conexion.cursor()
    
    
    cursor.execute("SELECT usuario FROM credenciales")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO credenciales (usuario, contrasena_hash) VALUES (?, ?)",
        (usuario_defecto, hashearContraseña(contrasena_defecto)))
        conexion.commit()
        
    conexion.close()
    
crearTablaCredenciales()
crearUsuarioAdminDefecto()

def verificarCredenciales(usuario, contrasena):
    conexion = obtenerConexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT contrasena_hash FROM credenciales WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    conexion.close()
    
    if fila is None:
        return False
    
    return fila[0] ==hashearContraseña(contrasena)