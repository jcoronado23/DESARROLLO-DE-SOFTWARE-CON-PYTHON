import json
import os

class DiccionarioInteligente:
    """
    Clase para gestionar un diccionario inteligente en español.
    Proporciona funcionalidades de búsqueda, filtrado y consulta de palabras.
    """
    
    def __init__(self, archivo_json='diccionario.json'):
        """
        Inicializa el diccionario inteligente cargando los datos del archivo JSON.
        
        Args:
            archivo_json (str): Ruta del archivo JSON con las palabras
        """
        self.archivo = archivo_json
        self.palabras = []
        self.cargar_diccionario()
    
    def cargar_diccionario(self):
        """Carga el diccionario desde el archivo JSON."""
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                self.palabras = datos.get('diccionario', [])
            print(f"✓ Diccionario cargado exitosamente con {len(self.palabras)} palabras")
        except FileNotFoundError:
            print(f"✗ Error: No se encontró el archivo '{self.archivo}'")
            self.palabras = []
        except json.JSONDecodeError:
            print(f"✗ Error: El archivo '{self.archivo}' no tiene un formato JSON válido")
            self.palabras = []
    
    def buscar_palabra(self, palabra):
        """
        Busca una palabra en el diccionario.
        
        Args:
            palabra (str): Palabra a buscar
            
        Returns:
            dict: Información de la palabra o None si no existe
        """
        palabra = palabra.lower().strip()
        for item in self.palabras:
            if item['palabra'].lower() == palabra:
                return item
        return None
    
    def buscar_por_significado(self, termino):
        """
        Busca palabras que contengan un término en su significado.
        
        Args:
            termino (str): Término a buscar en los significados
            
        Returns:
            list: Lista de palabras que contienen el término
        """
        termino = termino.lower().strip()
        resultados = []
        for item in self.palabras:
            if termino in item['significado'].lower():
                resultados.append(item)
        return resultados
    
    def listar_todas(self):
        """Muestra todas las palabras del diccionario."""
        if not self.palabras:
            print("El diccionario está vacío")
            return
        
        print("\n" + "="*60)
        print(f"{'DICCIONARIO INTELIGENTE - {0} palabras'.format(len(self.palabras)):^60}")
        print("="*60)
        
        for idx, item in enumerate(self.palabras, 1):
            print(f"\n{idx}. {item['palabra'].upper()}")
            print(f"   Significado: {item['significado']}")
    
    def obtener_significado(self, palabra):
        """
        Obtiene el significado de una palabra de forma amigable.
        
        Args:
            palabra (str): Palabra a consultar
        """
        resultado = self.buscar_palabra(palabra)
        
        if resultado:
            print(f"\n📖 {resultado['palabra'].upper()}")
            print(f"   {resultado['significado']}")
        else:
            print(f"\n✗ La palabra '{palabra}' no se encontró en el diccionario")
    
    def contar_palabras(self):
        """Retorna el número total de palabras en el diccionario."""
        return len(self.palabras)
    
    def obtener_palabras_aleatorias(self, cantidad=5):
        """
        Retorna palabras aleatorias del diccionario.
        
        Args:
            cantidad (int): Número de palabras a obtener
            
        Returns:
            list: Lista de palabras aleatorias
        """
        import random
        return random.sample(self.palabras, min(cantidad, len(self.palabras)))
    
    def es_palabra_valida(self, palabra):
        """
        Verifica si una palabra existe en el diccionario.
        
        Args:
            palabra (str): Palabra a verificar
            
        Returns:
            bool: True si existe, False en caso contrario
        """
        return self.buscar_palabra(palabra) is not None


def main():
    """Función principal - Interfaz interactiva del diccionario."""
    
    print("\n" + "="*60)
    print("BIENVENIDO AL DICCIONARIO INTELIGENTE EN ESPAÑOL".center(60))
    print("="*60)
    
    # Crear instancia del diccionario
    dic = DiccionarioInteligente('diccionario.json')
    
    if dic.contar_palabras() == 0:
        print("No hay palabras disponibles en el diccionario.")
        return
    
    while True:
        print("\n" + "-"*60)
        print("\n¿Qué deseas hacer?")
        print("1. Buscar una palabra")
        print("2. Buscar por significado")
        print("3. Ver todas las palabras")
        print("4. Ver palabras aleatorias")
        print("5. Contar palabras")
        print("6. Salir")
        print("-"*60)
        
        opcion = input("\nSelecciona una opción (1-6): ").strip()
        
        if opcion == '1':
            palabra = input("\nIngresa la palabra a buscar: ").strip()
            if palabra:
                dic.obtener_significado(palabra)
        
        elif opcion == '2':
            termino = input("\nIngresa un término para buscar en significados: ").strip()
            if termino:
                resultados = dic.buscar_por_significado(termino)
                if resultados:
                    print(f"\n✓ Se encontraron {len(resultados)} coincidencias:")
                    for item in resultados:
                        print(f"  • {item['palabra']}: {item['significado']}")
                else:
                    print(f"\n✗ No se encontraron palabras con '{termino}'")
        
        elif opcion == '3':
            dic.listar_todas()
        
        elif opcion == '4':
            cantidad = input("\n¿Cuántas palabras aleatorias deseas? (por defecto 5): ").strip()
            try:
                cantidad = int(cantidad) if cantidad else 5
                aleatorias = dic.obtener_palabras_aleatorias(cantidad)
                print(f"\n🎲 Palabras aleatorias:")
                for item in aleatorias:
                    print(f"  • {item['palabra']}: {item['significado']}")
            except ValueError:
                print("✗ Debes ingresar un número válido")
        
        elif opcion == '5':
            total = dic.contar_palabras()
            print(f"\n📊 El diccionario contiene {total} palabras")
        
        elif opcion == '6':
            print("\n¡Hasta luego! 👋")
            break
        
        else:
            print("\n✗ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
