from RepositorioUsuario import actualizarUsuario, crearUsuario, eliminarUsuario, leerUsuarios

def menu():
    
    while True:
        print("Mantenimiento de Usuarios",
            "1. Crear Usuario",
            "2. Leer todos los Usuarios",
            "3. Actualizar Usuario",
            "4. Eliminar Usuario",
            "5. Salir", sep="\n")
        opcion = int(input("Digite una opcion: "))
        
        if opcion == 1:
            crearUsuario()
        elif opcion == 2:
            leerUsuarios()
        elif opcion == 3:
            actualizarUsuario()
        elif opcion == 4:
            eliminarUsuario()
        elif opcion == "5":
            break
menu()