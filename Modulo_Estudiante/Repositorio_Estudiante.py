import Estudiante

usuarios = []

#Mantenimiento de un CRUD (Create, Read, Update, Delete) de usuarios
def crearUsuario():
    
    id= int(input("Ingrese el ID del usuario: "))
    nombre = input("Ingrese el nombre del usuario: ")
    nota_final = int(input("Ingrese la nota final del usuario: "))
    if nota_final < 0 or nota_final > 100:
        print("La nota final debe estar entre 0 y 100")
        return
    
    for usuario in usuarios:
        if usuario.id == id:
            print("Ya existe un usuario con esa ID")
            return
        
    nuevoEstudiante = Estudiante(id, nombre, nota_final)
    usuarios.append(nuevoEstudiante)
    
    print("Estudiante agregado satisfactoriamente")
    
    
def leerestudiantes():
    if len(usuarios) == 0:
        print("No hay estudiantes en el sistema")
        return
    
    for usuario in usuarios:
        usuario.mostrarDatos()
        
def buscarUsuario(id):
    for usuario in usuarios:
        if usuario.id == id:
            return usuario
        
    return None

#UPDATE
def actualizarUsuario():
    
    id = int(input("Digite el ID del estudiante: "))
    usuario = buscarUsuario(id)
    
    if usuario:
        nombre = input("Digite el nuevo nombre: ")
        nota_final = int(input("Digite la nueva nota final: "))
        if nota_final < 0 or nota_final > 100:
            print("La nota final debe estar entre 0 y 100")
            return
        usuario.nombre = nombre
        usuario.nota_final = nota_final
        print("Estudiante actualizado satisfactoriamente")
    else:
        print("No se ha encontrado el estudiante que quiere modificar")
        
def eliminarUsuario():
    id = int(input("Digite el ID del estudiante: "))
    usuario = buscarUsuario(id)
    
    if usuario:
        usuarios.remove(usuario)
        print("Estudiante eliminado satisfactoriamente")
    else:
        print("No se ha encontrado el estudiante que quiere eliminar")