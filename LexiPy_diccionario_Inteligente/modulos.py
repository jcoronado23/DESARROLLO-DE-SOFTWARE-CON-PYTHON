import conexion
from conexion import cargar, guardar, editar, eliminar
from datetime import datetime
import os
# Prueba de Git

class DiccionarioInteligente:

    def __init__(self):
        pass

    # Buscar una palabra
    def buscar_palabra(self, palabra):

        diccionario = cargar()

        return diccionario.get(palabra.lower())

    # Agregar una palabra
    def agregar_palabra(self, palabra, significado):

        return guardar(palabra, significado)
    
        # Editar una palabra
    def editar_palabra(self, palabra, nuevo_significado):

        return editar(palabra, nuevo_significado)

    # Eliminar una palabra
    def eliminar_palabra(self, palabra):

        return eliminar(palabra)

    # Listar todas las palabras
    def listar_palabras(self):

        diccionario = cargar()

        return sorted(diccionario.keys())

    # Obtener todo el diccionario
    def obtener_diccionario(self):
        return cargar()
    
    # Generar reporte
    def generar_reporte(self):

        diccionario = cargar()

        reporte = ""
        reporte += "REPORTE DEL DICCIONARIO INTELIGENTE\n"
        reporte += "=" * 70 + "\n"
        reporte += f"Cantidad total de palabras: {len(diccionario)}\n"
        reporte += f"Fecha de generación: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        reporte += "=" * 70 + "\n"
        reporte += f"{'Palabra':20} | Significado\n"
        reporte += "-" * 70 + "\n"

        for palabra in sorted(diccionario.keys()):
            reporte += f"{palabra:20} | {diccionario[palabra]}\n"

        ruta_reporte = os.path.join(
            os.path.dirname(__file__),
            "reporte_de_diccionario.txt"
        )

        with open(ruta_reporte, "w", encoding="utf-8") as archivo:
            archivo.write(reporte)

        return ruta_reporte