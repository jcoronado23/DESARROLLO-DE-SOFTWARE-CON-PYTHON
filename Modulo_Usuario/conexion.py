import sqlite3

nombreDb = "Usuario.db"


def obtenerConexion():
    conexion = sqlite3.connect(nombreDb)
    return conexion

def crearTablaUsuario():
    conexion = obtenerConexion()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            cedula TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            anno_nacimiento INTEGER NOT NULL,
            mes_nacimiento INTEGER NOT NULL,
            dia_nacimiento INTEGER NOT NULL
        )           
    """)
    conexion.commit()
    conexion.close()