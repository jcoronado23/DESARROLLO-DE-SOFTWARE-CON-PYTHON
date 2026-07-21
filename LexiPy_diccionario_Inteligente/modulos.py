import json
import os
from datetime import datetime

#Llamar a dictionary.json de LexiPy diccionario Inteligente en python
#Utilizar encodificación UTF-8 para leer y escribir en el archivo



class Diccionario_Inteligente():
    def __init__(self):
        self.archivo = "LexiPy_diccionario_Inteligente/dictionary.json"
        self.dictionary = {}
    
    #Cargar el diccionario desde un archivo dictionary.json
    def cargar_diccionario(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data.get("diccionario", []):
                    palabra = item.get("palabra")
                    significado = item.get("significado")
                    if palabra and significado:
                        self.dictionary[palabra] = significado
        except FileNotFoundError:
            print(f"El archivo '{self.archivo}' no se encontró. Se creará uno nuevo al guardar el diccionario.")
        except json.JSONDecodeError:
            print(f"El archivo '{self.archivo}' no contiene un formato JSON válido. Se creará uno nuevo al guardar el diccionario.")
    
    def buscar_palabra(self, palabra):
        return self.dictionary.get(palabra)
    
    def guardar_diccionario(self):
        data = {
            "diccionario": [{"palabra": palabra, "significado": significado} for palabra, significado in self.dictionary.items()]
        }
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    


    def agregar_palabra(self, palabra, significado):
        self.dictionary[palabra] = significado
        
    #Verifica si la palabra existe antes de editarla
    def editar_palabra(self, palabra, nuevo_significado):
        if palabra in self.dictionary:
            self.dictionary[palabra] = nuevo_significado
        else:
            print(f"La palabra '{palabra}' no se encuentra en el diccionario.")

    def eliminar_palabra(self, palabra):
        if palabra in self.dictionary:
            del self.dictionary[palabra]

    def listar_palabras(self):
        return list(self.dictionary.keys())
    
    # Generar reporte utilizar Encodificación UTF-8 para guardar el reporte en un archivo de texto
    # Ultimas 5 palabras agregadas al diccionario con significado con fecha y hora de creación y en forma de tabla
    # La ruta del archivo de reporte es "reporte_de_diccionario.txt" debe estar en la misma carpeta que el archivo main_.py

    def generar_reporte(self):
        reporte = "Reporte del Diccionario Inteligente\n"
        reporte += "=" * 40 + "\n"
        reporte += f"Fecha y hora de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        reporte += "=" * 40 + "\n"
        reporte += f"{'Palabra':<20} | {'Significado':<20}\n"
        reporte += "-" * 40 + "\n"

        for palabra, significado in list(self.dictionary.items())[-5:]:
            reporte += f"{palabra:<20} | {significado:<20}\n"

        return reporte