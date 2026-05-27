import Usuario

usuarios = []

#Mantenimiento de un CRUD (Create, Read, Update, Delete) de usuarios
def crearUsuario():
    
    cedula = input("Ingrese la cedula del usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")
    
    for usuario in usuarios:
        if usuario.cedula == cedula:
            print("Esta cedula ya esta en el registro")
            return
        
    nuevoUsuario = Usuario(cedula, nombre)
    usuarios.append(nuevoUsuario)
    
    print("Usuario agregado satisfactoriamente")
    
    
def leerUsuarios():
    if len(usuarios) == 0:
        print("No hay usuarios sitema")
        return
    
    for usuario in usuarios:
        usuario.mostrarDatos()
        
def buscarUsuario(Cedula):
    for usuario in usuarios:
        if usuario.cedula == Cedula:
            return usuario
        
    return None

#UPDATE
def actualizarUsuario():
    
    cedula = input("Digite su cedula: ")
    usuario = buscarUsuario(cedula)
    
    if usuario:
        nombre = input("Digite el nuevo nombre: ")
        
        usuario.nombre = nombre
        print("Usuario actualizado satisfactoriamente")
    else:
        print("No se ha encontrado el usuario que quiere modificar")
        
def eliminarUsuario():
    cedula = input("Digite su cedula: ")
    usuario = buscarUsuario(cedula)
    
    if usuario:
        usuarios.remove(usuario)
        print("Usuario eliminado satisfactoriamente")
    else:
        print("No se ha encontrado el usuario que quiere eliminar")