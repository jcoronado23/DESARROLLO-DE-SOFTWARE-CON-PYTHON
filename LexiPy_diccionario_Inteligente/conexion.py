import sqlite3

nombreDB = r"C:\Users\Jairo\Repos_GitHub\DESARROLLO DE SOFTWARE CON PYTHON\LexiPy_diccionario_Inteligente\dictionary.db"


def conectar():
    return sqlite3.connect(nombreDB)


def cargar():
    conexion = conectar()
    cursor = conexion.cursor()

    # Eliminamos el CREATE TABLE porque ya existe físicamente en tu archivo
    cursor.execute("""
        SELECT palabra, significado
        FROM diccionario
        ORDER BY palabra
    """)
    
    registros = cursor.fetchall()
    conexion.close()

    diccionario = {}
    for palabra, significado in registros:
        diccionario[palabra] = significado

    return diccionario

def guardar(palabra, significado):

    conexion = conectar()
    cursor = conexion.cursor()

    try:

        cursor.execute("""
            INSERT INTO diccionario(palabra, significado)
            VALUES (?, ?)
        """, (palabra.lower(), significado))

        conexion.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conexion.close()


def editar(palabra, nuevo_significado):

    conexion = conectar()
    cursor = conexion.cursor()

    try:

        cursor.execute("""
            UPDATE diccionario
            SET significado = ?
            WHERE palabra = ?
        """, (nuevo_significado, palabra.lower()))

        conexion.commit()

        return cursor.rowcount > 0

    finally:

        conexion.close()


def eliminar(palabra):

    conexion = conectar()
    cursor = conexion.cursor()

    try:

        cursor.execute("""
            DELETE FROM diccionario
            WHERE palabra = ?
        """, (palabra.lower(),))

        conexion.commit()

        return cursor.rowcount > 0

    finally:

        conexion.close()