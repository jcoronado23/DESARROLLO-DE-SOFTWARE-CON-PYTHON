import os
from modulos import Diccionario_Inteligente

#Menu principal del programa
def main():
    dic = Diccionario_Inteligente()
    dic.cargar_diccionario()
#Limpiar la pantalla antes de mostrar el menú
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        #"Título del programa"
        #menu de opciones
        print("=" * 30)
        print("LexiPy_diccionario_Inteligente") #metodo para mostrar = a los lados del titulo
        print("=" * 30)
        
        print("1. Buscar palabra")
        print("2. Agregar palabra")
        print("3. Editar palabra")
        print("4. Eliminar palabra")
        print("5. Listar palabras")
        print("6. Generar reporte")
        print("7. Salir")
        try:
            opcion = (int(input("Seleccione una opción: ")))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero correspondiente.\n")
            continue

        if opcion == 1:
            palabras = input("Ingrese la palabra a buscar: ")
            significado = dic.buscar_palabra(palabras)
            if significado:
                print(f"\nSignificado de '{palabras}': {significado}")
            else:
                print(f"La palabra '{palabras}' no se encuentra en el diccionario.\n")
            
            
        elif opcion == 2:
            palabra = input("Ingrese la nueva palabra: ")
            significado = input("Ingrese el significado: ")
            dic.agregar_palabra(palabra, significado)
            dic.guardar_diccionario()
            print(f"La palabra '{palabra}' ha sido agregada al diccionario.")

        elif opcion == 3:
            palabra = input("Ingrese la palabra a editar: ")
            if dic.buscar_palabra(palabra):
                nuevo_significado = input("Ingrese el nuevo significado: ")
                dic.editar_palabra(palabra, nuevo_significado)
                dic.guardar_diccionario()
                print(f"El significado de '{palabra}' ha sido actualizado.")
            else:
                print(f"La palabra '{palabra}' no se encuentra en el diccionario.")

        elif opcion == 4:
            palabra = input("Ingrese la palabra a eliminar: ")
            dic.eliminar_palabra(palabra)
            dic.guardar_diccionario()
            print(f"La palabra '{palabra}' ha sido eliminada del diccionario.")

        elif opcion == 5:
            palabras = dic.listar_palabras()
            if palabras:
                print("Palabras en el diccionario:")
                for p in palabras:
                    print(f"- {p}")
            else:
                print("El diccionario está vacío.")

        
        elif opcion == 6:
            reporte = dic.generar_reporte()
            print(reporte)
            # Guardar el reporte en un archivo de texto
            with open("LexiPy_diccionario_Inteligente/reporte.txt", "w", encoding="utf-8") as f:
                f.write(reporte)
            print("El reporte ha sido guardado en 'reporte.txt'.")
            
        elif opcion == 7:
            print("Gracias por usar LexiPy_diccionario_Inteligente. ¡Hasta luego!🖐️")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            
        # Verificar si el usuario desea realizar otra operación
        volver = input("¿Desea realizar otra operación? (s/n): ")
        if volver.lower() != "s":
        
            os.system('cls' if os.name == 'nt' else 'clear')
            break
#Limpiar la pantalla antes de mostrar el menú nuevamente
        os.system('cls' if os.name == 'nt' else 'clear')      
        
if __name__ == "__main__":
    main()