import pyreadline3
import os

#Limpiar la pantalla al iniciar el programa
os.system('cls' if os.name == 'nt' else 'clear')


# Comando interactivo, que permite al usuario ingresar comandos, navegar con flechas y salir
class ComandoInteractivo:
    def __init__(self):
        self.historial = []
        self.indice_historial = -1
        
# Ejecuta el comando ingresado por el usuario
    def ejecutar_comando(self, comando):
        comando = comando.strip()
        if comando:
            self.historial.append(comando)
            self.indice_historial = len(self.historial)
            os.system(comando)
            
# Permite al usuario ingresar comandos, navegar con flechas y salir
    def iniciar(self):
        print("Bienvenido al Comando Interactivo. Escribe tus comandos y presiona Enter.")
        print("Usa las flechas para navegar por el historial. Escribe 'salir' para salir.")
        
        while True:
            try:
                comando = input("> ")
                
                if comando.lower() == "salir":
                    print("Programa finalizado.")
                    break
                
                self.ejecutar_comando(comando)
            except KeyboardInterrupt:
                print("\nPrograma finalizado.")
                break
            
# Punto de entrada del programa

if __name__ == "__main__":
    comando_interactivo = ComandoInteractivo()
    comando_interactivo.iniciar()