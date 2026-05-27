from Repositorio_Estudiante import actualizarUsuario, crearUsuario, eliminarUsuario, leerestudiantes

def menu():
    
    while True:
        print("Mantenimiento de Estudiantes",
            "1. Crear Estudiante",
            "2. Leer todos los Estudiantes",
            "3. Actualizar Estudiante",
            "4. Eliminar Estudiante",
            "5. Salir", sep="\n")
        opcion = int(input("Digite una opcion: "))
        
        if opcion == 1:
            crearUsuario()
        elif opcion == 2:
            leerestudiantes()
        elif opcion == 3:
            actualizarUsuario()
        elif opcion == 4:
            eliminarUsuario()
        elif opcion == 5:
            break
menu()